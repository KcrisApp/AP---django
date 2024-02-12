import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import VueHtmlToPaper from 'vue-html-to-paper';
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
        faPassport     } from "@fortawesome/free-solid-svg-icons";
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

const options = {
        name: '_blank',
        specs: [
          'fullscreen=yes',
          'titlebar=yes',
          'scrollbars=yes'
        ],
        styles: [
          'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css',
          'https://unpkg.com/kidlat-css/css/kidlat.css'
        ],
        timeout: 1000, // default timeout before the print window appears
        autoClose: true, // if false, the window will not close after printing
        windowTitle: window.document.title, // override the window title
      }

const app = createApp(App);



app.use(router)
app.use(createPinia())
app.use(VueHtmlToPaper, options);
app.component("font-awesome-icon", FontAwesomeIcon)


app.mount('#app')
