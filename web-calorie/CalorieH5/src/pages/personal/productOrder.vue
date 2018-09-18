<template>
  <div>
    <navbar class="nav-bar" :list="nav_list" @navClick="navClick"></navbar>

    <div class="order-list">
      <div class="order-box" v-for="item in orderList">
        <img class="store-img" :src="item.storeImg" alt="">

        <div class="order-box-right">
          <div class="right-row-one">
            <div class="store-name m-ft-30 m-grey-color">{{item.storeName}}</div>
            <img class="more-img" src="/static/images/arrow.png" alt="">
            <div class="order-status m-ft-24 m-hex-grey tr">{{item.status}}</div>
          </div>

          <div class="product-box m-ft-24 m-hex-grey" v-for="product in item.productList">
            <div>{{product.productName}}</div>
            <div>x {{product.num}}</div>
          </div>
          <div class="product-total m-ft-21 m-grey-color tr">
            共{{item.count}}件商品，实付<span class="m-black">￥{{item.price}}</span>元
          </div>

          <div class="order-btns m-ft-24">
            <div class="to-evaluation-btn m-border-color">去评价</div>
            <div class="again-order-btn m-white">再来一单</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import navbar from '../../components/common/navbar'
  import common from '../../common/js/common'
  export default {
    name: "productOrder",
    data() {
        return {
          nav_list: [
            { click: true, name: "全部" },
            { click: false, name: "待接单" },
            { click: false, name: "派送中" },
            { click: false, name: "已完成" },
            { click: false, name: "已取消" }
          ],
          orderList: [
            { storeImg: "/static/images/product1.png", storeName: "某某便当", status: "订单派送中", productList: [
                { productName: "鳗鱼饭+汤", num: "2" }, { productName: "汤+鳗鱼饭", num: "1" }],
                count: "3", price: "39.52" },
            { storeImg: "/static/images/product1.png", storeName: "某某便当", status: "订单派送中", productList: [
                { productName: "鳗鱼饭+汤", num: "2" }, { productName: "汤+鳗鱼饭", num: "1" }],
              count: "3", price: "39.52" },
            { storeImg: "/static/images/product1.png", storeName: "某某便当", status: "订单派送中", productList: [
                { productName: "鳗鱼饭+汤", num: "2" }, { productName: "汤+鳗鱼饭", num: "1" }],
              count: "3", price: "39.52" },
            { storeImg: "/static/images/product1.png", storeName: "某某便当", status: "订单派送中", productList: [
                { productName: "鳗鱼饭+汤", num: "2" }, { productName: "汤+鳗鱼饭", num: "1" }],
              count: "3", price: "39.52" }
          ]
        }
    },
    components: { navbar },
    methods: {
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

    },
    created() {
      // 设置页面title
      common.changeTitle("商品订单");
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";

  .nav-bar {
    width: 100%;
    position: fixed;
    top: 0;
    background-color: @white;
  }
  .order-list {
    .order-box {
      width: 700px;
      display: flex;
      margin-bottom: 20px;
      padding: 30px 20px 50px 30px;
      box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.16);
      &:first-child {
        margin-top: 70px;
      }
      .store-img {
        width: 104px;
        height: 104px;
      }
      .order-box-right {
        flex: 1;
        .right-row-one {
          width: 556px;
          display: flex;
          margin: 30px 20px 0 20px;
          border-bottom: 1px #c7c7c7 solid;
          .store-name {
            padding: 0 30px 10px 0;
          }
          .more-img {
            width: 30px;
            height: 30px;
            padding-top: 8px;
          }
          .order-status {
            flex: 1;
            line-height: 45px;
          }
        }
        .product-box {
          width: 500px;
          display: flex;
          padding: 20px 0 0 80px;
          justify-content: space-between;
        }
        .product-total {
          padding: 20px 15px 50px 0;
        }
        .order-btns {
          width: 100%;
          display: flex;
          line-height: 55px;
          white-space: nowrap;
          .to-evaluation-btn {
            width: 240px;
            height: 50px;
            border-radius: 30px;
            border: solid 1px #576eea;
            margin: 0 30px 0 70px;
          }
          .again-order-btn {
            width: 240px;
            height: 50px;
            border-radius: 30px;
            background-image: linear-gradient(to right, @mainLeft, @mainRight);
          }
        }
      }
    }
  }
</style>
