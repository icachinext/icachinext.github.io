import comp from "/Users/chenwang/Dev/ICACHI/icachinext.github.io/docs/.vuepress/.temp/pages/posts/sticky2.html.vue"
const data = JSON.parse("{\"path\":\"/posts/sticky2.html\",\"title\":\"Sticky Article with Higher Priority\",\"lang\":\"zh-CN\",\"frontmatter\":{\"date\":\"2020-01-01T00:00:00.000Z\",\"category\":[\"Category C\"],\"tag\":[\"tag E\"],\"sticky\":10},\"headers\":[{\"level\":2,\"title\":\"Heading 2\",\"slug\":\"heading-2\",\"link\":\"#heading-2\",\"children\":[{\"level\":3,\"title\":\"Heading 3\",\"slug\":\"heading-3\",\"link\":\"#heading-3\",\"children\":[]}]}],\"git\":{\"updatedTime\":1753177855000,\"contributors\":[{\"name\":\"CranberryWong\",\"username\":\"CranberryWong\",\"email\":\"chen.wang.hec+icachinext@gmail.com\",\"commits\":2,\"url\":\"https://github.com/CranberryWong\"}],\"changelog\":[{\"hash\":\"53e05f47e01019deb47fa8695e19a75921a2b336\",\"time\":1753177855000,\"email\":\"chen.wang.hec+icachinext@gmail.com\",\"author\":\"CranberryWong\",\"message\":\"recommit\"},{\"hash\":\"f18684d11e8d59d6ab365c8a7042c45cf7948f08\",\"time\":1753173627000,\"email\":\"chen.wang.hec+icachinext@gmail.com\",\"author\":\"CranberryWong\",\"message\":\"vuepress\"}]},\"filePathRelative\":\"posts/sticky2.md\",\"excerpt\":\"\\n<p>Excerpt information which is added manually.</p>\\n\"}")
export { comp, data }

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept()
  if (__VUE_HMR_RUNTIME__.updatePageData) {
    __VUE_HMR_RUNTIME__.updatePageData(data)
  }
}

if (import.meta.hot) {
  import.meta.hot.accept(({ data }) => {
    __VUE_HMR_RUNTIME__.updatePageData(data)
  })
}
