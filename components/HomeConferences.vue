<script setup>
import { computed } from 'vue'
import conferenceData from '../data/conferences.json'
import { useSiteData } from './useSiteData'

const { site } = useSiteData()
const copy = computed(() => site.value.conferences)

const sorted = [...conferenceData].sort((a, b) => b.year - a.year)
const featured = sorted[0]
const others = sorted.slice(1)
</script>

<template>
  <section class="confs ic-section">
    <div class="ic-container">
      <header class="confs-head">
        <span class="ic-eyebrow">{{ copy.eyebrow }}</span>
        <h2>{{ copy.title }}</h2>
        <p>{{ copy.subtitle }}</p>
      </header>

      <a class="featured ic-card" :href="featured.link" target="_blank" rel="noopener">
        <div
          class="featured-image"
          :style="{ backgroundImage: `url(${featured.image})` }"
        ></div>
        <div class="featured-body">
          <span class="year-badge">{{ featured.year }}</span>
          <h3>{{ featured.title }}</h3>
          <p class="location">{{ featured.location }}</p>
          <span class="ic-link-arrow">访问会议官网</span>
        </div>
      </a>

      <div class="grid">
        <a
          v-for="c in others"
          :key="c.year"
          :href="c.link"
          target="_blank"
          rel="noopener"
          class="conf ic-card"
        >
          <div
            class="conf-image"
            :style="{ backgroundImage: `url(${c.image})` }"
          ></div>
          <div class="conf-body">
            <span class="year-badge sm">{{ c.year }}</span>
            <h4>{{ c.title }}</h4>
            <p class="location">{{ c.location }}</p>
          </div>
        </a>
      </div>

      <div class="cta-row">
        <a class="ic-link-arrow" :href="copy.viewAll.link">{{ copy.viewAll.text }}</a>
      </div>
    </div>
  </section>
</template>

<style scoped>
.confs {
  border-top: 1px solid var(--ic-border);
  background: var(--vp-c-bg-alt);
}

.confs-head {
  text-align: center;
  max-width: 720px;
  margin: 0 auto 64px;
}

.confs-head h2 {
  font-size: clamp(28px, 3.6vw, 44px);
  font-weight: 600;
  letter-spacing: -0.02em;
  margin: 0 0 16px;
  color: var(--vp-c-text-1);
}

.confs-head p {
  font-size: 16px;
  color: var(--vp-c-text-2);
  line-height: 1.7;
  margin: 0;
}

.featured {
  display: grid;
  grid-template-columns: 1.1fr 1fr;
  align-items: stretch;
  text-decoration: none;
  color: inherit;
  margin-bottom: 48px;
  min-height: 360px;
}

.featured-image {
  background-size: cover;
  background-position: center;
  min-height: 320px;
}

.featured-body {
  padding: 48px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 16px;
}

.year-badge {
  display: inline-block;
  border: 1px solid var(--ic-border-strong);
  color: var(--vp-c-text-1);
  font-size: 13px;
  font-weight: 500;
  padding: 4px 10px;
  border-radius: 999px;
  width: fit-content;
  letter-spacing: 0.02em;
}

.year-badge.sm {
  font-size: 12px;
  padding: 2px 8px;
}

.featured-body h3 {
  font-size: clamp(22px, 2.2vw, 30px);
  font-weight: 600;
  line-height: 1.25;
  margin: 0;
  color: var(--vp-c-text-1);
  letter-spacing: -0.01em;
}

.featured-body .location {
  color: var(--vp-c-text-2);
  margin: 0;
  font-size: 15px;
}

.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.conf {
  text-decoration: none;
  color: inherit;
  display: flex;
  flex-direction: column;
}

.conf-image {
  aspect-ratio: 16 / 10;
  background-size: cover;
  background-position: center;
  background-color: var(--vp-c-bg-soft);
}

.conf-body {
  padding: 20px 24px 24px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.conf-body h4 {
  font-size: 16px;
  font-weight: 600;
  line-height: 1.4;
  margin: 0;
  color: var(--vp-c-text-1);
}

.conf-body .location {
  font-size: 13px;
  color: var(--vp-c-text-3);
  margin: 0;
}

.cta-row {
  text-align: center;
  margin-top: 56px;
}

@media (max-width: 960px) {
  .featured { grid-template-columns: 1fr; }
  .featured-body { padding: 32px; }
  .grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 600px) {
  .grid { grid-template-columns: 1fr; }
}
</style>
