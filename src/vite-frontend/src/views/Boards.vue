<template>
  <main>
    <div class="container-fluid flex min-h-screen">
      <NavBar />
      <BoardForm
        v-show="showForm"
        @close-modal="togleModal"
        @save-data="updateBoardsList"
      />

      <div class="m-4 w-full">
        <div class="flex justify-between gap-2">
          <h1 class="text-2xl">
            <font-awesome-icon icon="hard-drive" class="text-blue-950" />
            Schede
          </h1>
          <div class="flex-1">
            <form class="">
              <div class="relative">
                <div
                  class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none"
                ></div>
                <input
                  type="search"
                  id="default-search"
                  class="block w-full p-2 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="Cerca per ordine o nome scheda"
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
              <th scope="col" class="px-2 py-4"></th>
            </tr>
          </thead>
          <tbody>
            <tr
              class="border-b dark:border-neutral-500"
              v-for="board in filteredList()"
              :key="board.uuid"
            >
              <td class="whitespace-nowrap px-6 py-4 font-medium">
                {{ board.board_name }}
              </td>
              <td class="whitespace-nowrap px-6 py-4">
                {{ board.board_code }}
              </td>
              <td class="whitespace-nowrap px-6 py-4">
                {{ board.created_at }}
              </td>
              <td class="whitespace-nowrap px-4 py-4">{{ board.board_rev }}</td>
              <td class="px-2 py-4">
                <div class="flex justify-center gap-4">
                  <router-link
                    :to="{
                      name: 'board-details',
                      params: { uuid: board.uuid },
                    }"
                    class=""
                  >
                    <font-awesome-icon
                      icon="fa-eye"
                      class="text-blue-950 hover:text-green-500"
                    />
                  </router-link>
                </div>
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
import BoardForm from "../components/BoardForm.vue";

const boards = ref([]);
const showForm = ref(false);
const search = ref("");

function togleModal() {
  showForm.value = !showForm.value;
}

function updateBoardsList(value) {
  console.log(value);
  togleModal();
  boards.value.unshift(value);
}

function filteredList() {
  return boards.value.filter((board) =>
    board.board_name.toLowerCase().includes(search.value.toLowerCase())
  );
}

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
