<template>
  <div class="col-lg-6">
    <!-- Blog -->
    <article>
      <a
        class="
                  card
                  align-items-start
                  flex-wrap flex-row
                  min-h-300rem
                  gradient-x-overlay-sm-white
                  bg-img-hero
                  rounded-lg-pseudo
                  transition-3d-hover
                  mb-7
                "
        @click="confirm(Resource_link)" style="cursor: pointer"
        :style="{backgroundImage:'url(' +Resource_img+ ')'}"
      >
        <div class="card-header border-0 bg-transparent w-100">
          <div class="media align-items-center">
            <!-- <span class="avatar avatar-sm avatar-circle mr-3">
              <img
                class="avatar-img"
                src="../../../static/img/committee/100x100/chen.png"
                alt="Image Description"
              />
            </span> -->
            <div class="media-body">
              <!-- <span class="d-inline-block text-white font-weight-bold"
                >Aaron Larsson</span
              > -->
              <small class="d-block text-white-70"></small>
            </div>
          </div>
        </div>

        <div class="card-footer border-0 bg-transparent mt-auto">
          <h3 class="h2 text-white" v-html="Resource_title">

          </h3>
          <p class="text-white-70 mb-0" v-html="Resource_content">

          </p>
        </div>
      </a>
    </article>
    <!-- End Blog -->

    <!-- Sticky Block End Point -->
    <div id="stickyBlockEndPoint"></div>
    <div class="modal fade" id="myModal_resource" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
            <h4 class="modal-title" id="myModalLabel"></h4>
          </div>
          <div class="modal-body" v-model="msg_resource">{{msg_resource}}</div>
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
export default {
  // 接受父组件的值
  props: {
    Resource_title: String,
    Resource_img: String,
    Resource_link: String,
    Resource_content:String,
    //Resource_pid:String,
    //confirm:methods,

  },
  data(){
    return{
      msg_resource:'请登录！',
    }
  },
   methods:{
    confirm(Resource_link)
    {
      let form = JSON.parse(window.localStorage.getItem('user_info'))
      if (window.localStorage.getItem('token')!=null)
      {
        if(form.membership!=1)
        {
          this.msg_resource = '您还不是会员，暂时无法下载!'
          $('#myModal_resource').modal('show')
        }
        else
        {
          this.msg_resource = '已开始下载'
          $('#myModal_resource').modal('show')
          window.open(Resource_link,'_blank')
        }
      }
      else {
        $('#myModal_resource').modal('show')
      }

      }
    },
  //   confirm(url){
  //     console.log(url)
  //     console.log(window.localStorage)
  //     if (window.localStorage.getItem('token')!=null)
  //     {
  //       window.open(url,'_blank')
  //     }
  //     else {
  //       this.msg3 = '请登录!'
  //       $('#myModal3').modal('show')
  //     }
  //   },
}
</script>
