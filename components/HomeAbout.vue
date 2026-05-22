<script setup>
import { computed } from 'vue'
import { useSiteData } from './useSiteData'

const { site } = useSiteData()
const about = computed(() => site.value.about)
</script>

<template>
  <section class="about ic-section">
    <div class="ic-container about-inner">
      <span class="ic-eyebrow">{{ about.eyebrow }}</span>
      <h2 class="about-title">{{ about.title }}</h2>
      <p class="about-summary">{{ about.summary }}</p>
      <a class="ic-link-arrow" :href="about.more.link">{{ about.more.text }}</a>
    </div>
  </section>
</template>

<style scoped>
.about {
  border-top: 1px solid var(--ic-border);
}

.about-inner {
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.about-title {
  font-size: clamp(28px, 3.6vw, 44px);
  font-weight: 600;
  letter-spacing: -0.02em;
  line-height: 1.2;
  margin: 0 0 28px;
  max-width: 18ch;
  color: var(--vp-c-text-1);
}

.about-summary {
  font-size: clamp(16px, 1.3vw, 18px);
  line-height: 1.75;
  color: var(--vp-c-text-2);
  max-width: 720px;
  margin: 0 0 32px;
}
</style>
