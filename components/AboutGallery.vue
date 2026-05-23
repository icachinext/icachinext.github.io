<script setup>
import { ref } from 'vue'

const props = defineProps({
  images: {
    type: Array,
    default: () => []
    // Each item: { src, alt }
  }
})

const lightbox = ref(null) // src of the open image, or null

function open(src) { lightbox.value = src }
function close()   { lightbox.value = null }

function onKey(e) {
  if (e.key === 'Escape') close()
}
</script>

<template>
  <div class="gallery">
    <button
      v-for="(img, i) in images"
      :key="i"
      class="thumb"
      @click="open(img.src)"
      :aria-label="`查看大图：${img.alt || i + 1}`"
    >
      <img :src="img.src" :alt="img.alt || ''" loading="lazy" />
    </button>
  </div>

  <!-- Lightbox -->
  <Teleport to="body">
    <div
      v-if="lightbox"
      class="lightbox"
      @click.self="close"
      @keydown="onKey"
      tabindex="-1"
      role="dialog"
      aria-modal="true"
    >
      <button class="lb-close" @click="close" aria-label="关闭">✕</button>
      <img :src="lightbox" class="lb-img" alt="" @click.stop />
    </div>
  </Teleport>
</template>

<style scoped>
/* ── Grid ── */
.gallery {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
  margin: 28px 0;
}

.thumb {
  padding: 0;
  border: none;
  background: var(--vp-c-bg-soft);
  cursor: pointer;
  overflow: hidden;
  border-radius: 4px;
  aspect-ratio: 3 / 2;
  display: block;
  width: 100%;
}

.thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 350ms ease, opacity 350ms ease;
}

.thumb:hover img {
  transform: scale(1.04);
  opacity: 0.88;
}

/* ── Lightbox ── */
.lightbox {
  position: fixed;
  inset: 0;
  z-index: 9999;
  background: rgba(0, 0, 0, 0.85);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  animation: lbFadeIn 200ms ease;
}

@keyframes lbFadeIn {
  from { opacity: 0 }
  to   { opacity: 1 }
}

.lb-img {
  max-width: 100%;
  max-height: 90vh;
  object-fit: contain;
  border-radius: 4px;
  box-shadow: 0 8px 40px rgba(0,0,0,0.6);
}

.lb-close {
  position: absolute;
  top: 16px;
  right: 20px;
  background: none;
  border: none;
  color: #fff;
  font-size: 22px;
  cursor: pointer;
  line-height: 1;
  opacity: 0.7;
  transition: opacity 150ms;
  padding: 4px 8px;
}

.lb-close:hover { opacity: 1; }

@media (max-width: 600px) {
  .gallery { grid-template-columns: repeat(2, 1fr); }
}
</style>
