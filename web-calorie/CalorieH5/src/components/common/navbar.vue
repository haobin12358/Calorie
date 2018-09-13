<template>
  <div>
    <div class="m-navbar" >
      <ul class="ul-four">
        <li v-for="(item, index) in list" :class="item.click?'active':''" @click="navClick(index)">
          <span class="m-navbar-text">{{item.name}}</span>
          <span class="m-dot" v-if="item.dot"></span>
          <div class="nav-bottom"> </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  import common from '../../common/js/common';
    export default {
      name: "navbar",
      data(){
        return{

        }
      },
      props:{
        list:{ type:Array, default:null }
      },
      methods:{
        navClick(v){
          if(this.list[v].click){
            return false;
          }
          common.changeTitle(this.list[v].name);
          this.$emit('navClick',v)
        }
      },
      mounted() {

      }
    }
</script>

<style lang="less" rel="stylesheet/less">
  @import "../../common/css/index";
  .m-navbar{
    margin-top: 10px;
    padding: 0 18px;
    .ul-four{
      display: flex;
      flex-flow: row;
      align-items: center;
      font-size: 24px;
      color: @greyColor;
      white-space: nowrap;
      justify-content: space-around;
      li{
        padding: 10px 0;
        position: relative;
        span.m-navbar-text{
          padding: 10px 20px;
        }
        .m-dot{
          position: absolute;
          width: 8px;
          height: 8px;
          border-radius: 50%;
          background-color: @mainColor;
        }
        .nav-bottom {
          width: 50px;
          height: 3px;
          margin: 10px 0 0 40px;
        }
        &.active{
          .nav-bottom {
            background-image: linear-gradient(to right, #2dd0ef, #8614d9);
          }
        }
      }
    }


  }
</style>
