<template>
  <main>
    <div class="container-fluid flex min-h-screen">
      <NavBar />
      <div class="m-4 w-full">
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
                  placeholder="Cerca per numero ordine o codice"
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
              <th scope="col" class="px-6 py-4">Data creazione</th>
              <th scope="col" class="px-6 py-4">Scheda</th>
              <th scope="col" class="px-6 py-4"></th>
            </tr>
          </thead>
          <tbody>
            <tr
              class="border-b dark:border-neutral-500"
              v-for="order in orders"
              :key="order.uuid"
            >
              <td class="whitespace-nowrap px-6 py-4 font-medium">
                {{ order.order_number }}
              </td>
              <td class="whitespace-nowrap px-6 py-4">
                {{ order.order_quantity }}
              </td>
              <td class="whitespace-nowrap px-6 py-4">
                {{ order.created_at }}
              </td>
              <td class="whitespace-nowrap px-6 py-4">{{ order.board_name }}</td>
              <td class="whitespace-nowrap px-6 py-4">
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
      </div>
    </div>
  </main>
</template>
<script setup>
import NavBar from "../components/NavBar.vue";
import { endpoints } from "../common/endpoints";
import { axios } from "../common/api.service";
import { ref, onMounted } from "vue";

const orders = ref([]);

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
