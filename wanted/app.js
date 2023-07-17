const puppeteer = require("puppeteer")

async function run() {
  const browser = await puppeteer.launch({ headless: false })
  const page = await browser.newPage()

  await page.setViewport({ width: 1280, height: 720 })
  await page.goto("https://www.wanted.co.kr/wdlist/518/669") // 프론트엔드 페이지

  await page.waitForSelector("[data-cy='job-card']")

  let prevNumElements = 0
  let scrollCount = 0

  // 스크롤 시작
  while (true) {
    await page.evaluate(() => {
      window.scrollBy(0, window.innerHeight)
    })
    await page.waitForTimeout(1000)

    // 3번의 스크롤마다 요소의 수를 체크합니다.
    if (++scrollCount % 3 === 0) {
      const elements = await page.$$("[data-cy='job-card']")
      console.log(elements.length, prevNumElements)
      if (prevNumElements === elements.length) {
        console.log("스크롤 종료!")
        break
      }
      prevNumElements = elements.length
    }
  }

  // 스크롤 끝나면 링크 수집
  const elements = await page.$$("[data-cy='job-card']")
  const links = new Set()
  for (let element of elements) {
    const linkElement = await element.$("a")
    const href = await page.evaluate(el => el.href, linkElement)
    links.add(href)
  }

  const countMap = new Map()

  // 각 페이지 별 작업
  for (let link of Array.from(links)) {
    const newPage = await browser.newPage()
    await newPage.setViewport({ width: 1280, height: 720 })
    await newPage.goto(link)

    await newPage.waitForSelector(".JobHeader_className__HttDA")

    const relevantTexts = await newPage.$$eval("h6", headers => {
      let texts = []

      for (let header of headers) {
        if (
          header.textContent === "자격요건" ||
          header.textContent === "우대사항"
        ) {
          let spanText =
            header.nextElementSibling.querySelector("span").textContent

          texts.push(spanText)
        }
      }

      return texts
    })

    for (let text of relevantTexts) {
      const matches = text.match(/[a-zA-Z0-9#.]+/g)
      if (matches) {
        for (let match of matches) {
          const upperMatch = match.toUpperCase()
          const count = countMap.get(upperMatch) || 0
          countMap.set(upperMatch, count + 1)
        }
      }
    }

    console.log(Array.from(countMap.entries()))

    newPage.close()
  }
}

run()
