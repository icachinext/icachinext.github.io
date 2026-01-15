import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "ICACHI",
  description: "International Chinese Association of Computer Human Interaction",
  head: [['link', { rel: 'icon', href: '/images/favicon.ico' }]],

  // Default to Chinese
  lang: 'zh-CN',

  locales: {
    root: {
      label: '简体中文',
      lang: 'zh-CN',
      title: 'ICACHI',
      description: '世界华人华侨人机交互协会',
      themeConfig: {
        logo: '/images/icachi-text.svg',
        nav: [
          { text: '主页', link: '/' },
          { text: '协会章程', link: '/bylaws' },
          { text: '关于我们', link: '/about' },
          { text: '新闻', link: '/news/' },
          { text: '会议', link: '/conference' },
          { text: '资源', link: '/resource' }
        ],
        outline: {
          label: ''
        },
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
          message: `
            <div class="footer-content">
              <div class="footer-section">
                <p><strong>协会联系人：</strong>付志勇</p>
                <p><strong>联系邮箱：</strong><a href="mailto:office@icachi.org">office@icachi.org</a></p>
                <p><strong>协会注册地址：</strong>849 Laurelwood Dr, Waterloo, ON, Canada</p>
              </div>
              <div class="footer-section wechat-section">
                <p><strong>微信公众号：</strong></p>
                <img src="/images/qr.jpg" alt="ICACHI WeChat" class="footer-qr"/>
              </div>
            </div>
          `,
          copyright: 'Copyright © 2012-present ICACHI'
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
        logo: '/images/icachi.svg',
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
          message: `
            <div class="footer-content">
              <div class="footer-section">
                <p><strong>Contact Person:</strong> Prof. Zhiyong Fu</p>
                <p><strong>Email:</strong> <a href="mailto:office@icachi.org">office@icachi.org</a></p>
                <p><strong>Registered Address:</strong> 849 Laurelwood Dr, Waterloo, ON, Canada</p>
              </div>
              <div class="footer-section wechat-section">
                <p><strong>WeChat Official Account:</strong></p>
                <img src="/images/qr.jpg" alt="ICACHI WeChat" class="footer-qr"/>
              </div>
            </div>
          `,
          copyright: 'Copyright © 2012-present ICACHI'
        }
      }
    }
  },

  themeConfig: {
    // Hide site title text (keep logo)
    siteTitle: false,

    // Remove social links (GitHub)
    socialLinks: [],

    search: {
      provider: 'local'
    }
  }
})
