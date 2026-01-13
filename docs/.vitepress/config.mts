import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "ICACHI",
  description: "International Chinese Association of Computer Human Interaction",
  head: [['link', { rel: 'icon', href: '/favicon.ico' }]],
  
  // Default to Chinese
  lang: 'zh-CN',

  locales: {
    root: {
      label: '简体中文',
      lang: 'zh-CN',
      title: 'ICACHI',
      description: '世界华人华侨人机交互协会',
      themeConfig: {
        nav: [
          { text: '主页', link: '/' },
          { text: '协会章程', link: '/bylaws' },
          { text: '关于', link: '/about' },
          { text: '新闻', link: '/news/' },
          { text: '会议', link: '/conference' },
          { text: '资源', link: '/resource' }
        ],
        sidebar: {
          '/bylaws': [
            {
              text: '协会章程',
              items: [
                // Will be auto-populated or manually set later
              ]
            }
          ]
        },
        footer: {
          message: 'Released under the MIT License.',
          copyright: 'Copyright © 2024-present ICACHI'
        }
      }
    },
    en: {
      label: 'English',
      lang: 'en-US',
      link: '/en/',
      title: 'ICACHI',
      description: 'International Chinese Association of Computer Human Interaction',
      themeConfig: {
        nav: [
          { text: 'Home', link: '/en/' },
          { text: 'ByLaws', link: '/en/bylaws' },
          { text: 'About', link: '/en/about' },
          { text: 'News', link: '/en/news/' },
          { text: 'Conference', link: '/en/conference' },
          { text: 'Resource', link: '/en/resource' }
        ],
        sidebar: {
          '/en/bylaws': [
             {
              text: 'ByLaws',
              items: []
            }
          ]
        },
        footer: {
          message: 'Released under the MIT License.',
          copyright: 'Copyright © 2024-present ICACHI'
        }
      }
    }
  },

  themeConfig: {
    socialLinks: [
      { icon: 'github', link: 'https://github.com/icachinext/icachinext.github.io' }
    ],
    search: {
      provider: 'local'
    }
  }
})
