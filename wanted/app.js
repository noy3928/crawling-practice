const puppeteer = require("puppeteer")
const pageDown = require("./utils/pageDown")

async function run() {
  const browser = await puppeteer.launch({ headless: false })
  const page = await browser.newPage()

  await page.setViewport({ width: 1280, height: 720 })
  await page.goto("https://www.wanted.co.kr/")

  await page.waitForSelector(".Menu_className__gGcYQ")
  const menuElement = await page.$(".Menu_className__gGcYQ")
  const firstLiElement = await menuElement.$("li")
  await firstLiElement.click()

  await page.waitForSelector(".JobGroup_JobGroup__H1m1m")
  await page.click(".JobGroup_JobGroup__H1m1m")

  await page.waitForSelector('[data-job-category-id="518"]')
  await page.click('[data-job-category-id="518"]')

  await page.waitForSelector(".JobCategory_JobCategory__btn__k3EFe")
  await page.click(".JobCategory_JobCategory__btn__k3EFe")

  await page.waitForSelector(".JobCategoryItem_JobCategoryItem__oUaZr")
  const jobCategories = await page.$$(".JobCategoryItem_JobCategoryItem__oUaZr")
  for (let jobCategory of jobCategories) {
    const jobCategoryText = await page.evaluate(
      el => el.textContent,
      jobCategory
    )
    if (jobCategoryText === "프론트엔드 개발자") {
      await jobCategory.click()
      break
    }
  }

  await page.click(".Button_Button__label__1Kk0v")

  await page.waitForSelector(".slick-slide")

  const cards = await page.$$(".Card_className__u5rsb")

  const el = await page.evaluate(el => el.outerHTML, cards)
  console.log(el)

  console.log(cards[0])
  //   await cards[0].$("a").click()
}

run()
