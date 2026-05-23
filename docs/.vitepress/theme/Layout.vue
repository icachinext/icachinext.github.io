<script setup>
import { onMounted, nextTick } from 'vue'
import DefaultTheme from 'vitepress/theme'
import { useSiteData } from '../../../components/useSiteData'
import SiteFooter from '../../../components/SiteFooter.vue'
import WeChatFloat from '../../../components/WeChatFloat.vue'

const { Layout } = DefaultTheme
const { site } = useSiteData()

// Physically reorder navbar: [menu][login][search][locale]
// CSS `order` fights scoped VitePress attributes; DOM reordering is definitive.
function fixNavOrder() {
  const body = document.querySelector('.VPNavBar .content-body')
  if (!body) return

  const menu  = body.querySelector('.menu')
  const login = body.querySelector('.ic-member-login')
  const search = body.querySelector('.search')
  // extra = mobile overflow flyout (shows 768–1279 px); we don't need it
  // because we show nav items + search individually at all desktop widths.
  const extra = body.querySelector('.extra')

  if (extra) extra.style.setProperty('display', 'none', 'important')

  // Re-insert in desired order: menu → login → search
  // translations and hamburger keep their natural positions (end of list)
  if (menu)   body.insertBefore(menu,   body.firstChild)
  if (login)  menu  ? menu.after(login)   : body.insertBefore(login,  body.firstChild)
  if (search) login ? login.after(search) : body.appendChild(search)
}

onMounted(async () => {
  await nextTick()
  fixNavOrder()
})
</script>

<template>
  <Layout>
    <template #nav-bar-content-after>
      <a
        class="ic-member-login"
        :href="site.memberLogin.link"
        target="_blank"
        rel="noopener"
        data-placeholder="member-login"
      >
        {{ site.memberLogin.text }}
      </a>
    </template>

    <template #layout-bottom>
      <SiteFooter />
      <WeChatFloat />
    </template>
  </Layout>
</template>
