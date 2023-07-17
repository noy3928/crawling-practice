const getLinks = async page => {
  const elements = await page.$$("[data-cy='job-card']")
  const links = new Set()
  for (let element of elements) {
    const linkElement = await element.$("a")
    const href = await page.evaluate(el => el.href, linkElement)
    links.add(href)
  }

  return Array.from(links)
}

module.exports = getLinks
