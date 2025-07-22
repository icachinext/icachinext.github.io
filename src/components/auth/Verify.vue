<template>
  <div>
    <!-- ========== MAIN ========== -->
    <!-- 安全验证界面-->
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
            <h1>安全验证</h1>
            <p>已发送验证码到您的邮箱，请输入您的验证码</p>
          </div>
        </div>
      </div>
      <!-- End Hero Section -->
      <!-- Login Form -->
      <div class="container space-1 space-lg-1">
        <form class="js-validate w-md-75 w-lg-50 mx-md-auto">
          <!-- Form Group -->
          <div class="js-form-message form-group">
            <label class="input-label" for="signinSrEmail">验证码</label>
            <input @keyup.enter="VerifyCode" v-model="captcha" type="text" class="form-control" name="email" id="signinSrEmail" placeholder="" aria-label="Verification code" required
                   data-msg="Please enter a valid captcha.">
            <input style="display: none">
          </div>
          <!-- End Form Group -->

          <!-- Button -->
          <div class="row align-items-center mb-5">
            <div class="col-sm-6 mb-3 mb-sm-0">
              <a class="font-size-1 font-weight-bold" href="/auth/SignIn">
                <i class="fas fa-angle-left fa-sm mr-1"></i> 返回登录
              </a>
            </div>

            <div class="col-sm-6 text-sm-right">
              <button @click="VerifyCode" type="button" class="btn btn-primary transition-3d-hover">验证</button>
            </div>
          </div>
          <!-- End Button -->
        </form>
      </div>
      <!-- End Login Form -->
    </main>
    <div class="modal fade" id="modal_verify" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
            <h4 class="modal-title" id="myModalLabel"></h4>
          </div>
          <div class="modal-body">{{modal_verify}}</div>
          <div class="modal-footer">
            <!--            <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>-->
            <button type="button" class="btn btn-primary" data-dismiss="modal">关闭</button>
          </div>
        </div><!-- /.modal-content -->
      </div><!-- /.modal-dialog -->
    </div>

    <!-- ========== END MAIN ========== -->
  </div>
</template>

<script>
export default {
  // 接受父组件的值
  data () {
    return {
      captcha:'',
      modal_verify:'',
    }
  },
  created () {
    // this.getAuth()
  },
  methods: {
    VerifyCode () {
      this.$axios.get('/public/isForgotPasswordCaptcha', {
        params: {
          email: window.localStorage.getItem('email'),
          captcha:this.captcha
        },
      })
        .then(res => {
          console.log(window.localStorage.getItem('email'))
          window.localStorage.setItem('captcha',this.captcha)
          //console.log(window.localStorage.getItem('captcha'))
          if(res.data.data==true)
          {
            this.$router.push('reset')
          }
          else
          {
            this.modal_verify = "验证码错误，请重新输入！"
            $('#modal_verify').modal('show')
          }
        })
        .catch(err => {
          console.error(err)
        })

    }

  }
}
</script>
