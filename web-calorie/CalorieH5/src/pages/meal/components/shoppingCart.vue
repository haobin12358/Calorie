<template>
  <div>
    <div class="to-order">
      <div class="cart-product-box">
        <img class="cart-img" src="/static/images/purple/meal_shop_cart.png" @click="toCart">
        <div class="cart-product-num" v-if="cart_num_show">{{cart_total}}</div>
      </div>
      <div class="cart-text">合计</div>
      <div class="cart-price">￥{{total_price}}</div>
      <div class="to-order-btn" @click="toOrder">去 下 单</div>
    </div>

    <div class="m-modal" v-if="cart_show">
      <div class="m-modal-state">
        <div class="food-list-box" v-if="cart_total != 0">
          <food-list :foodList="cartList"></food-list>
        </div>
        <div class="food-list-box" v-if="cart_total == 0">
          <img class="null-cart-img" src="/static/images/purple/meal_shop_cart2.png" alt="">
          <div class="m-ft-24 m-grey-color">购物车空空如也哦~</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  export default {
    name: "shoppingCart",
    data() {
      return {

      }
    },
    props:{  },
    components: {  },
    methods: {

    },
    mounted() {

    }
  }
</script>

<style lang="less" rel="stylesheet/less">

</style>
