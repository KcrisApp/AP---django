<template>
  <div
          class="block rounded-lg bg-white shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)] dark:bg-neutral-700"
        >
          <div
            class="border-b-2 border-neutral-100 px-6 py-3 dark:border-neutral-600 dark:text-neutral-50"
          >
          <div class="flex">

                <font-awesome-icon icon="hard-drive" class="text-2xl text-lime-600" />

                <p class="text-sm font-semibold leading-6 text-gray-900 ml-4 pt-1">
           Numero ordine: {{order.order_number}}
                </p>
          </div>
          </div>
          <div class="px-6 py-4 flex">
            <div class="flex-1 ">
              <h5
              class="mb-2 text-md font-medium leading-tight text-neutral-800 dark:text-neutral-50"
            >
            {{ order.board_name }}
            </h5>
            <div class="mb-2 text-base text-neutral-600 dark:text-neutral-200 " >
              <div class="flex gap-4">
                <p><b>Quantità:</b> {{ order.order_quantity }}</p>
                <p><b>Personalizzazione:</b> {{ order.order_customization }}</p>
                <p><b>Serialnumber:</b> {{ order.order_serialnumber }}</p>
              </div>
              
            </div>
            
            <p class="font-semibold  text-gray-900 text-sm">
               Data: {{ order.created_at }}
              </p>
            </div>
            <div>
              <button
              class="mt-4 block w-full  rounded bg-lime-600 px-4 py-1 text-sm font-medium text-white shadow hover:bg-green-800 focus:outline-none focus:ring"
            >
         
            <router-link
                  :to="{
                    name: 'order-details',
                    params: { order_number: order.order_number },
                  }"
                  
                >
                Vai
                </router-link> 
            </button>
            </div>
            
           
          </div>
        </div>
        
</template>
<script setup>

const props = defineProps({
order:{
  type:Object,
  required: true
}
})
</script>