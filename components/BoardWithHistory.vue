<script setup>
import { ref, computed, watchEffect } from 'vue'
import { useData } from 'vitepress'
import boardData from '../data/board.json'

// ── Role display order ───────────────────────────────────
const ROLE_ORDER = [
  'President',
  'Executive Vice President',
  'Vice President',
  'Secretary General',
  'Deputy Secretary General',
  'Board Member',
  'President of Youth Committee',
  'VP of Youth Committee',
  'Student Board Member',
  'Supervisor',
  'Honorary life President'
]

// ── Locale-aware labels ──────────────────────────────────
const { lang } = useData()
const t = computed(() => lang.value.startsWith('en')
  ? { current: 'Current Board', past: 'Previous Boards', empty: 'No data available.' }
  : { current: '现任理事会', past: '往届理事', empty: '暂无数据' }
)

// ── Load all past-board JSON files at build time ─────────
// Files live in data/past-boards/board-YYYY.json
const pastFiles = import.meta.glob('../data/past-boards/board-*.json', { eager: true })

// ── Mode: 'current' | 'past' ─────────────────────────────
const mode = ref('current')

// ── Extract sorted years from filenames ──────────────────
const pastYears = computed(() =>
  Object.keys(pastFiles)
    .map(path => {
      const m = path.match(/board-(\d{4})\.json$/)
      return m ? parseInt(m[1]) : null
    })
    .filter(Boolean)
    .sort((a, b) => b - a) // newest first
)

// Default to the most-recent year when switching to past
const selectedYear = ref(null)
watchEffect(() => {
  if (!selectedYear.value && pastYears.value.length) {
    selectedYear.value = pastYears.value[0]
  }
})

// ── Helpers ───────────────────────────────────────────────
function groupByRole(members) {
  const map = new Map()
  for (const m of members) {
    const r = (m.role || '').trim()
    if (!map.has(r)) map.set(r, [])
    map.get(r).push(m)
  }
  return ROLE_ORDER
    .map(role => ({ role, members: map.get(role) || [] }))
    .filter(g => g.members.length)
}

// ── Grouped data ──────────────────────────────────────────
const currentGrouped = computed(() => groupByRole(boardData))

const pastGrouped = computed(() => {
  if (!selectedYear.value) return []
  const key = Object.keys(pastFiles).find(p =>
    p.endsWith(`/board-${selectedYear.value}.json`)
  )
  if (!key) return []
  const raw = pastFiles[key]
  const data = raw.default ?? raw
  return groupByRole(Array.isArray(data) ? data : [])
})
</script>

<template>
  <div class="bwh">
    <!-- ── Tab bar ──────────────────────────────────────── -->
    <div class="bwh-tabs" role="tablist">
      <button
        role="tab"
        class="bwh-tab"
        :class="{ active: mode === 'current' }"
        :aria-selected="mode === 'current'"
        @click="mode = 'current'"
      >{{ t.current }}</button>
      <button
        role="tab"
        class="bwh-tab"
        :class="{ active: mode === 'past' }"
        :aria-selected="mode === 'past'"
        @click="mode = 'past'"
      >{{ t.past }}</button>
    </div>

    <!-- ── Current board ───────────────────────────────── -->
    <div v-if="mode === 'current'" class="board" role="tabpanel">
      <section v-for="g in currentGrouped" :key="g.role" class="group">
        <h3 class="group-title">{{ g.role }}</h3>
        <div class="grid">
          <div v-for="m in g.members" :key="m.name" class="member">
            <img :src="m.avatar" :alt="m.name" class="avatar" loading="lazy" />
            <div class="info">
              <h4>{{ m.name }}</h4>
              <p>{{ m.org }}</p>
            </div>
          </div>
        </div>
      </section>
    </div>

    <!-- ── Past boards ─────────────────────────────────── -->
    <div v-else class="board" role="tabpanel">
      <!-- Year pill selector -->
      <div v-if="pastYears.length" class="year-pills">
        <button
          v-for="y in pastYears"
          :key="y"
          class="year-pill"
          :class="{ active: selectedYear === y }"
          @click="selectedYear = y"
        >{{ y }}</button>
      </div>

      <template v-if="pastGrouped.length">
        <section v-for="g in pastGrouped" :key="g.role" class="group">
          <h3 class="group-title">{{ g.role }}</h3>
          <div class="grid">
            <div v-for="m in g.members" :key="m.name" class="member">
              <img :src="m.avatar" :alt="m.name" class="avatar" loading="lazy" />
              <div class="info">
                <h4>{{ m.name }}</h4>
                <p>{{ m.org }}</p>
              </div>
            </div>
          </div>
        </section>
      </template>
      <p v-else class="empty">{{ t.empty }}</p>
    </div>
  </div>
</template>

<style scoped>
/* ── Tab bar ─────────────────────────────────────────────── */
.bwh-tabs {
  display: flex;
  gap: 0;
  border-bottom: 1px solid var(--ic-border);
  margin-bottom: 40px;
}

.bwh-tab {
  padding: 10px 20px;
  background: none;
  border: none;
  border-bottom: 2px solid transparent;
  margin-bottom: -1px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  color: var(--vp-c-text-3);
  transition: color 150ms, border-color 150ms;
  white-space: nowrap;
}

.bwh-tab:hover {
  color: var(--vp-c-text-1);
}

.bwh-tab.active {
  color: var(--vp-c-text-1);
  border-bottom-color: var(--vp-c-text-1);
}

/* ── Year pill selector ──────────────────────────────────── */
.year-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 40px;
}

.year-pill {
  padding: 5px 14px;
  border: 1px solid var(--ic-border);
  border-radius: 999px;
  background: none;
  cursor: pointer;
  font-size: 13px;
  font-weight: 500;
  color: var(--vp-c-text-2);
  transition: all 150ms;
}

.year-pill:hover {
  border-color: var(--ic-border-strong);
  color: var(--vp-c-text-1);
}

.year-pill.active {
  background: var(--ic-border-strong);
  border-color: var(--ic-border-strong);
  color: var(--vp-c-bg);
}

/* ── Board member layout (mirrors BoardMembers.vue) ──────── */
.board {
  display: flex;
  flex-direction: column;
  gap: 56px;
  padding-bottom: 24px;
}

.group-title {
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--vp-c-text-3);
  margin: 0 0 24px;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--ic-border);
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 32px 24px;
}

.member {
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 12px;
  transition: filter var(--ic-transition);
}

.info h4 {
  margin: 0 0 4px;
  font-size: 14px;
  font-weight: 500;
  color: var(--vp-c-text-1);
  line-height: 1.3;
}

.info p {
  margin: 0;
  font-size: 12px;
  color: var(--vp-c-text-3);
  line-height: 1.4;
}

.empty {
  color: var(--vp-c-text-3);
  font-size: 14px;
  padding: 48px 0;
  text-align: center;
}
</style>
