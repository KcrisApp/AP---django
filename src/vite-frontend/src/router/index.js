import { createRouter, createWebHistory } from 'vue-router'
import { useStoreUser } from "../stores/storeUsers"

import HomeView from '../views/HomeView.vue'
import Ordini from '../views/Ordini.vue'
import Tools from '../views/Tools.vue'
import Boards from '../views/Boards.vue'
import Shipping from '../views/Shipping.vue'
import ShippingDetails from '../views/ShippingDetails.vue'
import BoardDetails from '../views/BoardDetails.vue'
import OrderDetails from '../views/OrderDetails.vue'
import TestDetails from '../views/TestDetails.vue'
import SmtDetails from '../views/SmtDetails.vue'
import WeldingDetails from '../views/WeldingDetails.vue'
import VerifyDetails from '../views/VerifyDetails.vue'
import CaratterizzazioneProdotto from '../views/CaratterizzazioneProdotto.vue'
import FoglioCestello from '../views/FoglioCestello.vue'
import AnnouncementDetails from '../views/AnnouncementDetails.vue'
import AnnouncementList from '../views/AnnouncementList.vue'
import Stats from '../views/Stats.vue'
import TestPage from '../views/TestPage.vue'
import Powatec from '../views/Powatec.vue'
import NotFound from '../views/NotFound.vue'



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
      component: () => Ordini

    },
    {
      path:'/tools/',
      name:'tools',
      component: () => Tools

    },
    {
      path:'/boards/',
      name:'boards',
      component: () => Boards

    },
    {
      path:'/shipping/',
      name:'shipping',
      component: () => Shipping


    },
    {
      path:'/shipping/:order_id/:order_qta',
      name:'shipping-details',
      component: () => ShippingDetails,
      props: true

    },
    {
      path: "/board/:uuid",
      name: "board-details",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => BoardDetails,
      props: true,
    },
    {
      path: "/order/:order_number",
      name: "order-details",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => OrderDetails,
      props: true,
    },
    {
      path: "/test/:test_number",
      name: "test-details",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => TestDetails,
      props: true,
    },
    {
      path: "/smt/:smt_number",
      name: "smt-details",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => SmtDetails,
      props: true,
    },
    ,
    {
      path: "/welding/:welding_number",
      name: "welding-details",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => WeldingDetails,
      props: true,
    },
    {
      path: "/verify/:verify_number",
      name: "verify-details",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => VerifyDetails,
      props: true,
    },
    {
      path: "/foglio-caratterizzazione/:uuid",
      name: "foglio-caratterizzazione",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => CaratterizzazioneProdotto,
      props: true

    },
    {
      path: "/foglio-cestello/:uuid",
      name: "foglio-cestello",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => FoglioCestello,
      props: true

    },
    {
      path: "/announcement-details/:uuid",
      name: "announcement-details",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => AnnouncementDetails,
      props: true

    },
    {
      path: "/announcement-list/",
      name: "announcement-list",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => AnnouncementList,

    },
    {
      path: "/stats/",
      name: "stat-page",
      component: () => Stats,
      beforeEnter: (to, from) => {
        // reject the navigation
      const store = useStoreUser()

       return store.permissionAccess ?  true :  "/"
     
      },
      
    },

    // Pagine di test non ancora implementate in rev 1.0
    {
      path: "/test-page/",
      name: "test-page",
      component: () => TestPage,
      beforeEnter: (to, from) => {
        // reject the navigation
        const store = useStoreUser()

       return store.permissionAccess ?  true :  "/"
     
      },
    },
    {
      path: "/powatec/",
      name: "powatec",
      component: () => Powatec,
      beforeEnter: (to, from) => {
        // reject the navigation
        const store = useStoreUser()

       return store.permissionAccess ?  true :  "/"
     
      },
    },
    {
      path: "/:catchAll(.*)",
      name: "page-not-found",
      component: () => NotFound,
    },
  
  ]
})


export default router
