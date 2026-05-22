import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "ICACHI",
  description: "International Chinese Association of Computer Human Interaction",
  head: [['link', { rel: 'icon', href: '/images/favicon.ico' }]],

  lang: 'zh-CN',
  appearance: false,

  locales: {
    root: {
      label: '简体中文',
      lang: 'zh-CN',
      title: 'ICACHI',
      description: '世界华人华侨人机交互协会',
      themeConfig: {
        logo: '/images/icachi.svg',
        nav: [
          { text: '主页', link: '/' },
          { text: '关于', link: '/about' },
          { text: '会议', link: '/conference' },
          { text: '新闻', link: '/news/' },
          { text: '资源', link: '/resource' }
        ],
        outline: { label: '本页内容' }
      }
    },
    en: {
      label: 'English',
      lang: 'en-US',
      link: '/en/',
      title: 'ICACHI',
      description: 'International Chinese Association of Computer Human Interaction',
      themeConfig: {
        logo: '/images/icachi.svg',
        nav: [
          { text: 'Home', link: '/en/' },
          { text: 'About', link: '/en/about' },
          { text: 'Conference', link: '/en/conference' },
          { text: 'News', link: '/en/news/' },
          { text: 'Resources', link: '/en/resource' }
        ]
      }
    }
  },

  themeConfig: {
    siteTitle: false,
    socialLinks: [],
    search: { provider: 'local' }
  }
})
