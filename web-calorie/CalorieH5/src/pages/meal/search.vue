<template>
  <div>
    <div class="search-header">
      <div class="search-box">
        <img class="search-img" src="/static/images/magnifier.png" alt="">
        <div class="search-text m-ft-21 m-hex tl">请输入商家/商品名称</div>
        <img class="search-img" src="/static/images/close.png" alt="">
      </div>
      <div class="search-btn m-ft-24 m-white">搜索</div>
    </div>

    <div class="search-tags">
      <div class="tags-title-row">
        <div class="tags-title m-ft-24 m-grey-color tl">热门推荐</div>
      </div>
      <div class="search-tags-box">
        <div class="search-tag m-ft-24 m-hex" v-for="item in tags">{{item}}</div>
      </div>
    </div>

    <div class="search-tags">
      <div class="tags-title-row">
        <div class="tags-title m-ft-24 m-grey-color tl">历史搜索</div>
        <div class="tags-clear-btn m-ft-20 m-border-color">清空</div>
      </div>
      <div class="search-tags-box">
        <div class="search-tag m-ft-24 m-hex" v-for="item in tags">{{item}}</div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "search",
    data() {
      return {
        tags: ["猪排饭", "猪排饭", "猪排饭猪排饭", "猪排饭", "猪排饭", "猪排饭", "猪排饭", "猪排饭猪排饭", "猪排饭", "猪排饭", "猪排饭猪排饭", "猪排饭", "猪排饭"]
      }
    },
    components: {  },
    methods: {

    },
    mounted() {

    },
    created() {

    }
  }
</script>

<style lang="less" rel="stylesheet/less">
  @import "../../common/css/index";

  .search-header {
    width: 720px;
    display: flex;
    padding: 10px 15px;
    background-image: linear-gradient(to right, @mainLeft, @mainRight);
    .search-box {
      width: 600px;
      display: flex;
      background-color: @white;
      .search-img {
        width: 30px;
        height: 30px;
        padding: 10px 15px;
      }
      .search-text {
        flex: 1;
        line-height: 50px;
      }
    }
    .search-btn {
      padding-left: 40px;
      line-height: 50px;
    }
  }
  .search-tags {
    padding: 25px 25px 50px 25px;
    box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.16);
    .tags-title-row {
      width: 700px;
      display: flex;
      line-height: 60px;
      border-bottom: 1px #d5d5d5 solid;
      .tags-title {
        flex: 1;
      }
      .tags-clear-btn {

      }
    }
    .search-tags-box {
      width: 700px;
      display: flex;
      flex-wrap: wrap;
      .search-tag {
        margin: 25px 25px 0 0;
        padding: 5px 20px;
        border: 1px #d5d5d5 solid;
      }
    }
  }
</style>
