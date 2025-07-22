<template>
  <div>
    <!-- ========== MAIN ========== -->
    <main id="content" role="main">
      <!--设置属性-->
<!--      <homepage-hero :heroTitle="heroTitle" :heroSubTitle="heroSubTitle"></homepage-hero>-->
      <div style="width: auto; height: 100px;"></div>
      <!-- Blog Card Section -->
      <div class="container space-top-md-1 space-bottom-2 space-bottom-lg-1">
        <div class="row justify-content-lg-end align-items-lg-center mb-7" >
          <div class="col-lg-6 mb-5 mb-lg-0" style="display: none;">
            <!-- Tags -->
            <div class="d-sm-flex align-items-sm-center text-center text-sm-left">
              <span class="d-block mr-sm-3 mb-2 mb-sm-1">标签:</span>
              <a v-for="(item,i) in tags" class="btn btn-xs btn-soft-secondary btn-pill mx-sm-1 mb-1" href="javascript:;" :key="item" @click="getPointNews(tags[i].tgid)">{{ tags[i].name }}</a>
<!--              <a class="btn btn-xs btn-soft-secondary btn-pill mx-sm-1 mb-1" href="javascript:;" value="2">Health</a>-->
<!--              <a class="btn btn-xs btn-soft-secondary btn-pill mx-sm-1 mb-1" href="javascript:;" value="3">Environment</a>-->
<!--              <a class="btn btn-xs btn-soft-secondary btn-pill mx-sm-1 mb-1" href="javascript:;" value="4">Adventure</a>-->
            </div>
            <!-- End Tags -->
          </div>
<!--搜索文章模块-->
          <div class="col-lg-4 " >
            <!-- Input -->
            <form class="input-group input-group-sm input-group-merge input-group-flush" >
              <input type="search" class="form-control" placeholder="搜索文章" aria-label="搜索文章" v-model="key"
                     aria-describedby="searchLabel" @keyup.enter="getKeyNews">
              <input style="display: none">
              <div class="input-group-append">
                <div class="input-group-text" id="searchLabel">
                  <a class="btn btn-xs btn-icon btn-ghost-secondary">
                  <i class="fas fa-search" @click="getKeyNews"></i>
                  </a>
                </div>
              </div>
            </form>
            <!-- End Input -->
          </div>
        </div>

        <!-- Blog Card -->
        <article class="card mb-11" >
          <div class="row no-gutters">
            <div class="col-lg-8">
              <div class="position-relative overflow-hidden">
                <img class="card-img" :src="news[0].banner" alt="Image Description" loading="eager" data-src="../../../static/img/committee/100x100/icachi-avatar.png">
                <figure class="d-none d-lg-block">
                  <svg class="ie-curved-x position-absolute top-0 right-0 bottom-0 mr-n1"
                       xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" viewBox="0 0 100.1 1920" height="100%">
                    <path fill="#fff" d="M0,1920c0,0,93.4-934.4,0-1920h100.1v1920H0z"/>
                  </svg>
                </figure>
                <figure class="d-lg-none m-n1">
                  <svg class="ie-curved-y position-absolute right-0 bottom-0 left-0" xmlns="http://www.w3.org/2000/svg"
                       x="0px" y="0px" viewBox="0 0 1920 100.1">
                    <path fill="#fff" d="M0,0c0,0,934.4,93.4,1920,0v100.1H0L0,0z"/>
                  </svg>
                </figure>
              </div>
            </div>

            <div class="col-lg-4">
              <div class="card-body d-flex flex-column h-100 p-4 p-lg-5">
                <h2 @click="getNowNews(news[0].pid)" style="cursor: pointer">
                  <a class="text-inherit"  v-html="news[0].title"></a>
                  <!-- <button class="button" @click="getMainNewsTitle">修改新闻标题</button> -->
                </h2>
                <p v-html="news[0].subtitle"></p>
<!--                <p v-html="news[0].content.substr(0,130)+'...'"></p>-->
                <div class="media align-items-center mt-auto">
                  <div class="avatar-group">
                    <a class="avatar avatar-xs avatar-circle" href="#" data-toggle="tooltip" data-placement="top"
                       title="Aaron Larsson">
                      <img class="avatar-img" src="../../../static/img/committee/100x100/icachi-avatar.png"
                           alt="Image Description">
                    </a>
                    <!-- <a class="avatar avatar-xs avatar-circle" href="#" data-toggle="tooltip" data-placement="top" title="John O'nolan">
                      <img class="avatar-img" src="../../../static/img/committee/100x100/chen.png" alt="Image Description">
                    </a> -->
                  </div>
                  <div class="media-body d-flex justify-content-end text-muted font-size-1 ml-2"
                       v-text="news[0].createTime.substr(0,10)">
                    July 15
                  </div>
                </div>
              </div>
            </div>
          </div>
        </article>
        <!-- End Blog Card -->

        <div class="row mb-3" v-if="this.page==1">
          <!--          <news-item v-for="(item,i) in news" :NewsTitle="item.title" :NewsImg="item.banner" :NewsSrc="item.refLink" :NewsDay="item.createTime"-->

          <news-item  v-for="(item,i) in news.slice(1,news.length)" :NewsTitle="item.title" :NewsSubtitle="item.subtitle" :NewsImg="item.banner"
                     :NewsDay="item.createTime.substr(0,10)" :pid="item.pid"
                      :key="item" ></news-item>
        </div>
        <div class="row mb-3" v-if="this.page>1">
          <!--          <news-item v-for="(item,i) in news" :NewsTitle="item.title" :NewsImg="item.banner" :NewsSrc="item.refLink" :NewsDay="item.createTime"-->

          <news-item v-for="(item,i) in news.slice(1,news.length)" :NewsTitle="item.title" :NewsSubtitle="item.subtitle" :NewsImg="item.banner"
                     :NewsDay="item.createTime.substr(0,10)" :pid="item.pid"
                      :key="item" ></news-item>
        </div>
          <!--  <div class="col-sm-6 col-lg-4 mb-3 mb-sm-8">  -->
          <!-- Blog Card -->
          <!--
          <article class="card h-100">
              <div class="card-img-top position-relative">
                <img class="card-img-top" :src="News2Img" alt="Image Description">
                <figure class="ie-curved-y position-absolute right-0 bottom-0 left-0 mb-n1">
                  <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" viewBox="0 0 1920 100.1">
                    <path fill="#fff" d="M0,0c0,0,934.4,93.4,1920,0v100.1H0L0,0z"/>
                  </svg>
                </figure>
              </div>

              <div class="card-body">
                <h3><a class="text-inherit" v-html="News2Title" :href="News2Src">ICACHI代表访问中国科协</a></h3>
                <p v-text="News2Content"></p>
              </div>

              <div class="card-footer border-0 pt-0">
                <div class="media align-items-center">
                  <div class="avatar-group">
                    <a class="avatar avatar-xs avatar-circle" href="#" data-toggle="tooltip" data-placement="top" title="Nataly Gaga">
                      <img class="avatar-img" src="../../../static/img/committee/100x100/icachi-avatar.png" alt="Image Description">
                    </a>
                  </div>
                  <div class="media-body d-flex justify-content-end text-muted font-size-1 ml-2" v-text="News2Day">
                    July 15
                  </div>
                </div>
              </div>
            </article>
            -->
          <!-- End Blog Card -->
          <!-- </div> -->


          <!--          <news-item :NewsTitle="news[2].title" :NewsImg="news[2].img" :NewsSrc="news[2].src" :NewsDay="news[2].date"-->
          <!--                     :NewsContent="news[2].content"></news-item>-->
          <!-- <div class="col-sm-6 col-lg-4 mb-3 mb-sm-8"> -->
          <!-- Blog Card -->
          <!--
          <article class="card bg-primary text-white h-100">
              <div class="card-body p-4 p-lg-5">
                <span class="badge badge-light py-2 px-3 mb-5 text-primary">Featured</span>
                <h3 class="h2"><a class="text-white" v-html="News3Title" :href="News3Src">2019人机交互领域发展蓝皮书在厦发布</a></h3>
                <p v-text="News3Content"></p>
              </div>
              <div class="card-footer bg-primary border-0 pt-0 px-5 pb-5">
                <div class="media align-items-center">
                  <div class="avatar-group">
                    <a class="avatar avatar-xs avatar-circle" href="#" data-toggle="tooltip" data-placement="top" title="Aaron Larsson">
                      <img class="avatar-img" src="../../../static/img/committee/100x100/icachi-avatar.png" alt="Image Description">
                    </a>
                  </div>
                  <div class="media-body d-flex justify-content-end text-white-70 font-size-1 ml-2" v-text="News3Day">
                    July 15
                  </div>
                </div>
              </div>
            </article>
            -->
          <!-- End Blog Card -->
          <!-- </div>  -->


          <!--          <news-item :NewsTitle="news[3].title" :NewsImg="news[3].img" :NewsSrc="news[3].src" :NewsDay="news[3].date"-->
          <!--                     :NewsContent="news[3].content"></news-item>-->


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
<!--        <div class="page-bar">-->
<!--          <ul>-->
<!--            <li v-if="page>1"><a v-on:click="page&#45;&#45;,pageClick()">上一页</a></li>-->
<!--            <li v-if="page==1"><a class="banclick">上一页</a></li>-->
<!--            <li v-for="index in indexs" v-bind:class="{ 'active': page == index}">-->
<!--              <a v-on:click="btnClick(index)">{{ index }}</a>-->
<!--            </li>-->
<!--            <li v-if="page!=all"><a v-on:click="page++,pageClick()">下一页</a></li>-->
<!--            <li v-if="page == all"><a class="banclick">下一页</a></li>-->
<!--            <li><a>共<i>{{all}}</i>页</a></li>-->
<!--          </ul>-->
<!--        </div>-->
        <!-- End Pagination -->
      </div>
      <!-- End Blog Card Section -->
    </main>
    <!-- ========== END MAIN ========== -->
<!--    模态框-->
    <div class="modal fade" id="myModal_news" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
            <h4 class="modal-title" id="myModalLabel"></h4>
          </div>
          <div class="modal-body">{{msg_news}}</div>
          <div class="modal-footer">
            <!--            <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>-->
            <button type="button" class="btn btn-primary" data-dismiss="modal">关闭</button>
          </div>
        </div><!-- /.modal-content -->
      </div><!-- /.modal-dialog -->
    </div>

  </div>
</template>

<script>
// type为2表示新闻
export default {
  data () {
    return {
      type: 2,
      heroTitle: 'newsroom.NewsRoom',
      heroSubTitle: 'aboutus.InternationalChineseAssociationOfComputerHumanInteraction',
      news: [],
      tags:[],
      page:1,
      pagesize:3,
      all:[],
      pageNumber:'',
      nowTag:'',
      key:'',
      msg_news:'',
    }
  },
  created () {
    this.getMainNewsTitle()
    this.getTags()
  },

  methods: {
    getTags(){
      this.$axios.get('/public/tag')
        .then(res => {
          console.log(res.data)
          this.tags = res.data.data
          console.log(this.tags)
        })
        .catch(err => {
          console.error(err)
        })
    },
    getMainNewsTitle (index) {
      //console.log(this.MainNewsTitle)
      this.$axios.get('/public/post', {
        params: {
          type: 2,
          pageNum: index,
          pageSize: 7,
        },
      })
        .then(res => {
          // console.log(res.data)
          this.news = res.data.data.list
          this.all = res.data.data.navigatepageNums//总共分了多少页

          console.log(res.data)
          console.log(this.all)
          //console.log(this.news)
        })
        .catch(err => {
          console.error(err)
        })
    },
    getPointNews(tid,index){
      this.$axios.get('/public/post',{
        params:{
          pageNum:index,
          pageSize:7,
          type:2,
          keyword:this.key,
          tgid:tid,
        }
      })
        .then(res => {
          console.log(res.data)
          this.news = res.data.data.list
          this.all = res.data.data.navigatepageNums//总共分了多少页
        })
        .catch(err => {
          console.log(err)
        })
    },
    //根据标签查询文章
    getTagNews (tgid) {
      //console.log(this.MainNewsTitle)
      this.$axios.get('/public/tag/'+tgid)
        .then(res => {
           console.log(res.data)
          this.news = res.data.data.postList
          this.all = res.data.data.postList.length///总共分了多少页
          console.log(this.news)
        })
        .catch(err => {
          console.log(err)
        })
    },

    //根据关键字查询文章
    getKeyNews () {
      console.log(this.key)
      this.$axios.get('/public/post',{
        params:{
          keyword:this.key,
          pageNum:1,
          pageSize:7,
          tgid:2,
          type:2,
        },
      })
        .then(res => {
          console.log(res.data)
          if(res.data.data.total==0)
          {
            this.msg_news = '暂无相关内容'
            $('#myModal_news').modal('show')
          }
          else {
            this.news = res.data.data.list
            this.all = res.data.data.navigatepageNums//总共分了多少页
          }
            console.log(res.data)

        })
        .catch(err => {
          console.log(err)
        })
    },

    // 点击链接跳转到新闻页
    getNowNews(pid){
      window.localStorage.setItem('newsPid', pid)
      window.location.href="/nownews"
    },
//分页
//     btnClick: function(data){//页码点击事件
//       if(data != this.page){
//         this.page = data
//       }
// //根据点击页数请求数据
//       this.getMainNewsTitle(this.page.toString());
//     },
    pageClick(){
//根据点击页数请求数据
      this.getMainNewsTitle(this.page);
      console.log(this.page);
    }
  },
//   computed: {
// //分页
//     indexs: function(){
//       var left = 1;
//       var right = this.all;
//       var ar = [];
//       if(this.all>= 5){
//         if(this.page > 3 && this.page < this.all-2){
//           left = this.page - 2
//           right = this.page + 2
//         }else{
//           if(this.page<=3){
//             left = 1
//             right = 5
//           }else{
//             right = this.all
//             left = this.all -4
//           }
//         }
//       }
//       while (left <= right){
//         ar.push(left)
//         left ++
//       }
//       return ar
//     }



}
</script>

