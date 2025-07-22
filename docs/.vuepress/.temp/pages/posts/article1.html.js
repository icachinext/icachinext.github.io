import comp from "/Users/chenwang/Dev/ICACHI/icachinext.github.io/docs/.vuepress/.temp/pages/posts/article1.html.vue"
const data = JSON.parse("{\"path\":\"/posts/article1.html\",\"title\":\"Article 1\",\"lang\":\"zh-CN\",\"frontmatter\":{\"date\":\"2022-01-01T00:00:00.000Z\",\"category\":[\"Category A\"],\"tag\":[\"tag A\",\"tag B\"]},\"headers\":[{\"level\":2,\"title\":\"Heading 2\",\"slug\":\"heading-2\",\"link\":\"#heading-2\",\"children\":[{\"level\":3,\"title\":\"Heading 3\",\"slug\":\"heading-3\",\"link\":\"#heading-3\",\"children\":[]}]}],\"git\":{\"updatedTime\":1753177855000,\"contributors\":[{\"name\":\"CranberryWong\",\"username\":\"CranberryWong\",\"email\":\"chen.wang.hec+icachinext@gmail.com\",\"commits\":2,\"url\":\"https://github.com/CranberryWong\"}],\"changelog\":[{\"hash\":\"53e05f47e01019deb47fa8695e19a75921a2b336\",\"time\":1753177855000,\"email\":\"chen.wang.hec+icachinext@gmail.com\",\"author\":\"CranberryWong\",\"message\":\"recommit\"},{\"hash\":\"f18684d11e8d59d6ab365c8a7042c45cf7948f08\",\"time\":1753173627000,\"email\":\"chen.wang.hec+icachinext@gmail.com\",\"author\":\"CranberryWong\",\"message\":\"vuepress\"}]},\"filePathRelative\":\"posts/article1.md\",\"excerpt\":\"\\n<h2>Heading 2</h2>\\n<p>Here is the content.</p>\\n<h3>Heading 3</h3>\\n<p>Here is the content.</p>\\n\"}")
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
