<template>
  <div>
    <!-- ========== FOOTER ========== -->
    <div style="height: 90px;background-color:white;"></div>
    <footer class="bg-dark">
      <div class="container">
        <div class="space-top-1 space-bottom-1 space-bottom-lg-1">
          <h3 class="text-white">{{ $t("contacts.Contacts") }}</h3>
          <hr class="opacity-xs my-0 space-bottom-1 space-bottom-lg-1">
          <div class="row justify-content-lg-between">
            <div class="col-lg-4  mb-5 mb-lg-0">

              <!-- Nav Link -->
              <ul class="nav nav-sm nav-x-0 nav-white flex-column">
                <li class="nav-item">
                  <a class="nav-link media" href="javascript:;">
                    <span class="media">
                      <span class="fas fa-user-circle mt-1 mr-2"></span>
                      <span class="media-body" style="letter-spacing: 1px">
                        {{$t('home.foot1')}} : Prof. Zhiyong Fu
                      </span>
                    </span>
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link media" href="javascript:;">
                    <span class="media">
                      <span class="fas fa-location-arrow mt-1 mr-2"></span>
                      <span class="media-body" style="width: 360px;letter-spacing: 1px">
                        {{ $t('home.foot2') }} : 849 Laurelwood Dr, Waterloo, ON, Canada
                      </span>
                    </span>
                  </a>
                </li>
<!--                传真-->
<!--                <li class="nav-item">-->
<!--                  <a class="nav-link media " href="tel:+852 2766-7279">-->
<!--                    <span class="media">-->
<!--                      <span class="fas fa-phone-alt mt-1 mr-2"></span>-->
<!--                      <span class="media-body">{{ $t('home.foot3') }} : +852 2766-7279, +81-887-57-2209</span>-->
<!--                    </span>-->
<!--                  </a>-->
<!--                </li>-->
<!--                电话-->
<!--                <li class="nav-item">-->
<!--                  <a class="nav-link media" href="tel:+81-887-57-2209">-->
<!--                    <span class="media">-->
<!--                      <span class="fas fa-fax mt-1 mr-2"></span>-->
<!--                      <span class="media-body">{{ $t('home.foot4') }} : +852 2774-0842, +81-887-57-2209</span>-->
<!--                    </span>-->
<!--                  </a>-->
<!--                </li>-->
              </ul>
              <!-- End Nav Link -->
            </div>
            <div class="col-lg-3 ml-lg-auto mb-5 mb-lg-0">
              <!-- Nav Link -->
              <ul class="nav nav-sm nav-x-0 nav-white flex-column">
                <li class="nav-item">
                  <a class="nav-link media" href="javascript:;">
                    <span class="media">
                      <span class="fas fa-home mt-1 mr-2"></span>
                      <span class="media-body" style="letter-spacing: 1px">
                        {{$t('home.foot5')}} : www.icachi.org
                      </span>
                    </span>
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link media" href="javascript:;">
                    <span class="media">
                      <span class="fas fa-envelope mt-1 mr-2"></span>
                      <span class="media-body" style="letter-spacing: 1px">
                        {{ $t('home.foot6') }} : office@icachi.org
                      </span>
                    </span>
                  </a>
                </li>
<!--                理事会成员ML-->
<!--                <li class="nav-item">-->
<!--                  <a class="nav-link media" href="tel:+852 2766-7279">-->
<!--                    <span class="media">-->
<!--                      <span class="fas fa-envelope mt-1 mr-2"></span>-->
<!--                      <span class="media-body">{{ $t('home.foot7') }} : board@icachi.org</span>-->
<!--                    </span>-->
<!--                  </a>-->
<!--                </li>-->
<!--                全体成员ML-->
<!--                <li class="nav-item">-->
<!--                  <a class="nav-link media" href="tel:+81-887-57-2209">-->
<!--                    <span class="media">-->
<!--                      <span class="fas fa-envelope mt-1 mr-2"></span>-->
<!--                      <span class="media-body">{{ $t('home.foot8') }} : members@icachi.org</span>-->
<!--                    </span>-->
<!--                  </a>-->
<!--                </li>-->
              </ul>
              <!-- End Nav Link -->




            </div>
            <div class="col-lg-3 ml-lg-auto mb-5 mb-lg-0">
              <!-- Leaflet -->
              <!--              地图模块-->
              <!--          <div id="map" class="min-h-240rem"-->
              <!--               data-hs-leaflet-options='{-->
              <!--                 "map": {-->
              <!--                   "scrollWheelZoom": false,-->
              <!--                   "coords": [37.4040344, -122.0289704]-->
              <!--                 },-->
              <!--                 "marker": [-->
              <!--                   {-->
              <!--                     "coords": [37.4040344, -122.0289704],-->
              <!--                     "icon": {-->
              <!--                       "iconUrl": "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fpic.51yuansu.com%2Fpic3%2Fcover%2F03%2F31%2F18%2F5b80d2672779c_610.jpg&refer=http%3A%2F%2Fpic.51yuansu.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1645034744&t=ebe9ad94cafe0b4958e2f6b78552cb12",-->
              <!--                       "iconSize": [50, 50]-->
              <!--                     },-->
              <!--                     "popup": {-->
              <!--                       "text": "153 Williamson Plaza, Maggieberg"-->
              <!--                     }-->
              <!--                   }-->
              <!--                 ]-->
              <!--                }'></div>-->
              <!--              二维码模块-->

              <img src="../../assets/img/QR_code/qrcode_ICACHI_1.jpg" width="100" style="position: absolute;right: 20px;top: -10px">
              <!-- End Leaflet -->
            </div>
          </div>
        </div>

<!--        <hr class="opacity-xs my-0" />-->

        <div class="space-1">
          <div class="row align-items-md-center mb-7" style="align-items: center">
            <div class="col-md-6 mb-4 mb-md-0">
              <!-- Logo -->
              <div class="">
                <a href="/" aria-label="Front" class="mr-4">
                  <img
                    src="../../assets/svg/logos/icachi-white-logo.svg"
                    alt="Logo"
                    style="width: 120px"
                  />
                </a>
                <a href="/" aria-label="Front">
                  <img
                    src="../../assets/svg/logos/icachi-white-text.svg"
                    alt="Logo"
                    style="width: 15rem"
                  />
                </a>
              </div>
              <!-- End Logo -->
            </div>
            <!--社交媒体部分-->
            <!--            <div class="col-md-6 text-md-right">-->
            <!--              <ul class="list-inline mb-0">-->
            <!--                &lt;!&ndash; Social Networks &ndash;&gt;-->
            <!--                <li class="list-inline-item">-->
            <!--                  <a class="btn btn-xs btn-icon btn-soft-light" href="#">-->
            <!--                    <i class="fab fa-facebook-f"></i>-->
            <!--                  </a>-->
            <!--                </li>-->
            <!--                <li class="list-inline-item">-->
            <!--                  <a class="btn btn-xs btn-icon btn-soft-light" href="#">-->
            <!--                    <i class="fab fa-google"></i>-->
            <!--                  </a>-->
            <!--                </li>-->
            <!--                <li class="list-inline-item">-->
            <!--                  <a class="btn btn-xs btn-icon btn-soft-light" href="#">-->
            <!--                    <i class="fab fa-twitter"></i>-->
            <!--                  </a>-->
            <!--                </li>-->
            <!--                <li class="list-inline-item">-->
            <!--                  <a class="btn btn-xs btn-icon btn-soft-light" href="#">-->
            <!--                    <i class="fab fa-weixin"></i>-->
            <!--                  </a>-->
            <!--                </li>-->
            <!--                &lt;!&ndash; End Social Networks &ndash;&gt;-->
            <!--              </ul>-->
            <!--            </div>-->
          </div>

          <!-- Copyright -->
          <div class="w-md-75 text-lg-center mx-lg-auto">
            <p class="text-white opacity-sm small">
              &copy; {{ $t("home.CopyRight") }}
            </p>

            <p class="text-white small">
              <!-- Nav Link -->
              <!-- <ul class="nav nav-sm nav-white nav-x-sm align-items-center">
                <li class="nav-item">
                  <a class="nav-link" href="#">Privacy &amp; Policy</a>
                </li>
                <li class="nav-item opacity mx-3">&#47;</li>
                <li class="nav-item">
                  <a class="nav-link" href="#">Terms</a>
                </li>
                <li class="nav-item opacity mx-3">&#47;</li>
                <li class="nav-item">
                  <a class="nav-link" href="#">FAQ</a>
                </li>
              </ul> -->
              <!-- End Nav Link -->
            </p>
          </div>
          <!-- End Copyright -->
        </div>
      </div>
    </footer>
    <a class="js-go-to go-to position-fixed animated hs-go-to-prevent-event" href="javascript:;" style="right: 38px; bottom: 120px;" data-hs-go-to-options="{

       &quot;position&quot;: {
         &quot;init&quot;: {
           &quot;right&quot;: 38
         },
         &quot;show&quot;: {
           &quot;bottom&quot;: 120
         },
         &quot;hide&quot;: {
           &quot;bottom&quot;: 15
         }
       }
     }">
      <i class="fas fa-angle-up"></i>
    </a>
    <div id="QR_code">
      <img  class="js-go-to go-toQR position-fixed animated hs-go-to-prevent-event" src="../../assets/img/QR_code/qrcode_ICACHI_1.jpg" style="right: 15px; bottom: 15px; width:90px;height: 90px" data-hs-go-to-options="{

       &quot;position&quot;: {
         &quot;init&quot;: {
           &quot;right&quot;: 15
         },
         &quot;show&quot;: {
           &quot;bottom&quot;: 15
         },
         &quot;hide&quot;: {
           &quot;bottom&quot;: 50
         }
       }
     }">
    </div>
    <!-- ========== END FOOTER ========== -->
  </div>
</template>

<script>
export default {
  props:{
    is_show:String
  },
  methods:{
    function () {
      //绑定滚动条事件
      //绑定滚动条事件
      $(window).bind("scroll", function () {
        var sTop = $(window).scrollTop();
        var sTop1 = parseInt(sTop);
        if (sTop1 <= 800) {
          if (!$("#QR_code").is(":visible")) {
            try {
              $("#QR_code").slideDown();
            } catch (e) {
              $("#QR_code").show();
            }
          }
        }
        else {
          if ($("#QR_code").is(":visible")) {
            try {
              $("#QR_code").slideDown();
            } catch (e) {
              $("#QR_code").hide();
            }
          }
        }
      });
    }
  },
  mounted () {
    this.function();
    // INITIALIZATION OF LEAFLET
    // =======================================================
    $('#map').each(function () {
      var leaflet = $.HSCore.components.HSLeaflet.init($(this)[0]);

      L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoiY3JhbmJlcnJ5d29uZyIsImEiOiJja3I1dGxtZ3owanA1MnFyMmdiYm05Z3FsIn0.zeKSvuFTyM7DfQ7TxK_uLg', {
        id: 'mapbox/light-v9'
      }).addTo(leaflet);
    });
  },

}
</script>
