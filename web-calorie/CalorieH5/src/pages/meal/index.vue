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
    <div class="menu-label">
      <menu-label :menuList="menuList"></menu-label>
    </div>
    <div class="text-row">
      <div class="row-left-text">在线点餐</div>
      <img class="row-right-img" src="/static/images/product1.png" alt="">
    </div>
    <div class="text-row">
      <div class="row-left-text">健康配送</div>
      <img class="row-right-img" src="/static/images/product1.png" alt="">
    </div>
    <div class="text-row">
      <div class="row-left-text">健康周边</div>
      <img class="row-right-img" src="/static/images/product1.png" alt="">
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  import menuLabel from '../../components/common/menuLabel'

  export default {
    name: "index",
    data() {
      return {
        bannerList: [
          { url: 'http://image.suning.cn/uimg/sop/commodity/201312200307287693_x.jpg' },
          { url: 'http://img.zcool.cn/community/01a16c57fb3e1aa84a0d304fc108d5.jpg@2o.jpg' },
          { url: 'http://img2.ph.126.net/3rqi6A6btkU7FsOzet7eqQ==/6597246788028637442.jpg' }
        ],
        menuList: [
          { icon: "/static/images/product1.png", name: "在线点餐" },
          { icon: "/static/images/product1.png", name: "健康配送" },
          { icon: "/static/images/product1.png", name: "健康周边" },
          { icon: "/static/images/product1.png", name: "健康卡" }
        ]
      }
    },
    components: { menuLabel },
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
  }
  .mt-swipe-box {
    margin-bottom: 130px;
    box-shadow: 0 5px 6px 0 rgba(0, 0, 0, 0.16);
  }
  .menu-label {
    position: absolute;
    top: 360px;
  }
  .text-row {
    width: 100%;
    display: flex;
    .row-left-text {
      flex: 1;
      font-size: 30px;
      font-weight: bold;
      padding: 10px 0;
      margin-left: 45px;
      text-align: left;
      color: @greyColor;
    }
    .row-right-img {
      width: 30px;
      height: 30px;
      padding: 15px 30px;
    }
  }
</style>
