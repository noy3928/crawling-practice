const getRequirements = async page => {
  const relevantTexts = await page.$$eval("h6", headers => {
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
}
