<template>
  <div>
    <!-- ========== HEADER ========== -->
    <header
      id="header"
      class="
        header
        header-box-shadow-on-scroll
        header-abs-top
        header-bg-transparent
        header-show-hide
      "
      data-hs-header-options='{
            "fixMoment": 1000,
            "fixEffect": "slide"
          }'
    >
      <!-- Search -->
      <div id="searchPushTop" class="search-push-top">
        <div class="container position-relative">
          <div class="search-push-top-content pt-3">
            <!-- Close Button -->
            <div class="search-push-top-close-btn">
              <div class="hs-unfold">
                <a
                  class="
                    js-hs-unfold-invoker
                    btn btn-icon btn-xs btn-soft-secondary
                    mt-2
                    mr-2
                  "
                  href="javascript:;"
                  data-hs-unfold-options='{
                  "target": "#searchPushTop",
                  "type": "jquery-slide",
                  "contentSelector": ".search-push-top"
                 }'
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
                </a>
              </div>
            </div>
            <!-- End Close Button -->

            <!-- Input -->
            <form class="input-group">
              <input
                type="search"
                class="form-control"
                v-model="selectVal"
                @blur='queryData'
                @input="queryData"
                placeholder=""
                aria-label="Search Front"
              />
              <div class="input-group-append">
                <button type="button" class="btn btn-primary">
                  {{ $t('home.Search') }}
                </button>
              </div>
            </form>
            <!-- End Input -->
          </div>
        </div>
      </div>
      <!-- End Search -->

      <div class="header-section" >
        <!-- Topbar -->
        <div class="container header-hide-content pt-2">
          <div class="d-flex align-items-center">
            <!-- Language -->
            <div class="hs-unfold">
              <!--              <a-->
              <!--                class="-->
              <!--                  js-hs-unfold-invoker-->
              <!--                  dropdown-nav-link dropdown-toggle-->
              <!--                  d-flex-->
              <!--                  align-items-center-->
              <!--                "-->
              <!--                href="javascript:;"-->
              <!--                data-hs-unfold-options='{-->
              <!--                  "target": "#languageDropdown",-->
              <!--                  "type": "css-animation",-->
              <!--                  "event": "hover",-->
              <!--                  "hideOnScroll": "true"-->
              <!--                 }'-->
              <!--              >-->
              <!-- <img class="dropdown-item-icon mr-2" src="./assets/vendor/flag-icon-css/flags/4x3/us.svg" alt="SVG"> -->
              <button type="button" class="btn btn-light" style="padding:0.2rem"><b><span class="d-none d-sm-inline-block" @click="changeLang()">{{ lang }}</span></b></button>

              <!--              </a>-->
              <!--页面显示为中文时，应显示English ,页面显示为English时，应显示简体中文-->
              <!--              <div-->
              <!--                id="languageDropdown"-->
              <!--                class="hs-unfold-content dropdown-menu"-->
              <!--              >-->
              <!--                <b><a class="dropdown-item active" @click="changeLang()">简体中文</a></b>-->
              <!--                &lt;!&ndash; <a class="dropdown-item" href="#">繁体中文</a> &ndash;&gt;-->
              <!--                &lt;!&ndash; <a class="dropdown-item" href="#">日本語</a> &ndash;&gt;-->
              <!--              </div>-->
            </div>
            <!-- End Language -->

            <div class="ml-auto">
              <!-- Jump To -->
              <div class="hs-unfold d-sm-none mr-2">
                <a
                  class="
                    js-hs-unfold-invoker
                    dropdown-nav-link dropdown-toggle
                    d-flex
                    align-items-center
                  "
                  href="javascript:;"
                  data-hs-unfold-options='{
                    "target": "#jumpToDropdown",
                    "type": "css-animation",
                    "event": "hover",
                    "hideOnScroll": "true"
                   }'
                >
                  Jump to
                </a>

                <div
                  id="jumpToDropdown"
                  class="hs-unfold-content dropdown-menu"
                >
                  <a class="dropdown-item"  v-model="username">{{username}}</a>
                  <!-- <a class="dropdown-item" href="./page-contacts-agency.html">联系我们</a> -->
                </div>
              </div>
              <!-- End Jump To -->

              <!-- Links -->
              <div class="nav nav-sm nav-y-0 d-none d-sm-flex ml-sm-auto">
<!--                <div style="align-items: center" >-->
<!--                  <button @click="LogOut"-->
<!--                          type="button"-->
<!--                          class="btn btn-outline-secondary btn-sm" style="margin: 0 auto"-->
<!--                  >-->
<!--                    退出登录-->
<!--                  </button>-->
<!--                </div>-->
                <a class="nav-link justify-content-center" v-model="username" >{{username}}</a>
                <!-- <a class="nav-link" href="./page-contacts-agency.html">联系我们</a> -->
              </div>
              <!-- End Links -->
            </div>

            <ul class="list-inline ml-2 mb-0">
              <!-- Search -->
              <li class="list-inline-item">
                <div class="hs-unfold">
                  <a
                    class="
                      js-hs-unfold-invoker
                      btn btn-xs btn-icon btn-ghost-secondary
                    "
                    href="javascript:;"
                    data-hs-unfold-options='{
                    "target": "#searchPushTop",
                    "type": "jquery-slide",
                    "contentSelector": ".search-push-top"
                   }'
                  >
                    <i class="fas fa-search"></i>
                  </a>
                </div>
              </li>
              <!-- End Search -->

              <!-- Shopping Cart -->
              <!-- <li class="list-inline-item">
              <div class="hs-unfold">
                <a class="js-hs-unfold-invoker btn btn-xs btn-icon btn-ghost-secondary" href="javascript:;"
                   data-hs-unfold-options='{
                    "target": "#shoppingCartDropdown",
                    "type": "css-animation",
                    "event": "hover",
                    "hideOnScroll": "true"
                   }'>
                  <i class="fas fa-shopping-cart"></i>
                </a>

                <div id="shoppingCartDropdown" class="hs-unfold-content dropdown-menu dropdown-menu-right dropdown-card text-center" style="min-width: 275px;">
                  <div class="card">
                    <div class="card-body">
                      <figure class="max-w-9rem mx-auto mb-3">
                        <img class="img-fluid" src="./assets/svg/illustrations/empty-cart.svg" alt="SVG">
                      </figure>
                      <span class="d-block">Your cart is empty</span>
                    </div>

                    <div class="card-footer">
                      <small>Free shipping on orders over <strong class="text-dark">$50</strong></small>
                    </div>
                  </div>
                </div>
              </div>
            </li> -->
              <!-- End Shopping Cart -->

              <!-- Account Login 右上角的小人头-->
              <li class="list-inline-item">
                <div class="hs-unfold">
                  <a
                    class="
                      js-hs-unfold-invoker
                      btn btn-icon btn-xs btn-ghost-secondary
                    "
                    href="javascript:;"
                    data-toggle="modal"
                    :data-target="judgment"
                  >
                    <i class="fas fa-user-circle"></i>
                  </a>
                </div>
              </li>
              <!-- End Account Login -->
            </ul>
          </div>
        </div>
        <!-- End Topbar -->

        <div id="logoAndNav" class="container">
          <!-- Nav -->
          <nav class="js-mega-menu navbar navbar-expand-lg pt-1 pb-2">
            <!-- Logo -->
            <!-- <a class="navbar-brand" href="/" aria-label="Front">
            <img src="{{ static_url('assets/svg/logos/icachi-logo.svg') }}" alt="Logo">
          </a>
          &nbsp;&nbsp;
          <a class="navbar-brand" href="/" aria-label="Front">
            <img src="{{ static_url('assets/svg/logos/icachi-text.svg') }}" alt="Logo" style="width:15rem;">
          </a> -->
            <router-link class="navbar-brand" to="/" aria-label="Front">
              <img
                src="../../assets/svg/logos/icachi-text-logo.svg"
                alt="Logo"
                style="width: 20rem"
              />
            </router-link>
            <!-- End Logo -->

            <!-- Responsive Toggle Button -->
            <button
              type="button"
              class="navbar-toggler btn btn-icon btn-sm rounded-circle"
              aria-label="Toggle navigation"
              aria-expanded="false"
              aria-controls="navBar"
              data-toggle="collapse"
              data-target="#navBar"
            >
              <span class="navbar-toggler-default">
                <svg
                  width="14"
                  height="14"
                  viewBox="0 0 18 18"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    fill="currentColor"
                    d="M17.4,6.2H0.6C0.3,6.2,0,5.9,0,5.5V4.1c0-0.4,0.3-0.7,0.6-0.7h16.9c0.3,0,0.6,0.3,0.6,0.7v1.4C18,5.9,17.7,6.2,17.4,6.2z M17.4,14.1H0.6c-0.3,0-0.6-0.3-0.6-0.7V12c0-0.4,0.3-0.7,0.6-0.7h16.9c0.3,0,0.6,0.3,0.6,0.7v1.4C18,13.7,17.7,14.1,17.4,14.1z"
                  />
                </svg>
              </span>
              <span class="navbar-toggler-toggled">
                <svg
                  width="14"
                  height="14"
                  viewBox="0 0 18 18"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    fill="currentColor"
                    d="M11.5,9.5l5-5c0.2-0.2,0.2-0.6-0.1-0.9l-1-1c-0.3-0.3-0.7-0.3-0.9-0.1l-5,5l-5-5C4.3,2.3,3.9,2.4,3.6,2.6l-1,1 C2.4,3.9,2.3,4.3,2.5,4.5l5,5l-5,5c-0.2,0.2-0.2,0.6,0.1,0.9l1,1c0.3,0.3,0.7,0.3,0.9,0.1l5-5l5,5c0.2,0.2,0.6,0.2,0.9-0.1l1-1 c0.3-0.3,0.3-0.7,0.1-0.9L11.5,9.5z"
                  />
                </svg>
              </span>
            </button>
            <!-- End Responsive Toggle Button -->

            <!-- Navigation -->
            <div id="navBar" class="collapse navbar-collapse">
              <div class="navbar-body header-abs-top-inner">
                <ul class="nav">
                  <li class="nav-item">
                    <b><router-link class="nav-link" to="/">{{
                        $t('home.Home')
                      }}
                    </router-link></b>
                  </li>
                  <li class="nav-item">
                    <b><router-link class="nav-link" to="/aboutus">{{
                        $t('aboutus.AboutUs')
                      }}
                    </router-link></b>
                  </li>
                  <li class="nav-item">
                    <b><router-link class="nav-link" to="/bylaws">{{
                        $t('bylaws.Bylaws')
                      }}
                    </router-link></b>
                  </li>
                  <li class="nav-item">
                    <b> <router-link class="nav-link" to="/newsroom">{{ $t('newsroom.NewsRoom') }}</router-link></b>
                  </li>
                  <li class="nav-item">
                    <b><router-link class="nav-link" to="/conference">{{
                        $t('conference.Conference')
                      }}
                    </router-link></b>
                  </li>
                  <li class="nav-item">
                    <b><router-link class="nav-link" to="/resource">{{
                        $t('resource.Resource')
                      }}
                    </router-link></b>
                  </li>
                  <!-- <li class="nav-item">
                    <router-link class="nav-link" to="/contacts">{{
                      $t("contacts.Contacts")
                    }}</router-link>
                  </li> -->
                  <li class="nav-item " v-if="this.judgment!='#logOut'">
                    <b><router-link class="nav-link" to="/auth/signup" >{{
                        $t('home.JoinUs')
                      }}
                    </router-link></b>
                  </li>
                  <li class="nav-item" v-if="this.judgment=='#logOut'">
                    <b><router-link class="nav-link" to="/auth/UserInfo">{{$t('home.userInfo')}}
                    </router-link></b>
                  </li>
                </ul>
              </div>
            </div>
            <!-- End Navigation -->
          </nav>
          <!-- End Nav -->
        </div>
      </div>
    </header>
    <!-- ========== END HEADER ========== -->

    <!-- Sign Up Modal -->
    <div
      class="modal fade"
      id="signupModal"
      tabindex="-1"
      role="dialog"
      aria-hidden="true"

    >
      <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
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

          <!--          登录表单-->
          <!-- Body -->
          <div class="modal-body p-sm-5">
            <form class="js-validate">
              <!-- Sign in -->
              <div id="signinModalForm">
                <div class="text-center mb-5">
                  <h2>{{$t('auth.WelcomeBack')}}{{ Welcomback }}</h2>
                  <p>
                    {{ $t('auth.DontHaveAnAccount') }}
                    <a
                      class=""
                      href="/auth/signup"
                    >{{ $t('auth.SignUpHere') }}</a
                    >
                  </p>
                </div>
                <!-- Form Group -->
                <div class="js-form-message form-group">
                  <label class="input-label" for="signinSrEmail">{{
                      $t('auth.EmailAddress')
                    }}</label>
                  <input v-model="loginForm.email"
                         type="email"
                         class="form-control"
                         name="email"
                         id="signinSrEmail"
                         :placeholder="''+$t('auth.emailHint')"
                         aria-label="Email address"
                         required
                         data-msg="Please enter a valid email address."
                  />
                </div>
                <!-- End Form Group -->

                <!-- Form Group -->
                <div class="js-form-message form-group">
                  <label class="input-label" for="signinSrPassword">
                    <span
                      class="d-flex justify-content-between align-items-center"
                    >
                      {{ $t('auth.Password') }}
                      <a
                        class="
                          link-underline
                          text-capitalize
                          font-weight-normal
                        "
                        href="/auth/recover"
                      >{{ $t('auth.ForgotYourPassword') }}</a
                      >
                    </span>
                  </label>
                  <input v-model="loginForm.password"
                         type="password"
                         class="form-control"
                         name="password"
                         id="signinSrPassword"
                         placeholder="********"
                         aria-label="********"
                         required
                         data-msg="Your password is invalid. Please try again."
                  />
                </div>
                <!-- End Form Group -->

                <button @click="getAuth"
                        type="button"
                        class="btn btn-block btn-primary transition-3d-hover"
                >
                  {{ $t('auth.SignIn') }}
                </button>
              </div>
              <!-- End Sign in -->
            </form>
          </div>
          <!-- End Body -->
        </div>
      </div>
    </div>
    <!-- End Sign Up Modal -->

    <!-- log Out  Modal -->
    <div
      class="modal fade"
      id="logOut"
      tabindex="-1"
      role="dialog"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered justify-content-center" role="document" style="align-items: center">
        <div class="modal-content" style="width: 300px">
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

          <!--          登录表单-->
          <!-- Body -->
          <div class="modal-body p-sm-5" style="width: 300px">
            <form class="js-validate">
              <!-- Sign in -->
              <div id="logOutForm" >
                <div class="text-center mb-5">
                  <h3>{{ Welcomback }}</h3>
                </div>
                <!-- End Form Group -->
                <div style="align-items: center" >
                <button @click="LogOut"
                        type="button"
                        class="btn btn-outline-secondary" style="display: block;margin: 0 auto"
                >
                  退出登录
                </button>
                </div>
              </div>
              <!-- End Sign in -->
            </form>
          </div>
          <!-- End Body -->
        </div>
      </div>
    </div>
    <!-- 模态框（Modal） -->
    <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
            <h4 class="modal-title" id="myModalLabel"></h4>
          </div>
          <div class="modal-body">{{ msg }}</div>
          <div class="modal-footer">
            <!--            <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>-->
            <button type="button" class="btn btn-primary" data-dismiss="modal">关闭</button>
          </div>
        </div><!-- /.modal-content -->
      </div><!-- /.modal-dialog -->
    </div>
    <!-- /.modal -->
    <!-- End log Out Modal -->
  </div>
</template>

<script>
export default {
  props: {
    // username:String,
    // judgment:String,
  },
  data () {
    return {
      loginForm: {
        email: '',
        password: '',
      },
      translForm:{
        doctype:'json',
        type:'AUTO',
        i:'翻译测试',
      },
      username: '',
      Welcomback: '',
      judgment: '#signupModal',
      msg: '1234567890',
      lang:'English',
      selectVal:'',//搜索关键字
    }
  },
  mounted () {
    let form = JSON.parse(window.localStorage.getItem('user_info'))
    this.username = form.name
    if(form!=null)
    {
      this.judgment = '#logOut'
      this.Welcomback = form.name
    }
    else
      this.judgment = '#signupModal'
    // if (username !== null) {
    //   this.Welcomback =  username
    //   this.judgment = '#logOut'
    // }
  },
  methods: {
    i18nChange: function (event) {
      locale: Cookies.get('language') || 'zh' // set local
    },
    queryData(){
      //并没有输入关键字时，就不要再搜索了
      if(this.selectVal===''||this.selectVal==null){
        this.orgList=JSON.parse(JSON.stringify(this.orgList));
        return;
      }
      //搜索
      let list=this.orgList.filter(item=>item.indexOf(this.selectVal)>=0);
      this.orgList=list;
    },
    getAuth () {
      this.$axios.post('/public/login', this.loginForm)
        .then(res => {
          console.log(res.data)
          console.log(res.data.data.token)
          window.localStorage.setItem('user', res.data)
          window.localStorage.setItem('username',res.data.data.name)
          window.localStorage.setItem('token', res.data.data.token)
          window.localStorage.setItem('user_info',JSON.stringify(res.data.data))

          this.$router.push('/')
          // alert("登录成功")
          this.username = res.data.data.name
          this.Welcomback = res.data.data.name
          this.judgment = '#logOut'
          this.msg = '登录成功!'
          $('#myModal').modal('show')
        })
        .catch(err => {
          console.log(err)
          this.msg = '登录失败！请检查您的信息！'
          $('#myModal').modal('show')
        })
      document.querySelector('#signupModal .btn-ghost-secondary').click()

    },
    LogOut () {
      window.localStorage.clear()
      this.$i18n.locale = 'zh'
      // alert("Success!")
      this.username = ''
      this.judgment = '#signupModal'
      if(this.$i18n.locale = 'en') {
        this.Welcomback = ''
      }
      else this.Welcomback = 'Welcome back'
      this.$router.push('/')
      this.$i18n.locale = 'zh'
      document.querySelector('#logOut .btn-ghost-secondary').click()
      // console.log($('#myModal'))
      this.msg = '退出成功!'
      $('#myModal').modal('show')
      this.$i18n.locale = 'zh'

    },
    // 改变语言
    changeLang(){
      if(this.lang=='English')
      {
        this.$i18n.locale = 'en'
        this.lang = '简体中文'

      }
      else {
        this.$i18n.locale = 'zh'
        this.lang = 'English'
      }
    },


  }
}
</script>
