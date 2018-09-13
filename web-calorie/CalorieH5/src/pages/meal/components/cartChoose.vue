<template>
  <div>
    <div class="add-cart-buy">
      <img class="choose-all-img" src="" alt="">
      <div class="m-ft-24 m-hex">全选</div>
      <div class="m-ft-24 m-hex">合计
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
    .choose-all-img {

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
