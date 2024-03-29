<template>
  <main>


      <div class="p-4 w-full">
        <div class="flex justify-between gap-2">
        <h1 class="text-2xl">
          <font-awesome-icon icon="table-list" class="text-blue-950" />
          Ordini
        </h1>
        <div class="flex-1">
            <form class="">
             
              <div class="relative">
                <div
                  class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none"
                >
                  
                </div>
                <input
                  type="search"
                  id="default-search"
                  class="block w-full p-2 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="Cerca per numero ordine"
                  v-model="search"
                  required
                />

              </div>
            </form>
          </div>
          </div>
        <hr class="my-4"/>

        <table class="text-left text-sm font-light flex-wrap w-full">
          <thead class="border-b font-medium dark:border-neutral-500">
            <tr>
              <th scope="col" class="px-6 py-4">Numero ordine</th>
              <th scope="col" class="px-6 py-4">Quantità</th>
              <th scope="col" class="px-6 py-4">Data di consegna</th>
              <th scope="col" class="px-6 py-4">Scheda</th>
              <th scope="col" class="px-6 py-4"></th>
            </tr>
          </thead>
          <tbody>
            <tr
              class="border-b dark:border-neutral-500"
              v-for="order in paginatedData"
              :key="order.uuid"
            >
              <td class="whitespace-nowrap px-6 py-4 font-medium">
                {{ order.order_number }}
              </td>
              <td class="whitespace-nowrap px-6 py-4">
                {{ order.order_quantity }}
              </td>
              <td class="whitespace-nowrap px-6 py-4">
           
              {{ useDateFormat( order.shipping_date) }}


              </td>
              <td class="whitespace-nowrap px-6 py-4">{{ order.board_name }}</td>
              <td class="whitespace-nowrap py-4">
                <router-link
                  :to="{
                    name: 'order-details',
                    params: { order_number: order.order_number },
                  }"
                  class="hover:text-green-600"
                >
                  <font-awesome-icon
                    icon="fa-eye"
                    class="text-blue-950 hover:text-green-500"
                  />
                </router-link>
              </td>
            </tr>
          </tbody>
        </table>


          <!-- Testpagination -->
          <div class=" text-center mt-4">


          <nav aria-label="Page navigation example">
          <ul class="inline-flex -space-x-px text-sm">
          <li v-show="pageNumber !== 0">

          <a @click.prevent="prevPage" class="disabled  flex items-center justify-center px-3 h-8 ms-0 leading-tight text-gray-500 bg-white border border-e-0 border-gray-300 rounded-s-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">Previous</a>
          </li>
          <li v-for="p in pageCounter">
          <a @click.prevent="setPage(p)"  class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">{{ p }}</a>
          </li>

          <li v-show ="pageNumber < pageCounter -1" >
          <a @click.prevent="nextPage" 

          class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 rounded-e-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">Next</a>
          </li>
          </ul>
          </nav>


          </div>
          <!-- Testpagination -->



      </div>
 
  </main>
</template>
<script setup>

import { endpoints } from "../common/endpoints";
import { axios } from "../common/api.service";
import { ref, onMounted, computed } from "vue";
import {useDateFormat } from "../use/useDateFormat"

const orders = ref([]);

const search = ref("");
const pageCounter = ref(0)



// Pagination
const size = ref(15);
const pageNumber = ref(0);




const paginatedData = computed(()=>{
  const start = pageNumber.value * size.value
  const end = start + size.value;

  let b = orders.value.filter((order) =>
    order.order_number.toLowerCase().includes(search.value.toLowerCase())
  )

  pageCounter.value =  Math.ceil(b.length/size.value);
  console.log(pageCounter.value)

  return b.slice(start, end);
  

})

const setPage = (page) =>{
  pageNumber.value = page - 1
}

const nextPage = () => {

  pageNumber.value++;
}

const prevPage = () => {
  pageNumber.value === 0 ? pageNumber.value = 0 : pageNumber.value--;
}



async function callApi() {
  let endpoint = endpoints["ordersCRUD"];
  try {
    const response = await axios.get(endpoint);
    orders.value.push(...response.data);
    console.log(response.data);
  } catch (error) {
    alert(error);
  }
}
// lifecycle hooks
onMounted(() => {
  callApi();
});
</script>
