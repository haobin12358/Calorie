<template>
  <div>
    <div class="login-btn" @click="toLogin">Login</div>
  </div>
</template>

<script type="text/ecmascript-6">
  export default {
    name: "login",
    data() {
      return {

      }
    },
    components: {},
    methods: {
      // 登录按钮
      toLogin() {
        this.$router.push('/diary');
      }
    },
    created() {}
  }
</script>

<style lang="less" rel="stylesheet/less">

  .login-btn {
    color: #ffffff;
    position: absolute;
    left: 25%;
    bottom: 20%;
    width: 50%;
    padding: 10px;
    border-radius: 30px;
    background-color: #f43b51;
  }
</style>
