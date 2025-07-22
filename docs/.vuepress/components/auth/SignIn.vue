<template>
  <div>
    <!-- ========== MAIN ========== -->
    <main id="content" role="main">
      <!--登录界面-->

      <homepage-hero :heroTitle="heroTitle" :heroSubTitle="heroSubTitle"></homepage-hero>
<!--      <home-header :username="username" :judgment="judgment"></home-header>-->
      <!-- Login Form -->
      <div class="container space-1 space-lg-1">
        <form class="js-validate w-md-75 w-lg-50 mx-md-auto" :model="loginForm">

          <!-- Form Group -->
          <div class="js-form-message form-group">
            <label class="input-label" for="signinSrEmail">{{ $t('auth.EmailAddress') }}</label>
            <input v-model="loginForm.email" type="email" class="form-control" name="email" id="signinSrEmail"
                   placeholder="Email address"
                   aria-label="Email address" required
                   data-msg="Please enter a valid email address.">
          </div>
          <!-- End Form Group -->

          <!-- Form Group -->
          <div class="js-form-message form-group">
            <label class="input-label" for="signinSrPassword">
            <span class="d-flex justify-content-between align-items-center">
              {{ $t('auth.Password') }}
              <!--忘记密码,跳转界面-->
              <a class="link-underline text-capitalize font-weight-normal"
                 href="/auth/recover">{{ $t('auth.ForgotYourPassword') }}</a>
            </span>
            </label>
            <input v-model="loginForm.password" type="password" class="form-control" name="password"
                   id="signinSrPassword" placeholder="********"
                   aria-label="********" required
                   data-msg="Your password is invalid. Please try again.">
          </div>
          <!-- End Form Group -->

          <!-- Button -->
          <div class="row align-items-center mb-5">
            <div class="col-sm-6 mb-3 mb-sm-0">
              <!--如果没有账户，跳转到注册界面-->
              <span class="font-size-1 text-muted">{{ $t('auth.DontHaveAnAccount') }}</span>
              <a class="font-size-1 font-weight-bold" href="/auth/signup">{{ $t('auth.SignUp') }}</a>
            </div>

            <div class="col-sm-6 text-sm-right">
              <button @click="getAuth" type="button" class="btn btn-primary transition-3d-hover">{{
                  $t('auth.SignIn')
                }}
              </button>
            </div>
          </div>
          <!-- End Button -->
        </form>
      </div>
      <!-- End Login Form -->
    </main>
    <!-- ========== END MAIN ========== -->
  </div>
</template>

<script>
export default {
  // 接受父组件的值
  data () {
    return {
      loginForm: {
        email: '',
        password: '',
      },
      heroTitle: 'auth.WelcomeBack',
      heroSubTitle: 'aboutus.InternationalChineseAssociationOfComputerHumanInteraction',
      username: 'FAQ',
      // judgment:'#signupModal'
    }
  },
  created () {
    // this.getAuth()

  },
  mounted () {
    console.log('1234567890')
  },
  methods: {
    getAuth () {
      this.$axios.post('/public/login', this.loginForm)
        .then(res => {
          console.log(res.data)
          console.log(res.data.data.token)
          window.localStorage.setItem('user', res.data)
          window.localStorage.setItem('username', res.data.data.name)
          window.localStorage.setItem('token', res.data.data.token)
          window.localStorage.setItem('user_info',res.data.data)
          window.localStorage.setItem('user_info',JSON.stringify(res.data.data))

          // this.username = res.data.data.name
          // this.judgment = '#logOut'
          alert('登录成功')
          window.location.href="/"
          // this.$router.push('/')

        })
        .catch(err => {
          console.error(err)
          alert('密码错误或账户不存在')
        })

    }

  }
}
</script>
