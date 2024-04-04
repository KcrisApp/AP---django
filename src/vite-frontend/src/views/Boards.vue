<template>
  <main>
 

    
      <BoardForm
        v-show="showForm"
        @close-modal="togleModal"
        @save-data="updateBoardsList"
      />

      <div class="p-4 w-full">
        <div class="flex justify-between gap-2 flex-wrap">
          <h1 class="text-2xl flex-1">
            <font-awesome-icon icon="hard-drive" class="text-blue-950" />
            Schede
          </h1>
          <div class="flex-2">
            <form class="">
              <div class="relative">
                <div
                  class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none"
                ></div>
                <input
                  type="search"
                  id="default-search"
                  class="block w-full p-2 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="Cerca per nome scheda"
                  v-model="search"
                />
              </div>
            </form>
          </div>
          <button
         
            class="hover:bg-blue-500 text-blue-950 font-semibold hover:text-white py-1 px-6 border border-blue-950 rounded"
            @click="togleModal"
          >
            <font-awesome-icon icon="folder-plus" /> Add
          </button>
        </div>

        <hr class="mt-2" />
        <table class="text-left text-sm font-light flex-wrap w-full">
          <thead class="border-b font-medium dark:border-neutral-500">
            <tr>
              <th scope="col" class="px-6 py-4">Scheda</th>
              <th scope="col" class="px-6 py-4">Codice</th>
              <th scope="col" class="px-6 py-4">Data creazione</th>
              <th scope="col" class="px-2 py-4">Revisione</th>
            
             
            </tr>
          </thead>
          <tbody>
            <tr
              class="border-b dark:border-neutral-500"
              v-for="board in paginatedData"
              :key="board.uuid"
            >
              <td class="whitespace-nowrap px-6 py-4 font-medium hover:text-green-600">
                
                <router-link
                    :to="{
                      name: 'board-details',
                      params: { uuid: board.id },
                    }"
               
                  >
                  {{ board.board_name }}
                  </router-link>
                  <span v-if="board.alert_info">
              <font-awesome-icon icon="bell" class=" text-red-700 ml-2"/>
            </span>
              </td>
              <td class="whitespace-nowrap px-6 py-4">
                {{ board.board_code }}
              </td>
              <td class="whitespace-nowrap px-6 py-4">
                {{ useDateFormatted(board.created_at) }}
              </td>
              <td class="whitespace-nowrap px-4 py-4">{{ board.board_rev }}
              
              </td>
         
            </tr>
          </tbody>
        </table>

        <!-- Testpagination -->
        <div class="text-center mt-4">
          <nav aria-label="Page navigation example">
            <ul class="inline-flex -space-x-px text-sm">
              <li v-show="pageNumber !== 0">
                <a
                  @click.prevent="prevPage"
                  class="disabled flex items-center justify-center px-3 h-8 ms-0 leading-tight text-gray-500 bg-white border border-e-0 border-gray-300 rounded-s-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
                  >Previous</a
                >
              </li>
              <li v-for="p in pageCounter" :key="p.uuid">
                <a
                  @click.prevent="setPage(p)"
                  class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
                  >{{ p }}</a
                >
              </li>

              <li v-show="pageNumber < pageCounter - 1">
                <a
                  @click.prevent="nextPage"
                  class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 rounded-e-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
                  >Next</a
                >
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
import BoardForm from "../components/BoardForm.vue";
import { useStoreUser } from "../stores/storeUsers";
import { useDateFormatted } from "../use/useDateFormatted"

// access the `store`
const store = useStoreUser();
// console.log(store.first_name);

const boards = ref([]);
const showForm = ref(false);
const search = ref("");

// Pagination
const pageCounter = ref(0);
const size = ref(15);
const pageNumber = ref(0);

const paginatedData = computed(() => {
  const start = pageNumber.value * size.value;
  const end = start + size.value;

  let b = boards.value.filter((board) =>
    board.board_name.toLowerCase().includes(search.value.toLowerCase())
  );

  pageCounter.value = Math.ceil(b.length / size.value);
  console.log(pageCounter.value);

  return b.slice(start, end);
});

const setPage = (page) => {
  pageNumber.value = page - 1;
};

const nextPage = () => {
  pageNumber.value++;
};

const prevPage = () => {
  pageNumber.value === 0 ? (pageNumber.value = 0) : pageNumber.value--;
};

function togleModal() {
  showForm.value = !showForm.value;
}

function updateBoardsList(value) {
  console.log(value);
  togleModal();
  boards.value.unshift(value);
}

// function filteredList() {
//    boards.value.filter((board) =>
//     board.board_name.toLowerCase().includes(search.value.toLowerCase())
//   );
// }

async function callApi() {
  let endpoint = endpoints["boardsCRUD"];
  try {
    const response = await axios.get(endpoint);
    boards.value.push(...response.data);
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
