import Vue from 'vue';
import Vuex from 'vuex';


Vue.use(Vuex);

let store= new Vuex.Store({
  state: {
    route: null,
    now:null,
    token:'',
    tabbar:[
      /*{
      name:'首页',
      icon:'',
      url:'index'
    },*/
      {
      name:'客服',
      icon:'/static/images/product1.png',
      url:'service'
    },{
      name:'发现',
      icon:'/static/images/product1.png',
      url:'discover'
    },{
      name:'购物车',
      icon:'/static/images/product1.png',
      url:'shopping'
    },{
      name:'我的',
      icon:'/static/images/product1.png',
      url:'personal'
    }],
    tabbar_select:'客服'
  },
  mutations: {
    add(state, route) {
      state.now = route.name;
      var len = Object.keys(state.route);
      if (len.length < 5 || !!state.route[route.name]) {
        state.route[route.name] = route.path;
      }else{
        delete state.route[len[0]];
        state.route[route.name] = route.path;
      }
    },
    remove(state,name){
      Vue.delete(state.route,name)
      // delete state.route[name]


      // this.$store.commit('remove',name)调用此方法
    }
  }
})


export default store
