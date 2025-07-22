<template>
    <div class="col-sm-6 col-lg-4 mb-3 mb-sm-8">
      <!-- Blog Card -->
      <article class="card h-100">
        <div class="position-relative">
          <img class="card-img-top" :src="NewsImg" alt="" loading="lazy">
          <figure class="ie-curved-y position-absolute right-0 bottom-0 left-0 m-n1">
            <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" viewBox="0 0 1920 100.1">
              <path fill="#fff" d="M0,0c0,0,934.4,93.4,1920,0v100.1H0L0,0z"/>
            </svg>
          </figure>
        </div>

        <div class="card-body">
          <h3 @click="get(pid)" style="cursor: pointer"><a class="text-inherit" v-html="NewsTitle" :href="NewsSrc"></a></h3>
          <p v-html="NewsSubtitle"></p>
<!--          <p v-html="NewsContent" style="display: none"></p>-->
        </div>

        <div class="card-footer border-0 pt-0">
          <div class="media align-items-center">
            <div class="avatar-group">
              <a class="avatar avatar-xs avatar-circle" href="#" data-toggle="tooltip" data-placement="top" title="Nataly Gaga">
                <img class="avatar-img" src="../../../static/img/committee/100x100/icachi-avatar.png" alt="">
              </a>
            </div>
            <div class="media-body d-flex justify-content-end text-muted font-size-1 ml-2" v-text="NewsDay">
            </div>
          </div>
        </div>
      </article>
      <!-- End Blog Card -->
    </div>
</template>

<script>
export default {
  // 接受父组件的值
  props: {
    NewsTitle: String,
    NewsSubtitle:String,
    NewsImg: String,
    NewsSrc: String,
    // NewsContent:String,
    NewsDay:String,
    pid:String,

  },
  methods:{
    get(PID){
      console.log(PID)
      console.log('texttext')
      window.localStorage.setItem('newsPid', PID)
      window.location.href="/nownews"
    }
  }
}
</script>
