<template>
  <div class="product-detail" :class="cart_show || params_show? 'active':''">
    <mt-swipe class="mt-swipe-imgs" :auto="0" :show-indicators="false" @change="handleChange">
      <mt-swipe-item v-for="item in productImgs" :key="item.id">
        <img :src="item" class="product-img">
      </mt-swipe-item>
    </mt-swipe>

    <div class="img-num">{{imgNum}}/{{productImgs.length}}</div>

    <div class="detail-row">
      <div class="product-name m-ft-30 m-grey-color m-ft-b tl">哑铃哑铃哑铃哑铃哑铃哑铃</div>
      <div class="product-price m-ft-30 m-price m-ft-b">￥168.05</div>
    </div>
    <div class="detail-row shadow-bottom">
      <div class="courier-price m-text">快递：0.00</div>
      <div class="sales-num m-text">月销：1526 笔</div>
      <div class="store-name m-text">健身器材1号店</div>
    </div>
    <div class="detail-row shadow-bottom">
      <div class="m-text">规格</div>
      <div class="color-choose-text m-grey-color tl">选择    颜色分类 重量</div>
      <img class="row-right-img" src="/static/images/arrow.png" alt="">
    </div>
    <div class="detail-row shadow-bottom">
      <div class="m-text">评分</div>
      <div class="score-imgs tl">
        <img class="score-img" :src="src" v-for="src in scoreList">
      </div>
      <div class="m-text">查看详情</div>
      <img class="row-right-img" src="/static/images/arrow.png" alt="">
    </div>

    <ul style="margin-bottom: 15%">
      <li v-for="brand in brandList">
        <img v-lazy="brand.img" class="detail-img">
      </li>
    </ul>

    <div class="add-cart-buy">
      <img class="cart-img" src="/static/images/purple/meal_shop_cart.png" @click="cartModal">
      <div class="add-cart m-text" @click="toParams">加入购物车</div>
      <div class="buy-now m-text" @click="submitOrder">立即购买</div>
    </div>

    <cart-choose v-if="cart_show" :cart_show="cart_show" @cartModal="cartModal" @toDetail="toDetail"></cart-choose>

    <product-params :params_show="params_show" @toParams="toParams"></product-params>
    <!--<add-cart-buy :cart_show="cart_show" @cartModal="cartModal" @toDetail="toDetail"></add-cart-buy>-->
  </div>
</template>

<script type="text/ecmascript-6">
import addCartBuy from './components/addCartBuy'
import cartChoose from './components/cartChoose'
import productParams from './components/productParams'
import common from '../../common/js/common';

  export default {
    name: "productDetail",
    data() {
      return {
        productImgs: ["http://upload.qulv.com/release/2018/04/12/15/04/f2nc2e1b.i0e.jpg", "http://img.52xie.com/images/upload/Image/201702/20170227133615072_948688.jpg",
          "http://09.imgmini.eastday.com/mobile/20180728/a42fa1e1b8858388f0d4b14abbb55d11_wmk.jpeg", "http://image.suning.cn/uimg/sop/commodity/208374587817637494699860_x.jpg",
          "http://p0.ifengimg.com/pmop/2018/0823/EDCBFAB32B5D51C73D01FDF08238CCE41CB41F08_size199_w750_h570.jpeg"],
        imgNum: 1,
        score: 4,
        scoreList: [],
        brandList: [
          {img: "http://pic1.win4000.com/wallpaper/8/599d1d60036a2.jpg"},
          {img: "http://bbsfiles.vivo.com.cn/vivobbs/attachment/forum/201804/25/145712qjc3gwcbtvgoct9w.jpg"},
          {img: "http://pic1.win4000.com/wallpaper/6/57eb314a3c143.jpg"},
          {img: "http://pic1.win4000.com/wallpaper/8/57eb322625b50.jpg"},
          {img: "http://pic1.win4000.com/wallpaper/6/59bcc06f60ecf.jpg"},
          {img: "http://pic1.win4000.com/wallpaper/6/59bcc080092c6.jpg"},
          {img: "http://pic1.win4000.com/wallpaper/6/59bcc07478a17.jpg"},
          {img: "http://pic1.win4000.com/wallpaper/6/59bcc08474821.jpg"}
        ],
        cart_show: false,
        params_show: false,
      }
    },
    components: { addCartBuy, cartChoose, productParams },
    methods: {
      // 切换轮播图时的事件
      handleChange(index) {
        this.imgNum = index + 1;
      },
      // 处理分数的星星数目
      scoreDo() {
        for (let i = 0; i < this.score; i ++) {
          this.scoreList.push("/static/images/star_full.png");
        }
        for (let j = 0; j < (5 - this.score); j ++) {
          this.scoreList.push("/static/images/star.png");
        }
      },
      // 关闭modal
      cartModal() {
        if(this.cart_show) {
          this.cart_show = false;
        }else if(!this.cart_show) {
          this.cart_show = true;
        }
      },
      // 关闭params_show_modal
      toParams() {
        if(this.params_show) {
          this.params_show = false;
        }else if(!this.params_show) {
          this.params_show = true;
        }
      },
      // 去餐品详情页
      toDetail(item) {
        // let pid = item.pid;
        this.cart_show = false;
      },
      // 立即购买
      submitOrder() {
        this.$router.push("/submitOrder");
      }
    },
    mounted() {
      let pid = this.$route.query.pid;
      // console.log(pid);

      this.scoreDo();
    },
    created() {
      // 设置页面title
      common.changeTitle("商品详情");
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";

  .product-detail {
    &.active {
      position: fixed;
    }
  }

  .mt-swipe-imgs {
    width: 750px;
    height: 570px;
    .product-img {
      width: 750px;
      height: 570px;
      box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.16);
    }
  }
  .img-num {
    width: 30px;
    height: 28px;
    font-size: 20px;
    padding: 1px 20px;
    opacity: 0.2;
    border-radius: 20px;
    background-color: @white;
    border: solid 1px #707070;
    position: absolute;
    top: 520px;
    right: 27px;
  }

  .detail-row {
    width: 690px;
    display: flex;
    padding: 25px 30px;
    .product-name {
      flex: 1;
      letter-spacing: 1.1px;
    }
    .product-price {

    }
    .courier-price {

    }
    .sales-num {
      flex: 1;
    }
    .store-name {

    }
    .color-choose-text {
      flex: 1;
      padding-left: 30px;
    }
    .score-imgs {
      flex: 1;
      padding-left: 20px;
      .score-img {
        width: 31px;
        height: 29px;
        padding-left: 10px;
      }
    }
    .row-right-img {
      width: 30px;
      height: 30px;
      padding: 2px 0 0 20px;
    }
    .m-text {
      font-size: 24px;
      color: @hex;
    }
  }
  .shadow-bottom {
    box-shadow: 0 4px 6px 0 rgba(0, 0, 0, 0.16);
  }

  .detail-img {
    width: 750px;
    height: auto;
    margin-bottom: -5px;
  }
  img[lazy=loading] {
    width: 750px;
    height: auto;
    margin: auto;
    background: url("/static/images/loading.gif") no-repeat fixed center;
  }

  .add-cart-buy {
    width: 100%;
    height: 77px;
    display: flex;
    padding-top: 13px;
    background-color: @white;
    border-top: 1px @hex solid;
    position: fixed;
    bottom: 0;
    .cart-img {
      width: 100px;
      height: 100px;
      position: absolute;
      left: 10px;
      bottom: 40px;
    }
    .add-cart {
      padding: 12px 65px;
      margin-left: 170px;
      border-radius: 40px 0 0 40px;
      background-image: linear-gradient(to right, @mainLeft, #5876E4);
    }
    .buy-now {
      padding: 12px 65px;
      border-radius: 0 40px 40px 0;
      background-image: linear-gradient(to right, #314ad1, @mainRight);
    }
    .m-text {
      width: 150px;
      height: 40px;
      font-size: 30px;
      color: @white;
    }
  }
</style>

