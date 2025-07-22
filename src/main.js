import Vue from 'vue'
import App from './App'
import router from './router'
import i18n from './lang'
// import store from './store/index.js'
import qs from 'qs/'
// 导入NProgress, 包对应的JS和CSS
import NProgress from 'nprogress'
import 'nprogress/nprogress.css'
// import './plugins/element.js'
// 导入全局样式表
// import './assets/css/global.css'


//引入状态管理vuex
import Vuex from 'vuex'

import HomeHeader from './components/snippets/HomeHeader'
import HomeFooter from './components/snippets/HomeFooter'
import HomePageHero from './components/snippets/HomePageHero'
import NewsItem from './components/snippets/NewsItem'
import ConferenceItem from './components/snippets/ConferenceItem'
import ResourceItem from "./components/snippets/ResourceItem";
import modalItem from "./components/snippets/modal-item";

Vue.config.productionTip = false

Vue.component('home-header', HomeHeader)
Vue.component('home-footer', HomeFooter)
Vue.component('homepage-hero', HomePageHero)
Vue.component('news-item', NewsItem)
Vue.component('conference-item', ConferenceItem)
Vue.component('resource-item',ResourceItem)
Vue.component('modal-item',modalItem)
Vue.prototype.$axios = axios


Vue.use(Vuex)
import axios from 'axios'

//挂载axios和设置路径
Vue.prototype.$http = axios
Vue.config.productionTip = false

axios.defaults.baseURL = 'https://icachi.org:8080/'
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'
axios.defaults.headers.put['Content-Type'] = 'application/x-www-form-urlencoded'
axios.interceptors.request.use(config => {
  NProgress.start()
  // (当content-type是x-www时才让数据转化为form-data,当content-type是json时,用默认的request payload)
  if (config.headers['Content-Type'] === undefined) {
    config.data = qs.stringify(config.data)
  }
  // 为请求头对象，添加token验证的Authorization字段
  config.headers.Authorization = window.localStorage.getItem('token')
  // 在最后必须 return config
  return config
})

// response 拦截器中,  隐藏进度条NProgress.done()
axios.interceptors.response.use(response => {
  NProgress.done()
  if (response.status === 200) {
    return Promise.resolve(response)
  } else {
    return Promise.resolve(response)
  }
}, error => {
  NProgress.done()
  if (error.response.status) {
    switch (error.response.status) {
      case 400:
        Vue.prototype.$message.error("客户端错误：请求失败")
        break;

      case 401:
        router.replace({
          path: '/login',
          query: {
            redirect: router.currentRoute.fullPath
          }
        });
        break;

      case 403:
        Vue.prototype.$message.error("登录过期，请重新登录")
        // 清除token
        store.dispatch('FedLogOut').then(() => {
          // 跳转登录页面，并将要浏览的页面fullPath传过去，登录成功后跳转需要访问的页面
          router.replace({
            path: '/login',
            query: {
              redirect: router.currentRoute.fullPath
            }
          })
        })
        break;

      // 404请求不存在
      case 404:
        Vue.prototype.$message.error("网络请求不存在")
        break;
      // 其他错误，直接抛出错误提示
      default:
        Vue.prototype.$message.error(error.response.data.message)
        break;
    }
  } else {
    Vue.prototype.$message.error("请求超时或当前已断网")
  }
})

// 响应拦截器
// axios.interceptors.response.use(function (response) {
//   //登录过期
//   if (response.status === 444) {
//     router.replace('/login');
//   }
//   return response;
// }
// // , function (error) {
// //   // 对响应错误做点什么
// //   return Promise.reject(error);
// // }
// );



Vue.filter('dataFormat', function (originVal) {
  const dt = new Date(originVal)

  const y = dt.getFullYear()
  const m = (dt.getMonth() + 1 + '').padStart(2, '0')
  const d = (dt.getDate() + '').padStart(2, '0')

  const hh = (dt.getHours() + '').padStart(2, '0')
  const mm = (dt.getMinutes() + '').padStart(2, '0')
  const ss = (dt.getSeconds() + '').padStart(2, '0')
  // yyyy-mm-dd hh:mm:ss
  return `${y}-${m}-${d} ${hh}:${mm}:${ss}`
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  axios,
  i18n,
  components: { App },
  template: '<App/>'
})



// new Vue({
//   router,
//   store,
//   render: h => h(App)
// }).$mount('#app')

