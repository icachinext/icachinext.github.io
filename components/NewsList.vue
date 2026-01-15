<script setup>
import { data as allNews } from '../docs/news.data'
import { ref, computed } from 'vue'

const props = defineProps({
  pageSize: {
    type: Number,
    default: 9 // 3x3 Grid looks better than 20 for simple demo, but user asked for 20.
  }
})

// Use user requested 20 per page if not overridden, but I'll stick to props for flexibility
const itemsPerPage = 20
const currentPage = ref(1)

const totalPages = computed(() => Math.ceil(allNews.length / itemsPerPage))

const displayedNews = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  return allNews.slice(start, start + itemsPerPage)
})

const prevPage = () => {
  if (currentPage.value > 1) currentPage.value--
}

const nextPage = () => {
  if (currentPage.value < totalPages.value) currentPage.value++
}
</script>

<template>
  <div class="news-container">
    <div class="news-grid">
      <div v-for="item in displayedNews" :key="item.url" class="news-card">
        <a :href="item.url" class="card-link">
          <div 
            class="card-image"
            :style="{ backgroundImage: `url(${item.cover || '/default-news.jpg'})` }"
          ></div>
          <div class="card-content">
            <span class="card-date">{{ item.date ? new Date(item.date).toLocaleDateString() : '' }}</span>
            <h3 class="card-title">{{ item.title }}</h3>
            <!-- <p v-if="item.excerpt" class="card-excerpt" v-html="item.excerpt"></p> -->
          </div>
        </a>
      </div>
    </div>
    
    <div v-if="totalPages > 1" class="pagination">
      <button 
        @click="prevPage" 
        :disabled="currentPage === 1"
        class="page-btn"
      >
        Previous
      </button>
      <span class="page-info">Page {{ currentPage }} of {{ totalPages }}</span>
      <button 
        @click="nextPage" 
        :disabled="currentPage === totalPages"
        class="page-btn"
      >
        Next
      </button>
    </div>
  </div>
</template>

<style scoped>
.news-container {
  padding: 2rem 0;
}

.news-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
  margin-bottom: 2rem;
}

.news-card {
  background: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  height: 100%;
}

.news-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 16px rgba(0,0,0,0.1);
}

.card-link {
  text-decoration: none;
  color: inherit;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.card-image {
  height: 200px;
  background-size: cover;
  background-position: center;
}

.card-content {
  padding: 1.5rem;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.card-date {
  font-size: 0.85rem;
  color: #666;
  margin-bottom: 0.5rem;
}

.card-title {
  margin: 0 0 1rem 0;
  font-size: 1.25rem;
  line-height: 1.4;
  color: var(--vp-c-text-1);
}

.card-excerpt {
  font-size: 0.95rem;
  color: var(--vp-c-text-2);
  line-height: 1.6;
  margin: 0;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
  margin-top: 3rem;
}

.page-btn {
  padding: 0.5rem 1rem;
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg);
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s;
}

.page-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.page-btn:not(:disabled):hover {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
}
</style>
