<template>
  <div>
    <!-- ========== MAIN ========== -->
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
            <h1>{{ $t("contacts." + title) }}</h1>
            <p>{{ $t("aboutus." + subtitle) }}</p>
          </div>
        </div>
      </div>
      <!-- End Hero Section -->

      <!-- Terms Content Section -->
      <div class="container space-2 space-bottom-lg-3">
        <div class="row">
          <div class="col-md-12 col-lg-12">
            <div id="intro" class="space-bottom-1" v-html="content"></div>
            <!-- <div id="mapcontainer"></div> -->
            <!-- Sticky Block End Point -->
            <div id="stickyBlockEndPoint"></div>
          </div>
        </div>
      </div>
      <!-- End Terms Content Section -->
    </main>
    <!-- ========== END MAIN ========== -->
  </div>
</template>

<script>
export default {
  data () {
    return {
      title: 'Contacts',
      subtitle: 'InternationalChineseAssociationOfComputerHumanInteraction',
      content: '<p>协会代表: Dr. Wei Li</p><p>协会地址: Prof. Grace Ngai, Department of Computing, Hong Kong Polytechnic University, Kowloon,Hong Kong</p><p>电话: +852 2766-7279, </p><p>传真: +852 2774-0842</p><br><p>协会网址: www.icachi.org</p><p>秘书处: office&commat;icachi.org</p><p>理事会成员 ML: board&commat;icachi.org</p><p>全体会员 ML: members&commat;icachi.org</p>'
    }
  }
}
</script>
