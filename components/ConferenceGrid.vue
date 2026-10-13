<script setup>
import { computed } from 'vue'
import { useData } from 'vitepress'
import conferenceData from '../data/conferences.json'
import { data as allNews } from '../docs/news.data'
import { timelinePath } from './newsThreads'

const sorted = [...conferenceData].sort((a, b) => b.year - a.year)
const { lang } = useData()
const isEn = computed(() => lang.value?.startsWith('en'))

const localeNews = computed(() => allNews.filter(item =>
  isEn.value ? item.url.startsWith('/en/news/') : item.url.startsWith('/news/')
))

function hasTimeline(thread) {
  return localeNews.value.some(item => item.thread === thread)
}

function timelineHref(thread) {
  return timelinePath(thread, isEn.value)
}
</script>

<template>
  <div class="conf-list">
    <article
      v-for="c in sorted"
      :key="c.year"
      class="row"
    >
      <span class="year">{{ c.year }}</span>
      <div class="body">
        <h3>{{ c.title }}</h3>
        <p class="location">{{ c.location }}</p>
        <div class="actions">
          <a :href="c.link" target="_blank" rel="noopener" class="action">
            {{ isEn ? 'Conference website' : '会议官网' }}
          </a>
          <a
            v-if="hasTimeline(c.thread)"
            :href="timelineHref(c.thread)"
            class="action timeline-action"
          >
            {{ isEn ? 'Timeline' : '时间线' }}
          </a>
        </div>
      </div>
      <div
        class="thumb"
        :style="{ backgroundImage: `url(${c.image})` }"
        role="img"
        :aria-label="c.shortTitle"
      />
    </article>
  </div>
</template>

<style scoped>
.conf-list {
  display: flex;
  flex-direction: column;
  border-top: 1px solid var(--ic-border);
  padding: 24px 0;
}

.row {
  display: grid;
  grid-template-columns: 100px 1fr 160px;
  gap: 32px;
  padding: 28px 0;
  border-bottom: 1px solid var(--ic-border);
  color: inherit;
  align-items: center;
}

.year {
  font-size: 22px;
  font-weight: 500;
  color: var(--vp-c-text-1);
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.01em;
}

.body h3 {
  margin: 0 0 6px;
  font-size: 17px;
  font-weight: 500;
  color: var(--vp-c-text-1);
  line-height: 1.4;
}

.location {
  margin: 0;
  font-size: 13px;
  color: var(--vp-c-text-3);
}

.actions {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 14px;
}

.action {
  display: inline-flex;
  align-items: center;
  min-height: 32px;
  padding: 5px 12px;
  border: 1px solid var(--ic-border);
  border-radius: 999px;
  color: var(--vp-c-text-2);
  font-size: 12px;
  font-weight: 500;
  text-decoration: none;
  transition: border-color var(--ic-transition), color var(--ic-transition);
}

.action:hover {
  border-color: var(--vp-c-text-1);
  color: var(--vp-c-text-1);
}

.timeline-action {
  border-color: var(--vp-c-text-1);
  background: var(--vp-c-text-1);
  color: var(--vp-c-bg);
}

.timeline-action:hover {
  color: var(--vp-c-bg);
  opacity: 0.72;
}

.thumb {
  aspect-ratio: 16 / 10;
  background-size: cover;
  background-position: center;
  background-color: var(--vp-c-bg-soft);
  border-radius: 4px;
}

@media (max-width: 720px) {
  .row {
    grid-template-columns: 64px 1fr;
    gap: 16px;
  }
  .thumb { display: none; }
  .year { font-size: 18px; }
}
</style>
