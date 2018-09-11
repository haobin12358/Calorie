<template>
  <div>
    <div class="mt-swipe-box">
      <mt-swipe :auto="15000">
        <mt-swipe-item v-for="item in bannerList" :key="item.id">
          <img :src="item.url" class="img">
        </mt-swipe-item>
      </mt-swipe>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  export default {
    name: "onlineOrder",
    data() {
      return {
        bannerList: [
          { url: 'http://image.suning.cn/uimg/sop/commodity/201312200307287693_x.jpg' },
          { url: 'http://img4.imgtn.bdimg.com/it/u=632938294,2120575488&fm=11&gp=0.jpg' },
          { url: 'http://img.zcool.cn/community/01a16c57fb3e1aa84a0d304fc108d5.jpg@2o.jpg' }
        ],
      }
    },
    components: {  },
    methods: {

    },
    mounted() {

    }
  }
</script>

<style lang="less" rel="stylesheet/less">
  @import "../../common/css/index";

  .mt-swipe-box {
    /*margin-bottom: 130px;*/
    height: 300px;
    box-shadow: 0 5px 6px 0 rgba(0, 0, 0, 0.16);
    .img {
      height: 300px;
    }
    .mint-swipe-indicators {
      top: 250px;
    }
  }
</style>
