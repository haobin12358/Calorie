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
    width: 100%;
    height: 77px;
    display: flex;
    padding-top: 13px;
    background-color: @white;
    position: fixed;
    bottom: 0;
    .cart-img {
      width: 88px;
      height: 88px;
      position: absolute;
      left: 10px;
      bottom: 40px;
    }
    .add-cart {
      padding: 12px 65px;
      margin-left: 170px;
      border-radius: 40px 0 0 40px;
      background-image: linear-gradient(to right, @mainLef, #5876E4);
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
