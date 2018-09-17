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
            <div class="m-text">x {{item.num}}</div>
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
          <div class="m-text">实付<span class="m-ft-30 m-black">￥40.0</span>元</div>
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
          <div class="time-text info-text" @click="popupVisible = true">{{time}}</div>
          <img class="drop-down-img" src="/static/images/purple/triangle.png" alt="">
        </div>
      </div>

      <mt-popup class="mt-popup" v-model="popupVisible" popup-transition="popup-fade" position="bottom">
        <div class="modal-row-one">
          <div class="popup-text m-grey tl" @click="popupVisible = false">取消</div>
          <div class="row-one-text tc">请选择送餐时间</div>
          <div class="popup-text tr" @click="timeDone">确定</div>
        </div>
        <mt-picker :slots="slots" @change="onValuesChange"></mt-picker>
      </mt-popup>

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

    <div class="to-pay-box">
      <img class="money-img" src="/static/images/purple/meal_money.png" alt="">
      <div class="m-ft-24 m-hex">合计</div>
      <div class="price-num m-ft-30 m-price m-ft-b tl">￥18.0</div>
      <div class="to-pay-btn">去 支 付</div>
    </div>

  </div>
</template>

<script type="text/ecmascript-6">
  import common from '../../common/js/common';

  export default {
    name: "productOrder",
    data() {
      return {
        productList: [
          { name: "鸡胸肉沙拉", num: "1" },
          { name: "龙利鱼沙拉", num: "2" }
        ],
        popupVisible: false,
        slots: [
          { values: ["11:00 - 11:30", "11:30 - 12:00", "12:00 - 12:30", "12:30 - 13:00", "13:00 - 13:30"] }
        ],
        time: "11:00-11:30",
        timeTemp: ""
      }
    },
    components: {  },
    methods: {
      // 监听送餐时间段选择器
      onValuesChange(picker, values) {
        this.timeTemp = values[0];
      },
      // 送餐时间-确定按钮
      timeDone() {
        this.popupVisible = false;
        this.time = this.timeTemp;
      }
    },
    mounted() {

    },
    created() {
      // 设置页面title
      common.changeTitle("商品订单");
    }
  }
</script>

<style lang="less" rel="stylesheet/less">
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
    .mt-popup {
      width: 100%;
      .modal-row-one {
        width: 100%;
        display: flex;
        .row-one-text {
          width: 50%;
          font-size: 28px;
          margin: 15px 30px;
          white-space: normal;
        }
        .popup-text {
          width: 20%;
          font-size: 28px;
          margin: 15px 30px;
        }
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
    margin-bottom: 100px;
    box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.16);
    .memo-text {
      padding: 40px;
    }
    .memo-input {
      letter-spacing: 1.2px;
      margin: 20px 0 20px 60px;
    }
  }
  .to-pay-box {
    width: 100%;
    display: flex;
    align-items: center;
    position: fixed;
    bottom: 0;
    background-color: @white;
    .money-img {
      width: 53px;
      height: 53px;
      padding: 0 10px 0 52px;
    }
    .price-num {
      flex: 1;
      padding-left: 18px;
    }
    .to-pay-btn {
      height: 40px;
      font-size: 30px;
      color: @white;
      white-space: normal;
      padding: 25px 90px;
      background-image: linear-gradient(to right, @mainLeft, @mainRight);
    }
  }
</style>
