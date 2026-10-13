<script setup lang="ts">
import { computed } from 'vue'
import { useData } from 'vitepress'
import { data as allNews, type NewsItem } from '../docs/news.data'
import { findConferenceThread } from './newsThreads'

const { params, lang } = useData()
const isEn = computed(() => lang.value?.startsWith('en'))
const thread = computed(() => params.value?.thread as string | undefined)
const conference = computed(() => findConferenceThread(thread.value))

const items = computed<NewsItem[]>(() =>
  allNews
    .filter(item => {
      const isCurrentLocale = isEn.value
        ? item.url.startsWith('/en/news/')
        : item.url.startsWith('/news/')
      return isCurrentLocale && item.thread === thread.value
    })
    .sort((a, b) => +new Date(b.date) - +new Date(a.date))
)

const copy = computed(() => isEn.value
  ? {
      official: 'Conference website',
      conferences: 'All conferences',
      updates: 'updates',
      empty: 'No news has been added to this timeline yet.'
    }
  : {
      official: '会议官网',
      conferences: '全部会议',
      updates: '条动态',
      empty: '该时间线暂无新闻。'
    }
)

function formatDate(date: string) {
  const parsed = new Date(date)
  return isNaN(parsed.getTime()) ? date : parsed.toISOString().slice(0, 10)
}
</script>

<template>
  <div class="timeline-page">
    <header v-if="conference" class="timeline-summary">
      <div class="summary-copy">
        <p class="conference-title">{{ conference.title }}</p>
        <p class="conference-meta">
          <span>{{ conference.location }}</span>
          <span v-if="conference.dates">{{ conference.dates }}</span>
          <span>{{ items.length }} {{ copy.updates }}</span>
        </p>
      </div>
      <div class="summary-actions">
        <a :href="conference.link" target="_blank" rel="noopener" class="action primary">
          {{ copy.official }}
        </a>
        <a :href="isEn ? '/en/conference' : '/conference'" class="action">
          {{ copy.conferences }}
        </a>
      </div>
    </header>

    <ol v-if="items.length" class="timeline-list">
      <li v-for="item in items" :key="item.url" class="timeline-item">
        <div class="timeline-rail" aria-hidden="true">
          <span class="timeline-dot" />
        </div>
        <time :datetime="formatDate(item.date)">{{ formatDate(item.date) }}</time>
        <article class="timeline-card">
          <h2><a :href="item.url">{{ item.title }}</a></h2>
          <p v-if="item.excerpt" class="excerpt" v-html="item.excerpt" />
          <div v-if="item.tags.length" class="tags">
            <span v-for="tag in item.tags" :key="tag" class="tag">{{ tag }}</span>
          </div>
        </article>
      </li>
    </ol>

    <p v-else class="empty">{{ copy.empty }}</p>
  </div>
</template>

<style scoped>
.timeline-page {
  padding: 8px 0 80px;
}

.timeline-summary {
  display: flex;
  justify-content: space-between;
  gap: 32px;
  padding: 24px;
  margin: 24px 0 48px;
  border: 1px solid var(--ic-border);
  border-radius: 8px;
  background: var(--vp-c-bg-soft);
}

.summary-copy { min-width: 0; }

.conference-title {
  margin: 0 0 10px;
  color: var(--vp-c-text-1);
  font-size: 17px;
  font-weight: 500;
  line-height: 1.5;
}

.conference-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 18px;
  margin: 0;
  color: var(--vp-c-text-2);
  font-size: 13px;
}

.summary-actions {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-shrink: 0;
}

.action {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 38px;
  padding: 7px 14px;
  border: 1px solid var(--ic-border);
  border-radius: 999px;
  color: var(--vp-c-text-1);
  font-size: 13px;
  font-weight: 500;
  text-decoration: none;
  transition: border-color var(--ic-transition), opacity var(--ic-transition);
}

.action:hover { border-color: var(--vp-c-text-1); }

.action.primary {
  border-color: var(--vp-c-text-1);
  background: var(--vp-c-text-1);
  color: var(--vp-c-bg);
}

.action.primary:hover { opacity: 0.72; }

.timeline-list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.timeline-item {
  display: grid;
  grid-template-columns: 28px 120px minmax(0, 1fr);
  gap: 20px;
  position: relative;
  min-height: 150px;
}

.timeline-rail {
  display: flex;
  justify-content: center;
  position: relative;
}

.timeline-rail::after {
  content: '';
  position: absolute;
  top: 14px;
  bottom: 0;
  width: 1px;
  background: var(--ic-border);
}

.timeline-item:last-child .timeline-rail::after { display: none; }

.timeline-dot {
  position: relative;
  z-index: 1;
  width: 11px;
  height: 11px;
  margin-top: 8px;
  border: 3px solid var(--vp-c-bg);
  border-radius: 50%;
  background: var(--vp-c-text-1);
  box-shadow: 0 0 0 1px var(--vp-c-text-1);
}

.timeline-item time {
  padding-top: 3px;
  color: var(--vp-c-text-3);
  font-size: 13px;
  font-variant-numeric: tabular-nums;
}

.timeline-card {
  padding: 0 0 42px;
  border-bottom: 1px solid var(--ic-border);
}

.timeline-item:last-child .timeline-card { border-bottom: 0; }

.timeline-card h2 {
  margin: 0 0 10px;
  border: 0;
  padding: 0;
  font-size: 20px;
  font-weight: 500;
  line-height: 1.45;
}

.timeline-card h2 a {
  color: var(--vp-c-text-1);
  text-decoration: none;
  transition: opacity var(--ic-transition);
}

.timeline-card h2 a:hover { opacity: 0.65; }

.excerpt {
  margin: 0;
  color: var(--vp-c-text-2);
  font-size: 14px;
  line-height: 1.7;
}

.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 14px;
}

.tag {
  padding: 2px 8px;
  border: 1px solid var(--ic-border);
  border-radius: 999px;
  color: var(--vp-c-text-3);
  font-size: 11px;
}

.empty {
  padding: 64px 0;
  border-top: 1px solid var(--ic-border);
  color: var(--vp-c-text-3);
  text-align: center;
}

@media (max-width: 720px) {
  .timeline-summary {
    flex-direction: column;
    margin-bottom: 36px;
  }

  .summary-actions { align-items: stretch; }

  .timeline-item {
    grid-template-columns: 22px minmax(0, 1fr);
    gap: 14px;
  }

  .timeline-item time {
    grid-column: 2;
    margin-bottom: 7px;
    padding-top: 0;
  }

  .timeline-rail {
    grid-row: 1 / span 2;
  }

  .timeline-card {
    grid-column: 2;
    padding-bottom: 34px;
  }

  .timeline-card h2 { font-size: 18px; }
}

@media (max-width: 480px) {
  .timeline-summary { padding: 20px; }
  .summary-actions { flex-direction: column; }
}
</style>
