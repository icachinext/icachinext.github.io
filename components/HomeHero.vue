<script setup>
import { computed, ref, onMounted, nextTick } from 'vue'
import { useSiteData } from './useSiteData'

const { site } = useSiteData()
const hero = computed(() => site.value.hero)
const memberLink = computed(() => site.value.memberLogin.link)

const logoRef  = ref(null)
const textRef  = ref(null)
const titleRef = ref(null) // measures center of 世界华人华侨人机交互协会

onMounted(async () => {
  await nextTick()
  if (!logoRef.value || !textRef.value || !titleRef.value) return

  const logoRect  = logoRef.value.getBoundingClientRect()
  const titleRect = titleRef.value.getBoundingClientRect()

  // How far right must the logo travel to center over the title text?
  const logoMid  = logoRect.left + logoRect.width / 2
  const titleMid = titleRect.left + titleRect.width / 2
  const offset   = titleMid - logoMid // positive = logo shifts rightward

  // Initial state: logo centered on title; text hidden and pulled left (opposite side)
  logoRef.value.style.cssText = `transform:translateX(${offset}px);transition:none;`
  textRef.value.style.cssText = `opacity:0;transform:translateX(-${Math.abs(offset) * 0.55}px);transition:none;`

  void logoRef.value.offsetWidth // force reflow

  // After 1 s pause: logo slides LEFT to natural position,
  // text slides RIGHT into natural position — diverging from center
  setTimeout(() => {
    requestAnimationFrame(() => {
      logoRef.value.style.cssText =
        'transform:translateX(0);transition:transform 1800ms cubic-bezier(0.25,0.46,0.45,0.94);'
      textRef.value.style.cssText =
        'opacity:1;transform:translateX(0);transition:opacity 1400ms 200ms ease,transform 1400ms 200ms ease;'
    })
  }, 1000)
})
</script>

<template>
  <section class="hero">
    <div class="ic-container hero-inner">

      <!-- Brand: logo and titles animate apart from the center -->
      <div class="hero-brand">
        <img src="/images/icachi-logo.svg" ref="logoRef" class="hi-logo" alt="ICACHI" />
        <div class="hi-text" ref="textRef">
          <h1 class="hero-title" ref="titleRef">{{ hero.title }}</h1>
          <p v-if="hero.titleEn" class="hero-title-en">{{ hero.titleEn }}</p>
        </div>
      </div>

      <p class="hero-sub">{{ hero.subtitle }}</p>

      <div class="hero-ctas">
        <a class="ic-btn" :href="hero.primaryCta.link">
          {{ hero.primaryCta.text }} <span aria-hidden="true">→</span>
        </a>
        <a class="ic-btn ic-btn-primary" :href="memberLink">
          加入我们 <span aria-hidden="true">→</span>
        </a>
      </div>

    </div>
  </section>
</template>

<style scoped>
.hero {
  padding: clamp(100px, 15vw, 180px) 0 clamp(80px, 10vw, 130px);
  background: var(--vp-c-bg);
  overflow: hidden; /* clip logo during its slide-in */
}

.hero-inner {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.hero-brand {
  display: inline-flex;
  align-items: center;
  gap: 32px;
  margin-bottom: 28px;
}

.hi-logo {
  height: 80px;
  width: auto;
  flex-shrink: 0;
}

.hi-text {
  text-align: left;
}

.hero-title {
  font-size: clamp(28px, 4vw, 56px);
  line-height: 1.1;
  font-weight: 600;
  letter-spacing: -0.03em;
  margin: 0 0 8px;
  color: var(--vp-c-text-1);
  white-space: nowrap;
}

.hero-title-en {
  font-size: clamp(11px, 0.85vw, 13px);
  font-weight: 500;
  letter-spacing: 0.01em;
  color: var(--vp-c-text-1);
  margin: 0;
  opacity: 0.5;
  line-height: 1.5;
  white-space: nowrap;
}

.hero-sub {
  font-size: clamp(15px, 1.3vw, 18px);
  line-height: 1.75;
  color: var(--vp-c-text-2);
  max-width: 640px;
  margin: 0 0 40px;
  text-align: center;
}

.hero-ctas {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
  justify-content: center;
}

/* Outline button */
.ic-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 24px;
  border: 1px solid var(--ic-border-strong);
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  font-size: 15px;
  font-weight: 500;
  border-radius: 999px;
  text-decoration: none;
  transition: all var(--ic-transition);
}

.ic-btn:hover {
  background: var(--ic-border-strong);
  color: var(--vp-c-bg);
}

/* Filled button (加入我们) */
.ic-btn-primary {
  background: var(--ic-border-strong);
  color: var(--vp-c-bg);
  border-color: var(--ic-border-strong);
}

.ic-btn-primary:hover {
  opacity: 0.75;
  background: var(--ic-border-strong);
  color: var(--vp-c-bg);
}

@media (max-width: 768px) {
  .hero-brand { flex-direction: column; gap: 20px; text-align: center; }
  .hi-text { text-align: center; }
  .hi-logo { height: 60px; }
  /* Allow wrapping on small screens */
  .hero-title    { white-space: normal; }
  .hero-title-en { white-space: normal; font-size: 12px; }
}
</style>
