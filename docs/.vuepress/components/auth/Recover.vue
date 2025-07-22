<template>
  <div>
    <!-- ========== MAIN ========== -->
<!--    忘记密码界面-->
  <main id="content" role="main">
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
            <h1>{{$t('auth.ForgotYourPassword')}}</h1>
            <p>{{ $t('auth.forgetPassword') }}</p>
          </div>
        </div>
      </div>
      <!-- End Hero Section -->
    <!-- Login Form -->
    <div class="container space-1 space-lg-1">
      <form class="js-validate w-md-75 w-lg-50 mx-md-auto">
        <!-- Form Group -->
        <div class="js-form-message form-group">
          <label class="input-label" for="signinSrEmail">{{ $t('auth.EmailAddress') }}</label>
          <input v-model="email" type="email" class="form-control" name="email" id="signinSrEmail" :placeholder="''+$t('auth.emailHint')" aria-label="Email address" required
                 data-msg="Please enter a valid email address.">
        </div>
        <!-- End Form Group -->

        <!-- Button -->
        <div class="row align-items-center mb-5">
          <div class="col-sm-6 mb-3 mb-sm-0">
            <a class="font-size-1 font-weight-bold" href="/auth/SignIn">
              <i class="fas fa-angle-left fa-sm mr-1"></i> {{$t('auth.back')}}
            </a>
          </div>

          <div class="col-sm-6 text-sm-right">
            <button @click="getPassword" type="button" class="btn btn-primary transition-3d-hover">{{$t('auth.reset')}}</button>
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
        email: ''
    }
  },
  created () {
    // this.getAuth()
  },
  methods: {
    isEmpty (obj) {
      if (typeof obj == 'undefined' || obj == null || obj == '') {
        return true
      } else {
        return false
      }
    },
    getPassword () {
      if(!this.isEmpty(this.email) ){
      this.$axios.get('/public/getForgotPasswordCaptcha', {
        params: {
          email: this.email,
        },
      })
        .then(res => {
          console.log(this.email)
          window.localStorage.setItem('email',this.email)
          this.$router.push('verify')
        })
        .catch(err => {
          console.error(err)
          alert("邮箱无效或未注册，请重新输入。")
        })
      }
      else {
        alert("请先输入邮箱！")
      }
    }

  }
}
</script>
