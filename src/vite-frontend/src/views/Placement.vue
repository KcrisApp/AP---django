<template>
  <h1 class="text-2xl mb-4 text-blue-900">
    <font-awesome-icon icon="laptop-code" class="text-blue-950" />
    Placement
  </h1>
  <div class="flex gap-2 justify-between">
    <p class="hover:text-green-600" @click="goBack">
      <font-awesome-icon icon="arrow-left-long" /> Back
    </p>
    <div class="flex">
      <button @click="resetAll"
        class="bg-transparent m-2 hover:bg-blue-500 text-blue-700 hover:text-white text-sm py-2 px-4 border border-blue-500 hover:border-transparent rounded-md">Reset
        all
      </button>
      <button @click="checkAll"
        class="bg-transparent m-2 hover:bg-green-500 text-green-700 hover:text-white text-sm py-2 px-4 border border-green-500 hover:border-transparent rounded-md">Check
        all
      </button>
    </div>
  </div>

  <!-- Idea si può usare la barra per vedere la percentuale di completamento -->

  <!-- <div
v-if="onLoad" 
class="my-5">
    <div class="flex justify-between mb-1">
  <span class="text-base font-medium text-blue-700 dark:text-white">Import file</span>
  <span class="text-sm font-medium text-blue-700 dark:text-white">45%</span>
</div>
<div class="w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-700">
  <div class="bg-blue-600 h-2.5 rounded-full" style="width: 45%"></div>
</div>
</div> -->

  <hr class="my-2">
  <div class="flex gap-2">
    <span
      class="bg-blue-100 text-blue-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded dark:bg-blue-900 dark:text-blue-300">Posizioni
      totali: {{ codeCount }}</span>
    <span
      class="bg-red-100 text-red-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded dark:bg-red-900 dark:text-red-300">Posizioni
      da verificare: {{ codeToBeCheckedItem }}</span>
    <span
      class="bg-green-100 text-green-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded dark:bg-green-900 dark:text-green-300">Posizioni
      verificate: {{ codeCheckedItem }}</span>
  </div>
  <div class="relative overflow-x-auto shadow-md sm:rounded-lg mt-4">
    <NoteForm v-model="note" v-if="showEditNote" @close-modal="closeModal" />
    <table
      class="w-full divide-y divide-gray-200 dark:divide-neutral-700 text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 overflow-x-auto over mt-4">
      <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
        <tr>
          <th scope="col" class="px-6 py-3">Tipo magazzino</th>
          <th scope="col" class="px-6 py-3">Componente/Qta</th>
          <th scope="col" class="px-6 py-3">Desc.Componente</th>
          <th scope="col" class="px-6 py-3">Note</th>
          <th scope="col" class="px-6 py-3"></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, idx) in placement" :key="idx" class="hover:bg-gray-100"
          :class="row.check ? 'line-through text-green-500 font-bold' : ''">
          <td class=" border-b dark:border-gray-700">
          <th scope="row" class="px-6 py-4 font-medium  whitespace-nowrap dark:text-white0">{{ row.type }}
          </th>
          </td>
          <td class=" border-b dark:border-gray-700">
          <th scope="row" class="px-6 py-4 font-medium  whitespace-nowrap dark:text-white0">{{ row.component }}
          </th>
          </td>
          <td class=" border-b dark:border-gray-700">
          <th scope="row" class="px-6 py-4 font-medium  whitespace-nowrap dark:text-white0">{{ row.desc }}
          </th>
          </td>
          <td @click="addNoteToItem(idx)" class=" border-b dark:border-gray-700">
          <th scope="row" class="px-6 py-4 font-medium  whitespace-wrap dark:text-white ">
            {{ row.note }}
          </th>
          </td>
          <td @click="addToList(idx)" class=" border-b dark:border-gray-700">
          <th scope="row" class="px-6 py-4 font-medium  whitespace-nowrap dark:text-white0">
            <span v-if="row.check">Ok</span>
            <span v-else="row.check">To check</span>
          </th>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { utils, writeFileXLSX } from 'xlsx';
import { endpoints } from "../common/endpoints";
import { axios } from "../common/api.service";
import NoteForm from "../components/NoteForm.vue"
import { useStoreUser } from "../stores/storeUsers";
import { useRouter } from "vue-router";

const props = defineProps({
  order_number: String,
});

const router = useRouter();


const onLoad = ref(false)
const placement = ref([])
const order = ref(null)
const showEditNote = ref(false)
const store = useStoreUser();
const note = ref("")
const selectId = ref(null)


// Conteggio codici
const codeCount = computed(() => {
  return placement.value.length
})
const codeCheckedItem = computed(() => {
  let counter = 0;
  for (const obj of placement.value) {
    if (obj.check) counter++;
  }
  return counter
})

const codeToBeCheckedItem = computed(() => {
  let counter = 0;
  for (const obj of placement.value) {
    if (!obj.check) counter++;
  }
  return counter
})
// Create xlsx Placement
function exportFile() {

  const ws = utils.json_to_sheet(bomResult.value);
  const wb = utils.book_new();
  utils.book_append_sheet(wb, ws, "Data");
  writeFileXLSX(wb, "placement.xlsx");


}


const addToList = (id) => {
  console.log(id)
  console.log(placement.value[id].check)

  placement.value[id].check = !placement.value[id].check
  updateData()
}

const addNoteToItem = (id) => {
  note.value = placement.value[id].note
  selectId.value = id
  showEditNote.value = true

}


const closeModal = () => {
  placement.value[selectId.value].note = note.value
  showEditNote.value = false
  selectId.value = null

  updateData()
}


const goBack = () => {
  router.back()
}

const resetAll = () => {
  for (const obj of placement.value) {
    obj.check = false
  }
}
const checkAll = () => {
  for (const obj of placement.value) {
    obj.check = true
  }
}



async function callApi() {

  onLoad.value = false
  const endpoint = `${endpoints["ordersCRUD"]}${props.order_number}/`;

  try {
    const response = await axios.get(endpoint);
    console.log(response);

    if (response.data.order_placement_pick_and_place) {

      placement.value = JSON.parse(response.data.order_placement_pick_and_place)
    }
    order.value = response.data.order_number

    console.log(response.data.order_placement_pick_and_place);
    onLoad.value = true
  } catch (error) {
    alert(error);
  }
}


async function updateData() {

  const endpoint = `${endpoints["ordersCRUD"]}${props.order_number}/`;
  let method = "PATCH";
  try {
    const response = await axios({
      method: method,
      url: endpoint,
      data: {
        order_placement_pick_and_place: JSON.stringify(placement.value),
      },

    });

  } catch (error) {
    alert(error.response);
  }
}

onMounted(() => {
  callApi()
})

</script>
