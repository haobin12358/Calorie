import Vue from 'vue'
import Router from 'vue-router'
import Layout from '../pages/layout/index';

Vue.use(Router)


export const constantRouterMap = [
  { path: '/login', component: () => import('../pages/login/login'), hidden: true },
  { path: '/register', component: () => import('../pages/login/register'),hidden: true },
  {
    path: '/',
    component: Layout,
    redirect: 'login',
    children: [{ path: '/login', component: () => import('../pages/login/login'), hidden: true }
    ],
  },
  {
    path: '/meal',
    component: Layout,
    redirect: 'meal/index',
    children: [{
      path: 'index',
      component: () => import('../pages/meal/index'),
      name: 'meal',
      meta: { title: 'meal', icon: 'meal', noCache: true }
    }],
  },
  {
    path: '/diary',
    component: Layout,
    redirect: 'diary/index',
    children: [{
      path: 'index',
      component: () => import('../pages/diary/index'),
      name: 'diary',
      meta: { title: 'diary', icon: 'meal', noCache: true }
    }],
  },
  {
    path: '/interaction',
    component: Layout,
    redirect: 'interaction/index',
    children: [{
      path: 'index',
      component: () => import('../pages/interaction/index'),
      name: 'interaction',
      meta: { title: 'interaction', icon: 'interaction', noCache: true }
    }],
  },
  {
    path: '/personal',
    component: Layout,
    redirect: 'personal/index',
    children: [{
      path: 'index',
      component: () => import('../pages/personal/index'),
      name: 'personal',
      meta: { title: 'personal', icon: 'personal', noCache: true }
    }],
  },

  /*餐配*/
  // 在线点餐
  { path: '/onlineOrder', component: () => import('../pages/meal/onlineOrder'), hidden: true },
  // 餐品详情
  { path: '/foodDetail', component: () => import('../pages/meal/foodDetail'), hidden: true },
  // 健康配送
  { path: '/healthDistribution', component: () => import('../pages/meal/healthDistribution'), hidden: true },
  // 健康周边
  { path: '/healthSurrounding', component: () => import('../pages/meal/healthSurrounding'), hidden: true },

  // 商品评价
  { path: '/productEvaluation', component: () => import('../pages/meal/productEvaluation'), hidden: true },
  // 商品订单
  { path: '/productOrder', component: () => import('../pages/meal/productOrder'), hidden: true },
  // 商品详情
  { path: '/productDetail', component: () => import('../pages/meal/productDetail'), hidden: true },
  // 提交订单
  { path: '/submitOrder', component: () => import('../pages/meal/submitOrder'), hidden: true },

];

export default new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRouterMap
})
