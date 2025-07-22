<template>
  <div>
    <!-- ========== MAIN ========== -->
    <main id="cotent" role="main">
      <!--      <homepage-hero :heroTitle="heroTitle" :heroSubTitle="heroSubTitle"></homepage-hero>-->
      <!--      <homepage-hero></homepage-hero>-->
      <!--<div style="width: auto;height: 100px"></div>-->
      <!-- Slick -->
<!--      <div class="position-relative" style="margin-top: 6rem">-->
<!--        &lt;!&ndash;        <ul class="demo1El" id="empile">&ndash;&gt;-->
<!--        &lt;!&ndash;          <li><img src="../../../static/img/p1.png"/></li>&ndash;&gt;-->
<!--        &lt;!&ndash;          <li><img src="../../../static/img/p2.png"/></li>&ndash;&gt;-->
<!--        &lt;!&ndash;          <li><img src="../../../static/img/p3.png"/></li>&ndash;&gt;-->
<!--        &lt;!&ndash;        </ul>&ndash;&gt;-->

<!--        &lt;!&ndash; Main Slider &ndash;&gt;-->
<!--        &lt;!&ndash;        class="js-slick-carousel slick container"&ndash;&gt;-->
<!--        &lt;!&ndash;轮播图模板&ndash;&gt;-->



<!--        <div-->
<!--          id="heroSlider"-->
<!--          class="js-slick-carousel slick "-->
<!--          data-hs-slick-carousel-options='{-->
<!--         "vertical": true,-->
<!--         "verticalSwiping": true,-->
<!--         "infinite": true,-->
<!--         "autoplay": true,-->
<!--         "autoplaySpeed": 5000,-->
<!--         "dots": true,-->
<!--         "dotsClass": "slick-pagination slick-pagination-white slick-pagination-vertical d-lg-none position-absolute bottom-0 right-0 mb-3 mr-3",-->
<!--         "asNavFor": "#heroSliderNav"-->
<!--       }'-->
<!--        >-->
<!--          <div-->
<!--            class="-->
<!--              js-slide-->
<!--              d-flex-->
<!--              gradient-x-overlay-sm-dark-->
<!--              bg-img-hero-->
<!--              min-h-380rem-->
<!--            "-->
<!--            style="-->
<!--              background-image: url(https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fi-1-lanrentuku.qqxzb-img.com%2F2020%2F12%2F5%2Fd64d35b1-71ec-4226-840d-f81cc0d397b0.jpg%3FimageView2%2F2%2Fw%2F1024&refer=http%3A%2F%2Fi-1-lanrentuku.qqxzb-img.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1646077974&t=193c5d37ad3f1795ab2d8420edc865a3);-->
<!--            "-->
<!--          >-->
<!--            <div class="container d-flex align-items-center min-h-500rem">-->
<!--              <div class="w-lg-60 mr-5">-->
<!--                <div class="mb-4 min-h-300rem max-w-100rem"   :style="{backgroundImage:'url(' + img1 + ')',}">-->

<!--                </div>-->
<!--              </div>-->
<!--            </div>-->
<!--          </div>-->

<!--          <div-->
<!--            class="-->
<!--              js-slide-->
<!--              d-flex-->
<!--              gradient-x-overlay-sm-dark-->
<!--              bg-img-hero-->
<!--              min-h-380rem-->
<!--            "-->
<!--            style="-->
<!--              background-image: url(https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fi-1-lanrentuku.qqxzb-img.com%2F2020%2F12%2F5%2Fd64d35b1-71ec-4226-840d-f81cc0d397b0.jpg%3FimageView2%2F2%2Fw%2F1024&refer=http%3A%2F%2Fi-1-lanrentuku.qqxzb-img.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1646077974&t=193c5d37ad3f1795ab2d8420edc865a3);-->
<!--            "-->

<!--          >-->
<!--            <div class="container d-flex align-items-center min-h-500rem">-->
<!--              <div class="w-lg-60 mr-5">-->
<!--                <div class="mb-4 min-h-300rem max-w-100rem"   :style="{backgroundImage:'url(' + img2 + ')',}">-->

<!--                </div>-->
<!--              </div>-->
<!--            </div>-->
<!--          </div>-->

<!--          <div-->
<!--            class="-->
<!--              js-slide-->
<!--              d-flex-->
<!--              gradient-x-overlay-sm-dark-->
<!--              bg-img-hero-->
<!--              min-h-380rem-->

<!--            "-->
<!--            style="-->
<!--              background-image: url(https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fi-1-lanrentuku.qqxzb-img.com%2F2020%2F12%2F5%2Fd64d35b1-71ec-4226-840d-f81cc0d397b0.jpg%3FimageView2%2F2%2Fw%2F1024&refer=http%3A%2F%2Fi-1-lanrentuku.qqxzb-img.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1646077974&t=193c5d37ad3f1795ab2d8420edc865a3);-->
<!--            "          >-->
<!--            <div class="container d-flex align-items-center min-h-500rem">-->
<!--              <div class="w-lg-60 mr-5">-->
<!--                <div class="mb-4 min-h-300rem max-w-100rem"   :style="{backgroundImage:'url(' + img3 + ')',}">-->

<!--                </div>-->
<!--              </div>-->
<!--            </div>-->
<!--          </div>-->
<!--        </div>-->
<!--        &lt;!&ndash;         End Main Slider&ndash;&gt;-->

<!--        &lt;!&ndash;         Slider Nav&ndash;&gt;-->
<!--        <div-->
<!--          class="-->
<!--            container-->
<!--            slick-pagination-line-wrapper-->
<!--            content-centered-y-->
<!--            right-0-->
<!--            left-0-->
<!--          "-->
<!--        >-->
<!--          <div class="content-centered-y right-0 mr-3">-->
<!--            <div-->
<!--              id="heroSliderNav"-->
<!--              class="-->
<!--                js-slick-carousel-->
<!--                slick slick-pagination-line-->
<!--                max-w-27rem-->
<!--                ml-auto-->
<!--              "-->
<!--              data-hs-slick-carousel-options='{-->
<!--             "vertical": true,-->
<!--             "verticalSwiping": true,-->
<!--             "infinite": true,-->
<!--             "autoplay": true,-->
<!--             "autoplaySpeed": 10000,-->
<!--             "slidesToShow": 3,-->
<!--             "isThumbs": true,-->
<!--             "asNavFor": "#heroSlider"-->
<!--           }'-->
<!--            >-->
<!--              <div class="js-slide my-3">-->
<!--                <span class="text-white" >ICACHI成员合照1</span>-->

<!--                <span class="slick-pagination-line-progress">-->
<!--                  <span class="slick-pagination-line-progress-helper"></span>-->
<!--                </span>-->
<!--              </div>-->
<!--              <div class="js-slide my-3">-->
<!--                <span class="text-white" >ICACHI成员合照2</span>-->

<!--                <span class="slick-pagination-line-progress">-->
<!--                  <span class="slick-pagination-line-progress-helper"></span>-->
<!--                </span>-->
<!--              </div>-->
<!--              <div class="js-slide my-3">-->
<!--                <span class="text-white" >ICACHI成员合照3</span>-->

<!--                <span class="slick-pagination-line-progress">-->
<!--                  <span class="slick-pagination-line-progress-helper"></span>-->
<!--                </span>-->
<!--              </div>-->
<!--            </div>-->
<!--          </div>-->
<!--        </div>-->
<!--        &lt;!&ndash; End Slider Nav &ndash;&gt;-->
<!--      </div>-->
      <!-- End Slick -->
      <div style="width: auto; height: 100px;"></div>
      <div class="container space-lg-1">
        <h3 id="intro" _msthash="65260" _msttexthash="84720194">世界华人华侨人机交互协会（ICACHI）</h3>
        <div class="mb-3">
          <p class="text-justify" style="margin-top: 1rem" _msthash="1004861" _msttexthash="1240962515">  世界华人华侨人机交互协会（英文名International Chinese Association of Computer Human Interaction简称“ICACHI”） 于2012年5月10日在美国Austin（ACM CHI2012国际会议期间）成立。理事会由27名来自于本研究领域（Human Computer Interaction：人机交互）且活跃在世界各地的海外华人华侨代表组成（包括两名监事）。 本会目标和定位（或协会宗旨，见图）：促进会员发展，提升会员在所在国及世界的地位，通过研究人机交互为人类做出自己应有的贡献。协会对内、对外是一个开发放和透明的纯学术团体。本协会是第一个由华人华侨创立的横跨世界、超越地域和地区的纯专业性（人机交互）科技团体组织。</p>

          <div class="collapse" id="collapseLinkDescription" _msthidden="2">
            <p class="text-justify" _msthash="724360" _msttexthash="123652256" _msthidden="1">The aim of this workshop is to rethink the relationship between humans and
              computers.
              The workshop will strive to achieve a common platform to advance various idea exchanges
              around the world, resulting in the evolution of a stronger workforce in order to create a better world
              to live in.
              We are inviting distinguished speakers from around the world and from several domains such as
              human-computer interaction, brain science, computer science, AI, engaged human, engaging technology,
              design so on.</p>

            <p class="text-justify" _msthash="724477" _msttexthash="1569852700" _msthidden="1">Covid-19 has significantly impacted the lives of every person on the planet. Much
              of the
              world that was familiar to most people is in pause mode. People are ordered to stay at home
              in order to save lives by slowing the spread of the deadly virus. Fortunately, with the fast
              development of computing technologies and digital services, along with the rapid
              construction of information infrastructures, people are able to source information from
              television media, radio broadcasts, social media, and various Internet avenues. Technologies
              are playing a central, critical, and arguably indispensable role in our daily lives during
              the pandemic. But the new efficiencies afforded by new technologies is a two-edged sword,
              and it is capable of healing or harming human relationships, human integrity and human
              enterprises. For example, efficient private and personal access to information, accessible
              publishing, and new modes of social interaction open the door to the dissemination of fake
              news, to trolling, to prejudiced opinions and to undue influence that overwhelms and
              confuses people more efficiently than ever before. On the other hand, responses to such
              threats seem to invite despotic intrusions into privacy and the potential diminishment of
              the right to personal opinions and personal expression. Thus, besides dealing with the
              relationship between humans and computers under consideration of the human future in general,
              the workshop also seeks to suggest how researchers who work on the relationship between
              humans and computers can help develop and enhance the user’s ability to distinguish between
              inauthentic and authentic information during and after the current crisis.</p>
          </div>
        </div>
        <div id="fancyboxGallery" class="container space-top-1 space-top-lg-1 space-1 space-lg-1">
          <div style='width:100%;height:100%;background-color:white;' id='modal_2'>
            <div class='modal_2' id='modalw'>
              <img id='bgImg' @click="notshow" />
            </div>
          </div>
        <div class="row mx-n2">
          <div class="col-4 col-sm px-2 mb-3 mb-sm-0" @click="showBgImg(img1)">
            <a class="js-fancybox media-viewer" href="javascript:;" data-hs-fancybox-options='{
                  "selector": "#fancyboxGallery .js-fancybox",
                  "speed": 700
                }' :data-src=img1 data-caption="IWHEC 2020">
              <img class="img-fluid rounded" :src=img1 alt="" id="img1" >

              <span class="media-viewer-container">
                    <span class="media-viewer-icon">
                      <i class="fas fa-plus media-viewer-icon-inner"></i>
                    </span>
                  </span>
            </a>
          </div>

          <div class="col-4 col-sm px-2 mb-3 mb-sm-0"  @click="showBgImg(img2)">
            <a class="js-fancybox media-viewer" href="javascript:;" data-hs-fancybox-options='{
                  "selector": "#fancyboxGallery .js-fancybox",
                  "speed": 700
                }' :data-src=img2 data-caption="IWHEC 2017">
              <img class="img-fluid rounded" :src=img2 alt="" id="img2">

              <span class="media-viewer-container">
                    <span class="media-viewer-icon">
                      <i class="fas fa-plus media-viewer-icon-inner"></i>
                    </span>
                  </span>
            </a>
          </div>

          <div class="col-4 col-sm px-2 mb-3 mb-sm-0"  @click="showBgImg(img3)">
            <a class="js-fancybox media-viewer" href="javascript:;" data-hs-fancybox-options='{
                  "selector": "#fancyboxGallery .js-fancybox",
                  "speed": 700
                }' :data-src=img3 data-caption="IWHEC 2019">
              <img class="img-fluid rounded" :src=img3 alt="" id="img3" >

              <span class="media-viewer-container">
                    <span class="media-viewer-icon">
                      <i class="fas fa-plus media-viewer-icon-inner"></i>
                    </span>
                  </span>
            </a>
          </div>

          <div class="col-4 col-sm px-2 mb-3 mb-sm-0" @click="showBgImg(img4)">
            <a class="js-fancybox media-viewer" href="javascript:;" data-hs-fancybox-options='{
                  "selector": "#fancyboxGallery .js-fancybox",
                  "speed": 700
                }' :data-src=img4 data-caption="IWHEC 2017">
              <img class="img-fluid rounded" :src=img4 alt="" id="img4">

              <span class="media-viewer-container">
                    <span class="media-viewer-icon">
                      <i class="fas fa-plus media-viewer-icon-inner"></i>
                    </span>
                  </span>
            </a>
          </div>

          <div class="col-4 col-sm px-2 mb-3 mb-sm-0" @click="showBgImg(img5)">
            <a class="js-fancybox media-viewer" href="javascript:;" data-hs-fancybox-options='{
                  "selector": "#fancyboxGallery .js-fancybox",
                  "speed": 700
                }' :data-src=img5 data-caption="IWHEC 2020">
              <img class="img-fluid rounded" :src=img5 alt="" id="img5" >

              <span class="media-viewer-container">
                    <span class="media-viewer-icon">
                      <i class="fas fa-plus media-viewer-icon-inner"></i>
                    </span>
                  </span>
            </a>
          </div>

          <div class="col-4 col-sm px-2 mb-3 mb-sm-0" @click="showBgImg(img6)">
            <a class="js-fancybox media-viewer" href="javascript:;" data-hs-fancybox-options='{
                  "selector": "#fancyboxGallery .js-fancybox",
                  "speed": 700
                }' :data-src=img6 data-caption="IWHEC 2020">
              <img class="img-fluid rounded" :src=img6 alt="" id="img6" >

              <span class="media-viewer-container">
                    <span class="media-viewer-icon">
                      <i class="fas fa-plus media-viewer-icon-inner"></i>
                    </span>
                  </span>
            </a>
          </div>

        </div>
      </div>
      </div>
  <!-- End Row -->

      <!-- Hero Section -->
      <!--      照片墙-->
      <!--    <div class="container space-top-2 space-top-lg-2 space-bottom-1">-->
      <!--      <div id="intro" class="space-bottom-1" v-html="content1"></div>-->
      <!--      &lt;!&ndash; Gallery Section &ndash;&gt;-->
      <!--      <div class="row mx-n2">-->
      <!--        <div class="col-6 col-md px-2 mb-3">-->
      <!--          <div class="h-250rem bg-img-hero"  :style="{backgroundImage:'url(' + img1 + ')'}" ></div>-->
      <!--        </div>-->
      <!--        <div class="col-md-3 d-none d-md-block px-2 mb-3">-->
      <!--          <div class="h-250rem bg-img-hero" :style="{backgroundImage:'url(' + img2 + ')'}"></div>-->
      <!--        </div>-->
      <!--        <div class="col-6 col-md px-2 mb-3">-->
      <!--          <div class="h-250rem bg-img-hero" :style="{backgroundImage:'url(' + img3 + ')'}"></div>-->
      <!--        </div>-->

      <!--        <div class="w-100"></div>-->

      <!--        <div class="col-6 col-md px-2 mb-3 mb-md-0">-->
      <!--          <div class="h-250rem bg-img-hero" :style="{backgroundImage:'url(' + img4 + ')'}"></div>-->
      <!--        </div>-->
      <!--        <div class="col-md-4 d-none d-md-block px-2 mb-3 mb-md-0">-->
      <!--          <div class="h-250rem bg-img-hero" :style="{backgroundImage:'url(' + img5 + ')'}"></div>-->
      <!--        </div>-->
      <!--        <div class="col-6 col-md px-2">-->
      <!--          <div class="h-250rem bg-img-hero" :style="{backgroundImage:'url(' + img6 + ')'}"></div>-->
      <!--        </div>-->
      <!--      </div>-->
      <!--      &lt;!&ndash; End Gallery Section &ndash;&gt;-->
      <!--    </div>-->
      <!-- End Hero Section -->

      <!-- Stats Section 30+ 70+-->
<!--      <div class="container space-top-lg-1 space-bottom-2 space-bottom-lg-1">-->
<!--        <div class="row justify-content-lg-center">-->
<!--          <div class="col-sm-3 col-lg-3 mb-7 mb-sm-0">-->
<!--            &lt;!&ndash; Stats &ndash;&gt;-->
<!--            <div class="text-center">-->
<!--              <span class="d-block display-4 font-size-md-down-4 text-dark text-uppercase mb-0">{{Detail1}}</span>-->
<!--              <span>{{ $t('home.tips1') }}</span>-->
<!--            </div>-->
<!--            &lt;!&ndash; End Stats &ndash;&gt;-->
<!--          </div>-->

<!--          <div class="col-sm-3 col-lg-3 mb-7 mb-sm-0">-->
<!--            &lt;!&ndash; Stats &ndash;&gt;-->
<!--            <div class="text-center">-->
<!--              <span class="d-block display-4 font-size-md-down-4 text-dark text-uppercase mb-0">70+</span>-->
<!--              <span>{{ $t('home.tips2') }}/{{$t('home.tips5')}}</span>-->
<!--            </div>-->
<!--            &lt;!&ndash; End Stats &ndash;&gt;-->
<!--          </div>-->

<!--          <div class="col-sm-3 col-lg-3">-->
<!--            &lt;!&ndash; Stats &ndash;&gt;-->
<!--            <div class="text-center">-->
<!--              <span class="d-block display-4 font-size-md-down-4 text-dark text-uppercase mb-0">{{Detail3}}</span>-->
<!--              <span>{{ $t('home.tips3') }}</span>-->
<!--            </div>-->
<!--            &lt;!&ndash; End Stats &ndash;&gt;-->
<!--          </div>-->

<!--          <div class="col-sm-3 col-lg-3">-->
<!--            &lt;!&ndash; Stats &ndash;&gt;-->
<!--            <div class="text-center">-->
<!--              <span class="d-block display-4 font-size-md-down-4 text-dark text-uppercase mb-0">{{Detail4}}</span>-->
<!--              <span>{{ $t('home.tips4') }}</span>-->
<!--            </div>-->
<!--            &lt;!&ndash; End Stats &ndash;&gt;-->
<!--          </div>-->
<!--        </div>-->
<!--      </div>-->
      <!-- End Stats Section 30+ 70+-->

      <!-- Divider -->
      <div class="container">
        <div class="w-lg-65 mx-lg-auto">
          <hr class="my-0">
        </div>
      </div>
      <!-- End Divider -->

      <!-- About Section -->
      <div class="container space-2 space-lg-2">
        <div class="row justify-content-lg-between">
          <div class="col-lg-6 mb-5 mb-lg-0">
            <img class="avatar-img" :src="img7" alt="" id="img7" >
          </div>
          <div class="col-lg-6" v-html="content2">
          </div>
        </div>
      </div>
      <!-- End About Section -->

      <!-- Divider -->
      <div class="container">
        <div class="w-lg-65 mx-lg-auto">
          <hr class="my-0">
<!--          分割线-->
        </div>
      </div>
      <!-- End Divider -->

      <!-- Team Section -->
<!--      <div class="container space-2 space-lg-1">-->
<!--        &lt;!&ndash; Title &ndash;&gt;-->
<!--        <div class="w-md-80 w-lg-60 text-center mx-md-auto mb-5 mb-md-6" style="align-items: center">-->
<!--&lt;!&ndash;          <span class="d-block small font-weight-bold text-cap mb-2">Our team</span>&ndash;&gt;-->
<!--          <h2 style="display: inline-block;margin: 0 auto">{{ $t('aboutus.ourteam') }}</h2>-->
<!--        </div>-->
<!--        &lt;!&ndash; End Title &ndash;&gt;-->
<!--        &lt;!&ndash;      <div class="col-sm-6 col-lg-3 px-2 mb-3">&ndash;&gt;-->

<!--        &lt;!&ndash;头像&ndash;&gt;-->
<!--&lt;!&ndash;        一.协会会长&ndash;&gt;-->
<!--        <div class="row mx-n2 mb-2 " style="display: flex;justify-content: center;align-items: center" >-->

<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class=" avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="协会会长" src="../../../static/img/committee/100x100/FuZhiyong.jpg" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">协会会长</span>-->
<!--                <a href="">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">付志勇</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">清华大学</p>-->
<!--              </div>-->
<!--              &lt;!&ndash;              社交媒体&ndash;&gt;-->
<!--              &lt;!&ndash;              <div class="card-footer border-0 pt-0">&ndash;&gt;-->
<!--              &lt;!&ndash;              &lt;!&ndash; Social Networks &ndash;&gt;&ndash;&gt;-->
<!--              &lt;!&ndash;              <ul class="list-inline mb-0">&ndash;&gt;-->
<!--              &lt;!&ndash;                <li class="list-inline-item">&ndash;&gt;-->
<!--              &lt;!&ndash;                  <a class="btn btn-xs btn-icon btn-soft-secondary rounded" href="#">&ndash;&gt;-->
<!--              &lt;!&ndash;                    <i class="fab fa-facebook-f"></i>&ndash;&gt;-->
<!--              &lt;!&ndash;                  </a>&ndash;&gt;-->
<!--              &lt;!&ndash;                </li>&ndash;&gt;-->
<!--              &lt;!&ndash;                <li class="list-inline-item">&ndash;&gt;-->
<!--              &lt;!&ndash;                  <a class="btn btn-xs btn-icon btn-soft-secondary rounded" href="#">&ndash;&gt;-->
<!--              &lt;!&ndash;                    <i class="fab fa-google"></i>&ndash;&gt;-->
<!--              &lt;!&ndash;                  </a>&ndash;&gt;-->
<!--              &lt;!&ndash;                </li>&ndash;&gt;-->
<!--              &lt;!&ndash;                <li class="list-inline-item">&ndash;&gt;-->
<!--              &lt;!&ndash;                  <a class="btn btn-xs btn-icon btn-soft-secondary rounded" href="#">&ndash;&gt;-->
<!--              &lt;!&ndash;                    <i class="fab fa-twitter"></i>&ndash;&gt;-->
<!--              &lt;!&ndash;                  </a>&ndash;&gt;-->
<!--              &lt;!&ndash;                </li>&ndash;&gt;-->
<!--              &lt;!&ndash;              </ul>&ndash;&gt;-->
<!--              &lt;!&ndash;              &lt;!&ndash; End Social Networks &ndash;&gt;&ndash;&gt;-->
<!--              &lt;!&ndash;            </div>&ndash;&gt;-->
<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--&lt;!&ndash;          <div class="col-sm-2">&ndash;&gt;-->
<!--&lt;!&ndash;            &lt;!&ndash; Team &ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;            <div class="card w-100 h-95 transition-3d-hover">&ndash;&gt;-->
<!--&lt;!&ndash;              <div class="card-body">&ndash;&gt;-->
<!--&lt;!&ndash;                <div class=" avatar-circle mb-4" style="margin-left: 0.7rem">&ndash;&gt;-->
<!--&lt;!&ndash;                  <img class="avatar-img"&ndash;&gt;-->
<!--&lt;!&ndash;                       data-container="body" data-toggle="popover" data-placement="top"&ndash;&gt;-->
<!--&lt;!&ndash;                       data-content="内容Content" data-trigger="hover focus"&ndash;&gt;-->
<!--&lt;!&ndash;                       title="简要介绍"&ndash;&gt;-->
<!--&lt;!&ndash;                       src="../../../static/img/committee/100x100/xiaojuan.png" alt="" >&ndash;&gt;-->
<!--&lt;!&ndash;                </div>&ndash;&gt;-->

<!--&lt;!&ndash;                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">{{ $t("aboutus.VicePresident") }}</span>&ndash;&gt;-->
<!--&lt;!&ndash;                <a href="https://www.cse.ust.hk/~mxj/">&ndash;&gt;-->
<!--&lt;!&ndash;                  <h4 class="text-lh-sm" style="text-align: center">麻晓娟</h4>&ndash;&gt;-->
<!--&lt;!&ndash;                </a>&ndash;&gt;-->
<!--&lt;!&ndash;                <p class="font-size-1" style="text-align: center">香港科技大学</p>&ndash;&gt;-->
<!--&lt;!&ndash;              </div>&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              社交媒体&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              <div class="card-footer border-0 pt-0">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              &lt;!&ndash; Social Networks &ndash;&gt;&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              <ul class="list-inline mb-0">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                <li class="list-inline-item">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  <a class="btn btn-xs btn-icon btn-soft-secondary rounded" href="#">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                    <i class="fab fa-facebook-f"></i>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  </a>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                </li>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                <li class="list-inline-item">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  <a class="btn btn-xs btn-icon btn-soft-secondary rounded" href="#">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                    <i class="fab fa-google"></i>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  </a>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                </li>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                <li class="list-inline-item">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  <a class="btn btn-xs btn-icon btn-soft-secondary rounded" href="#">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                    <i class="fab fa-twitter"></i>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  </a>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                </li>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              </ul>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              &lt;!&ndash; End Social Networks &ndash;&gt;&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;            </div>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;            </div>&ndash;&gt;-->
<!--&lt;!&ndash;            &lt;!&ndash; End Team &ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;          </div>&ndash;&gt;-->
<!--&lt;!&ndash;          <div class="col-sm-2">&ndash;&gt;-->
<!--&lt;!&ndash;            &lt;!&ndash; Team &ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;            <div class="card w-100 h-95 transition-3d-hover">&ndash;&gt;-->
<!--&lt;!&ndash;              <div class="card-body">&ndash;&gt;-->
<!--&lt;!&ndash;                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">&ndash;&gt;-->
<!--&lt;!&ndash;                  <img class="avatar-img"&ndash;&gt;-->
<!--&lt;!&ndash;                       data-container="body" data-toggle="popover" data-placement="top"&ndash;&gt;-->
<!--&lt;!&ndash;                       data-content="内容Content" data-trigger="hover focus"&ndash;&gt;-->
<!--&lt;!&ndash;                       title="简要介绍"&ndash;&gt;-->
<!--&lt;!&ndash;                       src="../../../static/img/committee/100x100/shuminzhai.png" alt="Image Description" >&ndash;&gt;-->
<!--&lt;!&ndash;                </div>&ndash;&gt;-->

<!--&lt;!&ndash;                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">顾问/咨询委员会</span>&ndash;&gt;-->
<!--&lt;!&ndash;                <a href="https://www.cse.ust.hk/~mxj/">&ndash;&gt;-->
<!--&lt;!&ndash;                  <h4 class="text-lh-sm" style="text-align: center">翟树民</h4>&ndash;&gt;-->
<!--&lt;!&ndash;                </a>&ndash;&gt;-->
<!--&lt;!&ndash;                <p class="font-size-1" style="text-align: center">美国谷歌</p>&ndash;&gt;-->
<!--&lt;!&ndash;              </div>&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              社交媒体&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              <div class="card-footer border-0 pt-0">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              &lt;!&ndash; Social Networks &ndash;&gt;&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              <ul class="list-inline mb-0">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                <li class="list-inline-item">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  <a class="btn btn-xs btn-icon btn-soft-secondary rounded" href="#">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                    <i class="fab fa-facebook-f"></i>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  </a>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                </li>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                <li class="list-inline-item">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  <a class="btn btn-xs btn-icon btn-soft-secondary rounded" href="#">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                    <i class="fab fa-google"></i>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  </a>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                </li>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                <li class="list-inline-item">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  <a class="btn btn-xs btn-icon btn-soft-secondary rounded" href="#">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                    <i class="fab fa-twitter"></i>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  </a>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                </li>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              </ul>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              &lt;!&ndash; End Social Networks &ndash;&gt;&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;            </div>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;            </div>&ndash;&gt;-->
<!--&lt;!&ndash;            &lt;!&ndash; End Team &ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;          </div>&ndash;&gt;-->
<!--&lt;!&ndash;          <div class="col-sm-2">&ndash;&gt;-->
<!--&lt;!&ndash;            &lt;!&ndash; Team &ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;            <div class="card w-100 h-95 transition-3d-hover">&ndash;&gt;-->
<!--&lt;!&ndash;              <div class="card-body">&ndash;&gt;-->
<!--&lt;!&ndash;                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">&ndash;&gt;-->
<!--&lt;!&ndash;                  <img class="avatar-img"&ndash;&gt;-->
<!--&lt;!&ndash;                       data-container="body" data-toggle="popover" data-placement="top"&ndash;&gt;-->
<!--&lt;!&ndash;                       data-content="内容Content" data-trigger="hover focus"&ndash;&gt;-->
<!--&lt;!&ndash;                       title="简要介绍"&ndash;&gt;-->
<!--&lt;!&ndash;                       src="../../../static/img/committee/100x100/ren.jpg" alt="Image Description" >&ndash;&gt;-->
<!--&lt;!&ndash;                </div>&ndash;&gt;-->

<!--&lt;!&ndash;                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">顾问/咨询委员会</span>&ndash;&gt;-->
<!--&lt;!&ndash;                <a href="https://www.cse.ust.hk/~mxj/">&ndash;&gt;-->
<!--&lt;!&ndash;                  <h4 class="text-lh-sm" style="text-align: center">任向实</h4>&ndash;&gt;-->
<!--&lt;!&ndash;                </a>&ndash;&gt;-->
<!--&lt;!&ndash;                <p class="font-size-1" style="text-align: center">日本高知工科大学</p>&ndash;&gt;-->
<!--&lt;!&ndash;              </div>&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              社交媒体&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              <div class="card-footer border-0 pt-0">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              &lt;!&ndash; Social Networks &ndash;&gt;&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              <ul class="list-inline mb-0">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                <li class="list-inline-item">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  <a class="btn btn-xs btn-icon btn-soft-secondary rounded" href="#">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                    <i class="fab fa-facebook-f"></i>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  </a>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                </li>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                <li class="list-inline-item">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  <a class="btn btn-xs btn-icon btn-soft-secondary rounded" href="#">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                    <i class="fab fa-google"></i>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  </a>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                </li>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                <li class="list-inline-item">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  <a class="btn btn-xs btn-icon btn-soft-secondary rounded" href="#">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                    <i class="fab fa-twitter"></i>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  </a>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                </li>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              </ul>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              &lt;!&ndash; End Social Networks &ndash;&gt;&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;            </div>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;            </div>&ndash;&gt;-->
<!--&lt;!&ndash;            &lt;!&ndash; End Team &ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;          </div>&ndash;&gt;-->
<!--&lt;!&ndash;          <div class="col-sm-2">&ndash;&gt;-->
<!--&lt;!&ndash;            &lt;!&ndash; Team &ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;            <div class="card w-100 h-95 transition-3d-hover">&ndash;&gt;-->
<!--&lt;!&ndash;              <div class="card-body">&ndash;&gt;-->
<!--&lt;!&ndash;                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">&ndash;&gt;-->
<!--&lt;!&ndash;                  <img class="avatar-img"&ndash;&gt;-->
<!--&lt;!&ndash;                       data-container="body" data-toggle="popover" data-placement="top"&ndash;&gt;-->
<!--&lt;!&ndash;                       data-content="内容Content" data-trigger="hover focus"&ndash;&gt;-->
<!--&lt;!&ndash;                       title="简要介绍"&ndash;&gt;-->
<!--&lt;!&ndash;                       src="../../../static/img/committee/100x100/yuan.png" alt="Image Description" >&ndash;&gt;-->
<!--&lt;!&ndash;                </div>&ndash;&gt;-->

<!--&lt;!&ndash;                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">专委会（学术期刊）</span>&ndash;&gt;-->
<!--&lt;!&ndash;                <a href="https://www.cse.ust.hk/~mxj/">&ndash;&gt;-->
<!--&lt;!&ndash;                  <h4 class="text-lh-sm" style="text-align: center">袁晓君</h4>&ndash;&gt;-->
<!--&lt;!&ndash;                </a>&ndash;&gt;-->
<!--&lt;!&ndash;                <p class="font-size-1" style="text-align: center">纽约州立大学</p>&ndash;&gt;-->
<!--&lt;!&ndash;              </div>&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              社交媒体&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              <div class="card-footer border-0 pt-0">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              &lt;!&ndash; Social Networks &ndash;&gt;&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              <ul class="list-inline mb-0">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                <li class="list-inline-item">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  <a class="btn btn-xs btn-icon btn-soft-secondary rounded" href="#">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                    <i class="fab fa-facebook-f"></i>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  </a>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                </li>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                <li class="list-inline-item">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  <a class="btn btn-xs btn-icon btn-soft-secondary rounded" href="#">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                    <i class="fab fa-google"></i>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  </a>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                </li>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                <li class="list-inline-item">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  <a class="btn btn-xs btn-icon btn-soft-secondary rounded" href="#">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                    <i class="fab fa-twitter"></i>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  </a>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                </li>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              </ul>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              &lt;!&ndash; End Social Networks &ndash;&gt;&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;            </div>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;            </div>&ndash;&gt;-->
<!--&lt;!&ndash;            &lt;!&ndash; End Team &ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;          </div>&ndash;&gt;-->
<!--&lt;!&ndash;          <div class="col-sm-2">&ndash;&gt;-->
<!--&lt;!&ndash;            &lt;!&ndash; Team &ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;            <div class="card w-100 h-95 transition-3d-hover">&ndash;&gt;-->
<!--&lt;!&ndash;              <div class="card-body">&ndash;&gt;-->
<!--&lt;!&ndash;                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">&ndash;&gt;-->
<!--&lt;!&ndash;                  <img class="avatar-img"&ndash;&gt;-->
<!--&lt;!&ndash;                       data-container="body" data-toggle="popover" data-placement="top"&ndash;&gt;-->
<!--&lt;!&ndash;                       data-content="内容Content" data-trigger="hover focus"&ndash;&gt;-->
<!--&lt;!&ndash;                       title="简要介绍"&ndash;&gt;-->
<!--&lt;!&ndash;                       src="../../../static/img/committee/100x100/liuwei.jpg" alt="Image Description" >&ndash;&gt;-->
<!--&lt;!&ndash;                </div>&ndash;&gt;-->

<!--&lt;!&ndash;                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">专委会（学术期刊）</span>&ndash;&gt;-->
<!--&lt;!&ndash;                <a href="https://www.cse.ust.hk/~mxj/">&ndash;&gt;-->
<!--&lt;!&ndash;                  <h4 class="text-lh-sm" style="text-align: center">刘伟</h4>&ndash;&gt;-->
<!--&lt;!&ndash;                </a>&ndash;&gt;-->
<!--&lt;!&ndash;                <p class="font-size-1" style="text-align: center">北京师范大学</p>&ndash;&gt;-->
<!--&lt;!&ndash;              </div>&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              社交媒体&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              <div class="card-footer border-0 pt-0">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              &lt;!&ndash; Social Networks &ndash;&gt;&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              <ul class="list-inline mb-0">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                <li class="list-inline-item">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  <a class="btn btn-xs btn-icon btn-soft-secondary rounded" href="#">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                    <i class="fab fa-facebook-f"></i>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  </a>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                </li>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                <li class="list-inline-item">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  <a class="btn btn-xs btn-icon btn-soft-secondary rounded" href="#">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                    <i class="fab fa-google"></i>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  </a>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                </li>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                <li class="list-inline-item">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  <a class="btn btn-xs btn-icon btn-soft-secondary rounded" href="#">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                    <i class="fab fa-twitter"></i>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  </a>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                </li>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              </ul>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              &lt;!&ndash; End Social Networks &ndash;&gt;&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;            </div>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;            </div>&ndash;&gt;-->
<!--&lt;!&ndash;            &lt;!&ndash; End Team &ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;          </div>&ndash;&gt;-->
<!--&lt;!&ndash;          <div class="col-sm-2">&ndash;&gt;-->
<!--&lt;!&ndash;            &lt;!&ndash; Team &ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;            <div class="card w-100 h-95 transition-3d-hover">&ndash;&gt;-->
<!--&lt;!&ndash;              <div class="card-body">&ndash;&gt;-->
<!--&lt;!&ndash;                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">&ndash;&gt;-->
<!--&lt;!&ndash;                  <img class="avatar-img"&ndash;&gt;-->
<!--&lt;!&ndash;                       data-container="body" data-toggle="popover" data-placement="top"&ndash;&gt;-->
<!--&lt;!&ndash;                       data-content="内容Content" data-trigger="hover focus"&ndash;&gt;-->
<!--&lt;!&ndash;                       title="简要介绍"&ndash;&gt;-->
<!--&lt;!&ndash;                       src="../../../static/img/committee/100x100/junhu.jpg" alt="Image Description" >&ndash;&gt;-->
<!--&lt;!&ndash;                </div>&ndash;&gt;-->

<!--&lt;!&ndash;                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">专委会（学术期刊）</span>&ndash;&gt;-->
<!--&lt;!&ndash;                <a href="https://www.cse.ust.hk/~mxj/">&ndash;&gt;-->
<!--&lt;!&ndash;                  <h4 class="text-lh-sm" style="text-align: center">胡军</h4>&ndash;&gt;-->
<!--&lt;!&ndash;                </a>&ndash;&gt;-->
<!--&lt;!&ndash;                <p class="font-size-1" style="text-align: center">埃因霍温理工大学</p>&ndash;&gt;-->
<!--&lt;!&ndash;              </div>&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              社交媒体&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              <div class="card-footer border-0 pt-0">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              &lt;!&ndash; Social Networks &ndash;&gt;&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              <ul class="list-inline mb-0">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                <li class="list-inline-item">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  <a class="btn btn-xs btn-icon btn-soft-secondary rounded" href="#">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                    <i class="fab fa-facebook-f"></i>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  </a>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                </li>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                <li class="list-inline-item">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  <a class="btn btn-xs btn-icon btn-soft-secondary rounded" href="#">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                    <i class="fab fa-google"></i>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  </a>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                </li>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                <li class="list-inline-item">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  <a class="btn btn-xs btn-icon btn-soft-secondary rounded" href="#">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                    <i class="fab fa-twitter"></i>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  </a>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                </li>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              </ul>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              &lt;!&ndash; End Social Networks &ndash;&gt;&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;            </div>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;            </div>&ndash;&gt;-->
<!--&lt;!&ndash;            &lt;!&ndash; End Team &ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;          </div>&ndash;&gt;-->
<!--&lt;!&ndash;          <div class="col-sm-2">&ndash;&gt;-->
<!--&lt;!&ndash;            &lt;!&ndash; Team &ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;            <div class="card w-100 h-95 transition-3d-hover">&ndash;&gt;-->
<!--&lt;!&ndash;              <div class="card-body">&ndash;&gt;-->
<!--&lt;!&ndash;                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">&ndash;&gt;-->
<!--&lt;!&ndash;                  <img class="avatar-img"&ndash;&gt;-->
<!--&lt;!&ndash;                       data-container="body" data-toggle="popover" data-placement="top"&ndash;&gt;-->
<!--&lt;!&ndash;                       data-content="内容Content" data-trigger="hover focus"&ndash;&gt;-->
<!--&lt;!&ndash;                       title="简要介绍"&ndash;&gt;-->
<!--&lt;!&ndash;                       src="../../../static/img/committee/100x100/jianzhao.jpg" alt="Image Description" >&ndash;&gt;-->
<!--&lt;!&ndash;                </div>&ndash;&gt;-->

<!--&lt;!&ndash;                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">专委会（学术活动）</span>&ndash;&gt;-->
<!--&lt;!&ndash;                <a href="https://www.cse.ust.hk/~mxj/">&ndash;&gt;-->
<!--&lt;!&ndash;                  <h4 class="text-lh-sm" style="text-align: center">赵健</h4>&ndash;&gt;-->
<!--&lt;!&ndash;                </a>&ndash;&gt;-->
<!--&lt;!&ndash;                <p class="font-size-1" style="text-align: center">加拿大滑铁卢大学</p>&ndash;&gt;-->
<!--&lt;!&ndash;              </div>&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              社交媒体&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              <div class="card-footer border-0 pt-0">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              &lt;!&ndash; Social Networks &ndash;&gt;&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              <ul class="list-inline mb-0">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                <li class="list-inline-item">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  <a class="btn btn-xs btn-icon btn-soft-secondary rounded" href="#">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                    <i class="fab fa-facebook-f"></i>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  </a>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                </li>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                <li class="list-inline-item">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  <a class="btn btn-xs btn-icon btn-soft-secondary rounded" href="#">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                    <i class="fab fa-google"></i>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  </a>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                </li>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                <li class="list-inline-item">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  <a class="btn btn-xs btn-icon btn-soft-secondary rounded" href="#">&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                    <i class="fab fa-twitter"></i>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                  </a>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                </li>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              </ul>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;              &lt;!&ndash; End Social Networks &ndash;&gt;&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;              &lt;!&ndash;                        </div>&ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;            </div>&ndash;&gt;-->
<!--&lt;!&ndash;            &lt;!&ndash; End Team &ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;          </div>&ndash;&gt;-->
<!--&lt;!&ndash;          <div class="col-sm-2">&ndash;&gt;-->
<!--&lt;!&ndash;            &lt;!&ndash; Team &ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;            <div class="card w-100 h-95 transition-3d-hover">&ndash;&gt;-->
<!--&lt;!&ndash;              <div class="card-body">&ndash;&gt;-->
<!--&lt;!&ndash;                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">&ndash;&gt;-->
<!--&lt;!&ndash;                  <img class="avatar-img"&ndash;&gt;-->
<!--&lt;!&ndash;                       data-container="body" data-toggle="popover" data-placement="top"&ndash;&gt;-->
<!--&lt;!&ndash;                       data-content="内容Content" data-trigger="hover focus"&ndash;&gt;-->
<!--&lt;!&ndash;                       title="简要介绍"&ndash;&gt;-->
<!--&lt;!&ndash;                       src="../../../static/img/committee/100x100/guihuanfeng.jpeg" alt="Image Description" >&ndash;&gt;-->
<!--&lt;!&ndash;                </div>&ndash;&gt;-->

<!--&lt;!&ndash;                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">专委会（学术活动）</span>&ndash;&gt;-->
<!--&lt;!&ndash;                <a href="https://www.cse.ust.hk/~mxj/">&ndash;&gt;-->
<!--&lt;!&ndash;                  <h4 class="text-lh-sm" style="text-align: center">冯桂焕</h4>&ndash;&gt;-->
<!--&lt;!&ndash;                </a>&ndash;&gt;-->
<!--&lt;!&ndash;                <p class="font-size-1" style="text-align: center">南京大学</p>&ndash;&gt;-->
<!--&lt;!&ndash;              </div>&ndash;&gt;-->
<!--&lt;!&ndash;            </div>&ndash;&gt;-->
<!--&lt;!&ndash;            &lt;!&ndash; End Team &ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;          </div>&ndash;&gt;-->
<!--&lt;!&ndash;          <div class="col-sm-2">&ndash;&gt;-->
<!--&lt;!&ndash;            &lt;!&ndash; Team &ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;            <div class="card w-100 h-95 transition-3d-hover">&ndash;&gt;-->
<!--&lt;!&ndash;              <div class="card-body">&ndash;&gt;-->
<!--&lt;!&ndash;                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">&ndash;&gt;-->
<!--&lt;!&ndash;                  <img class="avatar-img"&ndash;&gt;-->
<!--&lt;!&ndash;                       data-container="body" data-toggle="popover" data-placement="top"&ndash;&gt;-->
<!--&lt;!&ndash;                       data-content="内容Content" data-trigger="hover focus"&ndash;&gt;-->
<!--&lt;!&ndash;                       title="简要介绍"&ndash;&gt;-->
<!--&lt;!&ndash;                       src="../../../static/img/committee/100x100/jiyi.jpg" alt="Image Description" >&ndash;&gt;-->
<!--&lt;!&ndash;                </div>&ndash;&gt;-->

<!--&lt;!&ndash;                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">专委会（专题会议）</span>&ndash;&gt;-->
<!--&lt;!&ndash;                <a href="https://www.cse.ust.hk/~mxj/">&ndash;&gt;-->
<!--&lt;!&ndash;                  <h4 class="text-lh-sm" style="text-align: center">纪毅</h4>&ndash;&gt;-->
<!--&lt;!&ndash;                </a>&ndash;&gt;-->
<!--&lt;!&ndash;                <p class="font-size-1" style="text-align: center">广东工业大学</p>&ndash;&gt;-->
<!--&lt;!&ndash;              </div>&ndash;&gt;-->
<!--&lt;!&ndash;            </div>&ndash;&gt;-->
<!--&lt;!&ndash;            &lt;!&ndash; End Team &ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;          </div>&ndash;&gt;-->

<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class=" avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="协会副会长"-->
<!--                       src="../../../static/img/committee/100x100/xiaojuan.png" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">协会副会长</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">麻晓娟</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">香港科技大学</p>-->
<!--              </div>-->

<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->


<!--        </div>-->

<!--&lt;!&ndash;        二.协会副会长&ndash;&gt;-->


<!--        &lt;!&ndash;        三.顾问/咨询委员会&ndash;&gt;-->
<!--        <div class="row mx-n2 mb-2" style="display: flex;justify-content: center;align-items: center">-->
<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="发展顾问"-->
<!--                       src="../../../static/img/committee/100x100/shuminzhai.png" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">发展顾问</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">翟树民</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">美国谷歌</p>-->
<!--              </div>-->

<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="发展顾问"-->
<!--                       src="../../../static/img/committee/100x100/ren.jpg" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">发展顾问</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">任向实</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">日本高知工科大学</p>-->
<!--              </div>-->

<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="发展顾问"-->
<!--                       src="../../../static/img/committee/100x100/avatar.png" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">发展顾问</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">李维</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">加拿大华为</p>-->
<!--              </div>-->

<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="发展顾问"-->
<!--                       src="../../../static/img/committee/100x100/avatar.png" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">发展顾问</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">张虹</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">美国普渡大学</p>-->
<!--              </div>-->

<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->

<!--        </div>-->

<!--        &lt;!&ndash;        四.专委会   : 1. 学术期刊+教材   2. 学术活动  3. 专题会议  4.战略发展  &ndash;&gt;-->
<!--        <div class="row mx-n2 mb-2" style="display: flex;justify-content: center;align-items: center">-->

<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="理事"-->
<!--                       src="../../../static/img/committee/100x100/tuhuawei.jpeg" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">理事</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">涂华伟</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">澳洲乐卓博大学</p>-->
<!--              </div>-->
<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="理事"-->
<!--                       src="../../../static/img/committee/100x100/jianzhao.jpg" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">理事</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">赵健</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">加拿大滑铁卢大学</p>-->
<!--              </div>-->

<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="理事"-->
<!--                       src="../../../static/img/committee/100x100/avatar.png" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">理事</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">姚俊峰</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">厦门大学</p>-->
<!--              </div>-->
<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="理事"-->
<!--                       src="../../../static/img/committee/100x100/yuan.png" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">理事</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">袁晓君</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">纽约州立大学</p>-->
<!--              </div>-->

<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="理事"-->
<!--                       src="../../../static/img/committee/100x100/avatar.png" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">理事</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">王建民</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">同济大学</p>-->
<!--              </div>-->

<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="理事"-->
<!--                       src="../../../static/img/committee/100x100/junhu.jpg" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">理事</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">胡军</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">埃因霍温理工大学</p>-->
<!--              </div>-->

<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--          </div>-->
<!--        <div class="row mx-n2 mb-2" style="display: flex;justify-content: center;align-items: center">-->

<!--        <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="理事"-->
<!--                       src="../../../static/img/committee/100x100/liuwei.jpg" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">理事</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">刘伟</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">北京师范大学</p>-->
<!--              </div>-->

<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="理事"-->
<!--                       src="../../../static/img/committee/100x100/avatar.png" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">理事</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">王大阔</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">美国IBM研究院</p>-->
<!--              </div>-->

<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="理事"-->
<!--                       src="../../../static/img/committee/100x100/avatar.png" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">理事</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">孙华彤</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">美国华盛顿大学</p>-->
<!--              </div>-->

<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="理事"-->
<!--                       src="../../../static/img/committee/100x100/avatar.png" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">理事</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">米海鹏</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">清华大学</p>-->
<!--              </div>-->
<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="理事"-->
<!--                       src="../../../static/img/committee/100x100/avatar.png" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">理事</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">喻纯</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">清华大学</p>-->
<!--              </div>-->
<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--        <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="理事"-->
<!--                       src="../../../static/img/committee/100x100/guihuanfeng.jpeg" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">理事</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">冯桂焕</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">南京大学</p>-->
<!--              </div>-->
<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--</div>-->
<!--        <div class="row mx-n2 mb-2" style="display: flex;justify-content: center;align-items: center">-->

<!--        <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="理事"-->
<!--                       src="../../../static/img/committee/100x100/avatar.png" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">理事</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">杨兴栋</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">美国达特茅斯学院</p>-->
<!--              </div>-->
<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="理事"-->
<!--                       src="../../../static/img/committee/100x100/jiyi.jpg" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">理事</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">纪毅</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">广东工业大学</p>-->
<!--              </div>-->
<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="理事"-->
<!--                       src="../../../static/img/committee/100x100/avatar.png" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">理事</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">黄大源</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">加拿大华为</p>-->
<!--              </div>-->
<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="理事"-->
<!--                       src="../../../static/img/committee/100x100/chen.png" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">理事</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">王晨</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">日本高知工科大</p>-->
<!--              </div>-->

<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->

<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="扩大理事"-->
<!--                       src="../../../static/img/committee/100x100/avatar.png" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">扩大理事</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">赵盛东</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">新加坡国立大学</p>-->
<!--              </div>-->
<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->

<!--        &lt;!&ndash;        五.秘书处   : 1. 秘书长         2. 副秘书长      3.其它&ndash;&gt;-->
<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="扩大理事"-->
<!--                       src="../../../static/img/committee/100x100/avatar.png" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">扩大理事</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">郭诗辉</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">厦门大学</p>-->
<!--              </div>-->

<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--        </div>-->
<!--        <div class="row mx-n2 mb-2" style="display: flex;justify-content: center;align-items: center">-->

<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="扩大理事"-->
<!--                       src="../../../static/img/committee/100x100/gaoboyu.jpg" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">扩大理事</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">高博宇</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">暨南大学</p>-->
<!--              </div>-->

<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="扩大理事"-->
<!--                       src="../../../static/img/committee/100x100/avatar.png" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">扩大理事</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">陈玉</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">圣荷西州立大学</p>-->
<!--              </div>-->

<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="扩大理事"-->
<!--                       src="../../../static/img/committee/100x100/canliu.jpg" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">扩大理事</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">刘灿</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">香港城市大学</p>-->
<!--              </div>-->

<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="扩大理事"-->
<!--                       src="../../../static/img/committee/100x100/avatar.png" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">扩大理事</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">余盈盈</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">厦门大学</p>-->
<!--              </div>-->
<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--        <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="扩大理事"-->
<!--                       src="../../../static/img/committee/100x100/avatar.png" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">扩大理事</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">朱滨</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">瑞典皇家理工学院</p>-->
<!--              </div>-->
<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="扩大理事"-->
<!--                       src="../../../static/img/committee/100x100/avatar.png" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">扩大理事</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">夏晴</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">清华大学</p>-->
<!--              </div>-->
<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--        </div>-->

<!--        <div class="row mx-n2 mb-2" style="display: flex;justify-content: center;align-items: center">-->
<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="扩大理事"-->
<!--                       src="../../../static/img/committee/100x100/avatar.png" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">扩大理事</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">毕涛</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">英国伦敦大学学院</p>-->
<!--              </div>-->
<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="联络办公室"-->
<!--                       src="../../../static/img/committee/100x100/avatar.png" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">联络办公室</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">朱琳</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">清华大学</p>-->
<!--              </div>-->
<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="联络办公室"-->
<!--                       src="../../../static/img/committee/100x100/yuxin.jpeg" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">联络办公室</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">徐雨欣</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">加拿大滑铁卢大学</p>-->
<!--              </div>-->
<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->
<!--          <div class="col-sm-2">-->
<!--            &lt;!&ndash; Team &ndash;&gt;-->
<!--            <div class="card w-100 h-95 transition-3d-hover">-->
<!--              <div class="card-body">-->
<!--                <div class="  avatar-circle mb-4" style="margin-left: 0.7rem">-->
<!--                  <img class="avatar-img"-->
<!--                       data-container="body" data-toggle="popover" data-placement="top"-->
<!--                       data-content="内容Content" data-trigger="hover focus"-->
<!--                       title="联络办公室"-->
<!--                       src="../../../static/img/committee/100x100/maizijun.jpg" alt="Image Description" >-->
<!--                </div>-->

<!--                <span class="d-block small font-weight-bold text-cap mb-1" style="text-align: center">联络办公室</span>-->
<!--                <a href="https://www.cse.ust.hk/~mxj/">-->
<!--                  <h4 class="text-lh-sm" style="text-align: center">麦紫君</h4>-->
<!--                </a>-->
<!--                <p class="font-size-1" style="text-align: center">暨南大学</p>-->
<!--              </div>-->
<!--            </div>-->
<!--            &lt;!&ndash; End Team &ndash;&gt;-->
<!--          </div>-->


<!--        </div>-->

<!--        &lt;!&ndash;        北京/米兰办公室&ndash;&gt;-->

<!--        &lt;!&ndash;        多伦多办公室&ndash;&gt;-->

<!--        &lt;!&ndash;        广州办公室&ndash;&gt;-->

<!--        &lt;!&ndash;        六.青年委员会&ndash;&gt;-->

<!--        &lt;!&ndash;        七.监事&ndash;&gt;-->



<!--        &lt;!&ndash;        八.Chinese CHI Steering committee&ndash;&gt;-->
<!--&lt;!&ndash;        组织架构文字说明部分&ndash;&gt;-->
<!--      </div>-->
<!--      Team Section end-->

      <div class="container space-lg-1 space-2">
                <div class="w-md-80 w-lg-60 text-center mx-md-auto mb-5 mb-md-6" style="align-items: center">
                  <h2 style="display: inline-block;margin: 0 auto">{{ $t('aboutus.ourteam') }}</h2>
                </div>
        <div class="row">
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
          <div class="avatar avatar-circle">
            <img class="avatar-img" src="../../../static/img/committee/100x100/FuZhiyong.jpg" alt="">
          </div>
          <div class="ml-3">
            <h4 class="mb-0" style="display: inline-block">付志勇</h4>
            <small class="text-muted">清华大学</small>
            <small class="text-muted" style="display: block">协会会长</small>
          </div>
        </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
          <div class="avatar avatar-circle">
            <img class="avatar-img" src="../../../static/img/committee/100x100/xiaojuan.png" alt="">
          </div>
          <div class="ml-3">
            <h4 class="mb-0" style="display: inline-block">麻晓娟</h4>
            <small class="text-muted">香港科技大学</small>
            <small class="text-muted" style="display: block">协会副会长</small>
          </div>
        </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/shuminzhai.png" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">翟树民</h4>
              <small class="text-muted">美国谷歌</small>
              <small class="text-muted" style="display: block">顾问/咨询委员会</small>
            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/ren.jpg" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">任向实</h4>
              <small class="text-muted">日本高知工科大学</small>
              <small class="text-muted" style="display: block">顾问/咨询委员会</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/avatar.png" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">李维</h4>
              <small class="text-muted">加拿大华为</small>
              <small class="text-muted" style="display: block">顾问/咨询委员会</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/avatar.png" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">张虹</h4>
              <small class="text-muted">美国普渡大学</small>
              <small class="text-muted" style="display: block">顾问/咨询委员会</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/tuhuawei.jpeg" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">涂华伟</h4>
              <small class="text-muted">澳洲乐卓博大学</small>
              <small class="text-muted" style="display: block">战略发展专委会</small>
              <small class="text-muted" style="display: block">秘书处秘书长</small>


            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/jianzhao.jpg" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">赵健</h4>
              <small class="text-muted">加拿大滑铁卢大学</small>
              <small class="text-muted" style="display: block">学术活动专委会</small>
              <small class="text-muted" style="display: block">秘书处副秘书长</small>



            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/avatar.png" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">姚俊峰</h4>
              <small class="text-muted">厦门大学</small>
              <small class="text-muted" style="display: block">战略发展专委会</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/yuan.png" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">袁晓君</h4>
              <small class="text-muted">纽约州立大学奥尔巴尼分校</small>
              <small class="text-muted" style="display: block">学术期刊+教材专委会</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/avatar.png" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">王建民</h4>
              <small class="text-muted">同济大学</small>
              <small class="text-muted" style="display: block">学术期刊+教材专委会</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/junhu.jpg" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">胡军</h4>
              <small class="text-muted">埃因霍温理工大学</small>
              <small class="text-muted" style="display: block">学术期刊+教材专委会</small>
              <small class="text-muted" style="display: block">战略发展专委会</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/liuwei.jpg" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">刘伟</h4>
              <small class="text-muted">北京师范大学</small>
              <small class="text-muted" style="display: block">学术期刊+教材专委会</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/avatar.png" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">王大阔</h4>
              <small class="text-muted">美国IBM研究院</small>
              <small class="text-muted" style="display: block">学术活动专委会</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/avatar.png" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">孙华彤</h4>
              <small class="text-muted">美国华盛顿大学</small>
              <small class="text-muted" style="display: block">学术活动专委会</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/avatar.png" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">米海鹏</h4>
              <small class="text-muted">清华大学</small>
              <small class="text-muted" style="display: block">专题会议专委会</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/avatar.png" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">喻纯</h4>
              <small class="text-muted">清华大学</small>
              <small class="text-muted" style="display: block">专题会议专委会</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/guihuanfeng.jpeg" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">冯桂焕</h4>
              <small class="text-muted">南京大学</small>
              <small class="text-muted" style="display: block">学术活动专委会</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/avatar.png" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">杨兴栋</h4>
              <small class="text-muted">美国达特茅斯学院</small>
              <small class="text-muted" style="display: block">专题会议专委会</small>
              <small class="text-muted" style="display: block">战略发展专委会</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/jiyi.jpg" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">纪毅</h4>
              <small class="text-muted">广东工业大学</small>
              <small class="text-muted" style="display: block">专题会议专委会</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/avatar.png" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">黄大源</h4>
              <small class="text-muted">加拿大华为</small>
              <small class="text-muted" style="display: block">学术活动专委会</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/chen.png" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">王晨</h4>
              <small class="text-muted">日本高知工科大</small>
              <small class="text-muted" style="display: block">青年委员会</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/avatar.png" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">赵盛东</h4>
              <small class="text-muted">新加坡国立大学</small>
              <small class="text-muted" style="display: block">监事</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/avatar.png" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">郭诗辉</h4>
              <small class="text-muted">厦门大学</small>
              <small class="text-muted" style="display: block">秘书处</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/gaoboyu.jpg" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">高博宇</h4>
              <small class="text-muted">暨南大学</small>
              <small class="text-muted" style="display: block">秘书处</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/avatar.png" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">陈玉</h4>
              <small class="text-muted">圣荷西州立大学</small>
              <small class="text-muted" style="display: block">秘书处</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/canliu.jpg" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">刘灿</h4>
              <small class="text-muted">香港城市大学</small>
              <small class="text-muted" style="display: block">秘书处</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/avatar.png" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">佘莹莹</h4>
              <small class="text-muted">厦门大学</small>
              <small class="text-muted" style="display: block">监事</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/avatar.png" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">朱滨</h4>
              <small class="text-muted">瑞典皇家理工学院</small>
              <small class="text-muted" style="display: block">监事</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/avatar.png" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">夏晴</h4>
              <small class="text-muted">清华大学</small>
              <small class="text-muted" style="display: block">青年委员会</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/avatar.png" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">毕涛</h4>
              <small class="text-muted">英国伦敦大学学院</small>
              <small class="text-muted" style="display: block">青年委员会</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/avatar.png" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">朱琳</h4>
              <small class="text-muted">清华大学</small>
              <small class="text-muted" style="display: block">北京/米兰办公室-秘书处</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/yuxin.jpeg" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">徐雨欣</h4>
              <small class="text-muted">加拿大滑铁卢大学</small>
              <small class="text-muted" style="display: block">多伦多办公室-秘书处</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/maizijun.jpg" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block">麦紫君</h4>
              <small class="text-muted">暨南大学</small>
              <small class="text-muted" style="display: block">广州办公室-秘书处</small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/avatar.png" style="opacity: 0.0" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block"></h4>
              <small class="text-muted"></small>
              <small class="text-muted" style="display: block"></small>

            </div>
          </div>
          <div class="d-flex  align-items-center w-lg-25 mx-auto" style="justify-content: left;margin-top: 1rem;margin-bottom: 2rem">
            <div class="avatar avatar-circle">
              <img class="avatar-img" src="../../../static/img/committee/100x100/avatar.png" style="opacity: 0.0" alt="">
            </div>
            <div class="ml-3">
              <h4 class="mb-0" style="display: inline-block"></h4>
              <small class="text-muted"></small>
              <small class="text-muted" style="display: block"></small>

            </div>
          </div>



        </div>
      </div>
<!--      组织架构介绍-->
<!--      <div class="container space-2 space-lg-1" style="align-items: center;overflow: hidden">-->
<!--        <div id='module2022'   _modulestyle='86' _moduleid='2022'  class='form form2022 formStyle86 siteEditor '     style='float: left; ' _side='0' >-->
<!--          <div class='lightModuleOuterContent lightModuleOuterContent2022'><div class='fk-editor simpleText fk-editor-break-word  '><p style=""><span style=";"></span></p><span style="font-size: 16px;"><p style=""><span style=";"></span></p><span style="color: rgb(99, 99, 99); line-height: 14px; display: inline-block;"><p style=""><span style=";"></span></p></span></span><span style="font-size: 16px; color: rgb(108, 108, 108); line-height: 32px; display: inline-block; font-family: 微软雅黑, &quot;Microsoft YaHei&quot;;"><p style="">1. <b><span style=";">协会会长：</span></b></p><p><span style=";">付志勇</span><span style=";"> （清华大学）</span></p><p><span style=";"> </span></p><p style=""><span style=";">2. </span><b><span style=";">协会副会长：</span></b><span style=";"></span></p><p><span style=";">麻晓娟</span><span style=";">（</span><span style=";">香港科技大学</span><span style=";">）</span></p><p><span style=";"> </span></p><p style=""><span style=";">3. </span><b><span style=";">顾问/咨询委员会</span></b><span style=";">：</span></p><p><span style=";">翟树民（美国谷歌）</span></p><p><span style=";">任向实</span><span style=";">（日本高知工科大学）</span></p><p><span style=";">李维（加拿大华为）</span></p><p><span style=";">张虹（美国普渡大学）</span></p><p><span style=";"> </span></p><p style=""><span style=";">4. </span><b><span style=";">专委会</span></b><b><span style=";">：</span></b><b><span style=";"></span></b></p><p style=""><span style=";">（1） </span><b><span style=";">学术期刊</span></b><b><span style=";">+教材</span></b><b><span style=";"></span></b></p><p style=""><span style=";">袁晓君（纽约州立大学奥尔巴尼分校）</span></p><p style=""><span style=";">王建民（同济大学）</span></p><p style=""><span style=";">胡军</span>（埃因霍温理工大学）</p><p style=""><span style=";">刘伟（北京师范大学）</span></p><p><span style=";"> </span></p><p style=""><span style=";">（2） </span><b><span style=";">学术活动</span></b><b><span style=";"></span></b></p><p style=""><span style=";">王大阔</span><span style=";"> （美国I</span><span style=";">BM研究院</span><span style=";">）</span></p><p style=""><span style=";">赵健（</span>加拿大滑铁卢大学<span style=";">）</span></p><p style=""><span style=";">冯桂焕（南京大学）</span></p><p style=""><span style=";">黄大源（加拿大华为）</span></p><p style=""><span style=";">孙华彤（美国华盛顿大学塔科马校区）</span></p><p><span style=";"> </span></p><p style=""><span style=";">（3） </span><b><span style=";">专题会议</span></b><b><span style=";"></span></b></p><p style=""><span style=";">米海鹏</span><span style=";">（清华大学）</span></p><p style=""><span style=";">喻纯（清华大学）</span></p><p style=""><span style=";">杨兴栋</span>（美国达特茅斯学院）</p><p style=""><span style=";">纪毅（广东工业大学）</span></p><p><span style=";"> </span></p><p style=""><span style=";">（4） </span><b><span style=";">战</span></b><b><span style=";">略</span></b><b><span style=";">发展</span></b><b></b></p><p style="">杨兴栋（美国达特茅斯学院）</p><p style="">姚俊峰（厦门大学）</p><p style="">胡军（埃因霍温理工大学）</p><p style="">赵盛东（新加坡国立大学）</p><p style="">涂华伟（澳洲乐卓博大学）</p><p style=""><span style=";"></span></p><p style=""><span style=";"></span></p><p><br></p></span></div></div>-->
<!--        </div>-->
<!--        <div id='module3398'   _modulestyle='86' _moduleid='3398'  class='form form3398 formStyle86 siteEditor '     style='float: right;' _side='0' >-->
<!--          <div class='lightModuleOuterContent lightModuleOuterContent3398'><div class='fk-editor simpleText fk-editor-break-word  '><p style=""></p><span style="font-size: 16px;"><p style=""></p><span style="color: rgb(99, 99, 99); line-height: 14px;"><p style=""></p></span></span><span style="font-size: 16px; color: rgb(108, 108, 108); line-height: 32px; font-family: 微软雅黑, &quot;microsoft yahei&quot;;"><p style=""><span style="background-color: transparent;">5. </span><b style="background-color: transparent;">秘书处</b><b style="background-color: transparent;">：</b><br></p><p style=""><b>秘书长：</b>涂华伟（澳洲乐卓博大学）</p><p style=""><b>副秘书长：</b>赵健（加拿大滑铁卢大学）</p><p style="">郭诗辉 （厦门大学）</p><p style="">高博宇 （暨南大学）</p><p style="">陈玉 （美国圣荷西州立大学）</p><p style="">刘灿（香港城市大学）</p><p style=""> </p><p style=""><b>北京/米兰办公室：</b>朱琳（清华大学）</p><p style=""><b>多伦多办公室：</b>徐雨欣（加拿大滑铁卢大学）</p><p style=""><b>广州办公室：</b>麦紫君（暨南大学）</p><p style=""> </p><p style="">6. <b>青年委员会：</b></p><p style="">王晨（日本高知工科大）</p><p style="">夏晴（清华大学） </p><p style="">毕涛（英国伦敦大学学院）</p><p style=""> </p><p style="">7. <b>监事</b><b>：</b><b></b></p><p style="">赵盛东（新加坡国立大学） </p><p style="">佘莹莹（厦门大学）</p><p style="">朱滨（瑞典皇家理工学院）</p><p style=""><br></p><p style=""></p><p style=""></p><p> </p><p style="">8. <b>Chinese CHI </b><b>Steering</b><b> </b><b>committee</b><b> </b><b></b></p><p style="">• 2020：Xiangmin Fan, Junfeng Yao; Huawei Tu, Teng Han</p><p style="">• 2019：Junfeng Yao; Xingdong Yang, Da-Yuan Huang</p><p style="">• 2018：Zhiyong Fu; Jun Hu; Haipeng Mi, Xing-Dong Yang</p><p style="">• 2017：Yingqing XU; Yi Ji; Xiang-Dong Yang; Xiaojuan Ma</p><p style="">• 2016：Xiaojun Bi, Lu xiao; Feng Tian; Xianghua(Sharon) Ding</p><p style="">• 2015：Hao-Chuan Wang, Gary Hsieh; Xiaojun Bi, Henry Been-Lim duh, Yihsiu Chen</p><p style="">• 2014：Ellen Yi-Luen Do; Wei Li; Shengdong (Shen) Zhao; Hao-Chuan Wang</p><p style="">• 2013：Xiangshi Ren; Henry Been-Lim duh; Hong Tan</p></span></div></div>-->
<!--        </div>-->
<!--      </div>-->
<!--      组织架构结束-->
      <div class="container"><div class="w-lg-65 mx-lg-auto"><hr class="my-0"></div></div>      <div class="container space-lg-1 space-2">
        <div class="w-md-80 w-lg-60 text-center mx-md-auto mb-5 mb-md-6" style="align-items: center">
          <h2 style="display: inline-block;margin: 0 auto">Chinese CHI Steeringcommittee</h2>
          </div>
        <div>
          <ul class="list-article">
            <li>2020：Xiangmin Fan, Junfeng Yao; Huawei Tu, Teng Han</li>
            <li>2019：Junfeng Yao; Xingdong Yang, Da-Yuan Huang</li>
            <li>2018：Zhiyong Fu; Jun Hu; Haipeng Mi, Xing-Dong Yang</li>
            <li>2017：Yingqing XU; Yi Ji; Xiang-Dong Yang; Xiaojuan Ma</li>
            <li>2016：Xiaojun Bi, Lu xiao; Feng Tian; Xianghua(Sharon) Ding</li>
            <li>2015：Hao-Chuan Wang, Gary Hsieh; Xiaojun Bi, Henry Been-Lim duh, Yihsiu Chen</li>
            <li>2014：Ellen Yi-Luen Do; Wei Li; Shengdong (Shen) Zhao; Hao-Chuan Wang</li>
            <li>2013：Xiangshi Ren; Henry Been-Lim duh; Hong Tan</li>
          </ul>
        </div>
      </div>
<!--      <div class="container mb-4" style="overflow: hidden">-->
<!--          <a class="link-underline" href="javascript:;"-->
<!--             data-toggle="modal"-->
<!--             data-target="#aboutUs_content"><button type="button" class="btn btn-secondary btn-sm" style="float: right">{{ $t('home.LearnMore') }}</button>-->
<!--          </a>-->
<!--      </div>-->
      <div
        class="modal fade"
        id="aboutUs_content"
        tabindex="-1"
        role="dialog"
        aria-hidden="true"

      >
        <div class="modal-dialog modal-dialog-centered" role="document" style="max-width: 1200px">
          <div class="modal-content" style="max-width: 1200px">
            <!-- Header -->
            <div class="modal-close">
              <button
                type="button"
                class="btn btn-icon btn-sm btn-ghost-secondary"
                data-dismiss="modal"
                aria-label="Close"
              >
                <svg
                  width="10"
                  height="10"
                  viewBox="0 0 18 18"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    fill="currentColor"
                    d="M11.5,9.5l5-5c0.2-0.2,0.2-0.6-0.1-0.9l-1-1c-0.3-0.3-0.7-0.3-0.9-0.1l-5,5l-5-5C4.3,2.3,3.9,2.4,3.6,2.6l-1,1 C2.4,3.9,2.3,4.3,2.5,4.5l5,5l-5,5c-0.2,0.2-0.2,0.6,0.1,0.9l1,1c0.3,0.3,0.7,0.3,0.9,0.1l5-5l5,5c0.2,0.2,0.6,0.2,0.9-0.1l1-1 c0.3-0.3,0.3-0.7,0.1-0.9L11.5,9.5z"
                  />
                </svg>
              </button>
            </div>
            <!-- End Header -->

            <!-- 关于我们-->
            <!-- Body -->
            <div class="modal-body p-sm-5">
              <form class="js-validate">
                <!-- Sign in -->
                <div id="signinModalForm">
                  <div class=" mb-5">
                    <h2 style="text-align: center">{{$t('aboutus.AboutUs')}}</h2>
                    <div class="container space-2 space-lg-1" style="overflow: hidden;align-items: center">
                      <div    _modulestyle='86' _moduleid='2022'  class='form form2022 formStyle86 siteEditor '     style='float:left;margin-left: 50px ' _side='0' >
                        <div class='lightModuleOuterContent lightModuleOuterContent2022'><div class='fk-editor simpleText fk-editor-break-word  '><p style=""><span style=";"></span></p><span style="font-size: 16px;"><p style=""><span style=";"></span></p><span style="color: rgb(99, 99, 99); line-height: 14px; display: inline-block;"><p style=""><span style=";"></span></p></span></span><span style="font-size: 16px; color: rgb(108, 108, 108); line-height: 32px; display: inline-block; font-family: 微软雅黑, &quot;Microsoft YaHei&quot;;"><p style="">1. <b><span style=";">协会会长：</span></b></p><p><span style=";">付志勇</span><span style=";"> （清华大学）</span></p><p><span style=";"> </span></p><p style=""><span style=";">2. </span><b><span style=";">协会副会长：</span></b><span style=";"></span></p><p><span style=";">麻晓娟</span><span style=";">（</span><span style=";">香港科技大学</span><span style=";">）</span></p><p><span style=";"> </span></p><p style=""><span style=";">3. </span><b><span style=";">顾问/咨询委员会</span></b><span style=";">：</span></p><p><span style=";">翟树民（美国谷歌）</span></p><p><span style=";">任向实</span><span style=";">（日本高知工科大学）</span></p><p><span style=";">李维（加拿大华为）</span></p><p><span style=";">张虹（美国普渡大学）</span></p><p><span style=";"> </span></p><p style=""><span style=";">4. </span><b><span style=";">专委会</span></b><b><span style=";">：</span></b><b><span style=";"></span></b></p><p style=""><span style=";">（1） </span><b><span style=";">学术期刊</span></b><b><span style=";">+教材</span></b><b><span style=";"></span></b></p><p style=""><span style=";">袁晓君（纽约州立大学奥尔巴尼分校）</span></p><p style=""><span style=";">王建民（同济大学）</span></p><p style=""><span style=";">胡军</span>（埃因霍温理工大学）</p><p style=""><span style=";">刘伟（北京师范大学）</span></p><p><span style=";"> </span></p><p style=""><span style=";">（2） </span><b><span style=";">学术活动</span></b><b><span style=";"></span></b></p><p style=""><span style=";">王大阔</span><span style=";"> （美国I</span><span style=";">BM研究院</span><span style=";">）</span></p><p style=""><span style=";">赵健（</span>加拿大滑铁卢大学<span style=";">）</span></p><p style=""><span style=";">冯桂焕（南京大学）</span></p><p style=""><span style=";">黄大源（加拿大华为）</span></p><p style=""><span style=";">孙华彤（美国华盛顿大学塔科马校区）</span></p><p><span style=";"> </span></p><p style=""><span style=";">（3） </span><b><span style=";">专题会议</span></b><b><span style=";"></span></b></p><p style=""><span style=";">米海鹏</span><span style=";">（清华大学）</span></p><p style=""><span style=";">喻纯（清华大学）</span></p><p style=""><span style=";">杨兴栋</span>（美国达特茅斯学院）</p><p style=""><span style=";">纪毅（广东工业大学）</span></p><p><span style=";"> </span></p><p style=""><span style=";">（4） </span><b><span style=";">战</span></b><b><span style=";">略</span></b><b><span style=";">发展</span></b><b></b></p><p style="">杨兴栋（美国达特茅斯学院）</p><p style="">姚俊峰（厦门大学）</p><p style="">胡军（埃因霍温理工大学）</p><p style="">赵盛东（新加坡国立大学）</p><p style="">涂华伟（澳洲乐卓博大学）</p><p style=""><span style=";"></span></p><p style=""><span style=";"></span></p><p><br></p></span></div></div>
                      </div>
                      <div    _modulestyle='86' _moduleid='3398'  class='form form3398 formStyle86 siteEditor '     style='float: right;margin: 0 auto; ' _side='0' >
                        <div class='lightModuleOuterContent lightModuleOuterContent3398'><div class='fk-editor simpleText fk-editor-break-word  '><p style=""></p><span style="font-size: 16px;"><p style=""></p><span style="color: rgb(99, 99, 99); line-height: 14px;"><p style=""></p></span></span><span style="font-size: 16px; color: rgb(108, 108, 108); line-height: 32px; font-family: 微软雅黑, &quot;microsoft yahei&quot;;"><p style=""><span style="background-color: transparent;">5. </span><b style="background-color: transparent;">秘书处</b><b style="background-color: transparent;">：</b><br></p><p style=""><b>秘书长：</b>涂华伟（澳洲乐卓博大学）</p><p style=""><b>副秘书长：</b>赵健（加拿大滑铁卢大学）</p><p style="">郭诗辉 （厦门大学）</p><p style="">高博宇 （暨南大学）</p><p style="">陈玉 （美国圣荷西州立大学）</p><p style="">刘灿（香港城市大学）</p><p style=""> </p><p style=""><b>北京/米兰办公室：</b>朱琳（清华大学）</p><p style=""><b>多伦多办公室：</b>徐雨欣（加拿大滑铁卢大学）</p><p style=""><b>广州办公室：</b>麦紫君（暨南大学）</p><p style=""> </p><p style="">6. <b>青年委员会：</b></p><p style="">王晨（日本高知工科大）</p><p style="">夏晴（清华大学） </p><p style="">毕涛（英国伦敦大学学院）</p><p style=""> </p><p style="">7. <b>监事</b><b>：</b><b></b></p><p style="">赵盛东（新加坡国立大学） </p><p style="">佘莹莹（厦门大学）</p><p style="">朱滨（瑞典皇家理工学院）</p><p style=""><br></p><p style=""></p><p style=""></p><p> </p><p style="">8. <b>Chinese CHI </b><b>Steering</b><b> </b><b>committee</b><b> </b><b></b></p><p style="">• 2020：Xiangmin Fan, Junfeng Yao; Huawei Tu, Teng Han</p><p style="">• 2019：Junfeng Yao; Xingdong Yang, Da-Yuan Huang</p><p style="">• 2018：Zhiyong Fu; Jun Hu; Haipeng Mi, Xing-Dong Yang</p><p style="">• 2017：Yingqing XU; Yi Ji; Xiang-Dong Yang; Xiaojuan Ma</p><p style="">• 2016：Xiaojun Bi, Lu xiao; Feng Tian; Xianghua(Sharon) Ding</p><p style="">• 2015：Hao-Chuan Wang, Gary Hsieh; Xiaojun Bi, Henry Been-Lim duh, Yihsiu Chen</p><p style="">• 2014：Ellen Yi-Luen Do; Wei Li; Shengdong (Shen) Zhao; Hao-Chuan Wang</p><p style="">• 2013：Xiangshi Ren; Henry Been-Lim duh; Hong Tan</p></span></div></div>
                      </div>
                    </div>
                  </div>

                </div>
                <!-- End Sign in -->
              </form>
            </div>
            <!-- End Body -->
          </div>
        </div>
      </div>

      <!-- End Team Section -->
    </main>
    <!-- ========== END MAIN ========== -->
  </div>
</template>
<style>
#modal_2 {
  display: none;
}
.modal_2 {
  margin: auto;
  padding-top: 5%;
  width: 50%;
  height: 80%;
  z-index: 1;
}
.modal_2 img {
  animation-name: zoom;
  animation-duration: 0.6s;
  display: block;
  padding: 10px;
  margin: auto;
  max-width: 100%;
  max-height: 100%;
  box-shadow: 0 2px 6px rgb(0, 0, 0, 0.2), 0 10px 20px rgb(0, 0, 0, 0.2);
  border-radius: 12px;
  border: 1px solid white;
}
@keyframes zoom {
  from {transform: scale(0.1)}
  to {transform: scale(1)}
}

</style>

<script>
export default {
  data () {
    return {
      heroTitle: 'aboutus.AboutUs',
      heroSubTitle: 'aboutus.InternationalChineseAssociationOfComputerHumanInteraction',
      content1: '',
      content2: '',
      img1:'',
      img2:'',
      img3:'',
      img4:'',
      img5:'',
      img6:'',
      Detail1:'',
      Detail2:'',
      Detail3:'',
      Detail4:'',
      img7:'',
      aboutUs:'aboutUs_modal',
      modal_content:'',
    }

  },

  created(){
    this.getUS();

  },

  methods:{
    getUS () {
      //console.log(this.MainNewsTitle)
      this.$axios.get('/public/about/active')
        .then(res => {
          console.log(res.data.data)
          var data = res.data.data
          this.content1 = data.introductionTop
          this.content2 = data.introductionBottom
          this.img1 = data.photo1
          this.img2 = data.photo2
          this.img3 = data.photo3
          this.img4 = data.photo4
          this.img5 = data.photo5
          this.img6 = data.photo6
          this.Detail1 = data.detail1
          this.Detail2 = data.detail2
          this.Detail3 = data.detail3
          this.Detail4 = data.detail4
          this.img7 = data.photoBottom

        })
        .catch(err => {
          console.error(err)
        })
    },
    showBgImg(target){
      var modal_2 = document.getElementById('modal_2');
      var bgImg = document.getElementById('bgImg');
      modal_2.style.display = 'block';
      bgImg.src=target;
    },
    notshow(){
      var modal_2 = document.getElementById('modal_2');
      modal_2.style.display = 'none'
    }

  },

  mounted () {
    $(function (){
      $("[data-toggle='popover']").popover();
    });
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


