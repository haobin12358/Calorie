<template>
  <div>
    <div class="search-input m-ft-21 m-white tl">请输入商家/商品名称</div>
    <div class="address-choose m-ft-24 m-black tl">浙江工业大学（屏峰校区）</div>
    <div class="mt-swipe-box">
      <mt-swipe :auto="15000">
        <mt-swipe-item v-for="item in bannerList" :key="item.id">
          <img :src="item.url" class="img">
        </mt-swipe-item>
      </mt-swipe>
    </div>
    <div class="menu-label">
      <menu-label :menuList="menuList"></menu-label>
    </div>
    <div class="text-row">
      <div class="row-left-text">在线点餐</div>
      <img class="row-right-img" src="/static/images/product1.png" alt="">
    </div>

    <div class="online-order">
      <ul class="product-list" id="product-list">
      </ul>
    </div>

    <div class="text-row">
      <div class="row-left-text">健康配送</div>
      <img class="row-right-img" src="/static/images/product1.png" alt="">
    </div>
    <div class="text-row">
      <div class="row-left-text">健康周边</div>
      <img class="row-right-img" src="/static/images/product1.png" alt="">
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  import menuLabel from '../../components/common/menuLabel'

  export default {
    name: "index",
    data() {
      return {
        bannerList: [
          { url: 'http://image.suning.cn/uimg/sop/commodity/201312200307287693_x.jpg' },
          { url: 'http://img4.imgtn.bdimg.com/it/u=632938294,2120575488&fm=11&gp=0.jpg' },
          { url: 'http://img.zcool.cn/community/01a16c57fb3e1aa84a0d304fc108d5.jpg@2o.jpg' }
        ],
        menuList: [
          { icon: "/static/images/product1.png", name: "在线点餐" },
          { icon: "/static/images/product1.png", name: "健康配送" },
          { icon: "/static/images/product1.png", name: "健康周边" },
          { icon: "/static/images/product1.png", name: "健康卡" }
        ],
        onlineList: [
          { src: "/static/images/product1.png", name: "蒜泥娃娃菜", price: "800.0" },
          { src: "/static/images/product1.png", name: "蒜泥娃娃菜", price: "8.0" },
          { src: "/static/images/product1.png", name: "蒜泥娃娃菜", price: "8.0" },
          { src: "/static/images/product1.png", name: "蒜泥娃娃菜", price: "8.0" }
        ]
      }
    },
    components: { menuLabel },
    methods: {
      // 获取数据
      getData() {

        // 往ul中添加li
        for(let i = 0; i < this.onlineList.length; i ++) {
          var elem_li = document.createElement('li'); // 生成一个 li元素
          // 设置元素的内容
          elem_li.innerHTML = "<img src=" + this.onlineList[i].src + " class='product-img'><div class='product-bottom'><div class='product-name'>" + this.onlineList[i].name + "</div>"
            + "<div class='product-price'>￥" + this.onlineList[i].price + "</div></div>";
          document.getElementById('product-list').appendChild(elem_li);
        }
        /*// 给每个li添加点击事件
        let that = this;
        // let oli = document.getElementsByTagName("li");
        let oli = document.getElementsByClassName("product-img");
        for(let i = 0; i < oli.length; i ++){
          (function(j){
            oli[j].onclick = function () {
              that.toProduct(j);
            };
          })(i)
        }*/
      },
      // 去产品详情页
      toProduct(i) {
        let prid = this.recommend.products[i].prid;
        this.$router.push({path: "/productDetail", query: { prid }});
      },
    },
    mounted() {
      this.getData();
    }
  }
</script>

<style lang="less" rel="stylesheet/less">
  @import "../../common/css/index";

  .search-input {
    height: 40px;
    padding: 15px;
    background-image: linear-gradient(to right, @mainLef, @mainRight);

  }
  .address-choose {
    position: absolute;
    top: 70px;
    z-index: 1000;
    width: 730px;
    opacity: 0.3;
    padding: 10px;
    background-color: @white;
  }
  .mt-swipe-box {
    margin-bottom: 130px;
    box-shadow: 0 5px 6px 0 rgba(0, 0, 0, 0.16);
  }
  .menu-label {
    position: absolute;
    top: 360px;
  }
  .text-row {
    width: 100%;
    display: flex;
    .row-left-text {
      flex: 1;
      font-size: 30px;
      font-weight: bold;
      padding: 10px 0;
      margin-left: 45px;
      text-align: left;
      color: @greyColor;
    }
    .row-right-img {
      width: 30px;
      height: 30px;
      padding: 15px 30px;
    }
  }
  /*.online-order {
    width: 100%;
    display: flex;
    margin: 10px 0 30px 45px;
    .product-box {
      width: 231px;
      height: 305px;
      margin-right: 20px;
      border-radius: 20px;
      background-color: @white;
      box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.16);
      .product-img {
        width: 231px;
        height: 231px;
        padding-bottom: 15px;
        border-radius: 20px 20px 0 0;
      }
      .product-name {
        font-size: 24px;
        color: @greyColor;
      }
      .product-price {
        font-size: 24px;
        color: @priceColor;
      }
    }
  }*/

  .online-order{
    min-height: 305px;
    margin-left: 45px;
    .product-list {
      width: 100%;
      display: inline;
      white-space: nowrap;
      overflow-x: scroll;
      float: left;
      overflow-y: hidden;
      padding: 10px 0 5px 0;
      li {
        display: inline-block;
        width: 231px;
        height: 305px;
        margin-right: 20px;
        border-radius: 20px;
        background-color: @white;
        box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.16);
        .product-img {
          width: 231px;
          height: 231px;
          padding-bottom: 15px;
          border-radius: 20px 20px 0 0;
        }
        .product-bottom {
          width: 100%;
          display: flex;
          .product-name {
            flex: 1;
            font-size: 24px;
            color: @greyColor;
            margin-left: 11px;
            text-align: left;
          }
          .product-price {
            font-size: 24px;
            color: @priceColor;
            margin-right: 11px;
          }
        }
      }
    }
  }
  /*滚动条样式*/
  ::-webkit-scrollbar {
    margin-right: -40px;
  }
</style>
