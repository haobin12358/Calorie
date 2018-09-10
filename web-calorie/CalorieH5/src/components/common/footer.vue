<template>
    <mt-tabbar v-model="selected" :fixed="true">
      <template v-for="(item, index) in tabbar" >
        <mt-tab-item :id="item.name" @click="tabbarClick(item)">
          <img slot="icon" :src="item.icon">
          {{item.name}}
        </mt-tab-item>
      </template>
    </mt-tabbar>
</template>

<script type="text/ecmascript-6">
  import common from '../../common/js/common';
    export default {
      data() {
        return {
          name: '',
          selected: this.$store.state.tabbar[0].name,
          tabbar: this.$store.state.tabbar
        }
      },
      components: {},
      methods: {
        tabbarClick(v){
          console.log(v)
        }
      },
      watch: {
        selected: function (val, oldVal) {
          this.$store.state.tabbar_select = val;
          common.changeTitle(val);
          switch(val){
            case '日记':
              this.$router.push('/diary');
              break;
            case '餐配':
              this.$router.push('/meal');
              break;
            case '互动':
              this.$router.push('/interaction');
              break;
            case '我的':
              this.$router.push('/personal');
              break;
          }
        }
      },
      created() {

      }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";
</style>
