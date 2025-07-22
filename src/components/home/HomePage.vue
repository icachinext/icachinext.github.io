<template>
  <div>
    <!-- ========== MAIN CONTENT ========== -->
    <main id="content" role="main">
      <!-- Slick -->
      <div class="position-relative" style="margin-top: 6rem">
        <!-- Main Slider -->
<!--        class="js-slick-carousel slick container"-->

        <div
          id="heroSlider"
          class="js-slick-carousel slick "
          data-hs-slick-carousel-options='{
         "vertical": true,
         "verticalSwiping": true,
         "infinite": true,
         "autoplay": true,
         "autoplaySpeed": 10000,
         "dots": true,
         "dotsClass": "slick-pagination slick-pagination-white slick-pagination-vertical d-lg-none position-absolute bottom-0 right-0 mb-3 mr-3",
         "asNavFor": "#heroSliderNav"
       }'
        >

          <div
            class="
              js-slide
              d-flex
              gradient-x-overlay-sm-dark
              bg-img-hero
              min-h-500rem
            "
            style="
              background-image: url(../../../static/img/post/cf2023.jpg);width: 900px;
            "
          >
            <div class="container d-flex align-items-center min-h-500rem">
              <div class="w-lg-60 mr-5">
                <div class="mb-5">
                  <h3 class="h1 font-weight-bold text-white display-3"
                      data-hs-slick-carousel-animation="fadeInUp"
                      data-hs-slick-carousel-animation-delay="150" v-text="Display4Title" ></h3>
                  <h4 class="h1 font-weight-bold text-white display-5" style="white-space:nowrap;"
                      data-hs-slick-carousel-animation="fadeInUp"
                      data-hs-slick-carousel-animation-delay="150" v-text="Display4SubTitle1"></h4>
                  <h4 class="h1 font-weight-bold text-white display-5"
                      data-hs-slick-carousel-animation="fadeInUp"
                      data-hs-slick-carousel-animation-delay="150" v-text="Display4SubTitle2"></h4>
                  <hr data-hs-slick-carousel-animation="fadeInUp"
                      data-hs-slick-carousel-animation-delay="300">
                  <h3 class="font-weight-bold text-white"
                      data-hs-slick-carousel-animation="fadeInUp"
                      data-hs-slick-carousel-animation-delay="300" v-text="Display4Time" ></h3>
                </div>
                <a class="btn btn-primary btn-wide transition-3d-hover" :href="Display4Src" target="_blank"
                   data-hs-slick-carousel-animation="fadeInUp"
                   data-hs-slick-carousel-animation-delay="300">{{ $t("home.LearnMore") }} <i class="fas fa-angle-right fa-sm ml-1"></i></a>
              </div>
            </div>
          </div>

          <div
            class="
              js-slide
              d-flex
              gradient-x-overlay-sm-dark
              bg-img-hero
              min-h-500rem
            "
            style="
              background-image: url(../../../static/img/post/cf2022.jpg);width: 900px;
            "
          >
            <div class="container d-flex align-items-center min-h-500rem">
              <div class="w-lg-60 mr-5">
                <div class="mb-5">
                  <h3 class="h1 font-weight-bold text-white display-3"
                      data-hs-slick-carousel-animation="fadeInUp"
                      data-hs-slick-carousel-animation-delay="150" v-text="Display5Title" ></h3>
                  <h4 class="h1 font-weight-bold text-white display-5" style="white-space:nowrap;"
                      data-hs-slick-carousel-animation="fadeInUp"
                      data-hs-slick-carousel-animation-delay="150" v-text="Display5SubTitle1"></h4>
                  <h4 class="h1 font-weight-bold text-white display-5"
                      data-hs-slick-carousel-animation="fadeInUp"
                      data-hs-slick-carousel-animation-delay="150" v-text="Display5SubTitle2"></h4>
                  <hr data-hs-slick-carousel-animation="fadeInUp"
                      data-hs-slick-carousel-animation-delay="300">
                  <h3 class="font-weight-bold text-white"
                      data-hs-slick-carousel-animation="fadeInUp"
                      data-hs-slick-carousel-animation-delay="300" v-text="Display5Time" ></h3>
                </div>
                <a class="btn btn-primary btn-wide transition-3d-hover" :href="Display5Src" target="_blank"
                   data-hs-slick-carousel-animation="fadeInUp"
                   data-hs-slick-carousel-animation-delay="300">{{ $t("home.LearnMore") }} <i class="fas fa-angle-right fa-sm ml-1"></i></a>
              </div>
            </div>
          </div>

          <div
            class="
              js-slide
              d-flex
              gradient-x-overlay-sm-dark
              bg-img-hero
              min-h-500rem
            "
            style="background-image: url(../../../static/img/post/chinesechi2021.jpg);">
            <div class="container d-flex align-items-center min-h-500rem">
              <div class="w-lg-60 mr-5">
                <div class="mb-5">
                <h3 class="h1 font-weight-bold text-white display-3"
                    data-hs-slick-carousel-animation="fadeInUp"
                    data-hs-slick-carousel-animation-delay="150" v-text="Display1Title">Chinese CHI 2021</h3>
                <h4 class="h1 font-weight-bold text-white display-5"
                    data-hs-slick-carousel-animation="fadeInUp"
                    data-hs-slick-carousel-animation-delay="150" v-text="Display1SubTitle1">Identity · Value · Trust</h4>
                <h4 class="h1 font-weight-bold text-white display-5"
                    data-hs-slick-carousel-animation="fadeInUp"
                    data-hs-slick-carousel-animation-delay="150" v-text="Display1SubTitle2">认同 · 价值 · 信任</h4>
                <hr data-hs-slick-carousel-animation="fadeInUp"
                    data-hs-slick-carousel-animation-delay="300">
                <h3 class="font-weight-bold text-white"
                    data-hs-slick-carousel-animation="fadeInUp"
                    data-hs-slick-carousel-animation-delay="300" v-text="Display1Time">October 16~17, 2021, Online</h3>
              </div>
              <a class="btn btn-primary btn-wide transition-3d-hover" :href="Display1Src" target="_blank"
                 data-hs-slick-carousel-animation="fadeInUp"
                 data-hs-slick-carousel-animation-delay="300">{{ $t("home.LearnMore") }} <i class="fas fa-angle-right fa-sm ml-1"></i></a>
              </div>
            </div>
          </div>

          <div
            class="
              js-slide
              d-flex
              gradient-x-overlay-sm-dark
              bg-img-hero
              min-h-500rem
            "
            style="
              background-image: url(../../../static/img/post/iwhec2021.jpg);width: 900px;
            "
          >
            <div class="container d-flex align-items-center min-h-500rem">
              <div class="w-lg-60 mr-5">
                <div class="mb-5">
                <h3 class="h1 font-weight-bold text-white display-3"
                    data-hs-slick-carousel-animation="fadeInUp"
                    data-hs-slick-carousel-animation-delay="150" v-text="Display2Title" >IWHEC 2021</h3>
                <h4 class="h1 font-weight-bold text-white display-5"
                    data-hs-slick-carousel-animation="fadeInUp"
                    data-hs-slick-carousel-animation-delay="150" v-text="Display2SubTitle1">International Workshop on</h4>
                <h4 class="h1 font-weight-bold text-white display-5"
                    data-hs-slick-carousel-animation="fadeInUp"
                    data-hs-slick-carousel-animation-delay="150" v-text="Display2SubTitle2">Human-Engaged Computing 2021</h4>
                <hr data-hs-slick-carousel-animation="fadeInUp"
                    data-hs-slick-carousel-animation-delay="300">
                <h3 class="font-weight-bold text-white"
                    data-hs-slick-carousel-animation="fadeInUp"
                    data-hs-slick-carousel-animation-delay="300" v-text="Display2Time" >March 19 ~ 20, 2021, Online</h3>
              </div>
              <a class="btn btn-primary btn-wide transition-3d-hover" :href="Display2Src" target="_blank"
                 data-hs-slick-carousel-animation="fadeInUp"
                 data-hs-slick-carousel-animation-delay="300">{{ $t("home.LearnMore") }} <i class="fas fa-angle-right fa-sm ml-1"></i></a>
              </div>
            </div>
          </div>

          <div
            class="
              js-slide
              d-flex
              gradient-x-overlay-sm-dark
              bg-img-hero
              min-h-500rem
            "
            style="
              background-image: url(../../../static/img/post/cf2020.jpg);
            "
          >
            <div class="container d-flex align-items-center min-h-500rem">
              <div class="w-lg-60 mr-5">
                <div class="mb-5">
                <h3 class="h1 font-weight-bold text-white display-3"
                    data-hs-slick-carousel-animation="fadeInUp"
                    data-hs-slick-carousel-animation-delay="150" v-text="Display3Title" >ICACHI 云论坛系列</h3>
                <h4 class="h1 font-weight-bold text-white display-5"
                    data-hs-slick-carousel-animation="fadeInUp"
                    data-hs-slick-carousel-animation-delay="150" v-text="Display3SubTitle1">ICACHI Cloud Forum</h4>
                <h4 class="h1 font-weight-bold text-white display-5"
                    data-hs-slick-carousel-animation="fadeInUp"
                    data-hs-slick-carousel-animation-delay="150"></h4>
                <hr data-hs-slick-carousel-animation="fadeInUp"
                    data-hs-slick-carousel-animation-delay="300">
                <h3 class="font-weight-bold text-white"
                    data-hs-slick-carousel-animation="fadeInUp"
                    data-hs-slick-carousel-animation-delay="300" v-text="Display3Time">March ~ July, 2020, Online</h3>
              </div>
              <a class="btn btn-primary btn-wide transition-3d-hover" :href="Display3Src" target="_blank"
                 data-hs-slick-carousel-animation="fadeInUp"
                 data-hs-slick-carousel-animation-delay="300">{{ $t("home.LearnMore") }} <i class="fas fa-angle-right fa-sm ml-1"></i></a>
              </div>
            </div>
          </div>


        </div>
        <!-- End Main Slider -->

        <!-- Slider Nav -->
        <div
          class="
            container
            slick-pagination-line-wrapper
            content-centered-y
            right-0
            left-0
          "
        >
          <div class="content-centered-y right-0 mr-3">
            <div
              id="heroSliderNav"
              class="
                js-slick-carousel
                slick slick-pagination-line
                max-w-27rem
                ml-auto
              "
              data-hs-slick-carousel-options='{
             "vertical": true,
             "verticalSwiping": true,
             "infinite": true,
             "autoplay": true,
             "autoplaySpeed": 10000,
             "slidesToShow": 3,
             "isThumbs": true,
             "asNavFor": "#heroSlider"
           }'
            >
              <div class="js-slide my-4">
                <span class="text-white" v-text="Display4">Chinese CHI 2023</span>

                <span class="slick-pagination-line-progress">
                  <span class="slick-pagination-line-progress-helper"></span>
                </span>
              </div>
              <div class="js-slide my-4">
                <span class="text-white" v-text="Display5">Chinese CHI 2022</span>

                <span class="slick-pagination-line-progress">
                  <span class="slick-pagination-line-progress-helper"></span>
                </span>
              </div>
              <div class="js-slide my-4">
                <span class="text-white" v-text="Display1">Chinese CHI 2021</span>

                <span class="slick-pagination-line-progress">
                  <span class="slick-pagination-line-progress-helper"></span>
                </span>
              </div>
              <div class="js-slide my-4">
                <span class="text-white" v-text="Display2">IWHEC 2021</span>

                <span class="slick-pagination-line-progress">
                  <span class="slick-pagination-line-progress-helper"></span>
                </span>
              </div>
              <div class="js-slide my-4">
                <span class="text-white" v-text="Display3">ICACHI Cloud Forum</span>

                <span class="slick-pagination-line-progress">
                  <span class="slick-pagination-line-progress-helper"></span>
                </span>
              </div>


            </div>
          </div>
        </div>
        <!-- End Slider Nav -->
      </div>
      <!-- End Slick -->
      <!-- Hero Section -->
      <div class="d-lg-flex position-relative">
        <div
          class="
            container
            d-lg-flex
            align-items-lg-center
            space-1 space-top-xl-1 space-bottom-lg-1
          "
        >
          <!-- Content -->
          <div class="w-md-100">
            <h1 class="display-4 mb-4">
              {{ $t("aboutus.AboutUs") }}
            </h1>
            <div class="row">
              <div class="col-lg-5">
                <div class="pt-2 pb-lg-2">
                  <!-- Title -->
                  <div class="mb-4 mb-md-4">
                    <p v-text="$t('home.AboutUsContent')">
                    </p>
                  </div>
                  <!-- End Title -->
                  <!--                30+ 70+-->

<!--                  <div class="row">-->
                  <!--                    <div class="col-6 mb-3 mb-md-5">-->
                  <!--                      <div class="pr-lg-4">-->
                  <!--                        <span class="js-counter h2 text-primary">30</span>-->
                  <!--                        <span class="h2 text-primary">+</span>-->
                  <!--                        <p>-->
                  <!--                          {{ $t('home.tips1') }}-->
                  <!--                        </p>-->
                  <!--                      </div>-->
                  <!--                    </div>-->

                  <!--                    <div class="col-6 mb-3 mb-md-5">-->
                  <!--                      <div class="pr-lg-4">-->
                  <!--                        <span class="js-counter h2 text-primary">70</span>-->
                  <!--                        <span class="h2 text-primary">+</span>-->
                  <!--                        <span class="h2 text-primary">/{{$t('home.tips5')}}</span>-->

                  <!--                        <p>-->
                  <!--                          {{ $t('home.tips2') }}-->
                  <!--                        </p>-->
                  <!--                      </div>-->
                  <!--                    </div>-->

                  <!--                    <div class="col-6">-->
                  <!--                      <div class="pr-lg-4">-->
                  <!--                        <span class="js-counter h2 text-primary">95</span>-->
                  <!--                        <span class="h2 text-primary">%</span>-->
                  <!--                        <p>-->
                  <!--                          {{ $t('home.tips3') }}-->
                  <!--                        </p>-->
                  <!--                      </div>-->
                  <!--                    </div>-->

                  <!--                    <div class="col-6">-->
                  <!--                      <div class="pr-lg-4">-->
                  <!--                        <span class="js-counter h2 text-primary">20</span>-->
                  <!--                        <span class="h2 text-primary">+</span>-->
                  <!--                        <p>-->
                  <!--                          {{ $t('home.tips4') }}-->
                  <!--                        </p>-->
                  <!--                      </div>-->
                  <!--                    </div>-->
                  <!--                  </div>-->

                  <!--                30+ 70+ 结束-->

                </div>
                <br>
                <a
                  class="btn btn-primary btn-wide transition-3d-hover"
                  href="/auth/signup" target="_self"
                  >{{ $t("home.JoinUs") }}</a
                >
                <a class="btn btn-link btn-wide" href="/aboutus" target="_self"
                  >{{ $t("home.LearnMore") }} <i class="fas fa-angle-right fa-sm ml-1"></i
                ></a>
              </div>
              <div class="col-lg-7 justify-content-lg-end" >
          <!-- SVG Illustration -->
<!--                  <img class="img-fluid" style="margin-left:8rem;margin-top: -1rem" src="../../../static/svg/illustrations/discussion-scene-icachi.svg" alt="Image Description">-->
                  <img style="border-radius: 0.75rem;margin-left: 40%;width: 60%;" src="../../../static/img/official/aboutus/img7.jpg" alt="">

          <!-- End SVG Illustration -->
        </div>
            </div>
          </div>
          <!-- End Content -->
        </div>
      </div>
      <!-- End Hero Section -->

      <div class="container">
        <hr />
      </div>

      <!-- Articles Section -->
      <div class="container space-1 space-top-xl-1 space-bottom-lg-1">
        <!-- Title -->
        <div class="row mb-5">
          <div class="col-6">
            <h2 class="h3 mb-0">{{ $t("home.LatestNews") }}</h2>
          </div>
          <div class="col-6 text-right">
            <a class="font-weight-bold" href="/newsroom" target="_self"
              >{{ $t("home.ViewAll") }} <i class="fas fa-angle-right fa-sm ml-1"></i
            ></a>
          </div>
        </div>
        <!-- End Title -->

        <div class="row mx-n2 mx-lg-n3">
          <news-item :NewsTitle="news[0].title" :NewsImg="news[0].img"  :NewsDay="news[0].date" :NewsSubtitle="news[0].subtitle" :pid="news[0].pid"></news-item>
 <!--         <div class="col-sm-6 col-lg-4 mb-3 mb-sm-8">   -->
          <!-- Blog Card -->
  <!--
          <article class="card h-100">
            <div class="card-img-top position-relative">
              <img class="card-img-top" :src="News1Img" alt="Image Description">
              <figure class="ie-curved-y position-absolute right-0 bottom-0 left-0 mb-n1">
                <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" viewBox="0 0 1920 100.1">
                  <path fill="#fff" d="M0,0c0,0,934.4,93.4,1920,0v100.1H0L0,0z"/>
                </svg>
              </figure>
            </div>

            <div class="card-body">
              <h3><a class="text-inherit" v-html="News1Title" :href="News1Src">ICACHI代表访问中国科协</a></h3>
              <p v-text="News1Content"></p>
            </div>

            <div class="card-footer border-0 pt-0">
              <div class="media align-items-center">
                <div class="avatar-group">
                  <a class="avatar avatar-xs avatar-circle" href="#" data-toggle="tooltip" data-placement="top" title="Nataly Gaga">
                    <img class="avatar-img" src="../../../static/img/committee/100x100/icachi-avatar.png" alt="Image Description">
                  </a>
                </div>
                <div class="media-body d-flex justify-content-end text-muted font-size-1 ml-2" v-text="News1Day">
                  July 15
                </div>
              </div>
            </div>
          </article>
   -->
          <!-- End Blog Card -->
   <!--     </div>   -->

          <news-item :NewsTitle="news[1].title" :NewsImg="news[1].img"  :NewsDay="news[1].date" :NewsSubtitle="news[1].subtitle" :pid="news[1].pid"></news-item>

          <news-item :NewsTitle="news[2].title" :NewsImg="news[2].img"  :NewsDay="news[2].date" :NewsSubtitle="news[2].subtitle" :pid="news[2].pid"></news-item>


          <!--       <div class="col-sm-6 col-lg-4 mb-3 mb-sm-8">       -->
          <!-- Blog Card -->
  <!--
          <article class="card bg-primary text-white h-100">
            <div class="card-body p-4 p-lg-5">
              <span class="badge badge-light py-2 px-3 mb-5 text-primary">Featured</span>
              <h3 class="h2"><a class="text-white" v-html="News2Title" :href="News2Src">2019人机交互领域发展蓝皮书在厦发布</a></h3>
              <p v-text="News2Content"></p>
            </div>
            <div class="card-footer bg-primary border-0 pt-0 px-5 pb-5">
              <div class="media align-items-center">
                <div class="avatar-group">
                  <a class="avatar avatar-xs avatar-circle" href="#" data-toggle="tooltip" data-placement="top" title="Aaron Larsson">
                    <img class="avatar-img" src="../../../static/img/committee/100x100/icachi-avatar.png" alt="Image Description">
                  </a>
                </div>
                <div class="media-body d-flex justify-content-end text-white-70 font-size-1 ml-2" v-text="News2Day">
                  July 15
                </div>
              </div>
            </div>
          </article>
-->
          <!-- End Blog Card -->
 <!--       </div>       -->
        </div>
      </div>
      <!-- End Articles Section -->
    </main>
    <!-- ========== END MAIN CONTENT ========== -->
  </div>
</template>

<script>
export default {
  data () {
    return {
      title: 'Bylaws',
      subtitle: '2019 / 10 / 1',
      content:
        '<h2>第一章 总则</h2><br /><h4>第 1 条(名称及地址)</h4><p>(1) 本会的名称为世界华人华侨人机交互协会(英文名 International Chinese Association of Computer Human Interaction,简称「ICACHI」)。URL 为 http://www.icachi.org/</p><p>(2)本会的总部设在香港。协会地址: Prof. Grace Ngai, Department of Computing, Hong Kong Polytechnic University, Kowloon, Hong Kong</p><p>理事会成员 ML: board&commat;icachi.org</p><p>电话: +852 2766-7279, +81-887-57-2209</p><p>传真: +852 2774-0842, +81-887-57-2209</p><p>协会网址: www.icachi.org</p><p>秘书处: office&commat;icachi.org</p><p>全体会员 ML: members&commat;icachi.org</p><p>(3)本会在世界其他各地设协会的办事处。目前协会在北京和多伦多分别设有办事处。</p>',
      Display1Title:'Chinese CHI 2021',
      Display1Time:'October 16~17, 2021, Online',
      Display1SubTitle1:'Identity · Value · Trust',
      Display1SubTitle2:'认同 · 价值 · 信任',
      Display1Src:'http://chchi2021.icachi.org',
      Display2Title:'IWHEC 2021',
      Display2Time:'March 19 ~ 20, 2021, Online',
      Display2SubTitle1:'International Workshop on',
      Display2SubTitle2:'Human-Engaged Computing 2021',
      Display2Src:'http://iw2021.xrenlab.com',
      Display3Title:'ICACHI 云论坛系列',
      Display3Time:'March ~ July, 2020, Online',
      Display3SubTitle1:'ICACHI Cloud Forum',
      Display3SubTitle2:'',
      Display3Src:'http://cf2020.icachi.org',
      Display4Title:'Chinese CHI 2023',
      Display4Time:'November 13~14, 2023, Kurakura Island, Bali, Indonnesia',
      Display4SubTitle1:'Generative · Reflective · Envisioning',
      Display4SubTitle2:'创智 · 反思 · 展望',
      Display4Src:'https://chchi2023.icachi.org/',
      Display5Title:'Chinese CHI 2022',
      Display5Time:'November 5~6, 2022, Guangzhou (Online)',
      Display5SubTitle1:'Inclusion · Resilience · New Normal',
      Display5SubTitle2:'包容 · 韧性 · 新常态',
      Display5Src:'http://chchi2022.icachi.org/',

      Display1:'Chinese CHI 2021',
      Display2:'IWHEC 2021',
      Display3:'ICACHI Cloud Forum',
      Display4:'Chinese CHI 2023',
      Display5:'Chinese CHI 2022',

      AboutUsContent:'                      世界华人华侨人机交互协会（英文名International Chinese\n' +
        '                      Association of Computer Human\n' +
        '                      Interaction，简称“ICACHI”）于2012年5月10日在美国Austin（ACM\n' +
        '                      CHI2012国际会议期间）成立。理事会由27名来自于本研究领域（Human\n' +
        '                      Computer\n' +
        '                      Interaction：人机交互）且活跃在世界各地的海外华人华侨代表组成（包括两名监事）。',
      News1Src:'blog-single-article.html',
      News2Src:'blog-single-article.html',
      news:[
        {title:'',subtitle:'',date:'',img:'',src:'',pid:''},
        {title:'',subtitle:'',date:'',img:'',src:'',pid:''},
        {title:'',subtitle:'',date:'',img:'',src:'',pid:''},
        {title:'',subtitle:'',date:'',img:'',src:'',pid:''},

      ]

    }
  },
  getNowNews(pid){
    window.localStorage.setItem('newsPid', pid)
    window.location.href="/nownews"
  },

  created () {
    console.log(1)
    this.getMainNewsTitle()
  },
  methods: {
    getMainNewsTitle () {
      this.$axios.get('/public/post', {
        params: {
          type: 2,
          pageNum: 1,
          pageSize: 10,
        },
      })
        .then(res => {
          console.log(res.data)
          for(let i=0;i<3;i++)
          {
            this.news[i].title = res.data.data.list[i].title
            this.news[i].subtitle = res.data.data.list[i].subtitle;
            this.news[i].date = res.data.data.list[i].createTime.substr(0,10);
            this.news[i].pid = res.data.data.list[i].pid;
            this.news[i].img = res.data.data.list[i].banner;
            this.news[i].src = res.data.data.list[i].refLink;
          }


          //数据库还差一个IMG
          //this.MainNewsDay=
          // console.log(this.MainNewsTitle)
        })
        .catch(err => {
          console.error(err)
        })
    }
  },


  mounted () {
    // INITIALIZATION OF SLICK CAROUSEL
    // =======================================================
    $('#heroSliderNav').on('init', function (event, slick) {
      $(slick.$slider).find('.slick-pagination-line-progress .slick-pagination-line-progress-helper').each(function() {
        $(this).css({
          transitionDuration: (slick.options.autoplaySpeed - slick.options.speed) + 'ms'
        });
      });

      setTimeout(function() {
        $(slick.$slider).addClass('slick-dots-ready');
      });
    });

    $('#heroSliderNav').one('beforeChange', function (event, slick) {
      $(slick.$slider).find('.slick-pagination-line-progress .slick-pagination-line-progress-helper').each(function() {
        $(this).css({
          transitionDuration: (slick.options.autoplaySpeed + slick.options.speed) + 'ms'
        });
      });
    });

    // INITIALIZATION OF SLICK CAROUSEL
    // =======================================================
    $('.js-slick-carousel').each(function () {
      var slickCarousel = $.HSCore.components.HSSlickCarousel.init($(this))
    })

    $(window).on('resize', function() {
        $('#heroSliderNav').slick('setPosition');
      });
  }
}
</script>
