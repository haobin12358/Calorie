import Vue from 'vue'
import Router from 'vue-router'
import Layout from '../pages/layout/index';

Vue.use(Router)


export const constantRouterMap = [
  { path: '/login', component: () => import('../pages/login/login'), hidden: true },
  // { path: '/register', component: () => import('../pages/login/register'),hidden: true },
  // { path: '/search', component: () => import('../pages/index/search'), hidden: true },
  // { path: '/product', component: () => import('../pages/index/product'),hidden: true },
  {
    path: '/',
    component: Layout,
    redirect: 'login',
    children: [{ path: '/login', component: () => import('../pages/login/login'), hidden: true }
    ],
  },
  /*{
    path: '/index',
    component: Layout,
    redirect: 'index/index',
    children: [{
      path: 'index',
      component: () => import('../pages/index/index'),
      name: 'index',
      meta: { title: 'index', icon: 'index', noCache: true }
    }
    ],
  },*/
  {
    path: '/diary',
    component: Layout,
    redirect: 'diary/index',
    children: [{
      path: 'index',
      component: () => import('../pages/diary/index'),
      name: 'diary',
      meta: { title: 'diary', icon: 'diary', noCache: true }
    }
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
    }
    ],

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
    }
    ],

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
    }
    ],
  },

//  我的
  /*账号设置*/
  // { path: '/setUp', component: () => import('../pages/personal/setUp/index'), hidden: true },

];

export default new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRouterMap
})

