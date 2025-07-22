<template>
  <div>
    <!-- ========== MAIN ========== -->
    <main id="content" role="main">
      <!--      <homepage-hero :heroTitle="heroTitle" :heroSubTitle="heroSubTitle"></homepage-hero>-->
      <div style="width: auto;height: 150px"></div>

      <!-- Login Form -->
      <div class="container space-1 space-lg-1">
        <form class="js-validate w-md-75 w-lg-50 mx-md-auto" v-model="loginForm">

          <!-- Form Group -->
<!--          <div class="js-form-message form-group">-->
<!--            <label class="input-label">{{ $t('auth.avatar') }}</label>-->
<!--            <div class="media align-items-center">-->
<!--              <label class="avatar avatar-xl avatar-circle mr-4" for="avatarUploader">-->
<!--                <img :visible.sync="dialogVisible" id="avatarImg" class="avatar-img" :src="previewImage" alt="">-->
<!--              </label>-->

<!--              <div class="media-body" style="justify-content: right">-->
<!--                <div class="btn btn-outline-secondary file-attachment-btn " @click="$refs.file.click()" >上传头像-->
<!--                  <input type="file" class="js-file-attach file-attachment-btn-label" id="avatarUploader" hidden @change="onFileChange">-->
<!--                </div>-->

<!--              </div>-->
<!--            </div>-->
<!--          </div>-->
<!--          <input type="file" hidden ref='file' @change="onFileChange">-->
          <!-- Dialog 上传头像对话框 -->
<!--          <el-dialog-->
<!--            append-to-body-->
<!--            title="提示"-->
<!--            :visible.sync="dialogVisible"-->
<!--            width="30%"-->
<!--          >-->
<!--            &lt;!&ndash; src绑定处理后的图片路径 &ndash;&gt;-->
<!--            <img :src="previewImage" width="150px">-->
<!--            <span slot="footer" class="dialog-footer">-->
<!--            </span>-->
<!--          </el-dialog>-->
          <!-- Dialog 上传头像对话框 -->


          <label class="input-label">{{ $t('auth.EmailAddress') }}</label>
          <div class="input-group mb-4">
            <input v-model="loginForm.email"
                   type="email"
                   class="form-control"
                   :placeholder="''+$t('auth.emailHint')"
                   aria-label="邮箱地址"
                   aria-describedby="button-addon2"
                   required
                   data-msg="请输入有效的邮箱地址"
            />
            <button class="btn btn-outline-secondary" type="button" id="button-addon2" @click="captcha">{{ $t('auth.SendCaptcha') }}</button>
          </div>
          <!--          <div class="input-group mb-3">-->
          <!--            <input type="text" class="form-control" placeholder="Recipient's username" aria-label="Recipient's username" aria-describedby="button-addon2">-->
          <!--            <button class="btn btn-outline-secondary" type="button" id="button-addon2">发送验证码</button>-->
          <!--          </div>-->
          <!-- End Form Group -->

          <!-- Form Group -->
          <div class="js-form-message form-group">
            <label class="input-label">{{ $t('auth.Captcha') }}</label>
            <input v-model="loginForm.captcha"
                   type="text"
                   class="form-control"
                   name="code"
                   :placeholder="''+$t('auth.captchaHint')"
                   aria-label="验证码"
                   required
                   data-msg="请输入有效的验证码"
            />
          </div>
          <!-- End Form Group -->

          <!-- Form Group -->
          <div class="js-form-message form-group">
            <label class="input-label">{{ $t('auth.Password') }}</label>
            <input v-model="loginForm.password"
                   type="password"
                   minlength="6"
                   class="form-control"
                   name="password"
                   placeholder="********"
                   aria-label="********"
                   required
                   data-msg="长度需大于等于6位字符"
            />
          </div>
          <!-- End Form Group -->
          <!--for=表示我只要选择这个字段，就会选中输入框-->

          <!-- Form Group -->
          <div class="js-form-message form-group">
            <label class="input-label">{{ $t('auth.ConfirmPassword') }}</label>
            <input v-model="loginForm.confirmPassword"
                   type="password"
                   minlength="6"
                   class="form-control"
                   placeholder="********"
                   aria-label="********"
                   required
                   id="psw2"
                   data-msg="密码不匹配"
            />
          </div>
<!--          <div id="psw3-error" class="invalid-feedback" style="display: none; margin-top: -20px;-->
<!--    margin-bottom: 15px;">密码不匹配</div>-->
          <!-- End Form Group -->

          <!-- Form Group -->
          <div class="js-form-message form-group">
            <label class="input-label">{{ $t('auth.MemberName') }}</label>
            <input v-model="loginForm.name"
                   type="text"
                   class="form-control"
                   name="email"
                   :placeholder="''+$t('auth.nameHint')"
                   aria-label="请输入姓名"
                   required
                   @click="this.checkedPSW"
                   data-msg="请输入有效的姓名"
            />
          </div>
          <!-- End Form Group -->


          <!-- Form Group -->
          <div class="js-form-message form-group">
            <label class="input-label" >{{ $t('auth.Organization') }}</label>
            <input v-model="loginForm.organization"
                   type="text"
                   class="form-control"
                   name="email"
                   :placeholder="''+$t('auth.organizationHint')"
                   aria-label="工作单位"
                   required
                   data-msg="请输入有效的单位"
            />
          </div>
          <!-- End Form Group -->

          <!-- Form Group -->
          <label class="input-label">{{ $t('auth.Position') }}</label>
          <div class="input-group mb-4">

            <select id="signinPosition"
                    type="text"
                    class="btn btn-outline-secondary dropdown-toggle dropdown-menu-left align-content-center"
                    data-bs-toggle="dropdown"
                    required
            >
              <option value="教授" class="dropdown-item" >{{$t('auth.position1')}}</option>
              <option value="副教授" class="dropdown-item">{{$t('auth.position2')}}</option>
              <option value="讲师" class="dropdown-item">{{$t('auth.position3')}}</option>
              <option value="助教" class="dropdown-item">{{$t('auth.position4')}}</option>
              <option value="学生" class="dropdown-item">{{$t('auth.position5')}}</option>
              <option value="6" class="dropdown-item">{{$t('auth.position6')}}</option>

            </select>
            <input type="text" class="form-control align-content-center" aria-label="Text input with dropdown button" :placeholder="'              '+$t('auth.other')" v-model="positionElse">

          </div>
          <!-- End Form Group -->
          <!--          <div class="input-group mb-3">-->
          <!--            <button class="btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</button>-->
          <!--            <ul class="dropdown-menu">-->
          <!--              <li><a class="dropdown-item" href="#">Action</a></li>-->
          <!--              <li><a class="dropdown-item" href="#">Another action</a></li>-->
          <!--              <li><a class="dropdown-item" href="#">Something else here</a></li>-->
          <!--              <li><hr class="dropdown-divider"></li>-->
          <!--              <li><a class="dropdown-item" href="#">Separated link</a></li>-->
          <!--            </ul>-->
          <!--            <input type="text" class="form-control" aria-label="Text input with dropdown button">-->
          <!--          </div>-->
          <!-- Form Group -->
          <div class="js-form-message form-group">
            <label class="input-label" >{{ $t('auth.Phone') }}</label>
            <input v-model="loginForm.phone"
                   type="tel"
                   class="form-control"
                   name="email"
                   :placeholder="''+ $t('auth.phoneHint')"
                   aria-label="电话"
                   data-msg="请输入有效的电话号码"
            />
          </div>
          <!-- End Form Group -->

          <!-- Form Group -->
          <div class="js-form-message form-group">
            <label class="input-label" >{{ $t('auth.Fields') }}</label>
            <input
              type="text"
              name="tags"
              id="tags"
              class="form-control"
              :placeholder="''+$t('auth.tagHint')"
            />
          </div>
          <!-- End Form Group -->



          <!-- Checkbox -->
          <div class="js-form-message mb-5">
            <div
              class="
                      custom-control custom-checkbox
                      d-flex
                      align-items-center
                      text-muted
                    "
            >
              <input
                type="checkbox"
                class="custom-control-input"
                id="termsCheckbox"
                name="termsCheckbox"
                required
                data-msg="请阅读后同意我们的协议"

              />
              <label class="custom-control-label" for="termsCheckbox">
                <small>
                  {{ $t('auth.IAgreeToThe') }}
                  <a class="link-underline" href="javascript:;"
                     data-toggle="modal"
                     data-target="#terms">{{ $t('auth.TermsAndConditions') }}</a>
                </small>
              </label>

            </div>
          </div>
          <!-- End Checkbox -->

          <!-- Sign Up Modal -->
          <div
            class="modal fade"
            id="terms"
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

                <!-- 会员条款-->
                <!-- Body -->
                <div class="modal-body p-sm-5">
                  <form class="js-validate">
                    <!-- Sign in -->
                    <div id="signinModalForm">
                      <div class="text-center mb-5">
                        <h2>{{$t('auth.terms')}}</h2>
                        <p>
                          {{ $t('auth.termsContent') }}
                        </p>
                      </div>

                    </div>
                    <!-- End Sign in -->
                  </form>
                </div>
                <!-- End Body -->
              </div>
            </div>
          </div>
          <!-- End Sign Up Modal -->

          <!-- Button -->
          <div class="row align-items-center mb-5">
            <div class="col-sm-6 mb-3 mb-sm-0">
              <span class="font-size-1 text-muted">{{ $t('auth.AlreadyHaveAnAccount') }}</span>
              <a
                class="font-size-1 font-weight-bold"
                href="/auth/signin"
              >{{ $t('auth.SignIn') }}</a
              >
            </div>

            <div class="col-sm-6 text-sm-right" >
              <!--              <button @click="signUp"-->
              <button
                type="button"
                class="btn btn-primary transition-3d-hover"   @click="signUp"
              >
                {{ $t('auth.SignUp') }}
              </button>
            </div>
          </div>
          <!-- End Button -->
        </form>
      </div>
      <!-- 支付弹窗 -->
      <div v-if="this.checkSighUp"
           class="my-confirm"
           id="PayPal"
           tabindex="-1"
           role="dialog"
           aria-hidden="true"

      >
        <div class="modal-dialog modal-dialog-centered" role="document">
          <div class="modal-content">
            <!-- Header -->
            <div class="modal-close">
              <!--              <button-->
              <!--                type="button"-->
              <!--                class="btn btn-icon btn-sm btn-ghost-secondary"-->
              <!--                data-dismiss="modal"-->
              <!--                aria-label="Close"-->
              <!--              >-->
              <!--                <svg-->
              <!--                  width="10"-->
              <!--                  height="10"-->
              <!--                  viewBox="0 0 18 18"-->
              <!--                  xmlns="http://www.w3.org/2000/svg"-->
              <!--                >-->
              <path
                fill="currentColor"
                d="M11.5,9.5l5-5c0.2-0.2,0.2-0.6-0.1-0.9l-1-1c-0.3-0.3-0.7-0.3-0.9-0.1l-5,5l-5-5C4.3,2.3,3.9,2.4,3.6,2.6l-1,1 C2.4,3.9,2.3,4.3,2.5,4.5l5,5l-5,5c-0.2,0.2-0.2,0.6,0.1,0.9l1,1c0.3,0.3,0.7,0.3,0.9,0.1l5-5l5,5c0.2,0.2,0.6,0.2,0.9-0.1l1-1 c0.3-0.3,0.3-0.7,0.1-0.9L11.5,9.5z"
              />
              <!--                </svg>-->
              <!--              </button>-->
            </div>
            <!-- End Header -->

            <!--          登录表单-->
            <!-- Body -->
            <div class="modal-body p-sm-5">
              <form class="js-validate">
                <!-- Sign in -->
                <!--                      {{ $t('auth.DontHaveAnAccount') }}-->
                <div id="PayPalModalForm">
                  <div class="text-center mb-5">
                    <h2>现在成为我们的会员？</h2>

                  </div>
                  <!-- Form Group 支付的相关选择-->
                  <div id="smart-button-container">
                    <div style="text-align: center;vertical-align:middle;margin:0 auto;">
                      <div style="margin-bottom: 1.25rem;" >
                        <form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_blank">
                          <input type="hidden" name="cmd" value="_s-xclick">
                          <input type="hidden" name="hosted_button_id" value="7JZYEH225D2KU">
                          <input type="hidden" name="on0" value="">
                          <select name="os0" id="PaySelect"  style="margin: 0 auto;text-align: center"
                                  class="form-control"
                                  required
                          >
                            <option value="1" id="Regular Member">Regular Member : $45.00 USD - yearly</option>
                            <option value="2" id="Student Member">Student Member : $15.00 USD - yearly</option>
                          </select>

                          <!--                          <input type="hidden" name="currency_code" value="USD">-->
                          <!--                          <input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_subscribeCC_LG.gif" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">-->
                          <!--                          <img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="2" height="2">-->
                        </form>
                      </div>
                      <!--              按钮-->

                    </div>
                    <div>
                      <button @click="PayNow" type="button" class="btn btn-primary transition-3d-hover" style="float: left ;margin-left: 120px;" >支付</button>
                      <button @click="Later" type="button" class="btn  btn-primary transition-3d-hover" style="float: right ; margin-right: 130px">稍后</button>
                      <p></p>
                      <p></p>
                    </div>
                  </div>
                  <!-- End Form Group -->
                  <!-- End Form Group -->

                  <!--                  <button @click="getAuth"-->
                  <!--                          type="button"-->
                  <!--                          class="btn btn-block btn-primary transition-3d-hover"-->
                  <!--                  >-->
                  <!--                    {{ $t('auth.SignIn') }}-->
                  <!--                  </button>-->
                </div>
                <!-- End Sign in -->
              </form>
            </div>
            <!-- End Body -->
          </div>
        </div>
      </div>
      <!-- End Login Form -->
    </main>
    <!-- ========== END MAIN ========== -->
    <!-- 模态框（Modal） -->
    <div class="modal fade" id="myModal2" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
            <h4 class="modal-title" id="myModalLabel"></h4>
          </div>
          <div class="modal-body">{{msg2}}</div>
          <div class="modal-footer">
            <!--            <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>-->
            <button type="button" class="btn btn-primary" data-dismiss="modal">关闭</button>
          </div>
        </div><!-- /.modal-content -->
      </div><!-- /.modal-dialog -->
    </div>
    <!-- /.modal -->
  </div>
</template>

<script>
export default {
  mounted () {
    $('#tags').tagsInput();
  },
  // 接受父组件的值
  data () {
    return {
      previewImage:'https://s3.bmp.ovh/imgs/2022/01/a6722fdf38b398d8.png',//处理后的图片路径
      dialogVisible: false,//控制上传头像对话框
      heroTitle: 'home.JoinUs',
      heroSubTitle: 'aboutus.InternationalChineseAssociationOfComputerHumanInteraction',
      loginForm: {
        email: '',
        password: '',
        confirmPassword: '',
        name: '',
        phone: '',
        position: '',
        organization: '',
        field: '',
        country: '',
        membership: '1',
        biography: '',
        captcha: '',
      },
      checkSighUp:false,
      msg2:'',
      positionElse:'',
    }
  },

  methods: {
    isEmpty (obj) {
      if (typeof obj == 'undefined' || obj == null || obj == '') {
        return true
      } else {
        return false
      }
    },

    signUp () {
      var positionType = document.getElementById('signinPosition')
      var index = positionType.selectedIndex
      if(positionType.options[index].value==6)
      {
      this.loginForm.position = this.positionElse
      }
      else this.loginForm.position = positionType.options[index].value

      // alert($('#tags').val())
      this.loginForm.field = $('#tags').val()
      var isChecked = $("input[type='checkbox']").is(':checked')
      if(!this.isEmpty(this.loginForm.email) && !this.isEmpty(this.loginForm.password) && !this.isEmpty(this.loginForm.confirmPassword) && !this.isEmpty(this.loginForm.name)
        && !this.isEmpty(this.loginForm.position) && !this.isEmpty(this.loginForm.organization)
        && !this.isEmpty(this.loginForm.membership) && !this.isEmpty(this.loginForm.captcha)&&isChecked)
      {
        this.$axios.post('/public/register', this.loginForm)
          .then(res => {
            console.log(res.data)
            console.log(res.data.data.token)
            //window.localStorage.setItem('token',res.data.data.token)
            if (res.data.data !== '注册成功') {
              this.msg2 = res.data.data
              $('#myModal2').modal('show')
              // alert(res.data.data)
            } else {
              this.msg2 = '注册成功!'
              $('#myModal2').modal('show')
              // alert('Sign up success!')
              this.checkSighUp=true
              // this.$router.push('signin')
            }
          })
          .catch(err => {
            console.error(err)
          })
      }
      else
      {
        // this.checkSighUp = true
        this.msg2 = '检查您的信息!'
        $('#myModal2').modal('show')
        // alert('Check your information!')
      }
    },
    Later(){
      this.checkSighUp = false
      this.$router.push('signin')
    },
    checkedPSW(){
      // console.log(this.loginForm.password)
      // console.log(this.loginForm.confirmPassword)
      if((this.loginForm.confirmPassword!=this.loginForm.password)&&(this.loginForm.confirmPassword!=null))
      {
        $("#psw2").removeClass('is-valid')
        $("#psw2").addClass('is-invalid')
        // var target = document.getElementById('psw3-error')
        // if (target.style.display=="none")
        //   target.style.display="block";
      }
      else if(this.loginForm.confirmPassword!=null&&this.loginForm.confirmPassword==this.loginForm.password) {
        $("#psw2").removeClass('is-invalid')
        $("#psw2").addClass('is-valid')
      }
      else{
        $("#psw2").removeClass('is-invalid')
        $("#psw2").removeClass('is-valid')
      }
    },
    PayNow(){
      var payType = document.getElementById('PaySelect')
      var index2 = payType.selectedIndex
      if(payType.options[index2].value==1)
      {
        // 45
        window.location.href = "https://buy.stripe.com/7sl6rs3u39HB0NyfZ3"
      }
      // 15
      else window.location.href = "https://buy.stripe.com/28o034fcLaLF8g06os"
    },
    paypal () {
      this.$axios.get('/public/pay')
        .then(res => {
          window.location.href = res.data
          console.log(res.data)
          // window.location.href="https://www.baidu.com"
        })
        .catch(err => {
          console.error(err)
        })
    },
    onFileChange(){
      // 处理预览图片
      const file=this.$refs.file
      // URL.createObjectURL()方法会根据传入的参数创建一个指向该参数对象的URL
      const blobData=window.URL.createObjectURL(file.files[0])
      // console.log(blobData)
      // 将地址赋值给previewImage
      this.previewImage=blobData
      // 展示弹出层，预览用户选择图片
      this.dialogVisible=true
      // 解决选择相同文件不触发change事件问题
      this.$refs.file.value=''
    },

    captcha () {
      if(!this.isEmpty(this.loginForm.email) ){
      this.$axios.get('/public/getRegisterCaptcha', {
        params: {
          email: this.loginForm.email,
        },
      })
        .then(res => {
          console.log(res.data)
          this.msg2 = '验证码已经发送到您的邮箱，请查收!'
          $('#myModal2').modal('show')
          // alert('The verification code has been sent to your Email address,please check it!')
        })
        .catch(err => {
          console.error(err)
        })
      }
      else {
        this.msg2 = '请先输入邮箱！'
          $('#myModal2').modal('show')
      }
    }
  }
}
</script>

<style scoped>
.my-confirm {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 998;
  /* 这里防止当用户长按屏幕，出现的黑色背景色块，以及 iPhone 横平时字体的缩放问题 */
  -webkit-text-size-adjust: 100%;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}

</style>
