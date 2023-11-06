import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import { library } from "@fortawesome/fontawesome-svg-core";
import { faHardDrive, faFolderPlus, faTableList, faEye, faTrash, faExclamation, faCircleCheck } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";


library.add(faFolderPlus);
library.add(faTableList);
library.add(faHardDrive);
library.add(faEye);
library.add(faTrash);
library.add(faExclamation);
library.add(faCircleCheck);


const app = createApp(App);



app.use(router)
app.component("font-awesome-icon", FontAwesomeIcon)


app.mount('#app')
