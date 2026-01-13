<script setup>
import conferenceData from '../data/conferences.json'
</script>

<template>
  <div class="conf-grid">
    <div v-for="conf in conferenceData" :key="conf.year" class="conf-card">
      <div 
        class="conf-image"
        :style="{ backgroundImage: `url(${conf.image || '/default-conf.jpg'})` }"
      ></div>
      <div class="conf-content">
        <div class="conf-header">
          <span class="conf-year">{{ conf.year }}</span>
        </div>
        <h3><a :href="conf.link" target="_blank">{{ conf.title }}</a></h3>
        <p class="conf-location">📍 {{ conf.location }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.conf-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  padding: 2rem 0;
}

.conf-card {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
}

.conf-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 24px rgba(0,0,0,0.12);
}

.conf-image {
  height: 200px;
  background-size: cover;
  background-position: center;
}

.conf-content {
  padding: 1.5rem;
}

.conf-year {
  background: var(--vp-c-brand-1);
  color: white;
  padding: 0.2rem 0.6rem;
  border-radius: 4px;
  font-size: 0.8rem;
  font-weight: bold;
}

.conf-content h3 {
  margin: 1rem 0 0.5rem 0;
}

.conf-content a {
  text-decoration: none;
  color: var(--vp-c-text-1);
}

.conf-content a:hover {
  color: var(--vp-c-brand-1);
}

.conf-location {
  color: var(--vp-c-text-2);
  margin: 0;
}

@media (max-width: 768px) {
  .conf-grid {
    grid-template-columns: 1fr;
  }
}
</style>
