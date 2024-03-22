<template>
    <div
            class="block rounded-lg bg-white shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)] dark:bg-neutral-700"
          >
            <div
              class="border-b-2 border-neutral-100 px-6 py-3 dark:border-neutral-600 dark:text-neutral-50"
            >
            <div class="flex">

              <font-awesome-icon
                    v-if="annuncements.announcement_type === 'comunicato'" 
                    icon="circle-info"
                    class="text-4xl text-blue-800"
                  />

                  <font-awesome-icon 
                  v-if="annuncements.announcement_type === 'avviso'" 
                  icon="triangle-exclamation" 
                  class="text-3xl text-yellow-500" />

                  <p class="text-sm font-semibold leading-6 text-gray-900 ml-4 pt-1">
                   {{ annuncements.announcement_type }}
                  </p>
            </div>
            </div>
            <div class="px-6 py-4 flex">
              <div class="flex-1 ">
                <h5
                class="mb-2 text-md font-medium leading-tight text-neutral-800 dark:text-neutral-50"
              >
                {{ annuncements.announcement_title }}
              </h5>
              <div v-html="annuncements.announcement_content" class="mb-2 text-base text-neutral-600 dark:text-neutral-200 line-clamp-1" >
                
              </div>
              <p class="font-semibold  text-gray-900 text-sm">
                 Data: {{ annuncements.created_at }}
                </p>
              </div>
              <div>
                <button
                class="mt-4 block w-full  rounded bg-blue-900 px-4 py-1 text-sm font-medium text-white shadow hover:bg-green-800 focus:outline-none focus:ring"
              >
           
                <router-link
                    :to="{
                      name: 'announcement-details',
                      params: { uuid: annuncements.uuid },
                    }"
               
                  >
                  Leggi
                  </router-link>
              </button>
              </div>
              
             
            </div>
          </div>
          
</template>
<script setup>

const props = defineProps({
  annuncements:{
    type:Object,
    required: true
  }
})
</script>