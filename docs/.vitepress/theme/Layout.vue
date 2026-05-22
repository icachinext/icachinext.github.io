<script setup>
import DefaultTheme from 'vitepress/theme'
import { useSiteData } from '../../../components/useSiteData'
import SiteFooter from '../../../components/SiteFooter.vue'

const { Layout } = DefaultTheme
const { site } = useSiteData()
</script>

<template>
  <Layout>
    <template #nav-bar-content-after>
      <a
        class="ic-member-login"
        :href="site.memberLogin.link"
        data-placeholder="member-login"
      >
        {{ site.memberLogin.text }}
      </a>
    </template>

    <template #layout-bottom>
      <SiteFooter />
    </template>
  </Layout>
</template>
