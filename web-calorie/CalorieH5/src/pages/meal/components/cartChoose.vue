<template>
  <div>
    <div class="m-modal" v-if="cart_show">
      <div class="m-modal-state">
        <div class="product-list">
          <div class="product-box" v-for="(item, index) in productList">
            <img class="choose-img" v-if="chooseAll" src="/static/images/purple/meal_check.png">
            <img class="choose-img" v-if="!chooseAll" src="/static/images/purple/meal_uncheck.png">
            <img class="product-img" src="/static/images/product1.png" alt="">
            <div class="row-right">
              <div class="row-one">
                <div class="product-name m-ft-24 m-grey-color tl">哑铃哑铃哑铃</div>
                <div class="m-ft-24 m-price tr">￥168.05</div>
              </div>
              <div class="row-one">
                <div class="product-info m-ft-24 m-hex">黑色/15kg</div>
              </div>
              <div class="row-one">
                <div class="right-row-quantity">
                  <img class="quantity-img" src="/static/images/purple/meal_minus.png" v-if="item.num != 0" @click.stop="quantityChange(index, 'min')">
                  <div class="product-quantity m-ft-24 m-grey-color m-ft-b" v-if="item.num != 0">{{item.num}}</div>
                  <img class="quantity-img" src="/static/images/purple/meal_plus.png" v-if="item.inventory != 0" @click.stop="quantityChange(index, 'plus')">
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="cart-choose">
          <img class="choose-all-img" v-if="chooseAll" src="/static/images/purple/meal_check.png">
          <img class="choose-all-img" v-if="!chooseAll" src="/static/images/purple/meal_uncheck.png">
          <div class="m-ft-24 m-hex">全选</div>
          <div class="total-price m-ft-24 m-hex">合计
            <span class="m-ft-30 m-price m-ft-b">￥1903.02</span>
          </div>
          <div class="buy-btn">立即购买</div>
        </div>
      </div>

      <div class="overlay" @click="cartModal"></div>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">

  export default {
    name: "cartChoose",
    data() {
      return {
        chooseAll: false,
        productList: [
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "草莓甜点", price: "9", oldPrice: "12.00", rate: "95.8", inventory: "5", num: "2", fid: "as24dfd" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "草莓甜点", price: "9", oldPrice: "12.00", rate: "95.8", inventory: "5", num: "2", fid: "as24dfd" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "草莓甜点", price: "9", oldPrice: "12.00", rate: "95.8", inventory: "5", num: "2", fid: "as24dfd" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "草莓甜点", price: "9", oldPrice: "12.00", rate: "95.8", inventory: "5", num: "2", fid: "as24dfd" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "草莓甜点", price: "9", oldPrice: "12.00", rate: "95.8", inventory: "5", num: "2", fid: "as24dfd" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "草莓甜点", price: "12.12", oldPrice: "12.00", rate: "95.8", inventory: "10", num: "2", fid: "as24dfd" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "草莓甜点", price: "15.14", oldPrice: "12.00", rate: "95.8", inventory: "0", num: "0", fid: "as24dfd" }
        ],
      }
    },
    props:{
      cart_show: { type: Boolean, default: false },
    },
    methods: {
      // 餐品数量变化
      quantityChange(index, operation) {
        console.log(index, operation);
        // this.$emit('quantityChange', index, operation);
      },
      cartModal() {
        this.$emit("cartModal");
      },
      // 去商品详情页
      toDetail(item) {
        console.log(item);
        // this.$emit('toDetail', item);
      }
    },
    mounted() {

    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../../common/css/index";

  .m-modal{
    .overlay {
      position: fixed;
      top: 0;
      right: 0;
      bottom: 0;
      left: 0;
      z-index: 1003;
    }
    .m-modal-state{
      width: 620px;
      min-height: 780px;
      max-height: 900px;
      overflow: scroll;
      overflow-x: hidden;
      z-index: 1004;
      position: fixed;
      bottom: 120px;
      margin-left: 65px;
      border-radius: 20px;
      background-color: @white;
      .product-list {
        margin-bottom: 290px;
        .product-box {
          width: 570px;
          display: flex;
          margin: 20px 25px 0 25px;
          align-items: center;
          box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.16);
          .choose-img {
            width: 25px;
            height: 25px;
            padding: 0 16px;
          }
          .product-img {
            width: 120px;
            height: 120px;
            padding: 15px 0;
          }
          .row-right {
            flex: 1;
            padding: 0 25px 0 30px;
            .row-one {
              width: 100%;
              display: flex;
              .product-name {
                flex: 1;
              }
              .product-info {
                padding: 5px 0;
              }
              .right-row-quantity {
                width: 100%;
                display: flex;
                justify-content: flex-end;
                .quantity-img {
                  width: 42px;
                  height: 42px;
                }
                .product-quantity {
                  width: 40px;
                  padding: 8px 15px;
                }
              }
            }
          }
        }
      }
      .cart-choose {
        width: 620px;
        display: flex;
        align-items: center;
        background-color: @white;
        border-top: 1px solid @hex;
        position: fixed;
        bottom: 120px;
        border-radius: 0 0 20px 0;
        .choose-all-img {
          width: 30px;
          height: 30px;
          padding: 0 20px;
        }
        .total-price {
          flex: 1;
          line-height: 90px;
        }
        .buy-btn {
          height: 40px;
          font-size: 30px;
          color: @white;
          white-space: normal;
          padding: 25px 70px;
          border-radius: 0 0 20px 0;
          background-image: linear-gradient(to right, @mainLef, @mainRight);
        }
      }
    }
  }

  /*滚动条样式*/
  ::-webkit-scrollbar {
    height: 0;
    width: 0;
  }
</style>
