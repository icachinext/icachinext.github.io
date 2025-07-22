<template>
  <div>
    <!-- ========== MAIN ========== -->
    <main id="content" role="main">
      <!--设置属性-->
      <!--      <homepage-hero :heroTitle="heroTitle" :heroSubTitle="heroSubTitle"></homepage-hero>-->
      <div style="width: auto;height: 100px"></div>
      <div class="bg-dark" style="background-image: url(../../assets/svg/components/abstract-shapes-20.svg);">
        <div class="container space-1 space-top-lg-2 space-bottom-lg-3">
          <div class="row align-items-center">
            <div class="col">
              <div class="d-none d-lg-block">
                <h1 class="h2 text-white">个人信息</h1>
              </div>

              <!-- Breadcrumb -->
              <!-- End Breadcrumb -->
            </div>

<!--            <div class="col-auto">-->
<!--              <div class="d-none d-lg-block" @click="LogOut">-->
<!--                <a class="btn btn-sm btn-soft-light" >退出</a>-->
<!--              </div>-->

              <!-- Responsive Toggle Button -->
<!--              <button type="button" class="navbar-toggler btn btn-icon btn-sm rounde-circle d-lg-none" aria-label="Toggle navigation" aria-expanded="false" aria-controls="sidebarNav" data-toggle="collapse" data-target="#sidebarNav">-->
<!--              <span class="navbar-toggler-default">-->
<!--                <svg width="14" height="14" viewBox="0 0 18 18" xmlns="http://www.w3.org/2000/svg">-->
<!--                  <path fill="currentColor" d="M17.4,6.2H0.6C0.3,6.2,0,5.9,0,5.5V4.1c0-0.4,0.3-0.7,0.6-0.7h16.9c0.3,0,0.6,0.3,0.6,0.7v1.4C18,5.9,17.7,6.2,17.4,6.2z M17.4,14.1H0.6c-0.3,0-0.6-0.3-0.6-0.7V12c0-0.4,0.3-0.7,0.6-0.7h16.9c0.3,0,0.6,0.3,0.6,0.7v1.4C18,13.7,17.7,14.1,17.4,14.1z"></path>-->
<!--                </svg>-->
<!--              </span>-->
<!--                <span class="navbar-toggler-toggled">-->
<!--                <svg width="14" height="14" viewBox="0 0 18 18" xmlns="http://www.w3.org/2000/svg">-->
<!--                  <path fill="currentColor" d="M11.5,9.5l5-5c0.2-0.2,0.2-0.6-0.1-0.9l-1-1c-0.3-0.3-0.7-0.3-0.9-0.1l-5,5l-5-5C4.3,2.3,3.9,2.4,3.6,2.6l-1,1 C2.4,3.9,2.3,4.3,2.5,4.5l5,5l-5,5c-0.2,0.2-0.2,0.6,0.1,0.9l1,1c0.3,0.3,0.7,0.3,0.9,0.1l5-5l5,5c0.2,0.2,0.6,0.2,0.9-0.1l1-1 c0.3-0.3,0.3-0.7,0.1-0.9L11.5,9.5z"></path>-->
<!--                </svg>-->
<!--              </span>-->
<!--              </button>-->
              <!-- End Responsive Toggle Button -->
<!--            </div>-->
          </div>
        </div>
      </div>
      <div class="container space-1 space-top-lg-0 space-bottom-lg-2 mt-lg-n10">
        <div class="row">
          <div class="col-lg-3">
            <!-- Navbar -->
            <div class="navbar-expand-lg navbar-expand-lg-collapse-block navbar-light">
              <div id="sidebarNav" class="collapse navbar-collapse navbar-vertical">
                <!-- Card -->
                <div class="card mb-5">
                  <div class="card-body">
                    <!-- Avatar -->
                    <div class="d-none d-lg-block text-center mb-5">
                      <div class="avatar avatar-xxl avatar-circle mb-3">
                        <img class="avatar-img" :src="this.avatar_real" alt="Image Description">
                        <img class="avatar-status avatar-lg-status" src="../../assets/img/logos/ICACHI-logo.png" alt="" data-toggle="tooltip" data-placement="top" title="" data-original-title="Verified user">
                      </div>

                      <h4 class="card-title">{{this.name_real}}</h4>
                      <p class="card-text font-size-1">{{ this.email_real }}</p>
                    </div>
                    <!-- End Avatar -->

                    <!-- Nav -->
                    <h6 class="text-cap small">账户</h6>

                    <!-- List -->
                    <ul class="nav nav-sub nav-sm nav-tabs nav-list-y-2 mb-4">
                      <li class="nav-item">
                        <a class="nav-link active" disabled="true">
                          <i class="fas fa-id-card nav-icon"></i> 基本信息
                        </a>
                      </li>
                      <li class="nav-item" style="display: none">
                        <a class="nav-link " href="account-login-and-security.html">
                          <i class="fas fa-shield-alt nav-icon"></i> 登录 &amp; 安全
                        </a>
                      </li>
                    </ul>
                    <!-- End List -->


                    <div class="d-lg-none">
                      <div class="dropdown-divider"></div>

                      <!-- List -->
                      <ul class="nav nav-sub nav-sm nav-tabs nav-list-y-2">
                        <li class="nav-item">
                          <a class="nav-link text-primary" href="#">
                            <i class="fas fa-sign-out-alt nav-icon"></i> Log out
                          </a>
                        </li>
                      </ul>
                      <!-- End List -->
                    </div>
                    <!-- End Nav -->
                  </div>
                </div>
                <!-- End Card -->
              </div>
            </div>
            <!-- End Navbar -->
          </div>

          <div class="col-lg-9">
            <!-- Card -->
            <div class="card mb-3 mb-lg-5">
              <div class="card-header">
                <h5 class="card-title">基本信息</h5>
              </div>

              <!-- Body -->
              <div class="card-body">
                <div class="card-body">
                  <form class="card-body">
                    <div class="row mb-3">
                      <label for="inputEmail3" class="col-sm-4 col-form-label" style="margin: auto 0 auto 0">{{ $t('auth.avatar') }}</label>
                      <div class="col-sm-7">
                        <div>
                          <img :src=this.UserForm.avatar :visible.sync="dialogVisible" style="border-radius: 50%;width: 100px;height: 100px;float: top">
                          <div class="btn btn-outline-secondary file-attachment-btn " @click="$refs.file.click()" style="float: top;margin-left: 50px">上传头像
                            <input type="file" class="js-file-attach file-attachment-btn-label" id="avatarUploader" hidden @change="onFileChange">
                          </div>
                        </div>
                      </div>
                      <input type="file" hidden ref='file' @change="onFileChange">
                    </div>

                    <div class="row mb-3">
                      <label for="inputEmail3" class="col-sm-4 col-form-label">{{ $t('auth.EmailAddress') }}</label>
                      <div class="col-sm-7">
                        <input type="email" class="form-control" id="inputEmail3" :placeholder="''+this.UserForm.email" disabled>
                      </div>
                    </div>
                    <div class="row mb-3">
                      <label  class="col-sm-4 col-form-label">{{ $t('auth.MemberName') }}</label>
                      <div class="col-sm-7">
                        <input type="text" class="form-control" :placeholder="''+this.UserForm.name" v-model="this.UserForm.name">
                      </div>
                    </div>
                    <div class="row mb-3">
                      <label  class="col-sm-4 col-form-label">{{ $t('auth.Organization') }}</label>
                      <div class="col-sm-7">
                        <input type="text" class="form-control" :placeholder="''+this.UserForm.organization" v-model="this.UserForm.organization">
                      </div>
                    </div>
                    <div class="row mb-3">
                      <label  class="col-sm-4 col-form-label">{{ $t('auth.Position') }}</label>
                      <div class="col-sm-7">
                        <input type="text" class="form-control" :placeholder="''+this.UserForm.position" v-model="this.UserForm.position">
                      </div>
                    </div>
                    <div class="row mb-3">
                      <label  class="col-sm-4 col-form-label">{{ $t('auth.Phone') }}</label>
                      <div class="col-sm-7">
                        <input type="text" class="form-control" :placeholder="''+this.UserForm.phone" v-model="this.UserForm.phone">
                      </div>
                    </div>
                    <div class="row mb-3">
                      <label  class="col-sm-4 col-form-label">{{ $t('auth.Fields') }}</label>
                      <div class="col-sm-7">
                        <input type="text" class="form-control" :placeholder="''+this.UserForm.field" v-model="this.UserForm.field">
                      </div>
                    </div>
                    <div class="row mb-3">
                      <label  class="col-sm-4 col-form-label">是否已缴纳会费</label>
                      <div class="col-sm-7" style="line-height: 2.8">
                        <input type="radio" value="1" name="pay"  id="pay_yes"disabled :checked=this.ifPay_yes>
                        <label>是</label>
                        <input type="radio" value="2" name="pay" id="pay_no" disabled style="margin-left: 30px" :checked=this.ifPay_no>
                        <label>否</label>
                      </div>
                    </div>
                    <div class="row mb-3">
                      <label  class="col-sm-4 col-form-label">{{ $t('auth.Password') }}</label>
                      <div class="col-sm-7">
                        <a class="link-underline text-capitalize font-weight-normal"
                           href="/auth/recover" style="line-height: 2.8;">修改密码</a>
                      </div>
                    </div>
                  </form>
                </div>


              </div>
              <!-- End Body -->
<!--              justify-content-end-->
              <!-- Footer -->
              <div class="card-footer d-flex  justify-content-center">
                <button type="button" class="btn btn-outline-secondary" @click="change" style="margin-right: 5%;width: 47.5%">保存</button>
                <span class="mx-2"></span>
                <button type="button" class="btn btn-primary" @click="pay" style="width: 47.5%">成为会员</button>
              </div>
              <!-- End Footer -->
            </div>
            <!-- End Card -->

            <!-- Card -->
            <!-- End Card -->

            <!-- Card -->
            <!-- End Card -->

            <!-- 删除账户模块Card -->
<!--            <div class="card">-->
<!--              <div class="card-header">-->
<!--                <h5 class="card-title">永久删除您的帐户</h5>-->
<!--              </div>-->

<!--              &lt;!&ndash; Body &ndash;&gt;-->
<!--              <div class="card-body">-->
<!--                <p class="card-text">When you delete your account, you lose access to Front account services, and we permanently delete your personal data. You can cancel the deletion for 14 days.</p>-->

<!--                <div class="form-group">-->
<!--                  &lt;!&ndash; Custom Checkbox &ndash;&gt;-->
<!--                  <div class="custom-control custom-checkbox">-->
<!--                    <input type="checkbox" class="custom-control-input" id="deleteAccountCheckbox">-->
<!--                    <label class="custom-control-label" for="deleteAccountCheckbox">Confirm that I want to delete my account.</label>-->
<!--                  </div>-->
<!--                  &lt;!&ndash; End Custom Checkbox &ndash;&gt;-->
<!--                </div>-->

<!--                <div class="d-flex justify-content-end">-->
<!--                  <button type="submit" class="btn btn-danger transition-3d-hover">删除</button>-->
<!--                </div>-->
<!--              </div>-->
<!--              &lt;!&ndash; End Body &ndash;&gt;-->
<!--            </div>-->
            <!-- 删除账户模块结束End Card -->
          </div>
        </div>
        <!-- End Row -->
      </div>

      <!-- Blog Card Section -->
<!--      <div class="main mt-lg-n11" style="display: none">-->

<!--        <div class="container row justify-content-center " style="height: auto;margin: 20px auto;" >-->
<!--          <div class="justify-content-center  mb-5">-->
<!--            <div  style="margin-top: 1.1rem">-->
<!--          <img :src=this.UserForm.avatar :visible.sync="dialogVisible" style="border-radius: 50%;width: 100px;height: 100px;float: top">-->
<!--            <div class="btn btn-outline-secondary file-attachment-btn " @click="$refs.file.click()" style="float: top;display: block;margin-top: 10px">上传头像-->
<!--              <input type="file" class="js-file-attach file-attachment-btn-label" id="avatarUploader" hidden @change="onFileChange">-->
<!--            </div>-->
<!--            </div>-->
<!--            </div>-->
<!--          <input type="file" hidden ref='file' @change="onFileChange">-->


<!--&lt;!&ndash;          <div class="user_name">{{this.UserForm.name}}</div>&ndash;&gt;-->
<!--          <div class="user_info card mb-3 mb-lg-5">-->
<!--           <div class="card-body">-->
<!--            <form class="card-body">-->
<!--              <div class="row mb-3">-->
<!--                <label for="inputEmail3" class="col-sm-4 col-form-label">{{ $t('auth.EmailAddress') }}</label>-->
<!--                <div class="col-sm-7">-->
<!--                  <input type="email" class="form-control" id="inputEmail3" :placeholder="''+this.UserForm.email" disabled>-->
<!--                </div>-->
<!--              </div>-->
<!--              <div class="row mb-3">-->
<!--                <label  class="col-sm-4 col-form-label">{{ $t('auth.MemberName') }}</label>-->
<!--                <div class="col-sm-7">-->
<!--                  <input type="text" class="form-control" :placeholder="''+this.UserForm.name" v-model="this.UserForm.name">-->
<!--                </div>-->
<!--              </div>-->
<!--              <div class="row mb-3">-->
<!--                <label  class="col-sm-4 col-form-label">{{ $t('auth.Organization') }}</label>-->
<!--                <div class="col-sm-7">-->
<!--                  <input type="text" class="form-control" :placeholder="''+this.UserForm.organization" v-model="this.UserForm.organization">-->
<!--                </div>-->
<!--              </div>-->
<!--              <div class="row mb-3">-->
<!--                <label  class="col-sm-4 col-form-label">{{ $t('auth.Position') }}</label>-->
<!--                <div class="col-sm-7">-->
<!--                  <input type="text" class="form-control" :placeholder="''+this.UserForm.position" v-model="this.UserForm.position">-->
<!--                </div>-->
<!--              </div>-->
<!--              <div class="row mb-3">-->
<!--                <label  class="col-sm-4 col-form-label">{{ $t('auth.Phone') }}</label>-->
<!--                <div class="col-sm-7">-->
<!--                  <input type="text" class="form-control" :placeholder="''+this.UserForm.phone" v-model="this.UserForm.phone">-->
<!--                </div>-->
<!--              </div>-->
<!--              <div class="row mb-3">-->
<!--                <label  class="col-sm-4 col-form-label">{{ $t('auth.Fields') }}</label>-->
<!--                <div class="col-sm-7">-->
<!--                  <input type="text" class="form-control" :placeholder="''+this.UserForm.field" v-model="this.UserForm.field">-->
<!--                </div>-->
<!--              </div>-->
<!--              <div class="row mb-3">-->
<!--                <label  class="col-sm-4 col-form-label">是否已缴纳会费</label>-->
<!--                <div class="col-sm-7" style="line-height: 2.8">-->
<!--                  <input type="radio" value="1" name="pay"  id="pay_yes"disabled :checked=this.ifPay_yes>-->
<!--                  <label>是</label>-->
<!--                  <input type="radio" value="2" name="pay" id="pay_no" disabled style="margin-left: 30px" :checked=this.ifPay_no>-->
<!--                  <label>否</label>-->
<!--                </div>-->
<!--              </div>-->
<!--              <div class="row mb-3">-->
<!--                <label  class="col-sm-4 col-form-label">{{ $t('auth.Password') }}</label>-->
<!--                <div class="col-sm-7">-->
<!--                  <a class="link-underline text-capitalize font-weight-normal"-->
<!--                     href="/auth/recover" style="line-height: 2.8;">修改密码</a>-->
<!--                </div>-->
<!--              </div>-->
<!--              <div style="align-items: center;text-align: center">-->
<!--              <button type="button" class="btn btn-outline-secondary" @click="change" style="margin-right: 200px">保存</button>-->
<!--              <button type="button" class="btn btn-primary" @click="pay" >成为会员</button>-->
<!--              </div>-->
<!--            </form>-->
<!--</div>-->

<!--          </div>-->

<!--        </div>-->
<!--      </div>-->
      <div v-if="this.pay_check"
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
              <path
                fill="currentColor"
                d="M11.5,9.5l5-5c0.2-0.2,0.2-0.6-0.1-0.9l-1-1c-0.3-0.3-0.7-0.3-0.9-0.1l-5,5l-5-5C4.3,2.3,3.9,2.4,3.6,2.6l-1,1 C2.4,3.9,2.3,4.3,2.5,4.5l5,5l-5,5c-0.2,0.2-0.2,0.6,0.1,0.9l1,1c0.3,0.3,0.7,0.3,0.9,0.1l5-5l5,5c0.2,0.2,0.6,0.2,0.9-0.1l1-1 c0.3-0.3,0.3-0.7,0.1-0.9L11.5,9.5z"
              />

            </div>
            <!-- End Header -->
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
                    <div class="row justify-content-center">
                      <button @click="Later" type="button" class="btn  btn-outline-secondary transition-3d-hover" style="width: 42.5%;margin-right: 10%">稍后</button>
                      <button @click="PayNow" type="button" class="btn btn-primary  transition-3d-hover" style="margin-right:0px;width: 42.5%" >支付</button>
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


      <!-- End Blog Card Section -->
    </main>
    <!-- ========== END MAIN ========== -->
    <div class="modal fade" id="myModal_user" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
            <h4 class="modal-title" id="myModalLabel"></h4>
          </div>
          <div class="modal-body">{{msg_user}}</div>
          <div class="modal-footer">
            <!--            <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>-->
            <button type="button" class="btn btn-primary" data-dismiss="modal">关闭</button>
          </div>
        </div><!-- /.modal-content -->
      </div><!-- /.modal-dialog -->
    </div>

  </div>
</template>
<style>
.main{
  margin: 50px auto ;
  height: auto;
  overflow: hidden;
  align-items: center;
}
.user_avatar{
  height: 180px;
  margin: 10px auto;
}
/*.user_name{*/
/*  line-height: 100px;*/
/*  margin-left: 0;*/
/*  width: 100px;*/
/*  height: 100px;*/
/*  display: inline-block;*/
/*}*/
.user_info{
  float: right;
  margin-left: auto;
  background-color: #fff;
  max-width:1000px;
  min-width: 800px;
  height: auto;
}

</style>

<script>

// type为2表示新闻
export default {
  data () {
    return {
      msg_user:'',
      avatar_file:'',
      avatar_real:'',
      name_real:'',
      email_real:'',
      dialogVisible: false,//控制上传头像对话框
      name:'user_name',
      pay_check:false,
      ifPay_yes:false,
      ifPay_no:false,
      UserForm: {
        mid:'',
        avatar:'',
        email: '',
        // password: '',
        name: '',
        phone: '',
        position: '',
        organization: '',
        field: '',
        country: '1',
        membership: '',
        role:'',
        address:'1',
        postalCode:'1',
      },

    }
  },
  mounted() {
     // this.getUserInfo()
  },
  created () {
    this.getUserInfo();
  },
  methods:{
    getUserInfo () {
      //console.log(this.MainNewsTitle)
      let form = JSON.parse(window.localStorage.getItem('user_info'))
      //console.log(form)
      this.UserForm.mid = form.mid
      this.UserForm.name = form.name
      this.name_real = form.name
      this.email_real = form.email
      this.UserForm.email = form.email
      this.UserForm.membership = form.membership
      this.UserForm.phone = form.phone
      this.UserForm.field = form.field
      this.UserForm.organization = form.organization
      // this.UserForm.password = form.password
      this.UserForm.position = form.position
      this.UserForm.avatar = form.avatar
      this.avatar_real = form.avatar
      this.UserForm.role = form.role
      if (form.membership == 0) {
        // document.getElementById('pay_no').checked = true;
        this.ifPay_no = true;
      } else {
        // document.getElementById('pay_yes').checked = true;
        this.ifPay_yes = true;
      }

    },
    onFileChange(){
      // 处理预览图片
      const file=this.$refs.file
      // URL.createObjectURL()方法会根据传入的参数创建一个指向该参数对象的URL
      const blobData=window.URL.createObjectURL(file.files[0])
      // console.log(blobData)
      // 将地址赋值给previewImage
      const avatar_file = new window.File(
        [blobData],
        file.files[0].name,
        { type: file.files[0].type }
      );
      console.log(avatar_file)
      this.avatar_file = avatar_file
      this.$axios.post('/user/cos/upload', {
        param:{
          multipartFile:avatar_file,
        }
      })
        .then(res => {
          console.log(res.data)
        })
        .catch(err => {
          console.error(err)
        })
      this.UserForm.avatar=blobData
      console.log(this.UserForm.avatar)
      // 展示弹出层，预览用户选择图片
      this.dialogVisible=true
      // 解决选择相同文件不触发change事件问题
      this.$refs.file.value=''
    },
    pay(){
      this.pay_check = true
    },
    Later(){
      this.pay_check = false
    },
    PayNow(){
      var payType = document.getElementById('PaySelect')
      var index2 = payType.selectedIndex
      if(payType.options[index2].value==1)
      {
        // 45
        window.location.href = "https://buy.stripe.com/7sI6rs3u39HB0NyfZ3"
      }
      // 15
      else window.location.href = "https://buy.stripe.com/28o034fcLaLF8g06os"
    },
    LogOut () {
      console.log('退出')
      window.localStorage.clear()

      this.$router.push('/')
      // console.log($('#myModal'))
    },

    change(){
      let form = JSON.parse(window.localStorage.getItem('user_info'))
      console.log(this.UserForm.avatar)
      // 上传头像
      this.$axios.put('/user/member', {
        params: {
          mid:this.UserForm.mid,
          name:this.UserForm.name,
          organization: this.UserForm.organization,
          field: this.UserForm.field,
          phone:this.UserForm.phone,
          position:this.UserForm.position,
          country: this.UserForm.country,
          biography:'1',
          avatar:this.UserForm.avatar,
          address:this.UserForm.address,
          postalCode:this.UserForm.postalCode,

        },
      })
        .then(res => {
          this.msg_user = '修改成功！'
          $('#myModal_user').modal('show')
        })
        .catch(err => {
          console.error(err)
          this.msg_user = res.data.data.message
          $('#myModal_user').modal('show')
        })
    }
  }

}
</script>

