<template>
  <div>
    <div class="add-cart-buy">
      <img class="cart-img" src="/static/images/purple/meal_shop_cart.png" @click="cartModal">
      <div class="add-cart m-text">加入购物车</div>
      <div class="buy-now m-text" @click="submitOrder">立即购买</div>
    </div>

    <cart-choose v-if="cart_show" :cart_show="cart_show" @cartModal="cartModal" @toDetail="toDetail"></cart-choose>
  </div>
</template>

<script type="text/ecmascript-6">
  import cartChoose from './cartChoose'

  export default {
    name: "addCartBuy",
    data() {
      return {

      }
    },
    components: { cartChoose },
    props:{
      cart_show: { type: Boolean, default: false },
    },
    methods: {
      // 关闭modal
      cartModal() {
        this.$emit("cartModal");
      },
      // 去餐品详情页
      toDetail(item) {
        this.$emit('toDetail', item);
      },
      // 立即购买
      submitOrder() {
        this.$router.push("/submitOrder");
      }
    },
    mounted() {
      let pid = this.$route.query.pid;
      // console.log(pid);
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
