<template>

<button 
@click="showSidebar"
aria-controls="default-sidebar" type="button" class="inline-flex items-center p-2 mt-2 ms-3 text-sm text-gray-500 rounded-lg xl:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600">
   <span class="sr-only">Open sidebar</span>
   <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
   <path clip-rule="evenodd" fill-rule="evenodd" d="M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z"></path>
   </svg>
</button>

<aside 
id="default-sidebar" 
:class="sideBarHide ? '-translate-x-full': ''"
class="fixed top-0 left-0 z-40 w-64 h-screen transition-transform  xl:translate-x-0" aria-label="Sidebar">
   <div class="h-full px-3 py-4 overflow-y-auto bg-gray-200 dark:bg-gray-800">
      
      <ul class="space-y-2 font-medium">

         <div class="flex justify-between">
            <li>
            <a target="_blank" href="https://mceschedeelettroniche.com/" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">

               <!-- <h4 class="font-extrabold text-xl text-blue-900">MCE AP</h4>  -->
               <img src="http://127.0.0.1:8000/static/img/logo.png" alt="Mce logo" srcset="" width="150">
            </a>
         </li>
         <li v-show="!sideBarHide" @click.prevent="hideSidebar">
            <a  class="flex items-center xl:hidden p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
               <font-awesome-icon icon="xmark" />
               
            </a>
         </li>
         </div>
         
         <div class="pb-4">
            <span class="p-2">Benvenuto {{ store.userData.first_name }}</span>
            <p class="text-sm text-slate-500 p-2">{{ formatted }}</p> 
         </div>
         <hr class="h-px my-8 bg-slate-300 border-0 dark:bg-gray-700">
         <li
         @click="hideSidebar"
         >
            <a class="flex items-center p-2 text-blue-950 rounded-lg  dark:text-white hover:bg-white hover:text-blue-900   dark:hover:bg-gray-700 group">
              
               <font-awesome-icon icon="table-columns" class="text-lg"/>
               <RouterLink to="/" class="text-sm ml-2">Dashboard</RouterLink>
             
            </a>
         </li>
         <li
         @click="hideSidebar"
         >
            <a class="flex items-center p-2 text-blue-950 rounded-lg  dark:text-white hover:bg-white hover:text-blue-900   dark:hover:bg-gray-700 group">
              
               <font-awesome-icon icon="table-list" class=" text-lg" />
               <RouterLink to="/ordini" class="text-sm ml-2">Ordini</RouterLink>
             
            </a>
         </li>
         <li
         @click="hideSidebar"
         >
            <a class="flex items-center p-2 text-blue-950 rounded-lg dark:text-white hover:bg-white hover:text-blue-900   dark:hover:bg-gray-700 group">
               <font-awesome-icon icon="microchip" class="text-lg"/>
               <RouterLink to="/boards" class="text-sm ml-2">Schede</RouterLink>
            </a>
         </li>
         <li
         @click="hideSidebar"
         >
            <a class="flex items-center p-2 text-blue-950 rounded-lg dark:text-white hover:bg-white hover:text-blue-900   dark:hover:bg-gray-700 group">
               <font-awesome-icon icon="truck-fast" class="text-lg"/>
               <RouterLink to="/shipping" class="text-sm ml-2">Spedizioni</RouterLink>
            </a>
         </li>
         <li
         @click="hideSidebar"
         >
            <a class="flex items-center p-2 text-blue-950 rounded-lg dark:text-white hover:bg-white hover:text-blue-900   dark:hover:bg-gray-700 group">
               <font-awesome-icon icon="toolbox"  class="text-lg"/>
               <RouterLink to="/tools/" class="text-sm ml-2">Tools</RouterLink>
            </a>
         </li>
         <li >
            <a 
            @click="dropdownShow = !dropdownShow" 
            class=" flex items-center p-2 text-blue-950 rounded-lg dark:text-white hover:bg-white hover:text-blue-900   dark:hover:bg-gray-700 group">
               <font-awesome-icon icon="user-tie" />
               <span class="text-sm ml-2">Administration</span>
            </a>
            
            <ul 
            :class="dropdownShow ? 'hidden': ''"
            id="dropdown-example" 
            class=" py-2 space-y-2">
                  <li @click="dropdownShow = !dropdownShow" >
                     <a class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700">
                        <RouterLink to="/announcement-list/" class="text-sm ml-2">Comunicati</RouterLink>
                     </a>
                  </li>
                  <li
                   @click="dropdownShow = !dropdownShow" >
                     <a
                     v-if="store.permissionAccess"
                     href="/accounts/register/" 
                     class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-14 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700">
                        Add user
                     </a>
                  </li>
                  <!-- <li>
                     <a href="#" class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700">Billing</a>
                  </li>
                  <li>
                     <a href="#" class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700">Invoice</a>
                  </li> -->
            </ul>
         </li>
         <li
         @click="hideSidebar"
         >
            <a 
            v-if="store.permissionAccess"
            class="flex items-center p-2 text-blue-950 rounded-lg dark:text-white hover:bg-white hover:text-blue-900  dark:hover:bg-gray-700 group">
               <font-awesome-icon icon="chart-pie" />
               <RouterLink to="/stats/" class="text-sm ml-2">Statistiche</RouterLink>
            </a>
         </li>
  
         
         <hr class="h-px my-8 bg-slate-300 border-0 dark:bg-gray-700">
         <!-- <li>
            <a href="#" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
               <svg class="flex-shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 16">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 8h11m0 0L8 4m4 4-4 4m4-11h3a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-3"/>
               </svg>
               <span class="flex-1 ms-3 whitespace-nowrap">Sign In</span>
            </a>
         </li> -->
         <li>
            <a href="/accounts/logout/" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-white hover:text-red-700 dark:hover:bg-gray-700 group">
               <font-awesome-icon icon="right-from-bracket" />
               <span class="flex-1 ms-3 whitespace-nowrap">Logout</span>
            </a>
         </li>
      </ul>
     

   </div>
   
</aside>

<div class="p-4 xl:ml-64">
   
  <RouterView />
</div>
</template>
 

<script setup>
import { ref } from "vue";
import { RouterLink, RouterView } from 'vue-router'
import { useStoreUser } from '../stores/storeUsers'
import { useDateFormat, useNow } from '@vueuse/core'

const formatter = ref('HH:mm:ss DD-MM-YYYY ')
const formatted = useDateFormat(useNow(), formatter)

// access the `store` 
const store = useStoreUser()


const sideBarHide = ref(true)
const dropdownShow = ref(true)

const hideSidebar = () =>{
    sideBarHide.value = true
}
const showSidebar = () =>{
    sideBarHide.value = false
}


</script>  