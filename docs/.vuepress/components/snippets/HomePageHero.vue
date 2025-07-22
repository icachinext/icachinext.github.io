<template>
    <div>
        <!-- Hero Section -->
      <div
        class="bg-img-hero"
        v-bind:style="{
          backgroundImage:
            'url(' +
            require('../../assets/svg/components/abstract-shapes-12.svg') +
            ')',
        }"
      >
        <div
          class="
            container
            space-top-3 space-top-lg-4 space-bottom-2
            position-relative
            z-index-2
          "
        >
          <div class="w-md-80 w-lg-60 text-center mx-md-auto">
            <h1>{{ $t(heroTitle) }}</h1>
            <p>{{ $t(heroSubTitle) }}</p>
          </div>
        </div>
      </div>
      <!-- End Hero Section -->
    </div>
</template>

<script>
    export default {
    // 接受父组件的值
    props: {
        heroTitle: String,
        heroSubTitle: String,
        required: true
        }
    }
</script>