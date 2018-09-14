<template>
  <div>

    <div class="m-modal" v-if="params_show">
      <div class="m-modal-state">
        <div class="product-info">
          <div class="img-box">
            <img class="product-img" src="/static/images/product1.png" alt="">
            <img class="modal-close-img" src="/static/images/close.png" @click="toParams">
          </div>
          <div class="product-price m-ft-30 m-price">￥193.52</div>
        </div>

        <div class="params-row active">
          <div class="params-text m-text">颜色分类</div>
          <ul class="params-ul">
            <li class="params-li">红色</li>
            <li class="params-li">银色</li>
            <li class="params-li">银色</li>
            <li class="params-li">银色</li>
            <li class="params-li active">黑色</li>
          </ul>
        </div><div class="params-row">
        <div class="params-text m-text">颜色分类</div>
        <ul class="params-ul">
          <li class="params-li">红色</li>
          <li class="params-li">银色</li>
          <li class="params-li">银色</li>
          <li class="params-li">银色</li>
          <li class="params-li active">黑色</li>
        </ul>
      </div><div class="params-row">
        <div class="params-text m-text">颜色分类</div>
        <ul class="params-ul">
          <li class="params-li">红色</li>
          <li class="params-li">银色</li>
          <li class="params-li">银色</li>
          <li class="params-li">银色</li>
          <li class="params-li active">黑色</li>
        </ul>
      </div>

        <div class="params-row">
          <div class="params-text m-text">重量</div>
          <ul class="params-ul">
            <li class="params-li active">5kg</li>
            <li class="params-li">10kg</li>
            <li class="params-li">15kg</li>
          </ul>
        </div>

        <div class="params-row">
          <div class="params-text m-text">购买数量</div>
          <div class="right-row-quantity">
            <img class="quantity-img" src="/static/images/purple/meal_minus.png" @click.stop="quantityChange('min')">
            <div class="product-quantity m-ft-24 m-grey-color m-ft-b">5</div>
            <img class="quantity-img" src="/static/images/purple/meal_plus.png" @click.stop="quantityChange('plus')">
          </div>
        </div>

        <div class="btn-biv">
          <div class="params-done-btn" @click="toParams">确定</div>
        </div>

        <!--<div class="btn-biv">
          <div class="add-cart">加入购物车</div>
          <div class="buy-now">立即购买</div>
        </div>-->

      </div>
      <div class="overlay" @click="toParams"></div>
    </div>

  </div>
</template>

<script type="text/ecmascript-6">
  export default {
    name: "productParams",
    data() {
      return {

      }
    },
    props:{
      params_show: { type: Boolean, default: false },
    },
    methods: {
      // 关闭params_modal
      toParams() {
        this.$emit("toParams");
      },
      // 餐品数量变化
      quantityChange(operation) {
        console.log(operation);
        // this.$emit('quantityChange', index, operation);
      },
    },
    mounted() {

    },
    created() {

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
      opacity: 0.4;
      background-color: #DCDCDC;
    }
    .m-modal-state{
      width: 750px;
      height: 950px;
      overflow: scroll;
      overflow-x: hidden;
      z-index: 1004;
      position: fixed;
      bottom: 0;
      border-radius: 20px 20px 0 0;
      background-color: @white;
      .product-info {
        position: fixed;
        background-color: @white;
        .img-box {
          width: 100%;
          display: flex;
          .product-img {
            margin: 20px 180px 20px 260px;
            width: 230px;
            height: 230px;
            box-shadow: 0 5px 6px 0 rgba(0, 0, 0, 0.16);
          }
          .modal-close-img {
            width: 35px;
            height: 35px;
            margin: 20px;
          }
        }
        .product-price {
          margin-bottom: 10px;
        }
      }
      .params-row {
        margin: 0 65px;
        &.active {
          margin-top: 310px;
        }
        .params-text {
          text-align: left;
          padding: 20px 0 15px 0;
        }
        .params-ul {
          width: 100%;
          display: flex;
          flex-wrap: wrap;
          .params-li {
            width: 50px;
            height: 32px;
            font-size: 24px;
            padding: 4px 50px;
            margin-top: 15px;
            margin-right: 30px;
            line-height: 35px;
            color: @greyColor;
            border-radius: 30px;
            background-color: #d5d5d5;
            &.active {
              color: @white;
              background-color: @borderColor
            }
          }
        }
        .right-row-quantity {
          width: 100%;
          display: flex;
          justify-content: flex-end;
          margin-bottom: 120px;
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
      .btn-biv {
        width: 750px;
        height: 100px;
        background-color: @white;
        position: fixed;
        bottom: 0;
        .params-done-btn {
          width: 70px;
          height: 40px;
          font-size: 30px;
          color: @white;
          margin-left: 90px;
          margin-top: 15px;
          padding: 11px 250px;
          border-radius: 40px;
          background-image: linear-gradient(to right, @mainLeft, @mainRight);
        }
        .add-cart {

        }
        .buy-now {

        }
      }
    }
  }
  .m-text {
    font-size: 24px;
    color: @hex;
  }
  /*滚动条样式*/
  ::-webkit-scrollbar {
    height: 0;
    width: 0;
  }
</style>
