<template>
  <div>
    <div class="product-content">
      <img class="store-img" src="http://www.foodmodel.com.hk/wp-content/uploads/2014/04/2-580x580.jpg" alt="">
      <div class="product-right">
        <div class="product-row-one">
          <div class="store-name m-ft-30 m-grey-color">家和食堂</div>
          <img class="row-right-img" src="/static/images/arrow.png" alt="">
        </div>
        <div class="product-row-two">
          <div class="product-row" v-for="item in productList">
            <div class="product-name m-text tl">{{item.name}}</div>
            <div class="product-quantity m-text">x {{item.num}}</div>
          </div>
        </div>
        <div class="product-row-three">
          <div class="coupons-text m-text tl">优惠券</div>
          <div class="coupons-name m-ft-24 m-price">-￥5</div>
          <!--<div class="coupons-name m-text">暂无可用</div>-->
          <img class="row-right-img" src="/static/images/arrow.png" alt="">
        </div>
        <div class="product-row-four">
          <div class="coupons-num m-text tr">已优惠￥5</div>
          <div class="real-pay m-text">实付<span class="m-ft-30 m-black">￥40.0</span>元</div>
        </div>
      </div>
    </div>

    <div class="buyer-info">
      <div class="info-row">
        <div class="info-text">取餐方式：</div>
        <div class="row-right-one info-text">送餐上门</div>
      </div>
      <div class="info-row">
        <div class="info-text">送餐时间：</div>
        <div class="row-right-two">
          <div class="time-text info-text">11:00-11:30</div>
          <img class="drop-down-img" src="/static/images/purple/triangle.png" alt="">
        </div>
      </div>
      <div class="info-row">
        <div class="info-text">联系电话：</div>
        <div class="row-right-three">
          <input class="phone-input" type="text" maxlength="11">
        </div>
      </div>
      <div class="info-row">
        <div class="info-text">送餐地点：</div>
        <div class="address-text info-text tl">浙江工业大学屏峰校区家和西苑14幢112<span class="m-border-color">【默认】</span></div>
      </div>
    </div>

    <div class="memo">
      <div class="memo-text info-text">备 注</div>
      <textarea class="memo-input info-text" cols="35" rows="2"></textarea>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  export default {
    name: "productOrder",
    data() {
      return {
        productList: [
          { name: "鸡胸肉沙拉", num: "1" },
          { name: "龙利鱼沙拉", num: "2" }
        ]
      }
    },
    components: {  },
    methods: {

    },
    mounted() {

    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";

  .product-content {
    width: 100%;
    display: flex;
    box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.16);
    .store-img {
      width: 104px;
      height: 104px;
      padding: 30px 0 0 30px;
    }
    .product-right {
      flex: 1;
      padding: 50px 20px 50px 15px;
      .product-row-one {
        width: 100%;
        display: flex;
        padding: 15px 0 15px 0;
        border-bottom: 1px #c7c7c7 solid;
        .store-name {
          margin-left: 15px;
        }
      }
      .product-row-two {
        border-bottom: 1px #c7c7c7 solid;
        .product-row {
          width: 100%;
          display: flex;
          padding-top: 15px;
          &:last-child {
            margin-bottom: 35px;
          }
          .product-name {
            flex: 1;
            padding-left: 50px;
          }
          .product-quantity {

          }
        }
      }
      .product-row-three {
        width: 100%;
        display: flex;
        padding-top: 22px;
        .coupons-text {
          flex: 1;
          padding-top: 8px;
          padding-left: 50px;
        }
        .coupons-name {
          padding-top: 8px;
          margin-right: -20px;
        }
      }
      .product-row-four {
        width: 100%;
        display: flex;
        padding-top: 78px;
        .coupons-num {
          flex: 1;
          line-height: 50px;
          padding-right: 40px;
        }
        .real-pay {

        }
      }
    }
    .row-right-img {
      width: 30px;
      height: 30px;
      padding: 9px 0 0 30px;
    }
  }
  .m-text {
    font-size: 24px;
    color: @hexGrey;
  }

  .buyer-info {
    padding: 26px 36px 50px 36px;
    box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.16);
    .info-row {
      width: 100%;
      display: flex;
      padding-top: 24px;
      .row-right {

      }
      .row-right-one {
        width: 290px;
        padding: 5px;
        margin-left: 30px;
        border-radius: 30px;
        border: solid 1px @borderColor;
      }
      .row-right-two {
        width: 290px;
        display: flex;
        padding: 5px;
        margin-left: 30px;
        border-radius: 30px;
        border: solid 1px @borderColor;
        .time-text {
          flex: 1;
          padding: 3px;
          margin-right: -40px;
        }
        .drop-down-img {
          width: 35px;
          height: 25px;
          padding: 3px 5px 0 0;
        }
      }
      .row-right-three {
        .phone-input {
          width: 220px;
          height: 42px;
          margin-left: 30px;
          padding-left: 80px;
          border-radius: 30px;
          border: solid 1px @borderColor;
        }
      }
      .address-text {
        width: 420px;
        padding: 15px 20px;
        margin-left: 30px;
        line-height: 35px;
        letter-spacing: 1.2px;
        border-radius: 20px;
        border: solid 1px @borderColor;
      }
    }
  }
  .info-text {
    padding: 5px;
    font-size: 24px;
    color: @hexGrey;
  }

  .memo {
    width: 100%;
    display: flex;
    box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.16);
    .memo-text {
      padding: 40px;
    }
    .memo-input {
      letter-spacing: 1.2px;
      margin: 20px 0 20px 60px;
    }
  }
</style>
