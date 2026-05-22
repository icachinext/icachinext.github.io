<script setup>
import { computed } from 'vue'
import boardData from '../data/board.json'

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

function normalizeRole(r) {
  return (r || '').trim()
}

const grouped = computed(() => {
  const map = new Map()
  for (const m of boardData) {
    const r = normalizeRole(m.role)
    if (!map.has(r)) map.set(r, [])
    map.get(r).push(m)
  }
  return ROLE_ORDER
    .map(role => ({ role, members: map.get(role) || [] }))
    .filter(g => g.members.length)
})
</script>

<template>
  <div class="board">
    <section v-for="g in grouped" :key="g.role" class="group">
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
</template>

<style scoped>
.board {
  display: flex;
  flex-direction: column;
  gap: 56px;
  padding: 24px 0;
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
  filter: grayscale(0);
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
</style>
