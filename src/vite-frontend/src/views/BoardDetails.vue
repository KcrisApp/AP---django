<template>
  <main>
    <div class="container-fluid flex min-h-screen">
      <NavBar />

      <div class="m-4 w-full" v-for="b in board">

        <Alert
          v-show="showAlert"
          icon-type="error"
          title="Attenzione"
          message="Sei sicuro di voler eliminare la scheda?"
          @close-alert="togleAlert"
          @confirm="deleteBoard(b.uuid)"
        />
        <BoardForm
                v-show="showForm"
                @close-modal="togleForm"
                @save-data="updateBoard"
                v-bind:boardArr="b"
              />
        <OrderForm v-show="showModal" v-bind:board_id="b.id" @close-modal="togleModal" @save-data="updateOrder"/>
        <ModalImg v-show="showFormImg" @close-alert="togleImgForm" v-bind:board_id="b.id" @save-img="imgUpdate"/>
        <div class="flex justify-between my-4">
          <h1 class="text-2xl">
            <font-awesome-icon icon="hard-drive" class="text-blue-950" />
            Scheda: {{ b.board_name }}
          </h1>
          <div class="flex gap-2">
            <button
              class="hover:bg-blue-500 text-blue-950 font-semibold hover:text-white py-1 px-4 border border-blue-950 rounded"
              @click="togleModal"
            >
              <font-awesome-icon icon="folder-plus" /> Aggiungi ordine
            </button>
            <button
              class="hover:bg-amber-400 text-blue-950 font-semibold hover:text-white py-1 px-4 border border-blue-950 rounded"
              @click="togleForm"
            >
              <font-awesome-icon icon="folder-plus" /> Modifica
            </button>
            <button
              class="hover:bg-red-900 bg-red-600 text-white font-semibold py-1 px-4 border border-blue-950 rounded"
              @click="togleAlert"
            >
              Elimina
            </button>
          </div>
        </div>

        <hr class="my-2" />
        <div class="flex bg-slate-50 p-4 gap-4">
          <div class="col">
  
              
              <img class="h-auto max-w-xs" :src='b.board_img'>
              <button
              class="hover:bg-blue-500 text-blue-950 font-semibold hover:text-white py-1 px-4 border border-blue-950 rounded mt-4"
              @click="togleImgForm"
            >Carica/Modifica</button>
          </div>
          <div class="col">
            <p>
              Codice: <b> {{ b.board_code }}</b>
            </p>
            <p class="mt-2">
              Revisione: <b> {{ b.board_rev }}</b>
            </p>
            
            <p>
              Data di creazione: <b> {{ b.created_at }}</b>
            </p>
            <p class="mt-2">
              Cliente: <b> {{ b.customer }}</b>
            </p>
            

          </div>
        </div>
        <div class="flex justify-between mt-4">
          <h4 class="text-2xl">Ordini</h4>
          <p class="bg-s-100 text-blue-800 text-sm font-medium mr-2 px-2.5 py-0.5 rounded dark:bg-slate-300 dark:text-blue-300">Numero ordini: {{ orderCount }}</p> 
      
        </div>
       
        <hr class="my-2" />
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
              v-for="o in order"
              :key="order.uuid"
            >
              <td class="whitespace-nowrap px-6 py-2 font-medium">
                {{ o.order_number }}
              </td>
              <td class="whitespace-nowrap px-6 py-2">
                {{ o.order_quantity }}
              </td>
              <td class="whitespace-nowrap px-6 py-2">{{ o.created_at }}</td>
              <td class="whitespace-nowrap px-6 py-2">{{ b.board_name }}</td>
              <td class="whitespace-nowrap px-6 py-2">
                <router-link
                  :to="{
                    name: 'order-details',
                    params: { order_number: o.order_number },
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
import { ref, onMounted, computed } from "vue";
import Alert from "../components/Alert.vue";
import OrderForm from "../components/OrderForm.vue";
import BoardForm from "../components/BoardForm.vue";
import ModalImg from "../components/ModalImg.vue";
import { useRouter, useRoute } from "vue-router";

const board = ref([]);
const order = ref([]);


const showAlert = ref(false);
const showModal = ref(false);
const showForm = ref(false);
const showFormImg = ref(false);

const router = useRouter();
const route = useRoute();

const props = defineProps({
  uuid: String,
});

// a computed ref
const orderCount = computed(() => {
  return order.value.length;
});

async function callApi() {
  const endpoint = `${endpoints["boardsCRUD"]}${props.uuid}/`;

  try {
    const response = await axios.get(endpoint);

    board.value.push(response.data);
    order.value = response.data.order;


    console.log(response.data);
  } catch (error) {
    alert(error);
  }
}


async function deleteBoard(uuid) {
  let endpoint = `${endpoints["boardsCRUD"]}${uuid}/`;

  try {
    const response = await axios.delete(endpoint);
    togleAlert();
    router.push({ name: "boards" });
  } catch (error) {
    alert(error);
  }
}


function updateOrder(value) {
  togleModal()
  order.value.unshift(value);
}

function updateBoard(value) {
  togleForm()
  console.log(value)
  board.value[0].board_code = value.board_code
  board.value[0].board_name = value.board_name
  board.value[0].board_rev = value.board_rev
  board.value[0].customer = value.customer

}
function imgUpdate(value) {
  togleImgForm()
  board.value[0].board_img = value.board_img

}

function togleAlert() {
  showAlert.value = !showAlert.value;
}
function togleModal() {
  showModal.value = !showModal.value;
}

function togleForm() {
  showForm.value = !showForm.value;
}
function togleImgForm() {
  showFormImg.value = !showFormImg.value;
}
// lifecycle hooks
onMounted(() => {
  callApi();
  console.log(props.uuid);
});
</script>
