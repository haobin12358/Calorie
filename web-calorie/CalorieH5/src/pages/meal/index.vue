<template>
  <div>
    <div class="search-input m-ft-21 m-white tl">请输入商家/商品名称</div>
    <div class="address-choose m-ft-24 m-black tl">浙江工业大学（屏峰校区）</div>

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
    name: "index",
    data() {
      return {
        bannerList: [
          { url: 'http://image.suning.cn/uimg/sop/commodity/201312200307287693_x.jpg' },
          { url: 'http://img.zcool.cn/community/01a16c57fb3e1aa84a0d304fc108d5.jpg@2o.jpg' },
          { url: 'http://img2.ph.126.net/3rqi6A6btkU7FsOzet7eqQ==/6597246788028637442.jpg' }
          ],
      }
    },
    components: {},
    methods: {},
    created() {}
  }
</script>

<style lang="less" rel="stylesheet/less">
  @import "../../common/css/index";

  .search-input {
    height: 40px;
    padding: 15px;
    background-image: linear-gradient(to right, @mainLef, @mainRight);

  }
  .address-choose {
    position: absolute;
    top: 70px;
    z-index: 1000;
    width: 730px;
    opacity: 0.3;
    padding: 10px;
    background-color: @white;
    /*border: 2px red solid;*/
  }
  .mt-swipe-box {
    box-shadow: 0 5px 6px 0 rgba(0, 0, 0, 0.16);
  }
</style>
