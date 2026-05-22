<script setup>
import conferenceData from '../data/conferences.json'

const sorted = [...conferenceData].sort((a, b) => b.year - a.year)
</script>

<template>
  <div class="conf-list">
    <a
      v-for="c in sorted"
      :key="c.year"
      :href="c.link"
      target="_blank"
      rel="noopener"
      class="row"
    >
      <span class="year">{{ c.year }}</span>
      <div class="body">
        <h3>{{ c.title }}</h3>
        <p class="location">{{ c.location }}</p>
      </div>
      <div
        class="thumb"
        :style="{ backgroundImage: `url(${c.image})` }"
      ></div>
    </a>
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
  text-decoration: none;
  color: inherit;
  align-items: center;
  transition: opacity var(--ic-transition);
}

.row:hover { opacity: 0.7; }

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
