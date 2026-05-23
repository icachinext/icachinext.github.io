<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import * as d3 from 'd3-geo'
import * as topojson from 'topojson-client'

const svgRef = ref(null)
const containerRef = ref(null)
const width = ref(960)
const HEIGHT_RATIO = 0.52 // natural earth ~0.52

const CONF_LOCATIONS = [
  { year: 2013, city: '巴黎',   lat: 48.86,  lng:   2.35 },
  { year: 2014, city: '多伦多', lat: 43.65,  lng: -79.38 },
  { year: 2015, city: '首尔',   lat: 37.57,  lng: 126.98 },
  { year: 2016, city: '圣何塞', lat: 37.34,  lng: -121.89 },
  { year: 2017, city: '广州',   lat: 23.13,  lng: 113.26 },
  { year: 2018, city: '蒙特利尔', lat: 45.50, lng: -73.57 },
  { year: 2019, city: '厦门',   lat: 24.48,  lng: 118.09 },
  { year: 2022, city: '广州',   lat: 23.13,  lng: 113.26 },
  { year: 2023, city: '巴厘岛', lat: -8.41,  lng: 115.19 },
  { year: 2024, city: '深圳',   lat: 22.54,  lng: 114.06 },
  { year: 2025, city: '新加坡', lat:  1.30,  lng: 103.82 },
  { year: 2026, city: '澳门',   lat: 22.19,  lng: 113.54 },
]

let resizeObserver = null
let svgEl = null
let projection = null

function buildMap(worldData) {
  const w = width.value
  const h = Math.round(w * HEIGHT_RATIO)

  // Clear previous render
  if (svgRef.value) svgRef.value.innerHTML = ''

  projection = d3.geoNaturalEarth1()
    .fitSize([w, h], { type: 'Sphere' })

  const path = d3.geoPath().projection(projection)

  const ns = 'http://www.w3.org/2000/svg'
  svgEl = svgRef.value
  svgEl.setAttribute('viewBox', `0 0 ${w} ${h}`)

  // Ocean
  const ocean = document.createElementNS(ns, 'path')
  ocean.setAttribute('class', 'ocean')
  ocean.setAttribute('d', path({ type: 'Sphere' }))
  svgEl.appendChild(ocean)

  // Countries
  const countries = topojson.feature(worldData, worldData.objects.countries)
  const land = document.createElementNS(ns, 'path')
  land.setAttribute('class', 'land')
  land.setAttribute('d', path(countries))
  svgEl.appendChild(land)

  // Country borders
  const borders = topojson.mesh(worldData, worldData.objects.countries, (a, b) => a !== b)
  const borderPath = document.createElementNS(ns, 'path')
  borderPath.setAttribute('class', 'borders')
  borderPath.setAttribute('d', path(borders))
  svgEl.appendChild(borderPath)

  // Project conference locations
  const projected = CONF_LOCATIONS.map(c => {
    const [x, y] = projection([c.lng, c.lat])
    return { ...c, x, y }
  })

  // Draw routes as quadratic Bezier curves
  const routeGroup = document.createElementNS(ns, 'g')
  routeGroup.setAttribute('class', 'routes')
  for (let i = 0; i < projected.length - 1; i++) {
    const a = projected[i]
    const b = projected[i + 1]
    const mx = (a.x + b.x) / 2
    const my = (a.y + b.y) / 2
    const dx = b.x - a.x
    const dy = b.y - a.y
    const len = Math.sqrt(dx * dx + dy * dy)
    // Control point: lift perpendicular to chord, height = 22% of chord
    const lift = len * 0.22
    const cx = mx - (dy / len) * lift
    const cy = my + (dx / len) * lift

    const routePath = document.createElementNS(ns, 'path')
    routePath.setAttribute('d', `M${a.x},${a.y} Q${cx},${cy} ${b.x},${b.y}`)
    routePath.setAttribute('class', 'route')
    // Animate dash draw-in
    const totalLen = routePath.getTotalLength ? routePath.getTotalLength() : 200
    routePath.style.strokeDasharray = totalLen
    routePath.style.strokeDashoffset = totalLen
    routePath.style.animation = `drawRoute 0.8s ease-out ${0.3 + i * 0.12}s forwards`
    routeGroup.appendChild(routePath)
  }
  svgEl.appendChild(routeGroup)

  // Draw markers + labels
  const markerGroup = document.createElementNS(ns, 'g')
  markerGroup.setAttribute('class', 'markers')

  projected.forEach((c, i) => {
    const g = document.createElementNS(ns, 'g')
    g.setAttribute('class', 'marker')
    g.style.opacity = '0'
    g.style.animation = `fadeInMarker 0.4s ease-out ${0.6 + i * 0.12}s forwards`

    // Outer ring
    const ring = document.createElementNS(ns, 'circle')
    ring.setAttribute('cx', c.x)
    ring.setAttribute('cy', c.y)
    ring.setAttribute('r', 5)
    ring.setAttribute('class', 'marker-ring')
    g.appendChild(ring)

    // Inner dot
    const dot = document.createElementNS(ns, 'circle')
    dot.setAttribute('cx', c.x)
    dot.setAttribute('cy', c.y)
    dot.setAttribute('r', 2.5)
    dot.setAttribute('class', 'marker-dot')
    g.appendChild(dot)

    // Year label
    const label = document.createElementNS(ns, 'text')
    label.setAttribute('x', c.x)
    label.setAttribute('y', c.y - 10)
    label.setAttribute('class', 'year-label')
    label.setAttribute('text-anchor', 'middle')
    label.textContent = c.year
    g.appendChild(label)

    markerGroup.appendChild(g)
  })

  svgEl.appendChild(markerGroup)
}

async function init() {
  try {
    const res = await fetch('/data/world-110m.json')
    const world = await res.json()
    if (containerRef.value) {
      width.value = containerRef.value.clientWidth || 960
    }
    buildMap(world)

    resizeObserver = new ResizeObserver(entries => {
      const newW = entries[0].contentRect.width
      if (Math.abs(newW - width.value) > 10) {
        width.value = newW
        buildMap(world)
      }
    })
    if (containerRef.value) resizeObserver.observe(containerRef.value)
  } catch (e) {
    console.error('ConferenceMap: failed to load world data', e)
  }
}

onMounted(init)
onBeforeUnmount(() => {
  if (resizeObserver) resizeObserver.disconnect()
})
</script>

<template>
  <div class="conf-map-wrap" ref="containerRef">
    <svg ref="svgRef" class="conf-map-svg" aria-hidden="true" />
  </div>
</template>

<style scoped>
.conf-map-wrap {
  width: 100%;
  margin: 56px 0 48px;
  border-radius: 12px;
  overflow: hidden;
  background: #f0f2f5;
  border: 1px solid var(--ic-border);
}

.conf-map-svg {
  display: block;
  width: 100%;
  height: auto;
}

/* -- SVG element styles (not scoped, injected via :global since SVG children
   are created imperatively and won't receive scoped data-v attributes) */
</style>

<style>
/* Ocean */
.conf-map-svg .ocean {
  fill: #dce8f5;
}

/* Land */
.conf-map-svg .land {
  fill: #e8ebe8;
  stroke: none;
}

/* Country borders */
.conf-map-svg .borders {
  fill: none;
  stroke: #ffffff;
  stroke-width: 0.5;
}

/* Routes */
.conf-map-svg .route {
  fill: none;
  stroke: #1a1a1a;
  stroke-width: 1.2;
  stroke-linecap: round;
  opacity: 0.55;
}

/* Markers */
.conf-map-svg .marker-ring {
  fill: none;
  stroke: #1a1a1a;
  stroke-width: 1.2;
  opacity: 0.7;
}

.conf-map-svg .marker-dot {
  fill: #1a1a1a;
}

/* Year labels */
.conf-map-svg .year-label {
  font-family: var(--vp-font-family-base), system-ui, sans-serif;
  font-size: 9px;
  font-weight: 600;
  fill: #1a1a1a;
  letter-spacing: 0.02em;
}

/* Animations */
@keyframes drawRoute {
  to { stroke-dashoffset: 0; }
}

@keyframes fadeInMarker {
  to { opacity: 1; }
}
</style>
