<template>
  <div>
    <div class="menu-box">
      <div class="menu-icon-text" v-for="item in menuList">
        <img class="menu-icon" :src="item.icon" alt="">
        <div class="menu-text">{{item.name}}</div>
      </div>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  export default {
    name: "menuLabel",
    data() {
      return {

      }
    },
    props:{
      menuList: { type: Array, default: [] }
    },
    components: {},
    methods: {},
    created() {}
  }
</script>

<style lang="less" rel="stylesheet/less">
  @import "../../common/css/index";

  .menu-box {
    width: 660px;
    height: 130px;
    display: flex;
    padding-top: 28px;
    margin: 0 45px;
    border-radius: 20px;
    background-color: @white;
    box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.16);
    white-space: nowrap;
    justify-content: space-around;
    .menu-icon-text {
      .menu-icon {
        width: 65px;
        height: 65px;
      }
      .menu-text {
        padding-top: 10px;
        font-size: 20px;
        color: @greyColor;
      }
    }
  }
</style>
