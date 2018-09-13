<template>
  <div>
    <img class="food-img" :src="food.src" alt="">

    <div class="food-name m-ft-30 m-grey-color">{{food.name}}</div>

    <div class="food-formula m-ft-24 m-grey-color tl">配方：{{food.formula}}</div>

    <div class="food-evaluation m-ft-20 m-hex">
      <div class="food-rate tl">好评率：{{food.rate}}%</div>
      <div>评价详情</div>
      <img class="row-right-img" src="/static/images/arrow.png" alt="">
    </div>

    <div class="food-box" :class="food.inventory == 0? 'active':''">
      <div class="food-price m-ft-28 m-price m-ft-b">￥{{food.price}}</div>
      <div class="food-old-price m-ft-22 m-hex tl">￥{{food.oldPrice}}</div>
      <div class="food-null-text m-ft-24 m-white">售罄</div>
      <div class="right-row">
        <div class="right-row-quantity">
          <img class="food-quantity-img" src="/static/images/purple/meal_minus.png" v-if="food.num != 0" @click="quantityChange('min')">
          <div class="food-quantity m-ft-24 m-grey-color m-ft-b" v-if="food.num != 0">{{food.num}}</div>
          <img class="food-quantity-img" src="/static/images/purple/meal_plus.png" v-if="food.inventory != 0" @click="quantityChange('plus')">
        </div>
      </div>
    </div>

    <div class="to-order">
      <div class="cart-product-box">
        <img class="cart-img" src="/static/images/purple/meal_shop_cart.png" alt="">
        <div class="cart-product-num" v-if="cart_total != 0">{{cart_total}}</div>
      </div>
      <div class="cart-text">合计</div>
      <div class="cart-price">￥{{total_price}}</div>
      <div class="to-order-btn" @click="toOrder">去 下 单</div>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">

  export default {
    name: "foodDetail",
    data() {
      return {
        food: { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "草莓甜点", formula: "娃娃菜、大蒜、青红椒、猪肉泥", price: "10", oldPrice: "12.00",
          rate: "95.8", inventory: "10", num: "0", fid: "as24dfd" },
        cart_total: 1,
        total_price: 0,
      }
    },
    components: {  },
    methods: {
      // 菜品数量变化
      quantityChange(operation) {
        if(operation == "min") {
          this.food.num = Number(this.food.num) - 1;

          this.cart_total -= 1;
        }else if(operation == "plus") {
          this.food.num = Number(this.food.num) + 1;
          this.cart_total += 1;
        }
      },
      // 去下单
      toOrder() {

      }
    },
    mounted() {
      let fid = this.$route.query.fid;
      // console.log(fid);
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";

  .food-img {
    width: 750px;
    height: 570px;
    padding-bottom: 20px;
  }
  .food-name {

  }
  .food-formula {
    padding: 28px 0 20px 30px;
  }
  .food-evaluation {
    width: 100%;
    display: flex;
    .food-rate {
      flex: 1;
      padding-left: 30px;
    }
    .row-right-img {
      width: 30px;
      height: 30px;
      padding: 5px 30px;
    }
  }

  .food-box {
    width: 100%;
    display: flex;
    padding: 20px 0;
    &.active {
      //opacity: 0.2;
      background-color: #CBCBCB;
    }
    .food-price {
      padding: 0 60px 0 30px;
    }
    .food-old-price {
      /*flex: 1;*/
      padding-top: 5px;
      text-decoration: line-through;
    }
    .food-null-text {
      flex: 1;
      text-align: left;
      padding-left: 40px;
    }
    .right-row {
      display: flex;
      padding-right: 30px;
      .right-row-quantity {
        width: 100%;
        display: flex;
        justify-content: flex-end;
        .food-quantity-img {
          width: 42px;
          height: 42px;
        }
        .food-quantity {
          width: 40px;
          padding: 8px 15px;
        }
      }
    }
  }

  .to-order {
    width: 100%;
    display: flex;
    background-color: @white;
    position: fixed;
    bottom: 0;
    .cart-product-box {
      .cart-img {
        width: 100px;
        height: 100px;
        position: absolute;
        top: -25px;
        left: 20px;
      }
      .cart-product-num {
        position: absolute;
        top: -30px;
        left: 80px;
        width: 17px;
        height: 17px;
        padding: 7px;
        font-size: 18px;
        line-height: 20px;
        color: @white;
        border-radius: 50%;
        background-color: @priceColor;
      }
    }
    .cart-text {
      padding: 0 20px 0 130px;
      font-size: 24px;
      color: @hex;
      line-height: 90px;
    }
    .cart-price {
      flex: 1;
      text-align: left;
      font-size: 30px;
      font-weight: bold;
      color: @priceColor;
      line-height: 90px;
    }
    .to-order-btn {
      height: 40px;
      font-size: 30px;
      color: @white;
      white-space: normal;
      padding: 25px 90px;
      background-image: linear-gradient(to right, @mainLef, @mainRight);
    }
  }
</style>
