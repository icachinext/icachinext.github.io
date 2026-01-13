<script setup>
import boardData from '../data/board.json'
</script>

<template>
  <div class="board-grid">
    <div v-for="member in boardData" :key="member.name" class="member-card">
      <img :src="member.avatar" :alt="member.name" class="member-avatar">
      <div class="member-info">
        <h3>{{ member.name }}</h3>
        <p class="role">{{ member.role }}</p>
        <p class="org">{{ member.org }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.board-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 2rem;
  padding: 2rem 0;
}

.member-card {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
  transition: transform 0.3s ease;
  text-align: center;
  padding: 2rem 1rem;
}

.member-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}

.member-avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  margin-bottom: 1rem;
  object-fit: cover;
  border: 3px solid var(--vp-c-brand-1);
}

.member-info h3 {
  margin: 0.5rem 0;
  color: var(--vp-c-text-1);
}

.role {
  color: var(--vp-c-brand-1);
  font-weight: 600;
  margin: 0.2rem 0;
}

.org {
  color: var(--vp-c-text-2);
  font-size: 0.9rem;
}
</style>
