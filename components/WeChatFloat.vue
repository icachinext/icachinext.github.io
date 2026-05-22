<script setup>
import { ref } from 'vue'
import { useSiteData } from './useSiteData'

const { site } = useSiteData()
const open = ref(false)
</script>

<template>
  <div class="wc-float" @mouseenter="open = true" @mouseleave="open = false">
    <!-- QR popup -->
    <Transition name="wc-pop">
      <div v-if="open" class="wc-popup">
        <img :src="site.footer.wechat.qr" alt="WeChat QR" />
        <p>{{ site.footer.wechat.label }}</p>
      </div>
    </Transition>

    <!-- Trigger button -->
    <button class="wc-btn" aria-label="微信公众号">
      <svg viewBox="0 0 24 24" fill="currentColor" width="22" height="22">
        <path d="M8.691 2.188C3.891 2.188 0 5.476 0 9.53c0 2.212 1.17 4.203 3.002 5.55a.59.59 0 0 1 .213.665l-.39 1.48c-.019.07-.048.141-.048.213 0 .163.13.295.29.295a.326.326 0 0 0 .167-.054l1.903-1.114a.864.864 0 0 1 .717-.098 10.16 10.16 0 0 0 2.837.403c.276 0 .543-.027.811-.05-.857-2.578.157-4.972 1.932-6.446 1.703-1.415 3.882-1.98 5.853-1.838-.576-3.583-4.196-6.348-8.596-6.348zM5.785 5.991c.642 0 1.162.529 1.162 1.18a1.17 1.17 0 0 1-1.162 1.178A1.17 1.17 0 0 1 4.623 7.17c0-.651.52-1.18 1.162-1.18zm5.813 0c.642 0 1.162.529 1.162 1.18a1.17 1.17 0 0 1-1.162 1.178 1.17 1.17 0 0 1-1.162-1.178c0-.651.52-1.18 1.162-1.18zm5.34 2.867c-1.797-.052-3.746.512-5.28 1.786-1.72 1.428-2.687 3.72-1.78 6.22.942 2.453 3.666 4.229 6.884 4.229.826 0 1.622-.12 2.361-.336a.722.722 0 0 1 .598.082l1.584.926a.272.272 0 0 0 .14.047c.134 0 .24-.111.24-.247 0-.06-.023-.12-.038-.177l-.327-1.233a.582.582 0 0 1 .023-.419c-.01.007-.02.014-.029.021l.029-.021c1.519-1.137 2.5-2.835 2.5-4.728 0-3.292-2.979-5.998-6.905-6.15zm-2.401 3.048c.537 0 .972.44.972.982a.977.977 0 0 1-.972.982.977.977 0 0 1-.972-.982c0-.542.435-.982.972-.982zm4.796 0c.537 0 .972.44.972.982a.977.977 0 0 1-.972.982.977.977 0 0 1-.972-.982c0-.542.434-.982.972-.982z"/>
      </svg>
    </button>
  </div>
</template>

<style scoped>
.wc-float {
  position: fixed;
  bottom: 84px; /* above back-to-top button */
  right: 32px;
  z-index: 99;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.wc-btn {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: #07c160; /* WeChat green */
  color: #fff;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 16px rgba(7, 193, 96, 0.35);
  transition: transform 200ms ease, box-shadow 200ms ease;
}

.wc-btn:hover {
  transform: scale(1.08);
  box-shadow: 0 6px 20px rgba(7, 193, 96, 0.45);
}

.wc-popup {
  position: absolute;
  bottom: calc(100% + 12px);
  right: 0;
  background: #fff;
  border: 1px solid #ececec;
  border-radius: 8px;
  padding: 12px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.12);
  text-align: center;
  width: 148px;
}

.wc-popup img {
  width: 120px;
  height: 120px;
  display: block;
  margin: 0 auto 8px;
}

.wc-popup p {
  font-size: 12px;
  color: #525252;
  margin: 0;
  line-height: 1.4;
}

/* Popup transition */
.wc-pop-enter-active { transition: opacity 180ms ease, transform 180ms ease; }
.wc-pop-leave-active { transition: opacity 140ms ease, transform 140ms ease; }
.wc-pop-enter-from,
.wc-pop-leave-to { opacity: 0; transform: translateY(8px); }

@media (max-width: 640px) {
  .wc-float { bottom: 72px; right: 20px; }
}
</style>
