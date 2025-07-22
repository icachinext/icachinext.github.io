<template>
  <div class="js-slide gradient-x-overlay-lg-white bg-img-hero space-3 min-vh-lg-100"
       :style="{backgroundImage:'url(' + banner+ ')',backgroundRepeat:'no-repeat', backgroundPosition:'center center', backgroundSize: ''}">

    <!-- Hero News -->
    <div class="container d-lg-flex align-items-lg-center">
      <article class="w-lg-100 text-center mx-lg-auto">
            <span class="d-block mb-2"
                  data-hs-slick-carousel-animation="fadeInUp">
              <a class="d-block small text-white-70 font-weight-bold text-cap mb-2"
                 href="#">{{subtitle}}</a>
            </span>

        <h1 class="text-white mb-1 mb-md-1 display-2"
            data-hs-slick-carousel-animation="fadeInUp"
            data-hs-slick-carousel-animation-delay="150">{{title}}</h1>
        <h1 class="text-white mb-2 mb-md-2 display-5"
            data-hs-slick-carousel-animation="fadeInUp"
            data-hs-slick-carousel-animation-delay="150">{{content}}</h1>
        <hr data-hs-slick-carousel-animation="fadeInUp"
            data-hs-slick-carousel-animation-delay="200">
        <h2 class="text-white mb-4 mb-md-4"
            data-hs-slick-carousel-animation="fadeInUp"
            data-hs-slick-carousel-animation-delay="200">{{date}}</h2>
        <a class="btn btn-light btn-wide transition-3d-hover" :href="refLink"
           data-hs-slick-carousel-animation="fadeInUp"
           data-hs-slick-carousel-animation-delay="200">{{ $t('home.LearnMore') }} <i
          class="fas fa-angle-right fa-sm ml-1"></i></a>
      </article>
    </div>
    <!-- End Hero News -->
  </div>
</template>

<script>
export default {
  // 接受父组件的值
  props: {
    subtitle: String,
    title: String,
    content: String,
    date:String,
    banner:String,
    refLink:String,
  }
}
</script>
