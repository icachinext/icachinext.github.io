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

const dateLabel = computed(() => {
  const raw = frontmatter.value.date
  if (!raw) return ''
  if (typeof raw === 'string') return raw.slice(0, 10)
  const parsed = raw instanceof Date ? raw : new Date(raw)
  return Number.isNaN(parsed.getTime()) ? '' : parsed.toISOString().slice(0, 10)
})

const tags = computed(() => {
  const raw = frontmatter.value.tags
  return Array.isArray(raw) ? raw.filter(tag => typeof tag === 'string' && tag) : []
})

function tagHref(tag) {
  const base = isEn.value ? '/en/news/' : '/news/'
  return `${base}?tag=${encodeURIComponent(tag)}`
}
</script>

<template>
  <h1 v-if="frontmatter.title" class="news-title">{{ frontmatter.title }}</h1>
  <div v-if="dateLabel || tags.length || conference" class="news-meta">
    <time v-if="dateLabel" class="news-date" :datetime="dateLabel">{{ dateLabel }}</time>
    <a
      v-for="tag in tags"
      :key="tag"
      class="news-tag"
      :href="tagHref(tag)"
    >{{ tag }}</a>
    <a v-if="conference" :href="threadHref" class="thread-context">
      <span>{{ isEn ? 'Part of' : '所属时间线' }}</span>
      <strong>{{ conference.shortTitle }} Timeline</strong>
      <span aria-hidden="true">→</span>
    </a>
  </div>
</template>

<style scoped>
.news-title {
  margin: 0 0 16px;
  overflow-wrap: anywhere;
}

.news-meta {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
  margin: 0 0 28px;
}

.news-date {
  margin-right: 4px;
  color: var(--vp-c-text-3);
  font-size: 13px;
  font-variant-numeric: tabular-nums;
}

.news-tag,
.thread-context {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 12px;
  border: 1px solid var(--ic-border);
  border-radius: 999px;
  color: var(--vp-c-text-2);
  font-size: 12px;
  line-height: 1.4;
  text-decoration: none;
  transition: border-color var(--ic-transition), color var(--ic-transition);
}

.news-tag:hover,
.thread-context:hover {
  border-color: var(--vp-c-text-1);
  color: var(--vp-c-text-1);
}

.thread-context strong {
  color: var(--vp-c-text-1);
  font-weight: 500;
}
</style>
