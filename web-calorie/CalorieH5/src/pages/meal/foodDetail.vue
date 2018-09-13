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

    <shopping-cart :cart_num_show="cart_num_show" :cart_total="cart_total" :total_price="total_price"
                   :cart_show="cart_show" :cartList="cartList" @toCart="toCart" @toOrder="toOrder" @toDetail="toDetail"></shopping-cart>

  </div>
</template>

<script type="text/ecmascript-6">
  import shoppingCart from './components/shoppingCart';

  export default {
    name: "foodDetail",
    data() {
      return {
        food: { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "草莓甜点", formula: "娃娃菜、大蒜、青红椒、猪肉泥", price: "10", oldPrice: "12.00",
          rate: "95.8", inventory: "10", num: "0", fid: "as24dfd" },
        cartList: [],
        scroll: false,
        cart_num_show: false,
        cart_total: 0,
        total_price: 0,
        cart_show: false
      }
    },
    components: { shoppingCart },
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
      // 查看购物车
      toCart() {
        if(this.cart_show) {
          this.cart_show = false;
          if(this.cart_total != 0) {
            this.cart_num_show = true;
          }
        }else if(!this.cart_show) {
          this.cart_show = true;
          this.cart_num_show = false;
        }
      },
      // 去餐品详情页
      toDetail(item) {
        console.log(item);
        let fid = item.fid;
        this.$router.push({path: "/foodDetail", query: { fid }});
      },
      // 去下单
      toOrder() {
        this.$router.push("/productOrder");
      }
    },
    mounted() {
      let fid = this.$route.query.fid;
      // console.log(fid);

      // 确定购物车角标数字和总价
      for(let i = 0; i < this.cartList.length; i ++) {
        this.cart_total = this.cart_total + Number(this.cartList[i].num);
        this.total_price = this.total_price + Number(this.cartList[i].num) * Number(this.cartList[i].price);
      }
      if(this.cart_total == 0) {
        this.cart_num_show = false;
      }
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
      background-color: #CBCBCB;
    }
    .food-price {
      padding: 0 60px 0 30px;
    }
    .food-old-price {
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
</style>
