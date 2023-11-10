<template>
  <main>
    <div class="container-fluid flex min-h-screen">
      <NavBar />

      <div class="m-4 w-full">
        <div class="flex justify-between my-4">
          <div>
            <h1 class="text-2xl">
              <font-awesome-icon icon="microchip" />

              SMT 
            </h1>
            <p class="mt-2">Data: {{ smt.created_at }}</p>
            <p class="mt-2">Ordine: {{ smt.order_number }}</p>
          </div>

          <div class="flex gap-2">
            <button
            class="hover:bg-amber-400 max-h-8 text-sm text-blue-950 font-semibold hover:text-white py-1 px-4 border hover:border-none border-blue-950 rounded"
              @click="togleForm"
            >
              Aggiorna
            </button>
            <button
            class="hover:bg-red-900 max-h-8 text-sm bg-red-600 text-white font-semibold py-1 px-4 rounded"
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
              v-if="smt.status"
              class="text-white bg-green-700 p-1 px-2 rounded-md"
              >COMPLETATO</span
            >
            <span v-else class="text-white bg-yellow-400 p-1 px-2 rounded-md"
              >DA COMPLETARE</span
            >
          </h1>
        </div>
        <hr class="my-4" />

        <h1 class="text-xl text-center font-semibold">Controlli</h1>
        <div class="flex flex-wrap justify-center mt-5 p-2 bg-gray-100 rounded-lg">
          <CardCheck :status="smt.fridge_temperature" text="Temperatura frigo" />
          <CardCheck :status="smt.cream_expiration" text="Scadenza crema" />
          <CardCheck :status="smt.cream_deposit" text="Deposito crema" />
          <CardCheck :status="smt.pick_and_place_setup" text="P&P status" />
          <CardCheck :status="smt.frame_status" text="Stato telaio" />
          <CardCheck :status="smt.board_check" text="Controllo scheda" />
          <CardCheck :status="smt.oven_parameters" text="Parametri del forno" />
         
        </div>
     
        <div class="flex justify-between p-4 bg-gray-100 rounded-lg mt-2">
          <h1 class="text-blue-800 text-sm font-semibold">Status controlli:</h1>
          <h1 class="text-sm">
            <span
              v-if="smt.check_status"
              class="text-white bg-green-700 p-1 px-2 rounded-md"
              >PASS</span
            >
            <span v-else class="text-white bg-red-700 p-1 px-2 rounded-md"
              >FAIL</span
            >
          </h1>
        </div>

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
          <h1 class="text-xl text-center font-semibold mt-4">Pick and Place</h1>
          <div class="mt-4 bg-gray-100 p-4 rounded-md">
          <h4 class="text-blue-800 text-sm font-semibold">
          Programma Mydata:
          </h4>
          <hr class="my-1" />
          <p>{{ smt.mydata_program }}</p>
        </div>
        <h1 class="text-xl text-center font-semibold mt-4">Forni</h1>
        <div class="flex justify-around rounded-lg mt-2 gap-2">
          <div class="mt-4 bg-gray-100 p-4 rounded-md flex-1">
          <h4 class="text-blue-800 text-sm font-semibold">Forno TOP:</h4>
          <hr class="my-1" />
          <p>{{ smt.oven_top }}</p>
        </div>

        <div class="mt-4 bg-gray-100 p-4 rounded-md flex-1">
          <h4 class="text-blue-800 text-sm font-semibold">Forno BOT:</h4>
          <hr class="my-1" />
          <p>{{ smt.oven_bot }}</p>
        </div>

        </div>
        <div class="flex justify-around rounded-lg mt-2 gap-2">
          <div class="mt-4 bg-gray-100 p-4 rounded-md flex-1">
          <h4 class="text-blue-800 text-sm font-semibold">Profilo forno TOP:</h4>
          <hr class="my-1" />
          <p>{{ smt.recast_profile_top }}</p>
        </div>

        <div class="mt-4 bg-gray-100 p-4 rounded-md flex-1">
          <h4 class="text-blue-800 text-sm font-semibold">Profilo forno BOT:</h4>
          <hr class="my-1" />
          <p>{{ smt.recast_profile_bot }}</p>
        </div>

        </div>
        <h1 class="text-xl text-center font-semibold mt-4">Serigrafia</h1>
        <div class="flex justify-around rounded-lg mt-2 gap-2">
          <div class="mt-4 bg-gray-100 p-4 rounded-md flex-1">
          <h4 class="text-blue-800 text-sm font-semibold">My500 TOP:</h4>
          <hr class="my-1" />
          <p>{{ smt.my500_top }}</p>
        </div>

        <div class="mt-4 bg-gray-100 p-4 rounded-md flex-1">
          <h4 class="text-blue-800 text-sm font-semibold">My500 BOT:</h4>
          <hr class="my-1" />
          <p>{{ smt.my500_bot }}</p>
        </div>

        </div>



        <div class="flex justify-around rounded-lg mt-2 gap-2">
          <div class="mt-4 bg-gray-100 p-4 rounded-md flex-1">
          <h4 class="text-blue-800 text-sm font-semibold">Telaio serigrafico TOP:</h4>
          <hr class="my-1" />
          <p>{{ smt.screen_printer_top }}</p>
        </div>

        <div class="mt-4 bg-gray-100 p-4 rounded-md flex-1">
          <h4 class="text-blue-800 text-sm font-semibold">Telaio serigrafico BOT:</h4>
          <hr class="my-1" />
          <p>{{ smt.screen_printer_bot }}</p>
        </div>

        </div>








        <div class="flex justify-around rounded-lg mt-2 gap-2">
         
        <div class="mt-4 bg-gray-100 p-4 rounded-md flex-1">
          <h4 class="text-blue-800 text-sm font-semibold">
          Tipo crema:
          </h4>
          <hr class="my-1" />
          <p>{{ smt.cream_type }}</p>
        </div>

        <div class="mt-4 bg-gray-100 p-4 rounded-md flex-1">
          <CardCheck :status="smt.cream_test" text="Controllo crema" />
        </div>

        </div>







        <h1 class="text-xl text-center font-semibold mt-4">Info</h1>
        <div class="mt-4 bg-gray-100 p-4 rounded-md">
          <h4 class="text-blue-800 text-sm font-semibold">
            Componenti mancanti:
          </h4>
          <hr class="my-1" />
          <p>{{ smt.missing_component }}</p>
        </div>
        <div class="mt-4 bg-gray-100 p-4 rounded-md">
          <h4 class="text-blue-800 text-sm font-semibold">Note:</h4>
          <hr class="my-1" />
          <p>{{ smt.note }}</p>
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

const smt = ref("");

const showAlert = ref(false);
const showModal = ref(false);
const showForm = ref(false);
const showFormImg = ref(false);

const router = useRouter();
const route = useRoute();

const props = defineProps({
  smt_number: String,
});

// a computed ref
const orderCount = computed(() => {
  return order.value.length;
});

async function callApi() {
  const endpoint = `${endpoints["smtCRUD"]}${props.smt_number}/`;

  try {
    const response = await axios.get(endpoint);

    smt.value = response.data;
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

// lifecycle hooks
onMounted(() => {
  callApi();
  console.log(props.uuid);
});
</script>
