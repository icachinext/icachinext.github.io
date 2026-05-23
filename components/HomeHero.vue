<script setup>
import { computed, ref, onMounted, nextTick } from 'vue'
import { useSiteData } from './useSiteData'

const { site } = useSiteData()
const hero = computed(() => site.value.hero)
const memberLink = computed(() => site.value.memberLogin.link)

const logoRef  = ref(null)
const titleRef = ref(null) // <h1> — only used for measuring center
const textRef  = ref(null) // .hi-text (both title lines)
const bodyRef  = ref(null) // .hero-body (sub paragraph + CTAs)

onMounted(async () => {
  await nextTick()
  if (!logoRef.value || !titleRef.value || !textRef.value || !bodyRef.value) return

  const logoRect  = logoRef.value.getBoundingClientRect()
  const titleRect = titleRef.value.getBoundingClientRect()

  // How far right does the logo need to move to sit centered on the title?
  const logoMid  = logoRect.left + logoRect.width / 2
  const titleMid = titleRect.left + titleRect.width / 2
  const offset   = titleMid - logoMid

  // Initial state — logo displaced right over title center; all text hidden
  logoRef.value.style.cssText = `transform:translateX(${offset}px);transition:none;`
  textRef.value.style.cssText = `opacity:0;transition:none;`
  bodyRef.value.style.cssText = `opacity:0;transition:none;`

  void logoRef.value.offsetWidth // force reflow

  // ── Animation timing ──────────────────────────────────
  const PAUSE       = 600   // ms  initial hold before logo moves
  const SLIDE       = 900   // ms  logo slide duration
  const FADE        = 500   // ms  content fade-in duration
  // ──────────────────────────────────────────────────────

  // T + PAUSE: logo slides left to natural position
  setTimeout(() => {
    requestAnimationFrame(() => {
      logoRef.value.style.cssText =
        `transform:translateX(0);transition:transform ${SLIDE}ms cubic-bezier(0.25,0.46,0.45,0.94);`
    })
  }, PAUSE)

  // T + PAUSE + SLIDE (logo just landed): all content fades in simultaneously
  setTimeout(() => {
    requestAnimationFrame(() => {
      textRef.value.style.cssText = `opacity:1;transition:opacity ${FADE}ms ease;`
      bodyRef.value.style.cssText = `opacity:1;transition:opacity ${FADE}ms ease;`
    })
  }, PAUSE + SLIDE)
})
</script>

<template>
  <section class="hero">
    <div class="ic-container hero-inner">

      <!-- Brand row: logo animates left, text fades in -->
      <div class="hero-brand">
        <img src="/images/icachi-logo.svg" ref="logoRef" class="hi-logo" alt="ICACHI" />
        <!-- opacity:0 inline so there is no flash before JS runs -->
        <div class="hi-text" ref="textRef" style="opacity:0">
          <h1 class="hero-title" ref="titleRef">{{ hero.title }}</h1>
          <p v-if="hero.titleEn" class="hero-title-en">{{ hero.titleEn }}</p>
        </div>
      </div>

      <!-- Sub-copy + CTAs: hidden until logo lands, then fade in together -->
      <div class="hero-body" ref="bodyRef" style="opacity:0">
        <p class="hero-sub">{{ hero.subtitle }}</p>
        <div class="hero-ctas">
          <a class="ic-btn" :href="hero.primaryCta.link">
            {{ hero.primaryCta.text }}
          </a>
          <a class="ic-btn ic-btn-primary" :href="memberLink">
            加入我们
          </a>
        </div>
      </div>

    </div>
  </section>
</template>

<style scoped>
.hero {
  padding: clamp(100px, 15vw, 180px) 0 clamp(80px, 10vw, 130px);
  background: var(--vp-c-bg);
  overflow: hidden;
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

/* hero-body sits directly inside hero-inner (column flex) */
.hero-body {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
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
  .hero-title    { white-space: normal; }
  .hero-title-en { white-space: normal; font-size: 12px; }
}
</style>
