<template>
  <div>
    <div class="personal-header">
      <img class="header-img" src="/static/images/personal_bg.jpg" alt="">
      <div class="user-info">
        <div class="user-info-bac"></div>
        <div class="user-info-box">
          <div class="row-one">
            <img class="row-one-img" src="/static/images/gift.png" alt="">
            <img class="row-one-img" src="/static/images/setting.png" alt="">
          </div>
          <img class="user-img" src="/static/images/product1.png" alt="">
          <div class="user-name m-ft-30 m-white">居居女孩</div>
          <div class="user-identity m-ft-20 m-white">未认证</div>
          <div class="user-num">
            <div class="user-num-text">23岁</div>
            <div class="user-num-divide">|</div>
            <div class="user-num-text">165cm</div>
            <div class="user-num-divide">|</div>
            <div class="user-num-text">52kg</div>
          </div>
          <div class="user-school">
            <img class="user-school-img" src="/static/images/personal_department.png" alt="">
            <div class="user-school-text">浙江工业大学</div>
            <img class="user-school-img" src="/static/images/personal_person.png" alt="">
            <div class="user-school-text">学生</div>
            <img class="user-school-img" src="/static/images/personal_love.png" alt="">
            <div class="user-school-text">甜味、咸味</div>
          </div>
        </div>
      </div>
    </div>

    <div class="menu-label">
      <menu-label :menuList="menuList" @toPage="toPage"></menu-label>
    </div>

    <div class="personal-row">
      <div class="row-text"></div>
      <img class="row-img" src="/static/images/arrow.png" alt="">
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  import menuLabel from '../../components/common/menuLabel'
  import common from '../../common/js/common'

  export default {
    data() {
      return {
        menuList: [
          { icon: "/static/images/purple/tabbar_information_active.png", url: "onlineOrder", name: "商品订单" },
          { icon: "/static/images/purple/tabbar_interaction_active.png", url: "healthDistribution", name: "我的发布" },
          { icon: "/static/images/purple/tabbar_diary_active.png", url: "healthSurrounding", name: "我的收藏" }
        ],
      }
    },
    components: { menuLabel },
    methods: {
      // 页面跳转跳转
      toPage(item) {
        // this.$router.push('/' + item.url);
        // 设置页面title
        // common.changeTitle(item.name);
      }
    },
    created() {

    }
  }
</script>
<style lang="less" rel="stylesheet/less" >
  @import "../../common/css/index";

  .personal-header {
    .header-img {
      width: 750px;
      height: 600px;
      z-index: 1000;
    }
    .user-info {
      .user-info-bac {
        width: 750px;
        height: 600px;
        position: absolute;
        top: 0;
        z-index: 1001;
        opacity: 0.4;
        background-color: #000000;
      }
      .user-info-box {
        width: 100%;
        position: absolute;
        top: 0;
        z-index: 1002;
        .row-one {
          width: 100%;
          display: flex;
          justify-content: space-between;
          .row-one-img {
            width: 40px;
            height: 40px;
            padding: 10px 15px;
          }
        }
        .user-img {
          width: 180px;
          height: 180px;
          border-radius: 50%;
          /*border: 3px #ffffff solid;*/
          box-shadow: 0 5px 6px 0 rgba(0, 0, 0, 0.16);
        }
        .user-name {
          padding: 20px 0 10px 0;
        }
        .user-identity {
          width: 80px;
          padding: 2px 15px;
          margin-left: 320px;
          border-radius: 30px;
          background-color: #676E6E;
        }
        .user-num {
          width: 100%;
          display: flex;
          color: @white;
          padding: 30px 0 15px 0;
          justify-content: center;
          .user-num-text {
            font-size: 24px;
          }
          .user-num-divide {
            padding: 0 30px;
          }
        }
        .user-school {
          width: 100%;
          display: flex;
          color: @white;
          justify-content: center;
          .user-school-img {
            width: 40px;
            height: 40px;
            padding: 0 6px 0 15px;
          }
          .user-school-text {
            line-height: 45px;
          }
        }
      }
    }
  }
  .menu-label {
    position: absolute;
    top: 500px;
    z-index: 1003;
  }
  .personal-row {

  }
</style>
