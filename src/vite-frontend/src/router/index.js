import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory("/"),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path:'/ordini/',
      name:'ordini',
      component: () => import ('../views/Ordini.vue')

    },
    {
      path:'/tools/',
      name:'tools',
      component: () => import ('../views/Tools.vue')

    },
    {
      path:'/boards/',
      name:'boards',
      component: () => import ('../views/Boards.vue')

    },
    {
      path: "/board/:uuid",
      name: "board-details",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/BoardDetails.vue"),
      props: true,
    },
    {
      path: "/order/:order_number",
      name: "order-details",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/OrderDetails.vue"),
      props: true,
    },
    {
      path: "/test/:test_number",
      name: "order-details",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/TestDetails.vue"),
      props: true,
    },
    {
      path: "/:catchAll(.*)",
      name: "page-not-found",
      component: () => import("../views/NotFound.vue"),
    },
  ]
})

export default router
