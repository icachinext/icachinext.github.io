export const siteData = JSON.parse("{\"base\":\"/\",\"lang\":\"zh-CN\",\"title\":\"世界华人华侨人机交互协会\",\"description\":\"My first VuePress Site\",\"head\":[],\"locales\":{\"/zh/\":{\"lang\":\"zh-CN\",\"title\":\"世界华人华侨人机交互协会\",\"description\":\"中文描述\"},\"/en/\":{\"lang\":\"en-US\",\"title\":\"ICACHI\",\"description\":\"English Description\"}}}")

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept()
  if (__VUE_HMR_RUNTIME__.updateSiteData) {
    __VUE_HMR_RUNTIME__.updateSiteData(siteData)
  }
}

if (import.meta.hot) {
  import.meta.hot.accept(({ siteData }) => {
    __VUE_HMR_RUNTIME__.updateSiteData(siteData)
  })
}
