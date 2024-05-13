import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { library } from "@fortawesome/fontawesome-svg-core";

import {faLaptopCode, 
        faHardDrive, 
        faFolderPlus, 
        faTableList, 
        faEye, faTrash, 
        faExclamation, 
        faCircleCheck, 
        faMicrochip, 
        faSearch, 
        faPenToSquare,
        faArrowLeftLong,
        faBars,
        faXmark,
        faTruckFast,
        faRightFromBracket,
        faToolbox,
        faChartPie,
        faTableColumns,
        faTarpDroplet,
        faCamera,
        faCircleInfo,
        faTriangleExclamation,
        faPassport,
        faDiagramProject,
        faFilePdf,
        faUserTie,
        faCirclePlus,
        faBell,
        faRocket,
        faArrowUpAZ,
        faArrowDownAZ,
        faFileCsv,
        faFileZipper,
        faFilePen
      } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { createPinia } from 'pinia'

library.add(faFolderPlus);
library.add(faTableList);
library.add(faHardDrive);
library.add(faEye);
library.add(faTrash);
library.add(faExclamation);
library.add(faCircleCheck);
library.add(faLaptopCode);
library.add(faMicrochip);
library.add(faSearch);
library.add(faPenToSquare);
library.add(faArrowLeftLong);
library.add(faPassport);
library.add(faBars);
library.add(faXmark);
library.add(faRightFromBracket);
library.add(faTruckFast);
library.add(faToolbox);
library.add(faChartPie);
library.add(faTableColumns);
library.add(faTarpDroplet);
library.add(faCamera);
library.add(faCircleInfo);
library.add(faTriangleExclamation);
library.add(faUserTie);
library.add(faDiagramProject);
library.add(faFilePdf);
library.add(faCirclePlus);
library.add(faBell);
library.add(faRocket);
library.add(faArrowDownAZ);
library.add(faArrowUpAZ);
library.add(faFileCsv);
library.add(faFileZipper);
library.add(faFilePen);


const app = createApp(App);


app.use(createPinia())
app.use(router)
app.component("font-awesome-icon", FontAwesomeIcon)

app.mount('#app')
