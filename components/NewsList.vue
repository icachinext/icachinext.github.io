<script setup>
import { computed, ref, watch, onMounted } from 'vue'
import { useRoute, useRouter, useData } from 'vitepress'
import { data as allNews } from '../docs/news.data'

const PAGE_SIZE = 10

const route = useRoute()
const router = useRouter()
const { lang } = useData()
const isEn = computed(() => lang.value?.startsWith('en'))

// Scope news to current locale (Chinese = /news/, English = /en/news/)
const localeNews = computed(() => {
  return allNews.filter(n =>
    isEn.value ? n.url.startsWith('/en/news/') : n.url.startsWith('/news/')
  )
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
</script>

<template>
  <div class="news">
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
        <a :href="item.url">
          <time>{{ fmt(item.date) }}</time>
          <div class="body">
            <h3>{{ item.title }}</h3>
            <p v-if="item.excerpt" class="excerpt" v-html="item.excerpt"></p>
            <div v-if="item.tags && item.tags.length" class="tags">
              <span v-for="t in item.tags" :key="t" class="tag">{{ t }}</span>
            </div>
          </div>
          <div v-if="item.cover" class="thumb">
            <img :src="item.cover" :alt="item.title" />
          </div>
          <div v-else class="thumb thumb-empty" />
        </a>
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

.item a {
  display: grid;
  grid-template-columns: 140px 1fr 160px;
  gap: 32px;
  padding: 24px 0;
  text-decoration: none;
  color: inherit;
  align-items: center;
  transition: opacity var(--ic-transition);
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

.item a:hover { opacity: 0.65; }

.item time {
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
  .item a { grid-template-columns: 100px 1fr; }
  .thumb { display: none; }
}

@media (max-width: 480px) {
  .item a { grid-template-columns: 1fr; gap: 6px; }
  .item time { font-size: 12px; }
}
</style>
