<template>
  <div>
    <div class="search-input m-ft-21 m-white tl">
      <img class="row-img" src="/static/images/magnifier.png" alt="">
      <div>请输入商家/商品名称</div>
    </div>
    <div class="mt-swipe-box">
      <mt-swipe :auto="15000">
        <mt-swipe-item v-for="item in bannerList" :key="item.id">
          <img :src="item.url" class="img">
        </mt-swipe-item>
      </mt-swipe>
    </div>

    <navbar :list="nav_list" @navClick="navClick"></navbar>

    <div class="text-row">
      <div class="row-left-text">在线点餐</div>
      <img class="row-right-img" src="/static/images/arrow.png" alt="">
    </div>
    <div class="online-order">
      <ul class="product-list">
        <li class="product-box" v-for="item in onlineList">
          <img class="product-img" :src="item.src" alt="">
          <div class="product-bottom">
            <div class="product-name m-ft-24 m-grey-color tl">{{item.name}}</div>
            <div class="product-price">￥{{item.price}}</div>
          </div>
        </li>
      </ul>
    </div>
    <div class="text-row">
      <div class="row-left-text">健康配送</div>
      <img class="row-right-img" src="/static/images/arrow.png" alt="">
    </div>
    <div class="online-order">
      <ul class="product-list">
        <li class="health-box" v-for="item in healthList">
          <img class="health-img" :src="item.src" alt="">
          <div class="health-name m-ft-24 m-grey-color tl">{{item.name}}</div>
          <div class="health-bottom">
            <div class="health-price m-ft-24 m-price tl">￥{{item.price}}</div>
            <div class="bottom-btn">快捷下单</div>
          </div>
        </li>
      </ul>
    </div>
    <div class="text-row">
      <div class="row-left-text">健康周边</div>
      <img class="row-right-img" src="/static/images/arrow.png" alt="">
    </div>
    <div class="surrounding-health">
      <ul class="surrounding-list">
        <li class="surrounding-box" v-for="item in surroundingList">
          <img class="surrounding-img" :src="item.src" alt="">
          <div class="surrounding-bottom">
            <div class="surrounding-name m-ft-24 m-grey-color tl">{{item.name}}</div>
            <div class="surrounding-price m-ft-24 m-price tl">￥{{item.price}}</div>
          </div>
          <div class="surrounding-bottom">
            <div class="surrounding-from m-ft-21 m-hex tl">{{item.from}}</div>
            <div class="bottom-btn">快捷下单</div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  import menuLabel from '../../components/common/menuLabel'
  import navbar from '../../components/common/navbar'
  import common from '../../common/js/common';

  export default {
    name: "healthSurrounding",
    data() {
      return {
        bannerList: [
          { url: 'http://image.suning.cn/uimg/sop/commodity/201312200307287693_x.jpg' },
          { url: 'http://img4.imgtn.bdimg.com/it/u=632938294,2120575488&fm=11&gp=0.jpg' },
          { url: 'http://img.zcool.cn/community/01a16c57fb3e1aa84a0d304fc108d5.jpg@2o.jpg' }
        ],
        nav_list: [
          { click: false, name: "户外运动" },
          { click: true, name: "健身设备" },
          { click: false, name: "健康果蔬" },
          { click: false, name: "其他营养" }
        ],
        onlineList: [
          { src: "/static/images/product1.png", name: "蒜泥娃娃菜", price: "800.0" },
          { src: "/static/images/product1.png", name: "蒜泥娃娃菜", price: "8.0" },
          { src: "/static/images/product1.png", name: "蒜泥娃娃菜", price: "8.0" },
          { src: "/static/images/product1.png", name: "蒜泥娃娃菜", price: "8.0" }
        ],
        healthList: [
          { src: "/static/images/product1.png", name: "鸡胸肉土豆泥沙拉", price: "800.0" },
          { src: "/static/images/product1.png", name: "鸡胸肉土豆泥沙拉", price: "8.0" },
          { src: "/static/images/product1.png", name: "蒜泥娃娃菜", price: "8.0" },
          { src: "/static/images/product1.png", name: "蒜泥娃娃菜", price: "8.0" }
        ],
        surroundingList: [
          { src: "/static/images/product1.png", name: "蒜泥娃娃菜", price: "800.0", from: "早安city" },
          { src: "/static/images/product1.png", name: "蒜泥娃娃菜", price: "8.0", from: "早安city" },
          { src: "/static/images/product1.png", name: "蒜泥娃娃菜", price: "8.0", from: "早安city" },
          { src: "/static/images/product1.png", name: "蒜泥娃娃菜", price: "8.0", from: "早安city" }
        ]
      }
    },
    components: { menuLabel, navbar },
    methods: {
      // 顶部四个btn跳转
      toPage(item) {
        this.$router.push('/' + item.url);
        // 设置页面title
        common.changeTitle(item.name);
      },
      // 点击导航栏
      navClick(v){
        console.log(v);
        let arr = this.nav_list;
        for(let i = 0; i < arr.length; i ++){
          arr[i].click = false;
        }
        arr[v].click = true;
        this.nav_list = [].concat(arr);
      },
    },
    mounted() {

    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";

  .search-input {
    width: 720px;
    height: 40px;
    display: flex;
    padding: 15px;
    line-height: 45px;
    background-image: linear-gradient(to right, @mainLef, @mainRight);
  }
  .row-img {
    width: 40px;
    height: 40px;
    padding-right: 10px;
  }
  .mt-swipe-box {
    /*margin-bottom: 130px;*/
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
  .online-order {
    .product-list {
      width: 100%;
      display: inline-block;
      white-space: nowrap;
      overflow-x: scroll;
      overflow-y: hidden;
      float: left;
      padding: 10px 0 5px 0;
      .product-box {
        display: inline-block;
        width: 231px;
        height: 305px;
        margin-right: 20px;
        border-radius: 20px;
        background-color: @white;
        box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.16);
        &:first-child {
          margin-left: 45px;
        }
        &:last-child {
          margin-right: 45px;
        }
        .product-img {
          width: 231px;
          height: 231px;
          padding-bottom: 15px;
          border-radius: 20px 20px 0 0;
        }
        .product-bottom {
          width: 100%;
          display: flex;
          .product-name {
            flex: 1;
            font-size: 24px;
            color: @greyColor;
            margin-left: 11px;
            text-align: left;
          }
          .product-price {
            font-size: 24px;
            color: @priceColor;
            margin-right: 11px;
          }
        }
      }
      .health-box {
        display: inline-block;
        height: 400px;
        margin-right: 20px;
        border-radius: 20px;
        background-color: @white;
        box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.16);
        &:first-child {
          margin-left: 45px;
        }
        &:last-child {
          margin-right: 45px;
        }
        .health-img {
          width: 280px;
          height: 289px;
          border-radius: 20px 20px 0 0;
        }
        .health-name {
          font-size: 24px;
          margin-left: 11px;
          color: @greyColor;
          padding-bottom: 15px;
        }
        .health-bottom {
          width: 100%;
          display: flex;
          .health-price {
            flex: 1;
            margin-left: 11px;
            line-height: 47px;
          }
        }
      }
    }
  }
  .bottom-btn {
    color: @white;
    font-size: 21px;
    padding: 6px 28px;
    margin-right: 15px;
    border-radius: 30px;
    background-image: linear-gradient(to right, @mainLef, @mainRight);
  }
  .surrounding-health {
    margin: 15px 0 0 40px;
    .surrounding-list {
      display: flex;
      flex-wrap: wrap;
      .surrounding-box {
        width: 325px;
        height: 500px;
        border-radius: 20px;
        margin: 0 20px 20px 0;
        background-color: #ffffff;
        box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.16);
        .surrounding-img {
          width: 325px;
          height: 356px;
          border-radius: 20px 20px 0 0;
        }
        .surrounding-bottom {
          width: 100%;
          display: flex;
          .surrounding-name {
            flex: 1;
            padding: 15px 0 30px 20px;
          }
          .surrounding-price {
            padding: 15px 15px 0 0;
          }
          .surrounding-from {
            flex: 1;
            margin-left: 20px;
            line-height: 47px;
          }
        }
      }
    }
  }
  /*滚动条样式*/
  ::-webkit-scrollbar {
    height: 0;
  }
</style>
