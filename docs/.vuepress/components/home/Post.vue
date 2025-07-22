<template>
  <div>
  <!-- ========== MAIN ========== -->
  <main id="content" role="main">
    <!-- Article Description Section -->
    <div class="container space-top-3 space-bottom-2">
      <div class="w-lg-60 mx-lg-auto">
        <div class="mb-4">
          <h1 class="h2" v-text="MainNewsTitle">Chinese CHI 2019第七届国际华人人机交互大会于厦大成功召开</h1>
        </div>

        <!-- Author -->
        <div class="border-top border-bottom py-4 mb-5">
          <div class="row align-items-md-center">
            <div class="col-md-7 mb-5 mb-md-0">
              <div class="media align-items-center">
                <div class="avatar avatar-circle">
                  <img class="avatar-img" src="../../../static/img/committee/100x100/icachi-avatar.png" alt="Image Description">
                </div>
                <div class="media-body font-size-1 ml-3">
                  <span class="h6"><a href="blog-profile.html">ICACHI</a> <button type="button" class="btn btn-xs btn-soft-primary font-weight-bold transition-3d-hover py-1 px-2 ml-1">Follow</button></span>
                  <span class="d-block text-muted" v-text="ReleaseTime">July 15, 2019</span>
                </div>
              </div>
            </div>
            <div class="col-md-5">
              <div class="d-flex justify-content-md-end align-items-center">
                <span class="d-block small font-weight-bold text-cap mr-2">Share:</span>

                <a class="btn btn-xs btn-icon btn-soft-secondary rounded-circle ml-2" href="#">
                  <i class="fab fa-facebook-f"></i>
                </a>
                <a class="btn btn-xs btn-icon btn-soft-secondary rounded-circle ml-2" href="#">
                  <i class="fab fa-twitter"></i>
                </a>
                <a class="btn btn-xs btn-icon btn-soft-secondary rounded-circle ml-2" href="#">
                  <i class="fab fa-weixin"></i>
                </a>
              </div>
            </div>
          </div>
        </div>
        <!-- End Author -->
      </div>

      <div class="w-lg-60 mx-lg-auto">
        <p v-text="NewsContent1">第七届Chinese CHI国际华人人机交互大会由世界华人华侨人机交互协会、厦门大学、与厦门市科学技术协会主办，中国科学技术协会、福建省科学技术协会作为指导单位，厦门市计算机学会承办，作为连接全球范围华人人机交互学科学者、学术界和产业界的重要会议，于2019年6月28日在厦门大学思明校区科学艺术中心隆重举办，本届大会主题为“Happiness（幸福）、Culture（文化）、Innovation（创新）”。</p>

        <img class="rounded-lg w-100 mt-2 mb-4" :src="img1" alt="Image Description">

        <p v-text="NewsContent2">6月28日上午8点半，大会在厦门大学信息学院姚俊峰教授的主持下正式开幕，开幕式的主要内容有厦门大学副校长江云宝教授致欢迎词，福建省科学技术协会国际部郑恒强部长、世界华人华侨人机交互协会会长华为加拿大诺亚方舟人机交互实验室负责人李维研究员、厦门市科学技术协会林秋松副主席、厦门市计算机学会副会长雷蕴奇教授致辞。</p>
      </div>

      <div class="w-lg-60 mx-lg-auto">
        <div class="card bg-img-hero bg-dark text-white text-center p-4 my-4" style="background-image: url(../../../static/svg/components/abstract-shapes-1.svg);">
          <h4 class="text-white mb-3">Like what you're reading? Subscribe to our top stories.</h4>

          <!-- Form -->
          <form class="js-validate w-md-75 mx-md-auto">
            <div class="js-form-message">
              <div class="d-flex align-items-center">
                <label class="sr-only" for="subscribeSrArticle">Subscribe</label>
                <div class="input-group">
                  <input type="email" class="form-control" id="subscribeSrArticle" placeholder="Your email" aria-label="Your email">
                </div>
                <button type="submit" class="btn btn-light ml-3">Submit</button>
              </div>
            </div>
          </form>
          <!-- End Form -->
        </div>

        <p>Follow us on <a href="#">WeChat</a></p>

        <!-- Badges -->
        <div class="mt-5">
          <a class="btn btn-xs btn-soft-secondary mb-1" href="#">Ecommerce</a>
          <a class="btn btn-xs btn-soft-secondary mb-1" href="#">Website</a>
          <a class="btn btn-xs btn-soft-secondary mb-1" href="#">Bootstrap</a>
          <a class="btn btn-xs btn-soft-secondary mb-1" href="#">Startup</a>
          <a class="btn btn-xs btn-soft-secondary mb-1" href="#">Free</a>
        </div>
        <!-- End Badges -->

        <!-- Share -->
        <div class="row justify-content-sm-between align-items-sm-center mt-5">
          <div class="col-sm-6 mb-2 mb-sm-0">
            <div class="d-flex align-items-center">
              <span class="d-block small font-weight-bold text-cap mr-2">Share:</span>

              <a class="btn btn-xs btn-icon btn-ghost-secondary rounded-circle mr-2" href="#">
                <i class="fab fa-facebook-f"></i>
              </a>
              <a class="btn btn-xs btn-icon btn-ghost-secondary rounded-circle mr-2" href="#">
                <i class="fab fa-twitter"></i>
              </a>
              <a class="btn btn-xs btn-icon btn-ghost-secondary rounded-circle mr-2" href="#">
                <i class="fab fa-instagram"></i>
              </a>
              <a class="btn btn-xs btn-icon btn-ghost-secondary rounded-circle mr-2" href="#">
                <i class="fab fa-telegram"></i>
              </a>
            </div>
          </div>

          <div class="col-sm-6 text-sm-right">
            <a class="btn btn-xs btn-icon btn-soft-secondary rounded-circle mr-2" href="#" data-toggle="tooltip" data-placement="top" title="Bookmark story">
              <i class="far fa-bookmark"></i>
            </a>
            <a class="btn btn-xs btn-icon btn-soft-secondary rounded-circle" href="#" data-toggle="tooltip" data-placement="top" title="Report story">
              <i class="far fa-flag"></i>
            </a>
          </div>
        </div>
        <!-- End Share -->

        <!-- Author -->
        <div class="media align-items-center border-top border-bottom py-5 my-8">
          <div class="avatar avatar-circle avatar-xl">
            <img class="avatar-img" src="../../../static/img/committee/100x100/icachi-avatar.png" alt="Image Description">
          </div>
          <div class="media-body ml-3">
            <small class="d-block small font-weight-bold text-cap">Written by</small>
            <h3 class="mb-0"><a href="blog-profile.html">ICACHI</a> <button type="button" class="btn btn-xs btn-soft-primary font-weight-bold transition-3d-hover py-1 px-2 ml-1">Follow</button></h3>
            <p class="mb-0">Editor of ICACHI Media</p>
          </div>
        </div>
        <!-- End Author -->

        <div class="pt-2 mb-11">
          <div class="mb-4">
            <h3 v-text="CommentsNum">3 Comments</h3>
          </div>

          <ul class="list-unstyled">
            <!-- Comment -->
            <li class="mb-5">
              <div class="media align-items-center mb-2">
                <div class="avatar avatar-circle mr-3">
                  <img class="avatar-img" :src="img2" alt="Image Description">
                </div>
                <div class="media-body">
                  <div class="d-flex justify-content-between align-items-center">
                    <span class="h5 mb-0">Chen</span>
                    <small class="text-muted">1 day ago</small>
                  </div>
                </div>
              </div>

              <p v-text="Comment1">As a Special Education teacher this resonates so well with me. Fighting with gen ed teachers to flatten for the students with learning disabilities. It also confirms some things for me in my writing.</p>

              <a class="font-weight-bold" href="#">Reply</a>

              <ul class="list-unstyled mt-5">
                <!-- Comment -->
                <li class="mb-5">
                  <div class="border-left border-3 pl-4">
                    <div class="media align-items-center mb-2">
                      <div class="avatar avatar-circle mr-3">
                        <img class="avatar-img" src="../../../static/img/committee/100x100/icachi-avatar.png" alt="Image Description">
                      </div>
                      <div class="media-body">
                        <div class="d-flex justify-content-between align-items-center">
                          <span class="h5 mb-0">Chen</span>
                          <small class="text-muted">1 day ago</small>
                        </div>
                      </div>
                    </div>

                    <p>Love it Dave! We're all about keeping it up.</p>

                    <a class="font-weight-bold" href="#">Reply</a>
                  </div>
                </li>
                <!-- End Comment -->
              </ul>
            </li>
            <!-- End Comment -->

            <!-- Comment -->
            <li class="mb-5">
              <div class="media align-items-center mb-2">
                <div class="avatar avatar-circle mr-3">
                  <img class="avatar-img" src="../../../static/img/committee/100x100/chen.png" alt="Image Description">
                </div>
                <div class="media-body">
                  <div class="d-flex justify-content-between align-items-center">
                    <span class="h5 mb-0">Chen</span>
                    <small class="text-muted">2 days ago</small>
                  </div>
                </div>
              </div>

              <p v-text="Comment2">Since our attention spans seem to be shrinking by the day — keeping it simple is more important than ever.</p>

              <a class="font-weight-bold" href="#">Reply</a>
            </li>
            <!-- End Comment -->
          </ul>
        </div>

        <div class="mb-5">
          <h3>Post a comment</h3>
        </div>

        <!-- Form -->
        <form class="js-validate">
          <div class="form-row">
            <div class="col-sm-6 mb-sm-3">
              <div class="js-form-message form-group">
                <label class="input-label">Name</label>
                <input type="text" class="form-control" name="name" id="inputName" placeholder="Name" aria-label="Name" required
                       data-msg="Please enter your name.">
              </div>
            </div>

            <div class="col-sm-6 mb-sm-3">
              <div class="js-form-message form-group">
                <label class="input-label">Email</label>
                <input type="email" class="form-control" name="emailAddress" id="emailAddress" placeholder="Email address" aria-label="Email address" required
                       data-msg="Please enter a valid email address.">
              </div>
            </div>

            <div class="col-12 mb-sm-3">
              <div class="js-form-message form-group">
                <label class="input-label">Comment</label>
                <textarea class="form-control" rows="7" id="descriptionTextarea" placeholder="Comment" required
                          data-msg="Please enter your message."></textarea>
              </div>
            </div>
          </div>

          <div class="d-flex justify-content-center">
            <button type="submit" class="btn btn-primary btn-wide transition-3d-hover">Submit</button>
          </div>
        </form>
        <!-- End Form -->
      </div>
    </div>
    <!-- End Article Description Section -->

    <!-- Blog Card Section -->
    <div class="container">
      <div class="w-lg-75 border-top space-2 mx-lg-auto">
        <div class="mb-3 mb-sm-5">
          <h3>Related stories</h3>
        </div>

        <div class="row">
          <div class="col-md-6">
            <!-- Blog Card -->
            <article class="border-bottom h-100 py-5">
              <div class="row justify-content-between">
                <div class="col-6">
                  <a class="d-block small font-weight-bold text-cap mb-2" href="#">Product</a>
                  <h4 class="mb-0">
                    <a class="text-inherit" v-text="Story1Title" :href="Story1Src">Better is when everything works together</a>
                  </h4>
                </div>

                <div class="col-5">
                  <img class="img-fluid rounded" :src="Story1Img" alt="Image Description">
                </div>
              </div>
            </article>
            <!-- End Blog Card -->
          </div>

          <div class="col-md-6">
            <!-- Blog Card -->
            <article class="border-bottom h-100 py-5">
              <div class="row justify-content-between">
                <div class="col-6">
                  <a class="d-block small font-weight-bold text-cap mb-2" href="#">Tech</a>
                  <h4 class="mb-0">
                    <a class="text-inherit" v-text="Story2Title" :href="Story2Src">Should You Buy An Apple Pencil?</a>
                  </h4>
                </div>

                <div class="col-5">
                  <img class="img-fluid rounded" :src="Story2Img" alt="Image Description">
                </div>
              </div>
            </article>
            <!-- End Blog Card -->
          </div>

          <div class="col-md-6">
            <!-- Blog Card -->
            <article class="border-bottom h-100 py-5">
              <div class="row justify-content-between">
                <div class="col-6">
                  <a class="d-block small font-weight-bold text-cap mb-2" href="#">Product</a>
                  <h4 class="mb-0">
                    <a class="text-inherit" v-text="Story3Title" :href="Story3Src">This Watch gym partnerships give you perks for working out</a>
                  </h4>
                </div>

                <div class="col-5">
                  <img class="img-fluid rounded" :src="Story3Img" alt="Image Description">
                </div>
              </div>
            </article>
            <!-- End Blog Card -->
          </div>

          <div class="col-md-6">
            <!-- Blog Card -->
            <article class="border-bottom h-100 py-5">
              <div class="row justify-content-between">
                <div class="col-6">
                  <a class="d-block small font-weight-bold text-cap mb-2" href="#">Tech</a>
                  <h4 class="mb-0">
                    <a class="text-inherit" v-text="Story4Title" :href="Story4Src">Drone Company PrecisionHawk Names New CEO</a>
                  </h4>
                </div>

                <div class="col-5">
                  <img class="img-fluid rounded" :src="Story4Img" alt="Image Description">
                </div>
              </div>
            </article>
            <!-- End Blog Card -->
          </div>
        </div>
      </div>
    </div>
    <!-- End Blog Card Section -->
  </main>
  <!-- ========== END MAIN ========== -->
  </div>
</template>

<script>
export default {
  data () {
    return {
      title: 'Bylaws',
      subtitle: 'InternationalChineseAssociationOfComputerHumanInteraction',
      MainNewsTitle:'Chinese CHI 2019第七届国际华人人机交互大会于厦大成功召开',
      ReleaseTime:'July 15, 2019',
      NewsContent1:'第七届Chinese CHI国际华人人机交互大会由世界华人华侨人机交互协会、厦门大学、与厦门市科学技术协会主办，中国科学技术协会、福建省科学技术协会作为指导单位，厦门市计算机学会承办，作为连接全球范围华人人机交互学科学者、学术界和产业界的重要会议，于2019年6月28日在厦门大学思明校区科学艺术中心隆重举办，本届大会主题为“Happiness（幸福）、Culture（文化）、Innovation（创新）”。',
      NewsContent2:'6月28日上午8点半，大会在厦门大学信息学院姚俊峰教授的主持下正式开幕，开幕式的主要内容有厦门大学副校长江云宝教授致欢迎词，福建省科学技术协会国际部郑恒强部长、世界华人华侨人机交互协会会长华为加拿大诺亚方舟人机交互实验室负责人李维研究员、厦门市科学技术协会林秋松副主席、厦门市计算机学会副会长雷蕴奇教授致辞。',
      img1:'../../../static/img/post/news-1.jpg',
      img2:'../../../static/img/committee/100x100/chen.png',
      CommentsNum:'3 Comments',
      Comment1:'As a Special Education teacher this resonates so well with me. Fighting with gen ed teachers to flatten for the students with learning disabilities. It also confirms some things for me in my writing.',
      Comment2:'Since our attention spans seem to be shrinking by the day — keeping it simple is more important than ever.',
      Story1Title:'Better is when everything works together',
      Story1Src:'blog-single-article.html',
      Story1Img:'../../../static/img/post/news-2.png',
      Story2Title:'Should You Buy An Apple Pencil?',
      Story2Src:'../../../static/img/post/news-2.png',
      Story2Img:'../../../static/img/post/news-2.png',
      Story3Title:'This Watch gym partnerships give you perks for working out',
      Story3Src:'blog-single-article.html',
      Story3Img:'../../../static/img/post/news-2.png',
      Story4Title:'Drone Company PrecisionHawk Names New CEO',
      Story4Src:'blog-single-article.html',
      Story4Img:'../../../static/img/post/news-2.png',
      content: '<h2>第一章 总则</h2><br /><h4>第 1 条(名称及地址)</h4><p>(1) 本会的名称为世界华人华侨人机交互协会(英文名 International Chinese Association of Computer Human Interaction,简称「ICACHI」)。URL 为 http://www.icachi.org/</p><p>(2)本会的总部设在香港。协会地址: Prof. Grace Ngai, Department of Computing, Hong Kong Polytechnic University, Kowloon, Hong Kong</p><p>理事会成员 ML: board&commat;icachi.org</p><p>电话: +852 2766-7279, +81-887-57-2209</p><p>传真: +852 2774-0842, +81-887-57-2209</p><p>协会网址: www.icachi.org</p><p>秘书处: office&commat;icachi.org</p><p>全体会员 ML: members&commat;icachi.org</p><p>(3)本会在世界其他各地设协会的办事处。目前协会在北京和多伦多分别设有办事处。</p>'



    }
  }
}
</script>
