import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import { library } from "@fortawesome/fontawesome-svg-core";
import {faLaptopCode, faHardDrive, faFolderPlus, faTableList, faEye, faTrash, faExclamation, faCircleCheck, faMicrochip, faSearch } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";


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


const app = createApp(App);



app.use(router)
app.component("font-awesome-icon", FontAwesomeIcon)


app.mount('#app')
