<script setup>
import { computed, onBeforeUnmount, onMounted, ref, shallowRef } from 'vue'
import { useData, withBase } from 'vitepress'
import * as d3 from 'd3-geo'
import * as topojson from 'topojson-client'
import conferenceData from '../data/conferences.json'

const HEIGHT_RATIO = 0.52
const MOBILE_HEIGHT_RATIO = 0.68
const MAP_PADDING = 10
const DEFAULT_ZOOM = 1.32
const MIN_ZOOM = 0.85
const MAX_ZOOM = 2.25
const ZOOM_STEP = 0.2

const LABEL_OFFSETS = {
  'san-jose': { dx: 12, dy: -15, anchor: 'start' },
  toronto: { dx: -10, dy: -19, anchor: 'end' },
  montreal: { dx: 12, dy: 16, anchor: 'start' },
  paris: { dx: 12, dy: -14, anchor: 'start' },
  'online-beijing': { dx: -30, dy: -27, anchor: 'end' },
  seoul: { dx: 27, dy: -17, anchor: 'start' },
  guangzhou: { dx: -46, dy: 2, anchor: 'end' },
  xiamen: { dx: 48, dy: 0, anchor: 'start' },
  shenzhen: { dx: -52, dy: 24, anchor: 'end' },
  macau: { dx: 43, dy: 32, anchor: 'start' },
  singapore: { dx: -32, dy: 35, anchor: 'end' },
  bali: { dx: 31, dy: 24, anchor: 'start' },
}

const MOBILE_LABEL_LAYOUT = {
  'san-jose': { x: 0.02, y: 0.39, anchor: 'start' },
  toronto: { x: 0.02, y: 0.20, anchor: 'start' },
  montreal: { x: 0.02, y: 0.29, anchor: 'start' },
  paris: { x: 0.40, y: 0.23, anchor: 'start' },
  'online-beijing': { x: 0.64, y: 0.12, anchor: 'end' },
  seoul: { x: 0.98, y: 0.22, anchor: 'end' },
  guangzhou: { x: 0.64, y: 0.34, anchor: 'end' },
  xiamen: { x: 0.98, y: 0.38, anchor: 'end' },
  shenzhen: { x: 0.64, y: 0.47, anchor: 'end' },
  macau: { x: 0.98, y: 0.54, anchor: 'end' },
  singapore: { x: 0.64, y: 0.63, anchor: 'end' },
  bali: { x: 0.98, y: 0.72, anchor: 'end' },
}

const containerRef = ref(null)
const mapWidth = ref(960)
const worldData = shallowRef(null)
const loadError = ref(false)
const zoomLevel = ref(DEFAULT_ZOOM)
const { lang } = useData()
const isEn = computed(() => lang.value?.startsWith('en'))

let resizeObserver = null
let resizeFrame = 0

const copy = computed(() => isEn.value
  ? {
      title: 'Conference locations around the world',
      description: 'A zoomable world map showing the locations and years of ICACHI conferences from 2013 to 2026.',
      error: 'The conference map could not be loaded.',
      controls: 'Map zoom controls',
      zoomIn: 'Zoom in',
      zoomOut: 'Zoom out',
      resetZoom: 'Reset zoom',
    }
  : {
      title: '历届会议举办地',
      description: '可缩放世界地图展示 ICACHI 2013 至 2026 年历届会议的举办地点与年份。',
      error: '会议地图暂时无法加载。',
      controls: '地图缩放控件',
      zoomIn: '放大地图',
      zoomOut: '缩小地图',
      resetZoom: '恢复默认缩放',
    })

const canZoomIn = computed(() => zoomLevel.value < MAX_ZOOM)
const canZoomOut = computed(() => zoomLevel.value > MIN_ZOOM)

const locationGroups = computed(() => {
  const groups = new Map()

  conferenceData.forEach((conference) => {
    const location = conference.mapLocation
    if (!location) return

    if (!groups.has(location.id)) {
      groups.set(location.id, {
        ...location,
        years: [],
      })
    }
    groups.get(location.id).years.push(conference.year)
  })

  return [...groups.values()]
    .map(location => ({
      ...location,
      years: location.years.sort((a, b) => a - b),
    }))
    .sort((a, b) => a.years[0] - b.years[0])
})

function labelText(location) {
  const place = isEn.value ? location.labelEn : location.label
  return `${place} ${location.years.join(' · ')}`
}

function estimatedTextWidth(text) {
  let width = 0
  for (const character of text) {
    width += /[\u3400-\u9fff]/.test(character) ? 11 : 6.3
  }
  return width
}

function placeLabel(location, x, y, width, height) {
  const offset = LABEL_OFFSETS[location.id] || { dx: 12, dy: -14, anchor: 'start' }
  const needsDistributedLabels = width <= 520 || zoomLevel.value < DEFAULT_ZOOM
  const mobileLayout = needsDistributedLabels ? MOBILE_LABEL_LAYOUT[location.id] : null
  const text = labelText(location)
  const textWidth = estimatedTextWidth(text)
  let anchor = mobileLayout?.anchor || offset.anchor
  let labelX = mobileLayout ? width * mobileLayout.x : x + offset.dx
  const requestedY = mobileLayout ? height * mobileLayout.y : y + offset.dy
  const labelY = Math.max(15, Math.min(height - 7, requestedY))

  if (anchor === 'start' && labelX + textWidth > width - 7) {
    anchor = 'end'
    labelX = width - 7
  } else if (anchor === 'end' && labelX - textWidth < 7) {
    anchor = 'start'
    labelX = 7
  }

  const labelLeft = anchor === 'start' ? labelX : labelX - textWidth
  const labelRight = anchor === 'start' ? labelX + textWidth : labelX
  const lineX = x < labelLeft
    ? labelLeft - 4
    : x > labelRight
      ? labelRight + 4
      : labelX

  return {
    ...location,
    x,
    y,
    labelX,
    labelY,
    lineX,
    lineY: labelY - 4,
    anchor,
    text,
  }
}

const geometry = computed(() => {
  if (!worldData.value) return null

  const width = Math.max(mapWidth.value, 320)
  const heightRatio = width <= 520 ? MOBILE_HEIGHT_RATIO : HEIGHT_RATIO
  const height = Math.round(width * heightRatio)
  const projection = d3.geoNaturalEarth1().fitExtent(
    [[MAP_PADDING, MAP_PADDING], [width - MAP_PADDING, height - MAP_PADDING]],
    { type: 'Sphere' },
  )
  projection.scale(projection.scale() * zoomLevel.value)
  const [translateX, translateY] = projection.translate()
  const focusProgress = Math.min(
    1,
    Math.max(0, (zoomLevel.value - MIN_ZOOM) / (DEFAULT_ZOOM - MIN_ZOOM)),
  )
  projection.translate([
    translateX,
    translateY + height * 0.055 * focusProgress,
  ])
  const path = d3.geoPath(projection)
  const countries = topojson.feature(
    worldData.value,
    worldData.value.objects.countries,
  )
  const borders = topojson.mesh(
    worldData.value,
    worldData.value.objects.countries,
    (a, b) => a !== b,
  )
  const markers = locationGroups.value
    .map((location) => {
      const [x, y] = projection([location.lng, location.lat])
      return placeLabel(location, x, y, width, height)
    })
    .filter(marker => (
      marker.x >= -6
      && marker.x <= width + 6
      && marker.y >= -6
      && marker.y <= height + 6
    ))

  return {
    width,
    height,
    sphere: path({ type: 'Sphere' }),
    land: path(countries),
    borders: path(borders),
    markers,
  }
})

function zoomIn() {
  zoomLevel.value = Math.min(MAX_ZOOM, Number((zoomLevel.value + ZOOM_STEP).toFixed(2)))
}

function zoomOut() {
  zoomLevel.value = Math.max(MIN_ZOOM, Number((zoomLevel.value - ZOOM_STEP).toFixed(2)))
}

function resetZoom() {
  zoomLevel.value = DEFAULT_ZOOM
}

function updateWidth() {
  if (!containerRef.value) return
  cancelAnimationFrame(resizeFrame)
  resizeFrame = requestAnimationFrame(() => {
    mapWidth.value = containerRef.value.clientWidth || 960
  })
}

async function loadMap() {
  try {
    const response = await fetch(withBase('/data/world-110m.json'))
    if (!response.ok) throw new Error(`Map data request failed: ${response.status}`)
    worldData.value = await response.json()
  } catch (error) {
    loadError.value = true
    console.error('ConferenceMap: failed to load world data', error)
  }
}

onMounted(() => {
  updateWidth()
  loadMap()

  if (typeof ResizeObserver !== 'undefined') {
    resizeObserver = new ResizeObserver(updateWidth)
    resizeObserver.observe(containerRef.value)
  } else {
    window.addEventListener('resize', updateWidth)
  }
})

onBeforeUnmount(() => {
  cancelAnimationFrame(resizeFrame)
  resizeObserver?.disconnect()
  window.removeEventListener('resize', updateWidth)
})
</script>

<template>
  <figure ref="containerRef" class="conference-map">
    <svg
      v-if="geometry"
      class="conference-map__svg"
      :viewBox="`0 0 ${geometry.width} ${geometry.height}`"
      role="img"
      aria-labelledby="conference-map-title conference-map-description"
    >
      <title id="conference-map-title">{{ copy.title }}</title>
      <desc id="conference-map-description">{{ copy.description }}</desc>

      <path class="conference-map__ocean" :d="geometry.sphere" />
      <path class="conference-map__land" :d="geometry.land" />
      <path class="conference-map__borders" :d="geometry.borders" />

      <g
        v-for="(marker, index) in geometry.markers"
        :key="marker.id"
        class="conference-map__marker"
        :style="{ '--marker-delay': `${index * 45}ms` }"
      >
        <line
          class="conference-map__leader"
          :x1="marker.x"
          :y1="marker.y"
          :x2="marker.lineX"
          :y2="marker.lineY"
        />
        <circle
          class="conference-map__pin-ring"
          :cx="marker.x"
          :cy="marker.y"
          r="5"
        />
        <circle
          class="conference-map__pin"
          :cx="marker.x"
          :cy="marker.y"
          r="2.5"
        />
        <text
          class="conference-map__label"
          :x="marker.labelX"
          :y="marker.labelY"
          :text-anchor="marker.anchor"
        >{{ marker.text }}</text>
      </g>
    </svg>

    <div
      v-if="geometry"
      class="conference-map__controls"
      role="group"
      :aria-label="copy.controls"
    >
      <button
        type="button"
        class="conference-map__control"
        :aria-label="copy.zoomOut"
        :title="copy.zoomOut"
        :disabled="!canZoomOut"
        @click="zoomOut"
      >−</button>
      <button
        type="button"
        class="conference-map__control conference-map__control--reset"
        :aria-label="copy.resetZoom"
        :title="copy.resetZoom"
        :disabled="zoomLevel === DEFAULT_ZOOM"
        @click="resetZoom"
      >{{ Math.round(zoomLevel * 100) }}%</button>
      <button
        type="button"
        class="conference-map__control"
        :aria-label="copy.zoomIn"
        :title="copy.zoomIn"
        :disabled="!canZoomIn"
        @click="zoomIn"
      >+</button>
    </div>

    <p v-else-if="loadError" class="conference-map__status" role="status">
      {{ copy.error }}
    </p>

    <figcaption class="conference-map__accessible">
      {{ copy.description }}
      <ul>
        <li v-for="location in locationGroups" :key="location.id">
          {{ labelText(location) }}
        </li>
      </ul>
    </figcaption>
  </figure>
</template>

<style scoped>
.conference-map {
  position: relative;
  width: 100%;
  min-height: 180px;
  margin: 36px 0 48px;
  overflow: hidden;
  border: 1px solid var(--ic-border);
  border-radius: 12px;
  background: var(--vp-c-bg);
}

.conference-map__svg {
  display: block;
  width: 100%;
  height: auto;
}

.conference-map__controls {
  position: absolute;
  bottom: 14px;
  left: 14px;
  display: inline-flex;
  overflow: hidden;
  border: 1px solid var(--ic-border);
  border-radius: 999px;
  background: color-mix(in srgb, var(--vp-c-bg) 92%, transparent);
  box-shadow: 0 4px 14px rgb(0 0 0 / 6%);
  backdrop-filter: blur(8px);
}

.conference-map__control {
  display: grid;
  width: 34px;
  height: 34px;
  padding: 0;
  place-items: center;
  border: 0;
  border-right: 1px solid var(--ic-border);
  background: transparent;
  color: var(--vp-c-text-1);
  font: inherit;
  font-size: 19px;
  line-height: 1;
  cursor: pointer;
}

.conference-map__control:last-child {
  border-right: 0;
}

.conference-map__control--reset {
  width: 52px;
  font-size: 11px;
  font-variant-numeric: tabular-nums;
}

.conference-map__control:hover:not(:disabled),
.conference-map__control:focus-visible {
  background: var(--vp-c-bg-soft);
}

.conference-map__control:focus-visible {
  position: relative;
  z-index: 1;
  outline: 2px solid var(--vp-c-text-1);
  outline-offset: -2px;
}

.conference-map__control:disabled {
  color: var(--vp-c-text-3);
  cursor: default;
}

.conference-map__ocean {
  fill: var(--vp-c-bg);
}

.conference-map__land {
  fill: var(--vp-c-bg-soft);
}

.conference-map__borders {
  fill: none;
  stroke: var(--vp-c-bg);
  stroke-width: 0.65;
  vector-effect: non-scaling-stroke;
}

.conference-map__marker {
  opacity: 0;
  animation: conference-marker-in 420ms ease-out var(--marker-delay) forwards;
}

.conference-map__leader {
  stroke: var(--vp-c-text-2);
  stroke-width: 0.8;
  vector-effect: non-scaling-stroke;
}

.conference-map__pin-ring {
  fill: var(--vp-c-bg);
  stroke: var(--vp-c-text-1);
  stroke-width: 1.25;
  vector-effect: non-scaling-stroke;
}

.conference-map__pin {
  fill: var(--vp-c-text-1);
}

.conference-map__label {
  fill: var(--vp-c-text-1);
  stroke: var(--vp-c-bg);
  stroke-width: 3px;
  paint-order: stroke fill;
  font-family: var(--vp-font-family-base);
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.01em;
}

.conference-map__status {
  display: grid;
  min-height: 180px;
  margin: 0;
  place-items: center;
  color: var(--vp-c-text-2);
  font-size: 14px;
}

.conference-map__accessible {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

@keyframes conference-marker-in {
  from {
    opacity: 0;
    transform: translateY(3px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 640px) {
  .conference-map {
    margin: 28px 0 36px;
    border-radius: 8px;
  }

  .conference-map__controls {
    bottom: 8px;
    left: 8px;
  }

  .conference-map__control {
    width: 30px;
    height: 30px;
  }

  .conference-map__control--reset {
    width: 46px;
  }

  .conference-map__label {
    font-size: 9px;
    stroke-width: 2.5px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .conference-map__marker {
    opacity: 1;
    animation: none;
  }
}
</style>
