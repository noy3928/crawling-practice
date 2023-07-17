const scrollDown = async page => {
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
}

module.exports = scrollDown
