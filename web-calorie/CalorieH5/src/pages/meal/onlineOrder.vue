<template>
  <div style="margin-bottom: 50px">
    <div class="mt-swipe-box">
      <mt-swipe :auto="15000">
        <mt-swipe-item v-for="item in bannerList" :key="item.id">
          <img :src="item.url" class="img">
        </mt-swipe-item>
      </mt-swipe>
    </div>

    <div class="cook-style"  id="cookStyle" :class="scroll == true? 'active':''">
      <ul class="cook-style-list">
        <li class="cook-style-box" v-for="(item, index) in cookStyleList" @click="styleChoose(item, index)">
          <img class="cook-style-img" :class="index == style_select?'active':''" :src="item.src" alt="">
          <div class="cook-style-name">{{item.name}}</div>
        </li>
      </ul>
    </div>

    <div class="food-list">
      <div class="food-box" v-for="(item, index) in foodList" @click="toDetail(item)">
        <img class="food-img" :src="item.src" alt="">
        <div class="food-box-right">
          <div class="right-row">
            <div class="food-name">{{item.name}}</div>
            <div class="food-price">￥{{item.price}}</div>
          </div>
          <div class="right-row">
            <div class="food-rate">好评率：{{item.rate}}%</div>
            <div class="food-old-price">￥{{item.oldPrice}}</div>
          </div>
          <div class="right-row">
            <div class="right-row-quantity">
              <img class="food-quantity-img" src="/static/images/purple/meal_minus.png" v-if="item.num != 0" @click="quantityChange(index, 'min')">
              <div class="food-quantity m-ft-24 m-grey-color m-ft-b" v-if="item.num != 0">{{item.num}}</div>
              <img class="food-quantity-img" src="/static/images/purple/meal_plus.png" alt="" @click="quantityChange(index, 'plus')">
            </div>
          </div>
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
  import common from '../../common/js/common';

  export default {
    name: "onlineOrder",
    data() {
      return {
        bannerList: [
          { url: 'http://image.suning.cn/uimg/sop/commodity/201312200307287693_x.jpg' },
          { url: 'http://img4.imgtn.bdimg.com/it/u=632938294,2120575488&fm=11&gp=0.jpg' },
          { url: 'http://img.zcool.cn/community/01a16c57fb3e1aa84a0d304fc108d5.jpg@2o.jpg' }
        ],
        style_select: 0,
        cookStyleList: [
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "全部" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "包子粥类" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "面条米线" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "川菜" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "粤菜" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "肉类" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "蔬菜" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "水果" }
        ],
        foodList: [
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "草莓甜点", price: "10", oldPrice: "12.00", rate: "95.8", inventory: "0", num: "0", fid: "as24dfd" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "草莓甜点", price: "10.20", oldPrice: "12.00", rate: "95.8", inventory: "10", num: "2", fid: "as24dfd" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "草莓甜点", price: "10.00", oldPrice: "12.00", rate: "95.8", inventory: "10", num: "1", fid: "as24dfd" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "草莓甜点", price: "10.00", oldPrice: "12.00", rate: "95.8", inventory: "10", num: "0", fid: "as24dfd" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "草莓甜点", price: "10.00", oldPrice: "12.00", rate: "95.8", inventory: "10", num: "0", fid: "as24dfd" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "草莓甜点", price: "10.00", oldPrice: "12.00", rate: "95.8", inventory: "10", num: "0", fid: "as24dfd" }
        ],
        scroll: false,
        cart_total: 0,
        total_price: 0,
      }
    },
    components: {  },
    methods: {
      // 滑动固定顶部
      handleScroll () {
        let scrollTop = common.getScrollTop();
        let clientHeight = common.getClientHeight();
        if(scrollTop > clientHeight * 0.224) {
          this.scroll = true;
        }else {
          this.scroll = false;
        }
      },
      // 菜品种类选择
      styleChoose(item, index) {
        this.style_select = index;
        // console.log(item, index);
      },
      // 菜品数量变化
      quantityChange(index, operation) {
        if(operation == "min") {
          this.foodList[index].num = Number(this.foodList[index].num) - 1;
          this.cart_total -= 1;
        }else if(operation == "plus") {
          this.foodList[index].num = Number(this.foodList[index].num) + 1;
          this.cart_total += 1;
        }
      },
      // 去餐品详情页
      toDetail(item) {
        let fid = item.fid;
        this.$router.push({path: "/foodDetail", query: { fid }});
      },
      // 去下单
      toOrder() {

      }
    },
    mounted() {
      window.addEventListener('scroll', this.handleScroll);

      // 确定购物车角标数字和总价
      for(let i = 0; i < this.foodList.length; i ++) {
        this.cart_total = this.cart_total + Number(this.foodList[i].num);
        this.total_price = this.total_price + Number(this.foodList[i].num) * Number(this.foodList[i].price);
      }
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_order";

</style>
