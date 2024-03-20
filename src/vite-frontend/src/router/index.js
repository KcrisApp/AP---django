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
      path:'/shipping/',
      name:'shipping',
      component: () => import ('../views/Shipping.vue'),


    },
    {
      path:'/shipping/:order_id',
      name:'shipping-details',
      component: () => import ('../views/ShippingDetails.vue'),
      props: true

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
      name: "test-details",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/TestDetails.vue"),
      props: true,
    },
    {
      path: "/smt/:smt_number",
      name: "smt-details",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/SmtDetails.vue"),
      props: true,
    },
    ,
    {
      path: "/welding/:welding_number",
      name: "welding-details",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/WeldingDetails.vue"),
      props: true,
    },
    {
      path: "/verify/:verify_number",
      name: "verify-details",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/VerifyDetails.vue"),
      props: true,
    },
    {
      path: "/foglio-caratterizzazione/:uuid",
      name: "foglio-caratterizzazione",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/CaratterizzazioneProdotto.vue"),
      props: true

    },
    {
      path: "/foglio-cestello/:uuid",
      name: "foglio-cestello",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/FoglioCestello.vue"),
      props: true

    },
    {
      path: "/announcement-details/:uuid",
      name: "announcement-details",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/AnnouncementDetails.vue"),
      props: true

    },
    {
      path: "/announcement-list/",
      name: "announcement-list",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/AnnouncementList.vue"),

    },
    {
      path: "/stats/",
      name: "stat-page",
      component: () => import("../views/Stats.vue"),
    },
    {
      path: "/test-page/",
      name: "test-page",
      component: () => import("../views/TestPage.vue"),
    },
    {
      path: "/:catchAll(.*)",
      name: "page-not-found",
      component: () => import("../views/NotFound.vue"),
    },
  
  ]
})

export default router
