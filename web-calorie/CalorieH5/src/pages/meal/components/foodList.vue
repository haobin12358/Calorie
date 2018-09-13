<template>
  <div>
    <div class="food-list">
      <div class="food-box" v-for="(item, index) in foodList" :class="item.inventory == 0? 'active':''" @click="toDetail(item)">
        <img class="food-img" :src="item.src" alt="">
        <div class="food-box-right">
          <div class="right-row">
            <div class="food-name">{{item.name}}</div>
            <div class="food-price">￥{{item.price}}</div>
          </div>
          <div class="right-row">
            <div class="food-rate">好评率：{{item.rate}}%</div>
            <div class="food-null-text m-ft-24 m-white">售罄</div>
            <div class="food-old-price">￥{{item.oldPrice}}</div>
          </div>
          <div class="right-row">
            <div class="right-row-quantity">
              <img class="food-quantity-img" src="/static/images/purple/meal_minus.png" v-if="item.num != 0" @click.stop="quantityChange(index, 'min')">
              <div class="food-quantity m-ft-24 m-grey-color m-ft-b" v-if="item.num != 0">{{item.num}}</div>
              <img class="food-quantity-img" src="/static/images/purple/meal_plus.png" v-if="item.inventory != 0" @click.stop="quantityChange(index, 'plus')">
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  export default {
    name: "foodList",
    data() {
      return {

      }
    },
    props:{
      foodList: { type: Array, default: [] }
    },
    components: {  },
    methods: {
      // 餐品数量变化
      quantityChange(index, operation) {
        console.log(index);
        this.$emit('quantityChange', index, operation);
      },
      // 去商品详情页
      toDetail(item) {
        this.$emit('toDetail', item);
      }
    },
    mounted() {

    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  /*@import "../../../common/css/index";*/
  @import "../../../common/css/_order";

</style>
