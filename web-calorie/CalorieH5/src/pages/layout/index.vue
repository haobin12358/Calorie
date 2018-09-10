<template>
  <div>
    布局layout
    <m-content></m-content>
    <m-footer></m-footer>
  </div>
</template>

<script type="text/ecmascript-6">
  import mContent from './mContent'
  import mFooter from '../../components/common/footer'
  export default {
    name: "index",
    data() {
      return {

      }
    },
    components: { mContent, mFooter },
    methods: {},
    created() {}
  }
</script>

<style lang="less" rel="stylesheet/less">

</style>
