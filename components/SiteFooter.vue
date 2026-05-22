<script setup>
import { computed, ref, onMounted, onUnmounted } from 'vue'
import { useSiteData } from './useSiteData'

const { site } = useSiteData()

const footer = computed(() => site.value.footer)
const copyright = computed(() =>
  footer.value.copyright.replace('{{year}}', String(new Date().getFullYear()))
)

// Back-to-top
const showBackTop = ref(false)

function onScroll() {
  showBackTop.value = window.scrollY > 400
}

function scrollTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

onMounted(() => window.addEventListener('scroll', onScroll, { passive: true }))
onUnmounted(() => window.removeEventListener('scroll', onScroll))
</script>

<template>
  <footer class="ic-footer">
    <div class="ic-container ic-footer-inner">
      <div class="ic-footer-brand">
        <img src="/images/icachi.svg" alt="ICACHI" class="ic-footer-logo" />
        <p class="ic-footer-tagline">{{ footer.tagline }}</p>
      </div>

      <div class="ic-footer-cols">
        <div v-for="col in footer.columns" :key="col.heading" class="ic-footer-col">
          <h4>{{ col.heading }}</h4>
          <ul>
            <li v-for="l in col.links" :key="l.text">
              <a :href="l.link">{{ l.text }}</a>
            </li>
            <li v-for="t in col.text || []" :key="t" class="ic-footer-text">{{ t }}</li>
          </ul>
        </div>

      </div>
    </div>

    <div class="ic-container ic-footer-bottom">
      <span>{{ copyright }}</span>
    </div>
  </footer>

  <!-- Back to top -->
  <button
    class="ic-back-to-top"
    :class="{ visible: showBackTop }"
    aria-label="回到顶部"
    @click="scrollTop"
  >
    ↑
  </button>
</template>

<style scoped>
.ic-footer {
  background: #0a0a0a;
  padding: 80px 0 32px;
  margin-top: 0;
}

.ic-footer-inner {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 64px;
  align-items: start;
}

.ic-footer-logo {
  height: 36px;
  width: auto;
  display: block;
  margin-bottom: 16px;
  /* Invert logo for dark bg */
  filter: brightness(0) invert(1);
}

.ic-footer-tagline {
  font-size: 14px;
  color: #a3a3a3;
  line-height: 1.6;
  max-width: 320px;
  margin: 0;
}

.ic-footer-cols {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 40px;
}

.ic-footer-col h4 {
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: #fafafa;
  margin: 0 0 16px;
}

.ic-footer-col ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.ic-footer-col a {
  font-size: 14px;
  color: #a3a3a3;
  text-decoration: none;
  transition: color 200ms;
}

.ic-footer-col a:hover {
  color: #fafafa;
}

/* Plain text items (address, contact) — same color as links */
.ic-footer-text {
  font-size: 13px;
  color: #a3a3a3;
  line-height: 1.5;
}


.ic-footer-bottom {
  margin-top: 64px;
  padding-top: 24px;
  border-top: 1px solid #262626;
  font-size: 13px;
  color: #525252;
}

@media (max-width: 960px) {
  .ic-footer-inner { grid-template-columns: 1fr; gap: 48px; }
  .ic-footer-cols { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 560px) {
  .ic-footer-cols { grid-template-columns: 1fr; }
}
</style>
