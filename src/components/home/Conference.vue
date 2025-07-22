<template>
  <div>
    <!-- ========== MAIN ========== -->
    <main id="content" role="main">
      <!-- Hero Section -->
      <div class="js-slick-carousel slick slick-equal-height w-100"
           data-hs-slick-carousel-options='{
           "prevArrow": "<span class=\"fas fa-arrow-left slick-arrow slick-arrow-soft-white slick-arrow-left slick-arrow-centered-y rounded-circle ml-sm-2 ml-xl-4\"></span>",
       "nextArrow": "<span class=\"fas fa-arrow-right slick-arrow slick-arrow-soft-white slick-arrow-right slick-arrow-centered-y rounded-circle mr-sm-2 mr-xl-4\"></span>",
           "infinite": true,
           "autoplay": true,
           "autoplaySpeed": 10000,
           "dots": true,
           "rows": 0,
           "dotsClass": "slick-pagination slick-pagination-white position-absolute bottom-0 right-0 left-0 mb-3"
         }'>
<!--                     :style="{backgroundImage:'url(' + conference[0].banner+ ')',backgroundRepeat:'no-repeat', backgroundPosition:'center center', backgroundSize: ''}">-->
        <div class="js-slide gradient-x-overlay-lg-white bg-img-hero space-3 min-vh-lg-100"
             :style="{backgroundImage:'url(' + conference[6].banner+ ')',backgroundRepeat:'no-repeat', backgroundPosition:'center center', backgroundSize: ''}">

          <!--        style="background-image: url(../../../static/img/post/chinesechi2021.jpg  );">-->

          <!-- Hero News -->
          <div class="container d-lg-flex align-items-lg-center">
            <article class="w-lg-100 text-center mx-lg-auto">
            <span class="d-block mb-2"
                  data-hs-slick-carousel-animation="fadeInUp">
              <span class="d-block small text-white-70 font-weight-bold text-cap mb-2"
                >{{ conference[6].subtitle }}</span>
            </span>

              <h1 class="text-white mb-1 mb-md-1 display-2"
                  data-hs-slick-carousel-animation="fadeInUp"
                  data-hs-slick-carousel-animation-delay="150">{{ conference[6].title }}</h1>
              <h1 class="text-white mb-2 mb-md-2 display-5"
                  data-hs-slick-carousel-animation="fadeInUp"
                  data-hs-slick-carousel-animation-delay="150">{{ conference[6].content }}</h1>
              <!--              <h1 class="text-white mb-2 mb-md-2 display-5"-->
              <!--                  data-hs-slick-carousel-animation="fadeInUp"-->
              <!--                  data-hs-slick-carousel-animation-delay="150">{{ conference[0].banner }}</h1>-->
              <hr data-hs-slick-carousel-animation="fadeInUp"
                  data-hs-slick-carousel-animation-delay="200">
              <h2 class="text-white mb-4 mb-md-4"
                  data-hs-slick-carousel-animation="fadeInUp"
                  data-hs-slick-carousel-animation-delay="200">{{ conference[6].date }}</h2>
              <a class="btn btn-light btn-wide transition-3d-hover" :href="conference[6].refLink" target="_blank"
                 data-hs-slick-carousel-animation="fadeInUp"
                 data-hs-slick-carousel-animation-delay="200">{{ $t('home.LearnMore') }} <i
                class="fas fa-angle-right fa-sm ml-1"></i></a>
            </article>
          </div>
          <!-- End Hero News -->
        </div>

        <!--                <conference-item v-for="(item,i) in conference" :subtitle="item.subtitle" :title="item.title"-->
        <!--                                 :content="item.content"-->
        <!--                                 :banner="item.banner" :refLink="item.refLink" :date="item.date" :key="item"></conference-item>-->
        <div class="js-slide gradient-x-overlay-lg-white bg-img-hero space-3 min-vh-lg-100"
             :style="{backgroundImage:'url(' + conference[5].banner+ ')',backgroundRepeat:'no-repeat', backgroundPosition:'center center', backgroundSize: ''}">

          <!--        style="background-image: url(../../../static/img/post/iwhec2021.jpg);">-->
          <!-- Hero News -->
          <div class="container d-lg-flex align-items-lg-center">
            <article class="w-lg-100 text-center mx-lg-auto">
            <span class="d-block mb-2"
                  data-hs-slick-carousel-animation="fadeInUp">
              <span class="d-block small text-white-70 font-weight-bold text-cap mb-2" style="color: #21325b" >{{
                  conference[5].subtitle
                }}</span>
            </span>

              <h1 class="text-dark mb-1 mb-md-1 display-2"
                  data-hs-slick-carousel-animation="fadeInUp"
                  data-hs-slick-carousel-animation-delay="150">{{ conference[5].title }}</h1>
              <h1 class="text-dark mb-2 mb-md-2 display-5"
                  data-hs-slick-carousel-animation="fadeInUp"
                  data-hs-slick-carousel-animation-delay="150">{{ conference[5].content }}</h1>
              <!--              <h1 class="text-white mb-2 mb-md-2 display-5"-->
              <!--                  data-hs-slick-carousel-animation="fadeInUp"-->
              <!--                  data-hs-slick-carousel-animation-delay="150">{{ conference[1].banner }}</h1>-->
              <hr data-hs-slick-carousel-animation="fadeInUp"
                  data-hs-slick-carousel-animation-delay="200">
              <h2 class="text-dark mb-4 mb-md-4"
                  data-hs-slick-carousel-animation="fadeInUp"
                  data-hs-slick-carousel-animation-delay="200">{{ conference[5].date }}</h2>
              <a class="btn btn-dark btn-wide transition-3d-hover" :href="conference[5].refLink" target="_blank"
                 data-hs-slick-carousel-animation="fadeInUp"
                 data-hs-slick-carousel-animation-delay="200">{{ $t('home.LearnMore') }} <i
                class="fas fa-angle-right fa-sm ml-1"></i></a>
            </article>
          </div>
          <!-- End Hero News -->
        </div>
        <div class="js-slide gradient-x-overlay-lg-white bg-img-hero space-3 min-vh-lg-100"
             :style="{backgroundImage:'url(' + conference[4].banner+ ')',backgroundRepeat:'no-repeat', backgroundPosition:'center center', backgroundSize: ''}">

          <!--        style="background-image: url(../../../static/img/post/cf2020.jpg);">-->
          <!-- Hero News -->
          <div class="container d-lg-flex align-items-lg-center">
            <article class="w-lg-100 text-center mx-lg-auto">
            <span class="d-block mb-2"
                  data-hs-slick-carousel-animation="fadeInUp">
              <span class="d-block small text-white-70 font-weight-bold text-cap mb-2">
                {{
                  conference[4].subtitle
                }}</span>
            </span>

              <h1 class="text-white mb-1 mb-md-1 display-2"
                  data-hs-slick-carousel-animation="fadeInUp"
                  data-hs-slick-carousel-animation-delay="150">{{ conference[4].title }}</h1>
              <h1 class="text-white mb-2 mb-md-2 display-5"
                  data-hs-slick-carousel-animation="fadeInUp"
                  data-hs-slick-carousel-animation-delay="150">{{ conference[4].content }}</h1>
              <!--              <h1 class="text-white mb-2 mb-md-2 display-5"-->
              <!--                  data-hs-slick-carousel-animation="fadeInUp"-->
              <!--                  data-hs-slick-carousel-animation-delay="150">{{ conference[2].banner }}</h1>-->
              <hr data-hs-slick-carousel-animation="fadeInUp"
                  data-hs-slick-carousel-animation-delay="200">
              <h2 class="text-white mb-4 mb-md-4"
                  data-hs-slick-carousel-animation="fadeInUp"
                  data-hs-slick-carousel-animation-delay="200">{{ conference[4].date }}</h2>
              <a class="btn btn-light btn-wide transition-3d-hover" :href="conference[4].refLink" target="_blank"
                 data-hs-slick-carousel-animation="fadeInUp"
                 data-hs-slick-carousel-animation-delay="200">{{ $t('home.LearnMore') }} <i
                class="fas fa-angle-right fa-sm ml-1"></i></a>
            </article>
          </div>
          <!-- End Hero News -->
        </div>

        <div class="js-slide gradient-x-overlay-lg-white bg-img-hero space-3 min-vh-lg-100"
             :style="{backgroundImage:'url(' + conference[3].banner+ ')',backgroundRepeat:'no-repeat', backgroundPosition:'center center', backgroundSize: ''}">

          <!--        style="background-image: url(../../../static/img/post/chinesechi2021.jpg  );">-->

          <!-- Hero News -->
          <div class="container d-lg-flex align-items-lg-center">
            <article class="w-lg-100 text-center mx-lg-auto">
            <span class="d-block mb-2"
                  data-hs-slick-carousel-animation="fadeInUp">
              <span class="d-block small text-white-70 font-weight-bold text-cap mb-2"
                 >{{ conference[3].subtitle }}</span>
            </span>

              <h1 class="text-white mb-1 mb-md-1 display-2"
                  data-hs-slick-carousel-animation="fadeInUp"
                  data-hs-slick-carousel-animation-delay="150">{{ conference[3].title }}</h1>
              <h1 class="text-white mb-2 mb-md-2 display-5"
                  data-hs-slick-carousel-animation="fadeInUp"
                  data-hs-slick-carousel-animation-delay="150">{{ conference[3].content }}</h1>
              <!--              <h1 class="text-white mb-2 mb-md-2 display-5"-->
              <!--                  data-hs-slick-carousel-animation="fadeInUp"-->
              <!--                  data-hs-slick-carousel-animation-delay="150">{{ conference[0].banner }}</h1>-->
              <hr data-hs-slick-carousel-animation="fadeInUp"
                  data-hs-slick-carousel-animation-delay="200">
              <h2 class="text-white mb-4 mb-md-4"
                  data-hs-slick-carousel-animation="fadeInUp"
                  data-hs-slick-carousel-animation-delay="200">{{ conference[3].date }}</h2>
              <a class="btn btn-light btn-wide transition-3d-hover" :href="conference[3].refLink" target="_blank"
                 data-hs-slick-carousel-animation="fadeInUp"
                 data-hs-slick-carousel-animation-delay="200">{{ $t('home.LearnMore') }} <i
                class="fas fa-angle-right fa-sm ml-1"></i></a>
            </article>
          </div>
          <!-- End Hero News -->
        </div>
        <div class="js-slide gradient-x-overlay-lg-white bg-img-hero space-3 min-vh-lg-100"
             :style="{backgroundImage:'url(' + conference[2].banner+ ')',backgroundRepeat:'no-repeat', backgroundPosition:'center center', backgroundSize: ''}">

          <!--        style="background-image: url(../../../static/img/post/chinesechi2021.jpg  );">-->

          <!-- Hero News -->
          <div class="container d-lg-flex align-items-lg-center">
            <article class="w-lg-100 text-center mx-lg-auto">
            <span class="d-block mb-2"
                  data-hs-slick-carousel-animation="fadeInUp">
              <span class="d-block small text-white-70 font-weight-bold text-cap mb-2"
                 >{{ conference[2].subtitle }}</span>
            </span>

              <h1 class="text-white mb-1 mb-md-1 display-2"
                  data-hs-slick-carousel-animation="fadeInUp"
                  data-hs-slick-carousel-animation-delay="150">{{ conference[2].title }}</h1>
              <h1 class="text-white mb-2 mb-md-2 display-5"
                  data-hs-slick-carousel-animation="fadeInUp"
                  data-hs-slick-carousel-animation-delay="150">{{ conference[2].content }}</h1>
              <!--              <h1 class="text-white mb-2 mb-md-2 display-5"-->
              <!--                  data-hs-slick-carousel-animation="fadeInUp"-->
              <!--                  data-hs-slick-carousel-animation-delay="150">{{ conference[0].banner }}</h1>-->
              <hr data-hs-slick-carousel-animation="fadeInUp"
                  data-hs-slick-carousel-animation-delay="200">
              <h2 class="text-white mb-4 mb-md-4"
                  data-hs-slick-carousel-animation="fadeInUp"
                  data-hs-slick-carousel-animation-delay="200">{{ conference[2].date }}</h2>
              <a class="btn btn-light btn-wide transition-3d-hover" :href="conference[2].refLink" target="_blank"
                 data-hs-slick-carousel-animation="fadeInUp"
                 data-hs-slick-carousel-animation-delay="200">{{ $t('home.LearnMore') }} <i
                class="fas fa-angle-right fa-sm ml-1"></i></a>
            </article>
          </div>
          <!-- End Hero News -->
        </div>
      </div>
      <!-- End Hero Section -->
      <!-- Properties -->
      <!--    国际研讨会下方的小方块-->
      <div class="container space-2 space-bottom-lg-2">
        <div class="row mb-5">
          <div class="col-sm-6 col-lg-6 mb-3" style="max-height: fit-content">
            <!-- Property Item -->
            <a class="card card-no-gutters h-100" :href="conference[1].refLink" target="_blank">
              <img class="img-fluid-2 rounded-lg" :src="conference[1].banner" v-if="conference[1].banner"
                   alt="Image Description">

              <!-- Body -->
              <div class="card-body">

                <div class="row align-items-center">
                  <div class="col">
                    <h4 class="text-hover-primary">{{ conference[1].title }}</h4>
                  </div>
                </div>
                <ul class="list-inline list-separator font-size-1 text-body">
                  <li class="list-inline-item">
                    <i class="fas fa-calendar-alt text-muted mr-1"></i> {{conference[1].date}}
                  </li>
                  <li class="list-inline-item">
                    <i class="fas fa-map-marker-alt text-muted mr-1"></i> {{conference[1].location}}
                  </li>
                </ul>
              </div>
              <!-- End Body -->
            </a>
            <!-- End Property Item -->
          </div>
          <div class="col-sm-6 col-lg-6 mb-3" style="max-height: fit-content">
            <!-- Property Item -->
            <a class="card card-no-gutters h-100" :href="conference[0].refLink" target="_blank">
              <img class="img-fluid-2 rounded-lg" :src="conference[0].banner" v-if="conference[0].banner"
                   alt="Image Description">

              <!-- Body -->
              <div class="card-body">

                <div class="row align-items-center">
                  <div class="col">
                    <h4 class="text-hover-primary">{{ conference[0].title }}</h4>
                  </div>
                </div>
                <ul class="list-inline list-separator font-size-1 text-body">
                  <li class="list-inline-item">
                    <i class="fas fa-calendar-alt text-muted mr-1"></i> {{ conference[0].date }}
                  </li>
                  <li class="list-inline-item">
                    <i class="fas fa-map-marker-alt text-muted mr-1"></i> {{ conference[0].location }}
                  </li>
                </ul>
              </div>
              <!-- End Body -->
            </a>
            <!-- End Property Item -->
          </div>
        </div>
        <h5 class="text-center mb-7">
          <a class="link link-collapse small font-size-1 font-weight-bold pt-1" data-toggle="collapse" href="#collapseDescriptionSection" role="button" aria-expanded="false" aria-controls="collapseDescriptionSection">
            <span class="link-collapse-default">更多</span>
            <span class="link-collapse-active">收起</span>
            <span class="link-icon ml-1">+</span>
          </a>
        </h5>
        <h3 class="text-center">历届赞助商</h3>
        <div class="mb-5 container">
          <div class="w-md-75 w-lg-50 text-center mx-md-auto mb-7" style="align-items: center">
          </div>
          <div class="row justify-content-center text-center" style="align-items: center">
            <div class="col-4 col-lg-2 mb-5 mb-lg-0 img-fluid-2 justify-content-center -2">
              <img src="../../../static/img/sponser/img1.png">
            </div>
            <div class="col-4 col-lg-2 mb-5 mb-lg-0 img-fluid-2 justify-content-center">
              <img src="../../../static/img/sponser/img2.png">
            </div>
            <div class="col-4 col-lg-2 mb-5 mb-lg-0 img-fluid-2 justify-content-center">
              <img src="../../../static/img/sponser/img3.png">
            </div>
            <div class="col-4 col-lg-2 mb-5 mb-lg-0 img-fluid-2 justify-content-center">
              <img src="../../../static/img/sponser/img4.png">
            </div>
            <div class="col-4 col-lg-2 mb-5 mb-lg-0 img-fluid-2 justify-content-center">
              <img src="../../../static/img/sponser/img5.png">
            </div>
            <div class="col-4 col-lg-2 mb-5 mb-lg-0 img-fluid-2 justify-content-center">
              <img src="../../../static/img/sponser/img6.png">
            </div>
            <div class="col-4 col-lg-2 mb-5 mb-lg-0 img-fluid-2 justify-content-center">
              <img src="../../../static/img/sponser/img7.png">
            </div>
            <div class="col-4 col-lg-2 mb-5 mb-lg-0 img-fluid-2 justify-content-center">
              <img src="../../../static/img/sponser/img8.png">
            </div>
            <div class="col-4 col-lg-2 mb-5 mb-lg-0 img-fluid-2 justify-content-center">
              <img src="../../../static/img/sponser/img9.png">
            </div>
            <div class="col-4 col-lg-2 mb-5 mb-lg-0 img-fluid-2 justify-content-center">
              <img src="../../../static/img/sponser/img10.png">
            </div>
            <div class="col-4 col-lg-2 mb-5 mb-lg-0 img-fluid-2 justify-content-center">
              <img src="../../../static/img/sponser/img11.png">
            </div>
            <div class="col-4 col-lg-2 mb-5 mb-lg-0 img-fluid-2 justify-content-center justify-content-center">
              <img src="../../../static/img/sponser/img12.png">
            </div>
            <div class="col-4 col-lg-2 mb-5 mb-lg-0 img-fluid-2 justify-content-center">
              <img src="../../../static/img/sponser/img13.png">
            </div>
            <div class="col-4 col-lg-2 mb-5 mb-lg-0 img-fluid-2 justify-content-center">
              <img src="../../../static/img/sponser/img14.png">
            </div>
            <div class="col-4 col-lg-2 mb-5 mb-lg-0 img-fluid-2 justify-content-center">
              <img src="../../../static/img/sponser/img15.png">
            </div>
            <div class="col-4 col-lg-2 mb-5 mb-lg-0 img-fluid-2 justify-content-center">
              <img src="../../../static/img/sponser/img16.png">
            </div>
            <div class="col-4 col-lg-2 mb-5 mb-lg-0 img-fluid-2 justify-content-center">
              <img src="../../../static/img/sponser/img17.png">
            </div>
            <div class="col-4 col-lg-2 mb-5 mb-lg-0 img-fluid-2 justify-content-center">
              <img src="../../../static/img/sponser/img18.png">
            </div>
            <div class="col-4 col-lg-2 mb-5 mb-lg-0 img-fluid-2 justify-content-center">
              <img src="../../../static/img/sponser/img19.png">
            </div>
            <div class="col-4 col-lg-2 mb-5 mb-lg-0 img-fluid-2 justify-content-center">
              <img src="../../../static/img/sponser/img20.png">
            </div>

          </div>
        </div>
        <!-- End Properties -->
      </div>

    </main>
    <!-- ========== END MAIN ========== -->
  </div>
</template>

<style>
.conference-white-text {
  color: white !important;
}
.conference-transparent-btn{
  background-color: transparent;
  border-color: transparent;
}
.conference-link{
  color: white;
  display: block;
  padding:0.5rem 1rem;

}
</style>

<script>
export default {
  data () {
    return {
      title: 'Conference',
      subtitle: 'InternationalChineseAssociationOfComputerHumanInteraction',
      content: '<p>协会代表: Dr. Wei Li</p><p>协会地址: Prof. Grace Ngai, Department of Computing, Hong Kong Polytechnic University, Kowloon,Hong Kong</p><p>电话: +852 2766-7279, +81-887-57-2209</p><p>传真: +852 2774-0842, +81-887-57-2209</p><br><p>协会网址: www.icachi.org</p><p>秘书处: office&commat;icachi.org</p><p>理事会成员 ML: board&commat;icachi.org</p><p>全体会员 ML: members&commat;icachi.org</p>',
      conference: [
        {
          subtitle: 'annual conference',
          title: 'Chinese CHI 2023',
          content: 'Generative · Reflective · Envisioning',
          banner: 'https://img1.imgtp.com/2023/07/06/OYP3E0Jg.jpg',
          date: 'November 13~14, 2023, Kurakura Island, Bali, Indonnesia',
          refLink: 'https://chchi2023.icachi.org/',

        },
        {
          subtitle: 'annual conference',
          title: 'Chinese CHI 2022',
          content: 'Inclusion · Resilience · New Normal',
          banner: 'https://img1.imgtp.com/2023/07/06/8cRWAc7u.jpg',
          date: 'November 5~6, 2022, Guangzhou (Online)',
          refLink: 'http://chchi2022.icachi.org/',

        },
        {
          subtitle: 'annual conference',
          title: 'Chinese CHI 2021',
          content: 'Identity · Value · Trust',
          banner: '',
          date: 'October 16~17, 2021, Online',
          refLink: 'http://chchi2021.icachi.org',

        },
        {
          subtitle: 'forum series',
          title: 'ICACHI 云论坛系列',
          content: 'ICACHI Cloud Forum',
          banner: 'https://img1.imgtp.com/2023/07/06/yamMjasG.jpg',
          date: 'May ~ July, 2020, Online',
          refLink: 'http://cf2020.icachi.org'
        },
        {
          subtitle: 'international workshop',
          title: 'IWHEC 2021',
          content: 'International Workshop on',
          banner: 'https://img1.imgtp.com/2023/07/06/7Qs9hcFM.jpg',
          date: 'March 19 ~ 20, 2021, Online',
          refLink: 'http://iw2021.xrenlab.com'
        },
        {
          title: 'forum series',
          banner: '',
          date: 'May ~ July, 2020, Online',
          locaion:'',
          refLink: 'http://cf2020.icachi.org'
        },
        {
          title: 'forum series',
          banner: '',
          date: 'May ~ July, 2020, Online',
          locaion:'',
          refLink: 'http://cf2020.icachi.org'
        },
      ],
      // conference: []

    }
  },
  created () {
    console.log(1)
    this.getMainNewsTitle()
    // if (location.href.indexOf("#reloaded") == -1) {
    //   location.href = location.href + "#reloaded";
    //   location.reload();
    // }
  },
  mounted () {
    $('.js-slick-carousel').each(function () {
      var slickCarousel = $.HSCore.components.HSSlickCarousel.init($(this))
    })
    $('header a').addClass('conference-white-text')
    $('header b').addClass('conference-white-text')
    $('header button').addClass('conference-transparent-btn')
    $('header button').removeClass('btn-light')
    $('header .navbar-brand img').attr('src', require('../../assets/svg/logos/icachi-white-text-logo.svg'))
  },

  destroyed () {
    $('header a').removeClass('conference-white-text')
    $('header button').removeClass('conference-transparent-btn')
    $('header b').removeClass('conference-white-text')
    $('header button').addClass('btn-light')
    $('header .navbar-brand img').attr('src', require('../../assets/svg/logos/icachi-text-logo.svg'))
  },
  methods: {
    getMainNewsTitle () {
      //console.log(this.MainNewsTitle)
      this.$axios.get('/public/post', {
        params: {
          type: '5',
          pageNum: 1,
          pageSize: 10,
        },
      })
        .then(res => {
          console.log(res.data)
          this.conference = res.data.data.list
        })
        .catch(err => {
          console.error(err)
        })
    }
  }
}
</script>
