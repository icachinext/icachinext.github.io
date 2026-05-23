<script setup>
import { computed } from 'vue'
import conferenceData from '../data/conferences.json'
import { useSiteData } from './useSiteData'

const { site } = useSiteData()
const copy = computed(() => site.value.conferences)

const sorted = [...conferenceData].sort((a, b) => b.year - a.year)
const featured = sorted[0]
// Only show 3 most recent past conferences
const others = sorted.slice(1, 4)
</script>

<template>
  <section class="confs ic-section">
    <div class="ic-container">
      <header class="confs-head">
        <span class="ic-eyebrow">{{ copy.eyebrow }}</span>
        <h2>{{ copy.title }}</h2>
        <p v-if="copy.titleSub" class="title-sub">
          {{ copy.titleSub }}
        </p>
        <p>{{ copy.subtitle }}</p>
      </header>

      <!-- Featured: latest conference — image 2/3, text 1/3 -->
      <a class="featured ic-card" :href="featured.link" target="_blank" rel="noopener">
        <div
          class="featured-image"
          :style="featured.image ? { backgroundImage: `url(${featured.image})` } : {}"
        >
          <div v-if="!featured.image" class="featured-placeholder">
            <span>{{ featured.year }}</span>
          </div>
        </div>
        <div class="featured-body">
          <span class="year-badge">{{ featured.year }}</span>
          <h3>{{ featured.title }}</h3>
          <p v-if="featured.subtitle" class="conf-subtitle">{{ featured.subtitle }}</p>
          <p class="location">{{ featured.location }}</p>
          <p v-if="featured.dates" class="dates">{{ featured.dates }}</p>
          <span class="ic-link-arrow">访问会议官网</span>
        </div>
      </a>

      <!-- Past 3 conferences -->
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
            :style="c.image ? { backgroundImage: `url(${c.image})` } : {}"
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
  max-width: none;
  margin: 0 auto 56px;
}

.confs-head .ic-eyebrow {
  display: block;
  margin-bottom: 16px;
}

.confs-head h2 {
  font-size: clamp(28px, 3.6vw, 44px);
  font-weight: 600;
  letter-spacing: -0.02em;
  margin: 0 0 16px;
  color: var(--vp-c-text-1);
}

.title-sub {
  font-size: 13px;
  font-weight: 700;
  color: var(--vp-c-text-1);
  letter-spacing: 0.01em;
  margin: 0 0 10px !important;
  line-height: 1.5;
  white-space: nowrap;
}

.confs-head p {
  font-size: 15px;
  color: var(--vp-c-text-2);
  line-height: 1.7;
  margin: 0;
}

/* Featured: image takes 2/3, text 1/3 */
.featured {
  display: grid;
  grid-template-columns: 2fr 1fr;
  align-items: stretch;
  text-decoration: none;
  color: inherit;
  margin-bottom: 40px;
  min-height: 400px;
}

.featured-image {
  background-size: cover;
  background-position: center;
  background-color: var(--vp-c-bg-soft);
  min-height: 360px;
  position: relative;
}

.featured-placeholder {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #1a1a1a 0%, #3a3a3a 100%);
}

.featured-placeholder span {
  font-size: 72px;
  font-weight: 700;
  color: rgba(255,255,255,0.15);
  letter-spacing: -0.04em;
}

.featured-body {
  padding: 48px 40px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 14px;
  background: var(--vp-c-bg);
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
  font-size: clamp(20px, 2vw, 26px);
  font-weight: 600;
  line-height: 1.3;
  margin: 0;
  color: var(--vp-c-text-1);
  letter-spacing: -0.01em;
}

.conf-subtitle {
  font-size: 14px;
  color: var(--vp-c-text-2);
  margin: 0;
  line-height: 1.5;
}

.featured-body .location,
.featured-body .dates {
  color: var(--vp-c-text-2);
  margin: 0;
  font-size: 14px;
}

/* Past 3 grid */
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
  font-size: 15px;
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
  margin-top: 48px;
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
