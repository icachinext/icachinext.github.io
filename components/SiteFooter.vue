<script setup>
import { computed } from 'vue'
import { useSiteData } from './useSiteData'

const { site } = useSiteData()

const footer = computed(() => site.value.footer)
const copyright = computed(() =>
  footer.value.copyright.replace('{{year}}', String(new Date().getFullYear()))
)
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

        <div class="ic-footer-col ic-footer-wechat">
          <h4>{{ footer.wechat.label }}</h4>
          <img :src="footer.wechat.qr" alt="WeChat QR" />
        </div>
      </div>
    </div>

    <div class="ic-container ic-footer-bottom">
      <span>{{ copyright }}</span>
    </div>
  </footer>
</template>

<style scoped>
.ic-footer {
  border-top: 1px solid var(--ic-border);
  background: var(--vp-c-bg);
  padding: 80px 0 32px;
  margin-top: 120px;
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
}

.ic-footer-tagline {
  font-size: 14px;
  color: var(--vp-c-text-2);
  line-height: 1.6;
  max-width: 320px;
  margin: 0;
}

.ic-footer-cols {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 32px;
}

.ic-footer-col h4 {
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--vp-c-text-1);
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
  color: var(--vp-c-text-2);
  text-decoration: none;
  transition: color var(--ic-transition);
}

.ic-footer-col a:hover {
  color: var(--vp-c-text-1);
}

.ic-footer-text {
  font-size: 13px;
  color: var(--vp-c-text-3);
  line-height: 1.5;
}

.ic-footer-wechat img {
  width: 110px;
  height: 110px;
  border: 1px solid var(--ic-border);
  border-radius: 4px;
}

.ic-footer-bottom {
  margin-top: 64px;
  padding-top: 24px;
  border-top: 1px solid var(--ic-border);
  font-size: 13px;
  color: var(--vp-c-text-3);
}

@media (max-width: 960px) {
  .ic-footer-inner { grid-template-columns: 1fr; gap: 48px; }
  .ic-footer-cols { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 560px) {
  .ic-footer-cols { grid-template-columns: 1fr; }
}
</style>
