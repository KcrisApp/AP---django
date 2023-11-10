<template>
  <main>
    <div class="container-fluid flex min-h-screen">
      <NavBar />

      <div class="m-4 w-full">
        <div class="flex justify-between my-4">
          <div>
            <h1 class="text-2xl">
              <font-awesome-icon icon="laptop-code" class="text-blue-950" />

              Collauo: {{ verify.order_number }}
            </h1>
            <p class="mt-2">Data: {{ verify.created_at }}</p>
          </div>

          <div class="flex gap-2">
            <button
              class="hover:bg-amber-400 max-h-8 text-blue-950 font-semibold hover:text-white  px-4 border hover:border-none text-sm border-blue-950 rounded"
              @click="togleForm"
            >
              Aggiorna
            </button>
            <button
              class="hover:bg-red-900 max-h-8 bg-red-600 text-white font-semibold  px-4 rounded text-sm"
              @click="togleAlert"
            >
              Elimina
            </button>
          </div>
        </div>

        <hr class="my-2" />
        <div class="flex justify-between my-4">
          <h1 class="text-md font-semibold">Status:</h1>
          <h1 class="text-md">
            <span
              v-if="verify.status"
              class="text-white bg-green-700 p-1 px-2 rounded-md"
              >COMPLETATO</span
            >
            <span v-else class="text-white bg-yellow-400 p-1 px-2 rounded-md"
              >DA COMPLETARE</span
            >
          </h1>
        </div>
        <hr class="my-4" />

        <!-- <div class="flex bg-slate-50 p-4 gap-4">
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
        
          </div> -->

        <div class="mt-4 bg-gray-100 p-4 rounded-md">
          <h4 class="text-blue-800 text-sm font-semibold">Modifiche dopo collaudo:</h4>
          <hr class="my-1" />
          <p class="text-sm">{{ verify.changes_after_testing }}</p>
        </div>

        <div class="mt-4 bg-gray-100 p-4 rounded-md">
          <h4 class="text-blue-800 text-sm font-semibold">
            Componenti mancanti:
          </h4>
          <hr class="my-1" />
          <p class="text-sm">{{ verify.missing_component }}</p>
        </div>
        <div class="mt-4 bg-gray-100 p-4 rounded-md">
          <h4 class="text-blue-800 text-sm font-semibold">Lavorazioni manuali:</h4>
          <hr class="my-1" />
          <p class="text-sm">{{ verify.manual_work }}</p>
        </div>

        <!-- <table class="text-left text-sm font-light flex-wrap w-full">
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
          </table> -->
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
import CardCheck from "../components/CardCheck.vue";
import { useRouter, useRoute } from "vue-router";

const verify = ref("");

const showAlert = ref(false);
const showModal = ref(false);
const showForm = ref(false);
const showFormImg = ref(false);

const router = useRouter();
const route = useRoute();

const props = defineProps({
  verify_number: String,
});

async function callApi() {
  const endpoint = `${endpoints["verifyCRUD"]}${props.verify_number}/`;

  try {
    const response = await axios.get(endpoint);

    verify.value = response.data;
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
  togleModal();
  order.value.unshift(value);
}

function updateBoard(value) {
  togleForm();
  console.log(value);
  board.value[0].board_code = value.board_code;
  board.value[0].board_name = value.board_name;
  board.value[0].board_rev = value.board_rev;
  board.value[0].customer = value.customer;
}
function imgUpdate(value) {
  togleImgForm();
  board.value[0].board_img = value.board_img;
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
