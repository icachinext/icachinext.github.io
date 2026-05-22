<script setup>
import { computed } from 'vue'
import { useSiteData } from './useSiteData'

const { site } = useSiteData()
const hero = computed(() => site.value.hero)
</script>

<template>
  <section class="hero">
    <div class="ic-container hero-inner">
      <span class="ic-eyebrow">{{ hero.eyebrow }}</span>
      <h1 class="hero-title">{{ hero.title }}</h1>
      <p class="hero-sub">{{ hero.subtitle }}</p>
      <div class="hero-ctas">
        <a class="ic-btn" :href="hero.primaryCta.link">
          {{ hero.primaryCta.text }} <span aria-hidden="true">→</span>
        </a>
        <a class="ic-link-arrow" :href="hero.secondaryCta.link">
          {{ hero.secondaryCta.text }}
        </a>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero {
  padding: clamp(120px, 18vw, 220px) 0 clamp(80px, 12vw, 140px);
  background: var(--vp-c-bg);
}

.hero-inner {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.hero-title {
  font-size: clamp(40px, 6vw, 76px);
  line-height: 1.05;
  font-weight: 600;
  letter-spacing: -0.03em;
  margin: 0 0 24px;
  max-width: 14ch;
  color: var(--vp-c-text-1);
}

.hero-sub {
  font-size: clamp(16px, 1.4vw, 19px);
  line-height: 1.65;
  color: var(--vp-c-text-2);
  max-width: 640px;
  margin: 0 0 40px;
}

.hero-ctas {
  display: flex;
  align-items: center;
  gap: 24px;
  flex-wrap: wrap;
  justify-content: center;
}
</style>
