<script setup>
import { computed } from 'vue'
import { data as allNews } from '../docs/news.data'
import { useSiteData } from './useSiteData'

const { site, resourceList } = useSiteData()
const news = computed(() => site.value.news)
const resourcesCopy = computed(() => site.value.resources)

const top = computed(() => allNews.slice(0, 5))
const topResources = computed(() => resourceList.value.slice(0, 3))

function fmt(date) {
  if (!date) return ''
  const d = new Date(date)
  if (isNaN(d.getTime())) return date
  return d.toISOString().slice(0, 10)
}
</script>

<template>
  <section class="nr ic-section">
    <div class="ic-container nr-grid">
      <!-- News: 2/3 -->
      <div class="news-col">
        <header class="col-head">
          <h2>{{ news.title }}</h2>
        </header>

        <ul class="news-list">
          <li v-for="item in top" :key="item.url" class="news-item">
            <a :href="item.url">
              <time>{{ fmt(item.date) }}</time>
              <div class="news-body">
                <h3>{{ item.title }}</h3>
                <div v-if="item.tags && item.tags.length" class="tags">
                  <span v-for="t in item.tags" :key="t" class="tag">{{ t }}</span>
                </div>
              </div>
              <div v-if="item.cover" class="news-thumb">
                <img :src="item.cover" :alt="item.title" />
              </div>
              <div v-else class="news-thumb news-thumb-empty" />
            </a>
          </li>
          <li v-if="!top.length" class="empty">暂无新闻。</li>
        </ul>

        <a class="ic-link-arrow" :href="news.viewAll.link">{{ news.viewAll.text }}</a>
      </div>

      <!-- Resources: 1/3 -->
      <aside class="res-col">
        <header class="col-head">
          <h2>{{ resourcesCopy.title }}</h2>
        </header>

        <ul class="res-list">
          <li v-for="r in topResources" :key="r.title" class="res-item ic-card">
            <a :href="r.link" target="_blank" rel="noopener">
              <div class="res-body">
                <h4>{{ r.title }}<span class="res-type">{{ r.type }}</span></h4>
                <p>{{ r.description }}</p>
              </div>
              <span class="res-arrow" aria-hidden="true">↓</span>
            </a>
          </li>
        </ul>

        <a class="ic-link-arrow" :href="resourcesCopy.viewAll.link">
          {{ resourcesCopy.viewAll.text }}
        </a>
      </aside>
    </div>
  </section>
</template>

<style scoped>
.nr {
  border-top: 1px solid var(--ic-border);
}

.nr-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 80px;
  align-items: start;
}

.col-head {
  margin-bottom: 28px;
}

.col-head h2 {
  font-size: clamp(22px, 2.4vw, 32px);
  font-weight: 600;
  letter-spacing: -0.02em;
  margin: 0;
  color: var(--vp-c-text-1);
}

/* News list */
.news-list {
  list-style: none;
  padding: 0;
  margin: 0 0 32px;
  border-top: 1px solid var(--ic-border);
}

.news-item { border-bottom: 1px solid var(--ic-border); }

.news-item a {
  display: grid;
  grid-template-columns: 100px 1fr 88px;
  gap: 20px;
  padding: 20px 0;
  text-decoration: none;
  color: inherit;
  align-items: center;
  transition: opacity var(--ic-transition);
}

.news-thumb {
  width: 88px;
  aspect-ratio: 3 / 2;
  border-radius: 4px;
  overflow: hidden;
  background: var(--vp-c-bg-soft);
  flex-shrink: 0;
}

.news-thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.news-thumb-empty {
  background: transparent;
}

.news-item a:hover { opacity: 0.7; }

.news-item time {
  font-size: 13px;
  color: var(--vp-c-text-3);
  font-variant-numeric: tabular-nums;
}

.news-body h3 {
  font-size: 17px;
  font-weight: 500;
  line-height: 1.45;
  margin: 0;
  color: var(--vp-c-text-1);
}

.tags {
  display: flex;
  gap: 8px;
  margin-top: 8px;
  flex-wrap: wrap;
}

.tag {
  font-size: 11px;
  color: var(--vp-c-text-3);
  border: 1px solid var(--ic-border);
  padding: 2px 8px;
  border-radius: 999px;
}

.empty {
  padding: 24px 0;
  color: var(--vp-c-text-3);
  font-size: 14px;
}

/* Resources */
.res-list {
  list-style: none;
  padding: 0;
  margin: 0 0 32px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.res-item a {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 16px;
  align-items: center;
  padding: 16px 20px;
  text-decoration: none;
  color: inherit;
}

.res-body h4 {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
  font-size: 14px;
  font-weight: 500;
  margin: 0 0 4px;
  color: var(--vp-c-text-1);
}

.res-type {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.05em;
  color: var(--vp-c-text-3);
  border: 1px solid var(--ic-border);
  padding: 4px 8px;
  border-radius: 4px;
  flex-shrink: 0;
}

.res-body p {
  font-size: 12px;
  color: var(--vp-c-text-3);
  margin: 0;
  line-height: 1.4;
}

.res-arrow {
  font-size: 16px;
  color: var(--vp-c-text-3);
}

@media (max-width: 960px) {
  .nr-grid { grid-template-columns: 1fr; gap: 64px; }
}

@media (max-width: 600px) {
  .news-item a {
    grid-template-columns: 1fr;
    gap: 6px;
  }
}
</style>
