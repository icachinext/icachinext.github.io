<template>
  <div>
    <!-- ========== MAIN ========== -->
    <main id="content" role="main">
      <!--设置属性-->
      <!--      <homepage-hero :heroTitle="heroTitle" :heroSubTitle="heroSubTitle"></homepage-hero>-->
      <div style="width: auto;height: 100px"></div>
      <div class="container space-top-3 space-bottom-2">
        <div class="w-lg-70 mx-lg-auto">
          <div class="mb-4">
            <h1 class="h2" style="text-align: center" v-html="this.heroTitle"></h1>
          </div>

          <!-- Author -->
          <div class="border-top border-bottom py-4 mb-5">
            <div class="row align-items-md-center">
              <div class="col-md-7 mb-5 mb-md-0">
                <div class="media align-items-center">
                  <div class="avatar avatar-circle">
                    <img class="avatar-img" src="../../assets/img/logos/ICACHI-logo.png" alt="发布者头像">
                  </div>
                  <div class="media-body font-size-1 ml-3">
                    <span class="h6">
                      <a disabled="true">ICACHI</a>
                    </span>
                    <span class="d-block text-muted" v-text="this.createTime.substr(0,10)"></span>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- End Author -->
        </div>
        <div class="w-lg-70 mx-lg-auto">
          <div class="bg-soft-primary border-0 rounded-lg text-center p-3 my-5" style="margin: 0 auto ;width: 60%;height: fit-content">
            <img class="rounded-lg img-fluid-2" :src="this.img"  alt="">
          </div>
          <div style="text-align: center;margin-top: 50px" class="card">
            <div class="card-body p-5" style="text-align: left;align-items: center"><p v-html="this.content"></p></div>
          </div>
        </div>
      </div>

      <!-- Blog Card Section -->
<!--      <div class="container space-top-md-1 space-bottom-2 space-bottom-lg-1">-->
<!--        <div class="row justify-content-lg-between align-items-lg-center mb-7">-->

<!--        </div>-->

<!--        &lt;!&ndash; Blog Card &ndash;&gt;-->
<!--        <article class="card mb-11" >-->
<!--          <div >-->
<!--            <div class="col-lg-12">-->
<!--              <h2 style="text-align: center" v-html="this.heroTitle">-->
<!--                &lt;!&ndash; <button class="button" @click="getMainNewsTitle">修改新闻标题</button> &ndash;&gt;-->
<!--              </h2>-->
<!--              <div class="position-relative overflow-hidden" style="align-items: center">-->
<!--                <div align="center"><img style="margin-left:auto;margin-top: 50px" :src="this.img" alt="Image Description"></div>-->

<!--                <div style="text-align: center;margin-top: 50px"><p v-html="this.content"></p></div>-->
<!--              </div>-->
<!--            </div>-->
<!--          </div>-->
<!--        </article>-->
<!--        &lt;!&ndash; End Blog Card &ndash;&gt;-->

<!--            </div>-->
      <!-- End Blog Card Section -->
    </main>
    <!-- ========== END MAIN ========== -->
  </div>
</template>
<style>
p>img{
  text-align: center;
  align-items: center;
  margin-left: 22.5%;
  margin-right: 22.5%;
}

</style>
<script>
// type为2表示新闻
export default {
  data () {
    return {
      heroTitle: '',
      img:'',
      content: '',
      createTime:'',
      N_pid:'',
    }
  },
  created () {
    this.N_pid = window.localStorage.getItem('newsPid')
    this.GET(this.N_pid)
  },

  methods: {
    GET(N_pid) {
      //console.log(this.MainNewsTitle)
      this.$axios.get('/public/post/'+N_pid)
        .then(res => {
           console.log(res.data)
          let message = res.data.data
           this.heroTitle = message.title
          this.content = message.content
          this.createTime = message.createTime
          this.img = message.banner
          // this.all = res.data.data.navigatepageNums//总共分了多少页
          //
          // console.log(res.data)
          // console.log(this.all)
          //console.log(this.news)
        })
        .catch(err => {
          console.log(err)
        })
    },
    getTagNews(tgid) {
      //console.log(this.MainNewsTitle)
      this.$axios.get('/public/tag/' + tgid)
        .then(res => {
          // console.log(res.data)
          this.news = res.data.data.postList
          console.log(this.news)
        })
        .catch(err => {
          console.error(err)
        })
    },
    // 点击链接跳转到新闻页
    getNowNews(tgid) {

    },


  }
}
</script>
