<script setup>
import { computed, ref, watch, onMounted } from 'vue'
import { useRoute, useData } from 'vitepress'
import { data as allNews } from '../docs/news.data'
import { conferenceThreads, findConferenceThread, timelinePath } from './newsThreads'

const PAGE_SIZE = 10

const route = useRoute()
const { lang } = useData()
const isEn = computed(() => lang.value?.startsWith('en'))

// Scope news to current locale (Chinese = /news/, English = /en/news/)
const localeNews = computed(() => {
  return allNews.filter(n =>
    isEn.value ? n.url.startsWith('/en/news/') : n.url.startsWith('/news/')
  )
})

const pinnedTimeline = computed(() => conferenceThreads.find(conference =>
  conference.timelinePinned &&
  localeNews.value.some(item => item.thread === conference.thread)
))

const pinnedItems = computed(() => {
  if (!pinnedTimeline.value) return []
  return localeNews.value.filter(item => item.thread === pinnedTimeline.value.thread)
})

const allTags = computed(() => {
  const set = new Set()
  localeNews.value.forEach(n => (n.tags || []).forEach(t => set.add(t)))
  return [...set].sort()
})

const activeTag = ref('')
const currentPage = ref(1)

function syncFromUrl() {
  const search = typeof window !== 'undefined' ? window.location.search : ''
  const params = new URLSearchParams(search)
  activeTag.value = params.get('tag') || ''
  const p = parseInt(params.get('page') || '1', 10)
  currentPage.value = isNaN(p) || p < 1 ? 1 : p
}

onMounted(syncFromUrl)
watch(() => route.path, syncFromUrl)

function pushUrl() {
  if (typeof window === 'undefined') return
  const params = new URLSearchParams()
  if (activeTag.value) params.set('tag', activeTag.value)
  if (currentPage.value > 1) params.set('page', String(currentPage.value))
  const qs = params.toString()
  const url = window.location.pathname + (qs ? '?' + qs : '')
  window.history.replaceState({}, '', url)
}

const filtered = computed(() => {
  if (!activeTag.value) return localeNews.value
  return localeNews.value.filter(n => (n.tags || []).includes(activeTag.value))
})

const totalPages = computed(() => Math.max(1, Math.ceil(filtered.value.length / PAGE_SIZE)))

const pageItems = computed(() => {
  const start = (currentPage.value - 1) * PAGE_SIZE
  return filtered.value.slice(start, start + PAGE_SIZE)
})

function setTag(t) {
  activeTag.value = activeTag.value === t ? '' : t
  currentPage.value = 1
  pushUrl()
}

function goto(p) {
  if (p < 1 || p > totalPages.value) return
  currentPage.value = p
  pushUrl()
  if (typeof window !== 'undefined') {
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
}

function fmt(date) {
  if (!date) return ''
  const d = new Date(date)
  return isNaN(d.getTime()) ? date : d.toISOString().slice(0, 10)
}

function threadConference(thread) {
  return findConferenceThread(thread)
}

function threadHref(thread) {
  return timelinePath(thread, isEn.value)
}
</script>

<template>
  <div class="news">
    <a
      v-if="pinnedTimeline"
      :href="threadHref(pinnedTimeline.thread)"
      class="pinned-timeline"
    >
      <div>
        <span class="pinned-eyebrow">{{ isEn ? 'Featured timeline' : '置顶时间线' }}</span>
        <h2>{{ pinnedTimeline.shortTitle }} Timeline</h2>
        <p>{{ pinnedTimeline.title }}</p>
      </div>
      <div class="pinned-meta">
        <span>{{ pinnedItems.length }} {{ isEn ? 'updates' : '条动态' }}</span>
        <time v-if="pinnedItems[0]">{{ fmt(pinnedItems[0].date) }}</time>
        <strong>{{ isEn ? 'View timeline →' : '查看时间线 →' }}</strong>
      </div>
    </a>

    <div v-if="allTags.length" class="filter-row">
      <button
        class="chip"
        :class="{ active: !activeTag }"
        @click="setTag('')"
      >{{ isEn ? 'All' : '全部' }}</button>
      <button
        v-for="t in allTags"
        :key="t"
        class="chip"
        :class="{ active: activeTag === t }"
        @click="setTag(t)"
      >{{ t }}</button>
    </div>

    <ul class="list">
      <li v-for="item in pageItems" :key="item.url" class="item">
        <div class="item-row">
          <time>{{ fmt(item.date) }}</time>
          <div class="body">
            <h3><a :href="item.url" class="article-link">{{ item.title }}</a></h3>
            <p v-if="item.excerpt" class="excerpt" v-html="item.excerpt"></p>
            <div v-if="item.thread || (item.tags && item.tags.length)" class="tags">
              <a
                v-if="item.thread && threadConference(item.thread)"
                :href="threadHref(item.thread)"
                class="tag thread-tag"
              >{{ threadConference(item.thread).shortTitle }} Timeline</a>
              <span v-for="t in item.tags" :key="t" class="tag">{{ t }}</span>
            </div>
          </div>
          <a v-if="item.cover" :href="item.url" class="thumb" tabindex="-1" aria-hidden="true">
            <img :src="item.cover" :alt="item.title" />
          </a>
          <div v-else class="thumb thumb-empty" />
        </div>
      </li>
      <li v-if="!pageItems.length" class="empty">
        {{ isEn ? 'No news.' : '暂无新闻。' }}
      </li>
    </ul>

    <nav v-if="totalPages > 1" class="pager">
      <button class="page-btn" :disabled="currentPage === 1" @click="goto(currentPage - 1)">
        {{ isEn ? 'Previous' : '上一页' }}
      </button>
      <span class="page-info">{{ currentPage }} / {{ totalPages }}</span>
      <button class="page-btn" :disabled="currentPage === totalPages" @click="goto(currentPage + 1)">
        {{ isEn ? 'Next' : '下一页' }}
      </button>
    </nav>
  </div>
</template>

<style scoped>
.news { padding: 24px 0 80px; }

.pinned-timeline {
  display: flex;
  justify-content: space-between;
  gap: 32px;
  margin-bottom: 32px;
  padding: 28px 30px;
  border: 1px solid var(--vp-c-text-1);
  border-radius: 8px;
  background: var(--vp-c-text-1);
  color: var(--vp-c-bg);
  text-decoration: none;
  transition: opacity var(--ic-transition);
}

.pinned-timeline:hover { opacity: 0.82; }

.pinned-eyebrow {
  display: block;
  margin-bottom: 8px;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.08em;
  opacity: 0.65;
  text-transform: uppercase;
}

.pinned-timeline h2 {
  margin: 0 0 8px;
  border: 0;
  padding: 0;
  color: inherit;
  font-size: 24px;
  line-height: 1.3;
}

.pinned-timeline p {
  margin: 0;
  color: inherit;
  font-size: 13px;
  line-height: 1.5;
  opacity: 0.7;
}

.pinned-meta {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  justify-content: center;
  gap: 5px;
  flex-shrink: 0;
  font-size: 12px;
}

.pinned-meta span,
.pinned-meta time { opacity: 0.65; }

.pinned-meta strong {
  margin-top: 5px;
  font-size: 13px;
  font-weight: 500;
}

.filter-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 32px;
}

.chip {
  font-size: 13px;
  padding: 6px 14px;
  border-radius: 999px;
  border: 1px solid var(--ic-border);
  background: var(--vp-c-bg);
  color: var(--vp-c-text-2);
  cursor: pointer;
  transition: all var(--ic-transition);
}

.chip:hover { border-color: var(--vp-c-text-2); color: var(--vp-c-text-1); }

.chip.active {
  background: var(--vp-c-text-1);
  color: var(--vp-c-bg);
  border-color: var(--vp-c-text-1);
}

.list {
  list-style: none;
  margin: 0;
  padding: 0;
  border-top: 1px solid var(--ic-border);
}

.item { border-bottom: 1px solid var(--ic-border); }

.item-row {
  display: grid;
  grid-template-columns: 140px 1fr 160px;
  gap: 32px;
  padding: 24px 0;
  color: inherit;
  align-items: center;
}

.thumb {
  width: 160px;
  aspect-ratio: 3 / 2;
  border-radius: 4px;
  overflow: hidden;
  background: var(--vp-c-bg-soft);
  flex-shrink: 0;
}

.thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.thumb-empty {
  background: transparent;
}

.item-row > time {
  font-size: 13px;
  color: var(--vp-c-text-3);
  font-variant-numeric: tabular-nums;
}

.body h3 {
  font-size: 18px;
  font-weight: 500;
  line-height: 1.4;
  margin: 0 0 8px;
  color: var(--vp-c-text-1);
}

.article-link {
  color: inherit;
  text-decoration: none;
  transition: opacity var(--ic-transition);
}

.article-link:hover { opacity: 0.65; }

.excerpt {
  font-size: 14px;
  color: var(--vp-c-text-2);
  line-height: 1.6;
  margin: 0;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.tags {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-top: 10px;
}

.tag {
  font-size: 11px;
  color: var(--vp-c-text-3);
  border: 1px solid var(--ic-border);
  padding: 2px 8px;
  border-radius: 999px;
}

.thread-tag {
  color: var(--vp-c-text-2);
  text-decoration: none;
  transition: border-color var(--ic-transition), color var(--ic-transition);
}

.thread-tag:hover {
  border-color: var(--vp-c-text-1);
  color: var(--vp-c-text-1);
}

.empty {
  padding: 48px 0;
  text-align: center;
  color: var(--vp-c-text-3);
}

.pager {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 16px;
  margin-top: 48px;
}

.page-btn {
  padding: 8px 18px;
  border: 1px solid var(--ic-border);
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  border-radius: 999px;
  cursor: pointer;
  font-size: 13px;
  transition: all var(--ic-transition);
}

.page-btn:not(:disabled):hover {
  border-color: var(--vp-c-text-1);
}

.page-btn:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}

.page-info {
  font-size: 13px;
  color: var(--vp-c-text-2);
  font-variant-numeric: tabular-nums;
}

@media (max-width: 720px) {
  .item-row { grid-template-columns: 100px 1fr; }
  .thumb { display: none; }
}

@media (max-width: 480px) {
  .pinned-timeline { flex-direction: column; padding: 24px; }
  .pinned-meta { align-items: flex-start; }
  .item-row { grid-template-columns: 1fr; gap: 6px; }
  .item-row > time { font-size: 12px; }
}
</style>
