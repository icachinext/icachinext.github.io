<script setup>
import { computed, ref, onMounted, nextTick } from 'vue'
import { useSiteData } from './useSiteData'

const { site } = useSiteData()
const hero = computed(() => site.value.hero)
const memberLink = computed(() => site.value.memberLogin.link)

const stageRef = ref(null)
const logoRef  = ref(null)
const textRef  = ref(null)

onMounted(async () => {
  await nextTick()
  if (!stageRef.value || !logoRef.value || !textRef.value) return

  const logoRect  = logoRef.value.getBoundingClientRect()
  const stageRect = stageRef.value.getBoundingClientRect()

  // Offset needed to center the logo within the stage
  const logoCenter  = logoRect.left + logoRect.width / 2
  const stageCenter = stageRect.left + stageRect.width / 2
  const offset      = stageCenter - logoCenter

  // Initial state — no transition yet
  logoRef.value.style.cssText = `transform:translateX(${offset}px);transition:none;`
  textRef.value.style.cssText = `opacity:0;transform:translateX(${offset * 0.5}px);transition:none;`

  void logoRef.value.offsetWidth // force reflow

  // Animate to natural positions
  requestAnimationFrame(() => requestAnimationFrame(() => {
    logoRef.value.style.cssText =
      'transform:translateX(0);transition:transform 900ms cubic-bezier(0.25,0.46,0.45,0.94);'
    textRef.value.style.cssText =
      'opacity:1;transform:translateX(0);transition:opacity 700ms 250ms ease,transform 700ms 250ms ease;'
  }))
})
</script>

<template>
  <section class="hero">
    <div class="ic-container hero-inner">

      <!-- Animated brand: logo slides left, text slides from logo to right -->
      <div class="hero-stage" ref="stageRef">
        <div class="hero-brand">
          <img src="/images/icachi-logo.svg" ref="logoRef" class="hi-logo" alt="ICACHI" />
          <div class="hi-text" ref="textRef">
            <h1 class="hero-title">{{ hero.title }}</h1>
            <p v-if="hero.titleEn" class="hero-title-en">{{ hero.titleEn }}</p>
          </div>
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
  overflow: hidden; /* contain logo during slide-in */
}

.hero-inner {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

/* Stage: full width reference for centering calculation */
.hero-stage {
  width: 100%;
  display: flex;
  justify-content: center;
  margin-bottom: 28px;
}

.hero-brand {
  display: inline-flex;
  align-items: center;
  gap: 32px;
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
}

.hero-title-en {
  font-size: clamp(12px, 0.9vw, 14px);
  font-weight: 600;
  letter-spacing: 0.01em;
  color: var(--vp-c-text-1);
  margin: 0;
  opacity: 0.55;
  line-height: 1.5;
  max-width: 52ch;
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

/* Outline button (primary CTA) */
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

@media (max-width: 640px) {
  .hero-brand { flex-direction: column; gap: 20px; text-align: center; }
  .hi-text { text-align: center; }
  .hi-logo { height: 60px; }
}
</style>
