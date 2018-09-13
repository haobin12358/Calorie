<template>
  <div>
    <div class="add-cart-buy">
      <img class="cart-img" src="/static/images/purple/meal_shop_cart.png" alt="">
      <div class="add-cart m-text">加入购物车</div>
      <div class="buy-now m-text">立即购买</div>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">

  export default {
    name: "addCartBuy",
    data() {
      return {

      }
    },
    methods: {

    },
    mounted() {

    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../../common/css/index";

  .add-cart-buy {
    .cart-img {
      width: 88px;
      height: 88px;
    }
    .add-cart {

    }
    .buy-now {

    }
    m-text {
      width: 150px;
      height: 40px;
      font-size: 30px;
      color: @white;
    }
  }
</style>
