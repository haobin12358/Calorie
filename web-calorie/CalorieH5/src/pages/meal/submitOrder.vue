<template>
  <div>
    <div class="order-row">
      <img class="product-img" src="/static/images/product1.png" alt="">
      <div class="row-right">
        <div class="row-right-row">
          <div class="product-name m-ft-30 m-grey-color tl">哑铃哑铃哑铃哑铃哑铃哑铃哑铃哑铃哑铃哑铃哑铃哑铃哑铃哑铃</div>
          <div class="m-ft-24 m-price m-ft-b">￥1698.25</div>
        </div>
        <div class="product-info hex-text tl">黑色/15kg</div>
        <div class="greyC-text tr">x 1</div>
      </div>
    </div>

    <div class="order-row">
      <img class="wechat-pay-img" src="/static/images/wechat_pay.png" alt="">
      <div class="pay-text hex-text">微信支付</div>
      <img class="choose-img" src="/static/images/purple/meal_check_pay.png" alt="">
    </div>
    <div class="order-row">
      <img class="wechat-pay-img" src="/static/images/wechat_pay_blue.png" alt="">
      <div class="pay-text hex-text">优惠券</div>
      <img class="choose-img" src="/static/images/meal_uncheck.png" alt="">
    </div>

    <div class="order-row">
      <img class="pay-img" src="/static/images/pay_amount.png" alt="">
      <div class="pay-text hex-text">支付金额</div>
      <div class="pay-nums-text pay-num-text hex-text">运费：0</div>
      <div class="pay-num-text hex-text">合计：<span class="m-price">￥1698.25</span></div>
    </div>

    <div class="memo-box">
      <div class="hex-text tl">买家留言</div>
      <textarea class="memo-input greyC-text" cols="45" rows="3"></textarea>
    </div>

    <div class="address-box">
      <div class="hex-text tl">收件人</div>
      <div class="address-row">
        <div class="buyer-name greyC-text tl">居居女孩</div>
        <div class="greyC-text">15864446564</div>
      </div>
      <div class="address-row">
        <div class="address-text greyC-text tl">浙江工业大学（屏峰校区）家和西苑十四幢【默认】</div>
        <div class="m-ft-24 m-border-color">修改</div>
      </div>
    </div>

    <div class="pay-btn m-ft-38 m-white">支付订单</div>
  </div>
</template>

<script type="text/ecmascript-6">
  import common from '../../common/js/common';

  export default {
    name: "submitOrder",
    data() {
      return {

      }
    },
    components: {  },
    methods: {

    },
    mounted() {

    },
    created() {
      // 设置页面title
      common.changeTitle("提交订单");
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";

  .order-row {
    width: 660px;
    display: flex;
    padding: 25px 45px;
    box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.16);
  }
  .product-img {
    width: 185px;
    height: 185px;
  }
  .row-right {
    flex: 1;
    padding-left: 30px;
    .row-right-row {
      width: 100%;
      display: flex;
      .product-name {
        flex: 1;
        padding-right: 20px;
        display: -webkit-box;
        -webkit-box-orient: vertical;
        -webkit-line-clamp: 2;
        overflow: hidden;
      }
    }
    .product-info {
      padding: 10px 0 30px 0;
    }
  }
  .wechat-pay-img {
    width: 50px;
    height: 50px;
  }
  .pay-img {
    width: 50px;
    height: 50px;
  }
  .choose-img {
    width: 40px;
    height: 40px;
    padding-top: 5px;
  }
  .pay-nums-text {
    flex: 1;
    text-align: right;
    padding-right: 30px;
  }
  .pay-num-text {
    line-height: 50px;
  }
  .pay-text {
    flex: 1;
    text-align: left;
    line-height: 50px;
    padding-left: 30px;
  }
  .memo-box {
    padding: 26px 47px;
    box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.16);
    .memo-input {
      letter-spacing: 1.3px;
      margin-top: 20px;
    }
  }
  .address-box {
    margin-bottom: 200px;
    padding: 26px 47px;
    box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.16);
    .address-row {
      width: 100%;
      display: flex;
      padding-top: 20px;
      .buyer-name {
        flex: 1;
      }
      .address-text {
        flex: 1;
      }
    }
  }
  .pay-btn {
    width: 150px;
    height: 50px;
    padding: 25px 300px;
    white-space: nowrap;
    background-image: linear-gradient(to right, @mainLeft, @mainRight);
    position: fixed;
    bottom: 0;
  }
  .hex-text {
    font-size: 24px;
    color: @hex;
  }
  .greyC-text {
    font-size: 24px;
    color: @greyColor;
  }
</style>
