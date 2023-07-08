const puppeteer = require("puppeteer")

async function run() {
  // headless 모드를 끄고 브라우저를 띄웁니다.
  const browser = await puppeteer.launch({ headless: false })
  const page = await browser.newPage()

  await page.goto("https://www.wanted.co.kr/")

  const elements = await page.$$('[data-attribute-id="gnb"]')

  // 각 요소의 텍스트 가져오기
  for (let element of elements) {
    const textContent = await page.evaluate(el => el.textContent, element)
    console.log(textContent)
  }

  //   console.log(textContent)

  // 브라우저를 닫지 않고 유지하려면 아래 코드를 주석 처리하세요.
  // await browser.close();
}

run()
