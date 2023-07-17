const scrollDown = async page => {
  let prevNumElements = 0
  let scrollCount = 0
  let noChangeCount = 0 // 추가: 변화가 없는 경우를 세기 위한 카운터

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
        noChangeCount++ // 추가: 변화가 없는 경우 카운터 증가
        if (noChangeCount >= 5) {
          // 추가: 변화가 5번 이상 없는 경우에만 스크롤 종료
          console.log("스크롤 종료!")
          break
        }
      } else {
        noChangeCount = 0 // 추가: 요소의 수가 변화한 경우 카운터 초기화
      }
      prevNumElements = elements.length
    }
  }
}

module.exports = scrollDown
