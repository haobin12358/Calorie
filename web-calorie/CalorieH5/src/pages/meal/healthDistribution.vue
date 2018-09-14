<template>
  <div class="health-distribution" :class="cart_show? 'active':''">
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

    <food-list :foodList="foodList" @toDetail="toDetail"></food-list>

    <shopping-cart :cart_num_show="cart_num_show" :cart_total="cart_total" :total_price="total_price"
                   :cart_show="cart_show" :cartList="cartList" @toCart="toCart" @toOrder="toOrder" @toDetail="toDetail"></shopping-cart>

  </div>
</template>

<script type="text/ecmascript-6">
  import common from '../../common/js/common';
  import foodList from './components/foodList';
  import shoppingCart from './components/shoppingCart';

  export default {
    name: "healthDistribution",
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
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "肉类" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "肉类" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "肉类" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "蔬菜" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "水果" }
        ],
        foodList: [
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "草莓甜点", price: "9", oldPrice: "12.00", rate: "95.8", inventory: "5", num: "0", fid: "as24dfd" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "草莓甜点", price: "9", oldPrice: "12.00", rate: "95.8", inventory: "5", num: "2", fid: "as24dfd" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "草莓甜点", price: "9", oldPrice: "12.00", rate: "95.8", inventory: "5", num: "2", fid: "as24dfd" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "草莓甜点", price: "9", oldPrice: "12.00", rate: "95.8", inventory: "5", num: "2", fid: "as24dfd" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "草莓甜点", price: "9", oldPrice: "12.00", rate: "95.8", inventory: "5", num: "2", fid: "as24dfd" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "草莓甜点", price: "9", oldPrice: "12.00", rate: "95.8", inventory: "5", num: "2", fid: "as24dfd" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "草莓甜点", price: "9", oldPrice: "12.00", rate: "95.8", inventory: "5", num: "2", fid: "as24dfd" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "草莓甜点", price: "12.12", oldPrice: "12.00", rate: "95.8", inventory: "10", num: "2", fid: "as24dfd" },
          { src: "http://himg.china.cn/0/4_203_120316_750_750.jpg", name: "草莓甜点", price: "15.14", oldPrice: "12.00", rate: "95.8", inventory: "0", num: "0", fid: "as24dfd" }
        ],
        cartList: [],
        scroll: false,
        cart_num_show: true,
        cart_total: 0,
        total_price: 0,
        cart_show: false
      }
    },
    components: { foodList, shoppingCart },
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
        console.log(index, operation);
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
        console.log(item);
        let fid = item.fid;
        this.$router.push({path: "/foodDetail", query: { fid }});
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

          // 获取购物车中的列表
          for(let i = 0; i < this.foodList.length; i ++) {
            if(this.foodList[i].num != 0) {
              this.cartList.push(this.foodList[i]);
            }
          }
        }
      },
      // 去下单
      toOrder() {
        this.$router.push("/productOrder");
      }
    },
    mounted() {
      window.addEventListener('scroll', this.handleScroll);

      // 确定购物车角标数字和总价
      for(let i = 0; i < this.foodList.length; i ++) {
        this.cart_total = this.cart_total + Number(this.foodList[i].num);
        this.total_price = this.total_price + Number(this.foodList[i].num) * Number(this.foodList[i].price);
      }
      if(this.cart_total == 0) {
        this.cart_num_show = false;
      }
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_order";

</style>
