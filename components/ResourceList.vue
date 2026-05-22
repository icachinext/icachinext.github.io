<script setup>
import { useSiteData } from './useSiteData'

const { resourceList } = useSiteData()
</script>

<template>
  <ul class="list">
    <li v-for="r in resourceList" :key="r.title" class="item ic-card">
      <a :href="r.link" target="_blank" rel="noopener">
        <span class="type">{{ r.type }}</span>
        <div class="body">
          <h4>{{ r.title }}</h4>
          <p>{{ r.description }}</p>
        </div>
        <span class="arrow" aria-hidden="true">↓</span>
      </a>
    </li>
  </ul>
</template>

<style scoped>
.list {
  list-style: none;
  padding: 0;
  margin: 24px 0 0;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.item a {
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: 24px;
  align-items: center;
  padding: 20px 24px;
  text-decoration: none;
  color: inherit;
}

.type {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.06em;
  color: var(--vp-c-text-3);
  border: 1px solid var(--ic-border);
  padding: 4px 10px;
  border-radius: 4px;
}

.body h4 {
  margin: 0 0 4px;
  font-size: 15px;
  font-weight: 500;
  color: var(--vp-c-text-1);
}

.body p {
  margin: 0;
  font-size: 13px;
  color: var(--vp-c-text-3);
}

.arrow {
  font-size: 18px;
  color: var(--vp-c-text-3);
}
</style>
