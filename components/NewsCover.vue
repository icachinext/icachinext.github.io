<script setup>
import { useData } from 'vitepress'
const { frontmatter } = useData()
</script>

<template>
  <div v-if="frontmatter.cover" class="news-cover">
    <img :src="frontmatter.cover" :alt="frontmatter.title || ''" />
  </div>
</template>

<style scoped>
.news-cover {
  width: 100%;
  margin: 0 0 36px;
  border-radius: 8px;
  overflow: hidden;
  background: var(--vp-c-bg-soft);
}

.news-cover img {
  width: 100%;
  max-height: 420px;
  object-fit: cover;
  display: block;
}
</style>
