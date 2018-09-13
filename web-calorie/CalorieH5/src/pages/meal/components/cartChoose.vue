<template>
  <div>
    <div class="cart-choose">
      <img class="choose-all-img" v-if="chooseAll" src="/static/images/purple/meal_check.png">
      <img class="choose-all-img" v-if="!chooseAll" src="/static/images/purple/meal_uncheck.png">
      <div class="choose-all-text m-ft-24 m-hex">全选</div>
      <div class="total-price m-ft-24 m-hex">合计
        <span class="m-ft-30 m-price m-ft-b">￥193.02</span>
      </div>
      <div class="buy-btn">立即购买</div>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">

  export default {
    name: "cartChoose",
    data() {
      return {
        chooseAll: false
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

  .cart-choose {
    width: 100%;
    display: flex;
    align-items: center;
    border-top: 1px solid @hex;
    .choose-all-img {
      width: 30px;
      height: 30px;
      padding: 0 30px;
    }
    .choose-all-text {

    }
    .total-price {
      flex: 1;
    }
    .buy-btn {
      height: 40px;
      font-size: 30px;
      color: @white;
      white-space: normal;
      padding: 25px 90px;
      background-image: linear-gradient(to right, @mainLef, @mainRight);
    }
  }
</style>
