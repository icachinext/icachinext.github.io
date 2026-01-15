<script setup>
import { data as newsData } from '../docs/news.data'
import conferenceData from '../data/conferences.json'
import { ref, computed, onMounted, onUnmounted } from 'vue'

const currentSlide = ref(0)
const timer = ref(null)

// Prepare Data: 1st is Latest Conference, 2-4 are Top 3 News
const slides = computed(() => {
  const latestConf = conferenceData[0] || null
  const topNews = newsData.slice(0, 3).map(n => ({
    title: n.title,
    subtitle: n.date ? new Date(n.date).toLocaleDateString() : '',
    image: n.cover,
    link: n.url,
    type: 'News'
  }))

  const result = []
  if (latestConf) {
    result.push({
      title: latestConf.title,
      subtitle: `${latestConf.location} | ${latestConf.year}`,
      image: latestConf.image,
      link: latestConf.link,
      type: 'Conference'
    })
  }
  
  return [...result, ...topNews]
})

const nextSlide = () => {
  if (slides.value.length === 0) return
  currentSlide.value = (currentSlide.value + 1) % slides.value.length
}

const prevSlide = () => {
  if (slides.value.length === 0) return
  currentSlide.value = (currentSlide.value - 1 + slides.value.length) % slides.value.length
}

onMounted(() => {
  // Auto-play
  timer.value = setInterval(nextSlide, 6000)
})

onUnmounted(() => {
  if (timer.value) clearInterval(timer.value)
})
</script>

<template>
  <div class="hero-wrapper" v-if="slides.length > 0">
    <div class="hero-slider">
      <div 
        v-for="(item, index) in slides" 
        :key="index"
        class="slide"
        :class="{ active: index === currentSlide }"
        :style="{ backgroundImage: `url(${item.image || '/default-cover.jpg'})` }"
      >
        <div class="slide-overlay">
          <div class="slide-content">
            <span class="slide-tag">{{ item.type }}</span>
            <h2 class="slide-title">
              <a :href="item.link">{{ item.title }}</a>
            </h2>
            <p class="slide-subtitle">{{ item.subtitle }}</p>
            <a :href="item.link" class="slide-btn">Read More</a>
          </div>
        </div>
      </div>

      <div class="slider-controls">
        <button @click="prevSlide" class="control-btn left">❮</button>
        <button @click="nextSlide" class="control-btn right">❯</button>
      </div>

      <div class="slider-dots">
        <span 
          v-for="(_, index) in slides" 
          :key="index"
          class="dot"
          :class="{ active: index === currentSlide }"
          @click="currentSlide = index"
        ></span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.hero-wrapper {
  /* Full viewport width and comfortable height */
  width: 100vw;
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  margin-top: -40px; /* Counteract default padding if any, adjustment for VitePress default layout */
}

.hero-slider {
  position: relative;
  width: 100%;
  height: 85vh; /* Occupy most of the screen */
  max-height: 800px;
  min-height: 500px;
  overflow: hidden;
  background-color: #000;
}

.slide {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  opacity: 0;
  transition: opacity 1s ease-in-out, transform 6s ease;
  transform: scale(1.05); /* Zoom effect start */
}

.slide.active {
  opacity: 1;
  transform: scale(1); /* Zoom effect end */
  z-index: 1;
}

.slide-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.3); /* Darken entire image slightly */
  background: linear-gradient(to top, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.2) 60%, rgba(0,0,0,0.3) 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.slide-content {
  max-width: 800px;
  padding: 2rem;
  color: white;
  animation: fadeUp 1s ease-out 0.3s backwards;
}

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

.slide-tag {
  display: inline-block;
  background-color: var(--vp-c-brand-1);
  color: white;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 600;
  margin-bottom: 1rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.slide-title {
  margin: 0;
  font-size: 3.5rem;
  line-height: 1.2;
  font-weight: 800;
  margin-bottom: 1rem;
  text-shadow: 0 4px 8px rgba(0,0,0,0.3);
}

.slide-title a {
  color: white;
  text-decoration: none;
  transition: opacity 0.3s;
}

.slide-title a:hover {
  opacity: 0.8;
}

.slide-subtitle {
  font-size: 1.5rem;
  margin-bottom: 2rem;
  font-weight: 300;
  opacity: 0.9;
}

.slide-btn {
  display: inline-block;
  padding: 12px 30px;
  background-color: white;
  color: var(--vp-c-text-1);
  text-decoration: none;
  border-radius: 30px;
  font-weight: 600;
  transition: all 0.3s ease;
}

.slide-btn:hover {
  background-color: var(--vp-c-brand-1);
  color: white;
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.2);
}

.slider-controls {
  position: absolute;
  top: 50%;
  width: 100%;
  display: flex;
  justify-content: space-between;
  transform: translateY(-50%);
  padding: 0 2rem;
  z-index: 10;
  pointer-events: none;
}

.control-btn {
  pointer-events: auto;
  background: rgba(255,255,255,0.1);
  backdrop-filter: blur(4px);
  border: 1px solid rgba(255,255,255,0.2);
  color: white;
  font-size: 2rem;
  cursor: pointer;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s;
}

.control-btn:hover {
  background: white;
  color: black;
}

.slider-dots {
  position: absolute;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 0.8rem;
  z-index: 10;
}

.dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  border: 2px solid white;
  background: transparent;
  cursor: pointer;
  transition: all 0.3s;
}

.dot.active {
  background: white;
  transform: scale(1.2);
}

@media (max-width: 768px) {
  .slide-title {
    font-size: 2rem;
  }
  .slide-subtitle {
    font-size: 1.1rem;
  }
  .hero-slider {
    height: 60vh;
  }
}
</style>
