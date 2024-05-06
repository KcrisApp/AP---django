import { createRouter, createWebHistory } from "vue-router";
import { useStoreUser } from "../stores/storeUsers";

import HomeView from "../views/HomeView.vue";
import Ordini from "../views/Ordini.vue";
import Tools from "../views/Tools.vue";
import Boards from "../views/Boards.vue";
import Shipping from "../views/Shipping.vue";
import ShippingDetails from "../views/ShippingDetails.vue";
import BoardDetails from "../views/BoardDetails.vue";
import OrderDetails from "../views/OrderDetails.vue";
import TestDetails from "../views/TestDetails.vue";
import SmtDetails from "../views/SmtDetails.vue";
import WeldingDetails from "../views/WeldingDetails.vue";
import VerifyDetails from "../views/VerifyDetails.vue";
import CaratterizzazioneProdotto from "../views/CaratterizzazioneProdotto.vue";
import FoglioCestello from "../views/FoglioCestello.vue";
import AnnouncementDetails from "../views/AnnouncementDetails.vue";
import AnnouncementList from "../views/AnnouncementList.vue";
import Stats from "../views/Stats.vue";
import TestPage from "../views/TestPage.vue";
import TestPagePlacement from "../views/TestPagePlacement.vue";
import Placement from "../views/Placement.vue";
import Bom from "../views/Bom.vue";
import PageBomUpload from "../views/PageBomUpload.vue";
import Powatec from "../views/Powatec.vue";
import UsersList from "../views/UsersList.vue";
import UserDetails from "../views/UserDetails.vue";
import UserPersonalInfo from "../views/UserPersonalInfo.vue";
import NotFound from "../views/NotFound.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,

    },
    {
      path: "/ordini/",
      name: "ordini",
      component: Ordini,
    },
    {
      path: "/tools/",
      name: "tools",
      component: Tools,
    },
    {
      path: "/boards/",
      name: "boards",
      component: Boards,
    },
    {
      path: "/shipping/",
      name: "shipping",
      component: Shipping,
    },
    {
      path: "/shipping/:order_id/:order_qta",
      name: "shipping-details",
      component: ShippingDetails,
      props: true,
    },
    {
      path: "/board/:uuid",
      name: "board-details",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: BoardDetails,
      props: true,
    },
    {
      path: "/order/:order_number",
      name: "order-details",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: OrderDetails,
      props: true,
    },
    {
      path: "/test/:test_number",
      name: "test-details",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: TestDetails,
      props: true,
    },
    {
      path: "/smt/:smt_number",
      name: "smt-details",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: SmtDetails,
      props: true,
    },
    ,
    {
      path: "/welding/:welding_number",
      name: "welding-details",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: WeldingDetails,
      props: true,
    },
    {
      path: "/verify/:verify_number",
      name: "verify-details",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: VerifyDetails,
      props: true,
    },
    {
      path: "/foglio-caratterizzazione/:uuid",
      name: "foglio-caratterizzazione",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: CaratterizzazioneProdotto,
      props: true,
    },
    {
      path: "/foglio-cestello/:uuid",
      name: "foglio-cestello",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: FoglioCestello,
      props: true,
    },
    {
      path: "/announcement-details/:uuid",
      name: "announcement-details",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: AnnouncementDetails,
      props: true,
    },
    {
      path: "/announcement-list/",
      name: "announcement-list",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: AnnouncementList,
    },
    {
      path: "/users-list/",
      name: "users-list",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: UsersList,
      beforeEnter: async (to, from) => {
        // reject the navigation
        const store = useStoreUser();
        await store.getUserData()
      
        const user = store.userInfo
        console.log(user)
        return store.permissionAccess ? true : "/";
      },
    },
    {
      path: "/users-details/:username",
      name: "users-details",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: UserDetails,
      props: true,
      beforeEnter:async (to, from) => {
        // reject the navigation
        const store = useStoreUser();
        await store.getUserData()
      
        const user = store.userInfo
        console.log(user)
        return store.permissionAccess ? true : "/";
      },
    },
    {
      path: "/my-info/",
      name: "my-info",
      // route level code-splitting
      // this generates a separate chunk (QuestionView.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: UserPersonalInfo,
    },
    {
      path: "/stats/",
      name: "stat-page",
      component: Stats,
      beforeEnter: async(to, from) => {
        // reject the navigation
        const store = useStoreUser();
        await store.getUserData()
      
        const user = store.userInfo
        console.log(user)
        return store.permissionAccess ? true : "/";
      },
    },

    // Pagine di test non ancora implementate in rev 1.0
    {
      path: "/upload-bom/:order_number",
      name: "upload-bom",
      component: PageBomUpload,
      props:true,
      beforeEnter:async (to, from) => {
        // reject the navigation
        const store = useStoreUser();
        await store.getUserData()
      
        const user = store.userInfo
        console.log(user)
        return store.permissionAccess ? true : "/";
      },
    },
    {
      path: "/bom/:order_number",
      name: "bom",
      component: Bom,
      props: true,

    },
    // Pagine di test non ancora implementate in rev 1.0
    {
      path: "/placement/:order_number",
      name: "placement",
      component: Placement,
      props: true,

    },
    {
      path: "/upload_placement/:order_number",
      name: "upload_placement",
      component: TestPagePlacement,
      props: true,
      beforeEnter:async (to, from) => {
        // reject the navigation
        const store = useStoreUser();
        await store.getUserData()
      
        const user = store.userInfo
        console.log(user)
        return store.permissionAccess ? true : "/";
      },
    },
    {
      path: "/powatec/",
      name: "powatec",
      component: Powatec,
      beforeEnter: async(to, from) => {
        // reject the navigation
       
        const store = useStoreUser();
        await store.getUserData()
        return store.permissionAccess ? true : "/";
      },
    },
    {
      path: "/:catchAll(.*)",
      name: "page-not-found",
      component: NotFound,
    },
  ],
});






export default router;
