const puppeteer = require("puppeteer")
const getLinks = require("./utils/getLinks")
const scrollDown = require("./utils/scrollDown")
const getRequirementsFromPage = require("./utils/getRequirementsFromPage")

async function run() {
  const browser = await puppeteer.launch({ headless: false })
  const page = await browser.newPage()

  await page.setViewport({ width: 1280, height: 720 })
  await page.goto("https://www.wanted.co.kr/wdlist/518/669") // 프론트엔드 페이지

  await page.waitForSelector("[data-cy='job-card']")

  await scrollDown(page)
  const links = await getLinks(page)
  const countMap = new Map()
  for (let link of links) {
    await getRequirementsFromPage(browser, link, countMap)
  }
}

run()
