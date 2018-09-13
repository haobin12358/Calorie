<template>
  <div>
    <div class="evaluation-box" v-for="item in evaluationList">
      <img class="user-img" :src="item.src" alt="">
      <div class="box-right">
        <div class="user-name e-text tl">{{item.name}}</div>
        <div class="evaluation-score">
          <div class="evaluation-title e-text">评价：</div>
          <div class="evaluation-score-imgs">
            <img class="evaluation-score-img" :src="src" v-for="src in item.scoreList">
          </div>
          <div class="evaluation-level e-text tr">{{item.evaluation_level}}</div>
        </div>
        <div class="evaluation-text e-text tl">评价内容：{{item.text}}</div>
        <div class="evaluation-imgs tl">
          <img class="evaluation-img" :src="img" v-for="img in item.srcList">
        </div>
      </div>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  export default {
    name: "productEvaluation",
    data() {
      return {
        evaluationList: [
          { src: "http://img4.duitang.com/uploads/item/201312/05/20131205171915_fhy3N.thumb.700_0.jpeg", name: "居居女孩", score: "4", text: "非常好吃！",
            srcList: ["http://imgsrc.baidu.com/image/c0%3Dshijue1%2C0%2C0%2C294%2C40/sign=685e3c62c9cec3fd9f33af36bee1be4a/fd039245d688d43f56d8505c771ed21b0ef43b2f.jpg",
              "http://imgsrc.baidu.com/image/c0%3Dshijue1%2C0%2C0%2C294%2C40/sign=685e3c62c9cec3fd9f33af36bee1be4a/fd039245d688d43f56d8505c771ed21b0ef43b2f.jpg",
              "http://imgsrc.baidu.com/image/c0%3Dshijue1%2C0%2C0%2C294%2C40/sign=685e3c62c9cec3fd9f33af36bee1be4a/fd039245d688d43f56d8505c771ed21b0ef43b2f.jpg",
              "http://imgsrc.baidu.com/image/c0%3Dshijue1%2C0%2C0%2C294%2C40/sign=685e3c62c9cec3fd9f33af36bee1be4a/fd039245d688d43f56d8505c771ed21b0ef43b2f.jpg",
              "http://imgsrc.baidu.com/image/c0%3Dshijue1%2C0%2C0%2C294%2C40/sign=685e3c62c9cec3fd9f33af36bee1be4a/fd039245d688d43f56d8505c771ed21b0ef43b2f.jpg"],
            scoreList: [], evaluation_level: ""
          },
          { src: "http://f.hiphotos.baidu.com/zhidao/pic/item/e4dde71190ef76c68a3a96589b16fdfaae5167dc.jpg", name: "居居女孩", score: "3", text: "好吃好吃好吃好吃好吃好吃好吃好吃好吃好吃好吃好吃好吃好吃好吃好吃好吃好吃！",
            srcList: ["http://imgsrc.baidu.com/image/c0%3Dshijue1%2C0%2C0%2C294%2C40/sign=685e3c62c9cec3fd9f33af36bee1be4a/fd039245d688d43f56d8505c771ed21b0ef43b2f.jpg",
              "http://imgsrc.baidu.com/image/c0%3Dshijue1%2C0%2C0%2C294%2C40/sign=685e3c62c9cec3fd9f33af36bee1be4a/fd039245d688d43f56d8505c771ed21b0ef43b2f.jpg",
              "http://imgsrc.baidu.com/image/c0%3Dshijue1%2C0%2C0%2C294%2C40/sign=685e3c62c9cec3fd9f33af36bee1be4a/fd039245d688d43f56d8505c771ed21b0ef43b2f.jpg"],
            scoreList: [], evaluation_level: ""
          }
        ],
      }
    },
    components: {  },
    methods: {
      // 处理分数的星星数目和评价等级
      score() {
        for(let i = 0; i < this.evaluationList.length; i ++) {

          if(this.evaluationList[i].score == 1) {
            this.evaluationList[i].evaluation_level = "差";
          }else if(this.evaluationList[i].score == 2) {
            this.evaluationList[i].evaluation_level = "一般";
          }else if(this.evaluationList[i].score == 3) {
            this.evaluationList[i].evaluation_level = "好";
          }else if(this.evaluationList[i].score == 4) {
            this.evaluationList[i].evaluation_level = "很好";
          }else if(this.evaluationList[i].score == 5) {
            this.evaluationList[i].evaluation_level = "非常好";
          }

          for (let j = 0; j < this.evaluationList[i].score; j ++) {
            this.evaluationList[i].scoreList.push("/static/images/star_full.png");
          }
          for (let m = 0; m < (5 - this.evaluationList[i].score); m ++) {
            this.evaluationList[i].scoreList.push("/static/images/star.png");
          }
        }
        console.log(this.evaluationList)
      }
    },
    mounted() {
      let fid = this.$route.query.fid;
      // console.log(fid);

      this.score();
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";

  .evaluation-box {
    width: 100%;
    display: flex;
    box-shadow: 0 5px 6px 0 rgba(0, 0, 0, 0.16);
    .user-img {
      width: 90px;
      height: 90px;
      padding: 25px 30px;
    }
    .box-right {
      flex: 1;
      padding: 25px 30px 0 0;
      .user-name {

      }
      .evaluation-score {
        width: 100%;
        display: flex;
        margin: 20px 0;
        border-bottom: 1px #c7c7c7 solid;
        .evaluation-title {

        }
        .evaluation-score-imgs {
          flex: 1;
          text-align: left;
          padding-bottom: 5px;
          .evaluation-score-img {
            width: 30px;
            left: 29px;
            padding-left: 15px;
          }
        }
        .evaluation-level {

        }
      }
      .evaluation-text {
        letter-spacing: 1.2px;
      }
      .evaluation-imgs {
        width: 100%;
        display: block;
        flex-wrap: wrap;
        padding-bottom: 85px;
        .evaluation-img {
          width: 170px;
          height: 170px;
          padding: 10px 20px 0 0;
        }
      }
    }
    .e-text {
      font-size: 24px;
      color: @hexGrey;
    }
  }
</style>
