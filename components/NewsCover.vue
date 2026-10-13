<script setup>
import { computed } from 'vue'
import { useData } from 'vitepress'
import { findConferenceThread, timelinePath } from './newsThreads'

const { frontmatter, lang } = useData()
const isEn = computed(() => lang.value?.startsWith('en'))
const conference = computed(() => findConferenceThread(frontmatter.value.thread))
const threadHref = computed(() => conference.value
  ? timelinePath(conference.value.thread, isEn.value)
  : '')
</script>

<template>
  <a v-if="conference" :href="threadHref" class="thread-context">
    <span>{{ isEn ? 'Part of' : '所属时间线' }}</span>
    <strong>{{ conference.shortTitle }} Timeline</strong>
    <span aria-hidden="true">→</span>
  </a>
  <div v-if="frontmatter.cover" class="news-cover">
    <img :src="frontmatter.cover" :alt="frontmatter.title || ''" />
  </div>
</template>

<style scoped>
.thread-context {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin: 0 0 20px;
  padding: 6px 12px;
  border: 1px solid var(--ic-border);
  border-radius: 999px;
  color: var(--vp-c-text-2);
  font-size: 12px;
  text-decoration: none;
  transition: border-color var(--ic-transition), color var(--ic-transition);
}

.thread-context:hover {
  border-color: var(--vp-c-text-1);
  color: var(--vp-c-text-1);
}

.thread-context strong {
  color: var(--vp-c-text-1);
  font-weight: 500;
}

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
