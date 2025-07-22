<template>
  <div>
    <!-- ========== MAIN ========== -->
    <main id="content" role="main">

<!--      <homepage-hero :heroTitle="heroTitle" :heroSubTitle="heroSubTitle"></homepage-hero>-->
      <div style="width: auto;height: 150px"></div>

      <!-- Blogs Section -->
      <div class="container space-1 space-lg-1">
        <div class="row justify-content-lg-between">
          <resource-item v-for="(item,i) in source" :Resource_title="item.title" :Resource_content="item.content" :Resource_img="item.banner" :confirm="confirm" :Resource_link="item.refLink"></resource-item>
<!--         资源-->
<!--          <div class="col-lg-6">-->
<!--            &lt;!&ndash; Blog &ndash;&gt;-->
<!--            <article>-->
<!--              <a-->
<!--                class="-->
<!--                  card-->
<!--                  align-items-start-->
<!--                  flex-wrap flex-row-->
<!--                  min-h-300rem-->
<!--                  gradient-x-overlay-sm-white-->
<!--                  bg-img-hero-->
<!--                  rounded-lg-pseudo-->
<!--                  transition-3d-hover-->
<!--                  mb-7-->
<!--                "-->
<!--                @click="confirm(source[0].attachmentSet[0].url)"-->
<!--                style="background-image: url('../../../static/img/post/icachi-default.png')"-->
<!--              >-->
<!--                <div class="card-header border-0 bg-transparent w-100">-->
<!--                  <div class="media align-items-center">-->
<!--                    &lt;!&ndash; <span class="avatar avatar-sm avatar-circle mr-3">-->
<!--                      <img-->
<!--                        class="avatar-img"-->
<!--                        src="../../../static/img/committee/100x100/chen.png"-->
<!--                        alt="Image Description"-->
<!--                      />-->
<!--                    </span> &ndash;&gt;-->
<!--                    <div class="media-body">-->
<!--                      &lt;!&ndash; <span class="d-inline-block text-white font-weight-bold"-->
<!--                        >Aaron Larsson</span-->
<!--                      > &ndash;&gt;-->
<!--                      <small class="d-block text-white-70"></small>-->
<!--                    </div>-->
<!--                  </div>-->
<!--                </div>-->

<!--                <div class="card-footer border-0 bg-transparent mt-auto">-->
<!--                  <h3 class="h2 text-white">-->
<!--                    2019人机交互领域发展蓝皮书-->
<!--                  </h3>-->
<!--                  <p class="text-white-70 mb-0">-->
<!--                    2019年6月28日，伴随着世界华人华侨人机交互大会Chinese CHI 2019在厦门大学科学与艺术中心开幕，国内首份人机交互领域发展蓝皮书也同期发布。-->
<!--                  </p>-->
<!--                </div>-->
<!--              </a>-->
<!--            </article>-->
<!--            &lt;!&ndash; End Blog &ndash;&gt;-->

<!--            &lt;!&ndash; Sticky Block End Point &ndash;&gt;-->
<!--            <div id="stickyBlockEndPoint"></div>-->
<!--          </div>-->
<!--          <div class="col-lg-6">-->
<!--            &lt;!&ndash; Blog &ndash;&gt;-->
<!--            <article>-->
<!--              <a-->
<!--                class="-->
<!--                  card-->
<!--                  align-items-start-->
<!--                  flex-wrap flex-row-->
<!--                  min-h-300rem-->
<!--                  gradient-x-overlay-sm-white-->
<!--                  bg-img-hero-->
<!--                  rounded-lg-pseudo-->
<!--                  transition-3d-hover-->
<!--                  mb-7-->
<!--                "-->
<!--                @click="confirm(source[0].attachmentSet[0].url)"-->
<!--                style="background-image: url('https://pic1.zhimg.com/v2-f82f5a2fd910f0094b16697413980367_1440w.jpg?source=172ae18b')"-->
<!--              >-->
<!--                <div class="card-header border-0 bg-transparent w-100">-->
<!--                  <div class="media align-items-center">-->
<!--                    &lt;!&ndash; <span class="avatar avatar-sm avatar-circle mr-3">-->
<!--                      <img-->
<!--                        class="avatar-img"-->
<!--                        src="../../../static/img/committee/100x100/chen.png"-->
<!--                        alt="Image Description"-->
<!--                      />-->
<!--                    </span> &ndash;&gt;-->
<!--                    <div class="media-body">-->
<!--                      &lt;!&ndash; <span class="d-inline-block text-white font-weight-bold"-->
<!--                        >Aaron Larsson</span-->
<!--                      > &ndash;&gt;-->
<!--                      <small class="d-block text-white-70"></small>-->
<!--                    </div>-->
<!--                  </div>-->
<!--                </div>-->

<!--                <div class="card-footer border-0 bg-transparent mt-auto">-->
<!--                  <h3 class="h2 text-white">-->
<!--                    ICACHI 云论坛系列笔记-->
<!--                  </h3>-->
<!--                  <p class="text-white-70 mb-0">-->
<!--                    讲座笔记| ICACHI 云论坛系列第三期：面向未来的物联网交互技术-->
<!--                  </p>-->
<!--                </div>-->
<!--              </a>-->
<!--            </article>-->
<!--            &lt;!&ndash; End Blog &ndash;&gt;-->

<!--            &lt;!&ndash; Sticky Block End Point &ndash;&gt;-->
<!--            <div id="stickyBlockEndPoint1"></div>-->
<!--          </div>-->

<!--          资源结束-->
<!--          <div class="col-lg-3">-->
<!--            <div class="mb-7">-->
<!--              <div class="mb-3">-->
<!--                <h3>Newsletter</h3>-->
<!--              </div>-->

<!--              &lt;!&ndash; Form &ndash;&gt;-->
<!--              <form class="js-validate mb-2">-->
<!--                <label class="sr-only" for="subscribeSr">Subscribe</label>-->
<!--                <div class="input-group input-group-flush mb-3">-->
<!--                  <input-->
<!--                    type="email"-->
<!--                    class="form-control form-control-sm"-->
<!--                    name="email"-->
<!--                    id="subscribeSr"-->
<!--                    placeholder="Your email"-->
<!--                    aria-label="Your email"-->
<!--                    required-->
<!--                    data-msg="Please enter a valid email address."-->
<!--                  />-->
<!--                </div>-->
<!--                <button type="submit" class="btn btn-sm btn-primary btn-block">-->
<!--                  Subscribe-->
<!--                </button>-->
<!--              </form>-->
<!--              &lt;!&ndash; End Form &ndash;&gt;-->

<!--              <p class="small">-->
<!--                Get special offers on the latest developments from Front.-->
<!--              </p>-->
<!--            </div>-->

<!--            <div class="mb-7">-->
<!--              <div class="mb-3">-->
<!--                <h3>Paper Template</h3>-->
<!--              </div>-->

<!--              &lt;!&ndash; Blog &ndash;&gt;-->
<!--              <article class="mb-3">-->
<!--                <a class="card card-frame p-3" href="#">-->
<!--                  <div class="media align-items-center">-->
<!--                    <div class="media-body mr-2">-->
<!--                      <h4 class="h6 mb-0">Chinese CHI Template</h4>-->
<!--                      <span class="d-block font-size-1 text-body"-->
<!--                      >Feb 08, 2020</span-->
<!--                      >-->
<!--                    </div>-->
<!--                    <i class="fas fa-angle-right"></i>-->
<!--                  </div>-->
<!--                </a>-->
<!--              </article>-->
<!--              &lt;!&ndash; End Blog &ndash;&gt;-->

<!--              &lt;!&ndash; Blog &ndash;&gt;-->
<!--              <article class="mb-3">-->
<!--                <a class="card card-frame p-3" href="#">-->
<!--                  <div class="media align-items-center">-->
<!--                    <div class="media-body mr-2">-->
<!--                      <h4 class="h6 mb-0">Poster Template</h4>-->
<!--                      <span class="d-block font-size-1 text-body"-->
<!--                      >Feb 09, 2020</span-->
<!--                      >-->
<!--                    </div>-->
<!--                    <i class="fas fa-angle-right"></i>-->
<!--                  </div>-->
<!--                </a>-->
<!--              </article>-->
<!--              &lt;!&ndash; End Blog &ndash;&gt;-->

<!--              &lt;!&ndash; Blog &ndash;&gt;-->
<!--              <article class="mb-3">-->
<!--                <a class="card card-frame p-3" href="#">-->
<!--                  <div class="media align-items-center">-->
<!--                    <div class="media-body mr-2">-->
<!--                      <h4 class="h6 mb-0">Late Breaking Work</h4>-->
<!--                      <span class="d-block font-size-1 text-body"-->
<!--                      >Feb 10, 2020</span-->
<!--                      >-->
<!--                    </div>-->
<!--                    <i class="fas fa-angle-right"></i>-->
<!--                  </div>-->
<!--                </a>-->
<!--              </article>-->
<!--              &lt;!&ndash; End Blog &ndash;&gt;-->
<!--            </div>-->

<!--            &lt;!&ndash; Sticky Block Start Point &ndash;&gt;-->
<!--            <div id="stickyBlockStartPoint"></div>-->

<!--            <div-->
<!--              class="js-sticky-block"-->
<!--              data-hs-sticky-block-options='{-->
<!--                 "parentSelector": "#stickyBlockStartPoint",-->
<!--                 "breakpoint": "lg",-->
<!--                 "startPoint": "#stickyBlockStartPoint",-->
<!--                 "endPoint": "#stickyBlockEndPoint",-->
<!--                 "stickyOffsetTop": 40,-->
<!--                 "stickyOffsetBottom": 20-->
<!--               }'-->
<!--            >-->

<!--              <div class="mb-7">-->
<!--                <div class="mb-3">-->
<!--                  <h3>Tags</h3>-->
<!--                </div>-->

<!--                <a class="btn btn-xs btn-soft-secondary mb-1" href="#"-->
<!--                >Business</a-->
<!--                >-->
<!--                <a class="btn btn-xs btn-soft-secondary mb-1" href="#"-->
<!--                >Adventure</a-->
<!--                >-->
<!--                <a class="btn btn-xs btn-soft-secondary mb-1" href="#"-->
<!--                >Community</a-->
<!--                >-->
<!--                <a class="btn btn-xs btn-soft-secondary mb-1" href="#"-->
<!--                >Announcements</a-->
<!--                >-->
<!--                <a class="btn btn-xs btn-soft-secondary mb-1" href="#"-->
<!--                >Tutorials</a-->
<!--                >-->
<!--                <a class="btn btn-xs btn-soft-secondary mb-1" href="#"-->
<!--                >Resources</a-->
<!--                >-->
<!--                <a class="btn btn-xs btn-soft-secondary mb-1" href="#"-->
<!--                >Classic</a-->
<!--                >-->
<!--                <a class="btn btn-xs btn-soft-secondary mb-1" href="#"-->
<!--                >Photography</a-->
<!--                >-->
<!--                <a class="btn btn-xs btn-soft-secondary mb-1" href="#"-->
<!--                >Interview</a-->
<!--                >-->
<!--              </div>-->
<!--            </div>-->
<!--          </div>-->
        </div>
        <!-- Pagination -->
        <div id="page">
          <nav aria-label="Page navigation">
            <ul class="pagination mb-0">
              <li class="page-item" v-if="page>1">
                <a class="page-link"  aria-label="Next" @click="page--,pageClick()">
                  <span class="d-none d-sm-inline-block mr-1">上一页</span>
                  <span aria-hidden="true">&laquo;</span>
                </a>
              </li>
              <div v-for="(item,i) in all"  :key="item" >
                <li :class="{'page-item active':page==item  }" ><a class="page-link" @click="page=item,pageClick()" >{{item}}</a></li>
              </div>
              <!--            <li :class="{'page-item active':page==2}" ><a class="page-link" @click="page=2,pageClick()" >2</a></li>-->
              <!--            <li :class="{'page-item active':page==3}" ><a class="page-link" @click="page=3,pageClick()">3</a></li>-->
              <!--            <li :class="{'page-item active':page==4}" ><a class="page-link" @click="page=4,pageClick()">4</a></li>-->
              <!--            <li :class="{'page-item active':page==5}" ><a class="page-link" @click="page=5,pageClick()">5</a></li>-->
              <li class="page-item" v-if="page<all.length">
                <a class="page-link"  aria-label="Next" @click="page++,pageClick()">
                  <span class="d-none d-sm-inline-block mr-1">下一页</span>
                  <span aria-hidden="true">&raquo;</span>
                </a>
              </li>
            </ul>
          </nav>
        </div>
        <!--分页-->
<!--        &lt;!&ndash; Pagination &ndash;&gt;-->
<!--        <nav aria-label="Page navigation">-->
<!--          <ul class="pagination mb-0">-->
<!--            <li class="page-item active">-->
<!--              <a class="page-link" href="#">1</a>-->
<!--            </li>-->
<!--            <li class="page-item"><a class="page-link" href="#">2</a></li>-->
<!--            <li class="page-item disabled">-->
<!--              <a class="page-link" href="#">...</a>-->
<!--            </li>-->
<!--            <li class="page-item"><a class="page-link" href="#">5</a></li>-->
<!--            <li class="page-item">-->
<!--              <a class="page-link" href="#" aria-label="Next">-->
<!--                <span class="d-none d-sm-inline-block mr-1">Next</span>-->
<!--                <span aria-hidden="true">&raquo;</span>-->
<!--              </a>-->
<!--            </li>-->
<!--          </ul>-->
<!--        </nav>-->
<!--        &lt;!&ndash; End Pagination &ndash;&gt;-->
      </div>
      <!-- End Blogs Section -->
    </main>
    <!-- ========== END MAIN ========== -->

    <!-- 模态框（Modal） -->
    <div class="modal fade" id="myModal3" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
            <h4 class="modal-title" id="myModalLabel"></h4>
          </div>
          <div class="modal-body" v-model="msg3">{{msg3}}</div>
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
import router from '../../router'

export default {
  data () {
    return {
      msg3:'',
      heroTitle: 'resource.Resource',
      heroSubTitle: 'aboutus.InternationalChineseAssociationOfComputerHumanInteraction',
      source: [],
      page:1,
      pagesize:6,
      all:[],
      pageNumber:'',
      username_x:'',
    }
  },
  created () {
    this.getSource()
  },
  mounted() {
    this.username_x = window.localStorage.getItem('username')
  },
  methods: {
    getSource () {
      this.$axios.get('/public/post', {
        params: {
          type: 6,
          pageNum: 1,
          pageSize: 10,
          keyword:'',
          tgid:'',
        },
      })
        .then(res => {
          // console.log(res.data)
          this.source = res.data.data.list
          console.log(this.source)
          this.all = res.data.data.navigatepageNums//总共分了多少页
        })
        .catch(err => {
          console.error(err)
        })
    },
    confirm(url){
      console.log(url)
      console.log(this.username_x)
      console.log(window.localStorage)
      if (this.username_x!=null)
      {
        window.open(url,'_blank')
      }
      else {
        this.msg3 = '请登录!'
        $('#myModal3').modal('show')
      }
    },
    pageClick(){
//根据点击页数请求数据
      this.getMainNewsTitle(this.page);
      console.log(this.page);
    },

  }
}
</script>
