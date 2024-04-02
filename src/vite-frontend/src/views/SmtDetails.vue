<template>
  <main>
   
      <div class="p-4 w-full">
        <Info v-show="msg" :message="msg" :icon-type="iconType" />

        <div class="" v-if="isLoading">
        <router-link
                  :to="{
                    name: 'order-details',
                    params: { order_number:smt.order_number  },
                  }"
                  class="hover:text-green-600"
                >
                <font-awesome-icon icon="arrow-left-long" /> Back to {{ smt.order_number }}
                
                </router-link>
                <hr class="my-4">
        </div>


        <div class="flex justify-between my-4">
          <div>
            <h1 class="text-2xl mb-4 text-blue-900">
              <font-awesome-icon icon="microchip" />

              SMT 
            </h1>
            <p class="mt-2">Data: {{ useDateFormat(smt.created_at) }}</p>
            <p class="mt-2">Ordine: {{ smt.order_number }}</p>
          </div>

          <div class="flex gap-2">
            <button
            v-if="store.isSmtUser"
            class="hover:bg-amber-400 max-h-8 text-sm text-blue-950 font-semibold hover:text-white py-1 px-4 border hover:border-none border-blue-950 rounded"
              @click="togleSmtForm"
            >
              Aggiorna
            </button>
          
            
          </div>
        </div>

        <hr class="my-2" />
        <div class="flex justify-between my-4 ">
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
        <div class="mt-4 bg-gray-100 p-4 rounded-md">
          <h4 class="text-blue-800 text-sm font-semibold mb-4">Firma operatore:</h4>
          <p class="">{{ smt.firma }}</p>
          <hr>
        </div>
       
    
      </div>

    <SmtForm
      v-show="showForm"
      @close-modal="togleSmtForm"
      @save-data="updateSmt"
      v-if="isLoading"
      :smt="smt"
    />
  </main>
</template>
<script setup>

import { endpoints } from "../common/endpoints";
import { axios } from "../common/api.service";
import { ref, onMounted } from "vue";
import SmtForm from "../components/SmtForm.vue";
import CardCheck from "../components/CardCheck.vue";
import  Info from "../components/Info.vue"
import {useDateFormat } from "../use/useDateFormat"
import { useStoreUser } from "../stores/storeUsers";
// access the `store`
const store = useStoreUser();

const smt = ref({});



const showForm = ref(false);
const isLoading = ref(false);
const iconType = ref(false);
const msg = ref("");

const props = defineProps({
  smt_number: String,
});



async function callApi() {
  const endpoint = `${endpoints["smtCRUD"]}${props.smt_number}/`;

  try {
    const response = await axios.get(endpoint);

    smt.value = response.data;
    console.log(response.data);
    isLoading.value = true

  } catch (error) {
    alert(error);
  }
}



function updateSmt(value) {
  togleSmtForm();


  if (typeof value === 'number') {
      msg.value =  "Aggiornametno non riuscito"
      iconType.value =  false
  }
  else{
  smt.value = value; 
  msg.value =  "Aggiornametno avvenuto con successo"
  iconType.value =  true
  }
  

  setTimeout(() => msg.value = "", 5000)
}


function togleSmtForm() {
  showForm.value = !showForm.value;
}


// lifecycle hooks
onMounted(() => {
  callApi();

});
</script>
