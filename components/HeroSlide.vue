<script setup>
import { data as news } from '../docs/news.data'
import { ref, onMounted, onUnmounted } from 'vue'

const currentSlide = ref(0)
const timer = ref(null)

const nextSlide = () => {
  currentSlide.value = (currentSlide.value + 1) % news.length
}

const prevSlide = () => {
  currentSlide.value = (currentSlide.value - 1 + news.length) % news.length
}

onMounted(() => {
  timer.value = setInterval(nextSlide, 5000)
})

onUnmounted(() => {
  clearInterval(timer.value)
})
</script>

<template>
  <div class="hero-container">
    <div class="hero-content">
      <h1 class="hero-title">ICACHI</h1>
      <p class="hero-subtitle">世界华人华侨人机交互协会</p>
      <p class="hero-tagline">International Chinese Association of Computer Human Interaction</p>
      <div class="hero-actions">
        <a href="/about" class="hero-btn primary">关于我们</a>
        <a href="/bylaws" class="hero-btn secondary">协会章程</a>
      </div>
    </div>
    
    <div class="hero-slider">
      <div 
        v-for="(item, index) in news.slice(0, 4)" 
        :key="item.url"
        class="slide"
        :class="{ active: index === currentSlide }"
        :style="{ backgroundImage: `url(${item.cover || '/default-cover.jpg'})` }"
      >
        <div class="slide-overlay">
          <h3><a :href="item.url">{{ item.title }}</a></h3>
          <p>{{ item.date }}</p>
        </div>
      </div>
      
      <div class="slider-controls">
        <button @click="prevSlide" class="control-btn">❮</button>
        <button @click="nextSlide" class="control-btn">❯</button>
      </div>
      
      <div class="slider-dots">
        <span 
          v-for="(_, index) in news.slice(0, 4)" 
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
.hero-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  padding: 4rem 2rem;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  border-radius: 12px;
  margin: 2rem 0;
  align-items: center;
}

.hero-content {
  padding-right: 2rem;
}

.hero-title {
  font-size: 3.5rem;
  font-weight: 800;
  background: -webkit-linear-gradient(315deg, #3451b2 25%, #3a5ccc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 0.5rem;
}

.hero-subtitle {
  font-size: 1.5rem;
  color: #333;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.hero-tagline {
  font-size: 1.1rem;
  color: #666;
  margin-bottom: 2rem;
}

.hero-actions {
  display: flex;
  gap: 1rem;
}

.hero-btn {
  padding: 0.8rem 1.5rem;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s ease;
}

.hero-btn.primary {
  background-color: var(--vp-c-brand-1);
  color: white;
}

.hero-btn.secondary {
  border: 2px solid var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
}

.hero-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.hero-slider {
  position: relative;
  height: 400px;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0,0,0,0.15);
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
  transition: opacity 0.8s ease;
}

.slide.active {
  opacity: 1;
}

.slide-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);
  padding: 2rem;
  color: white;
}

.slide-overlay h3 {
  margin: 0;
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}

.slide-overlay a {
  color: white;
  text-decoration: none;
}

.slider-controls {
  position: absolute;
  top: 50%;
  width: 100%;
  display: flex;
  justify-content: space-between;
  transform: translateY(-50%);
  padding: 0 1rem;
  pointer-events: none;
}

.control-btn {
  pointer-events: auto;
  background: rgba(255,255,255,0.3);
  border: none;
  color: white;
  font-size: 2rem;
  cursor: pointer;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.3s;
}

.control-btn:hover {
  background: rgba(255,255,255,0.6);
}

.slider-dots {
  position: absolute;
  bottom: 1rem;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 0.5rem;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: rgba(255,255,255,0.5);
  cursor: pointer;
}

.dot.active {
  background: white;
}

@media (max-width: 768px) {
  .hero-container {
    grid-template-columns: 1fr;
  }
}
</style>
