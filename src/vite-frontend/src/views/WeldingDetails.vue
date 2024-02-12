<template>
  <main>
      <div class="p-4 w-full">
        <div class="" v-if="isLoading">
        <router-link
                  :to="{
                    name: 'order-details',
                    params: { order_number:welding.order_number  },
                  }"
                  class="hover:text-green-600"
                >
                <font-awesome-icon icon="arrow-left-long" /> Back to {{ welding.order_number }}
                
                </router-link>
                <hr class="my-4">
        </div>


        <div class="flex justify-between my-4">
          <div>
            <h1 class="text-2xl mb-4 text-blue-900">
              <font-awesome-icon icon="tarp-droplet" />

              Saldatura 
            </h1>
            
            <p class="mt-2">Data: {{ welding.created_at }}</p>
            <p class="mt-2">Ordine: {{ welding.order_number }}</p>
          </div>

          <div class="flex gap-2">
            <button
            class="hover:bg-amber-400 max-h-8 text-sm text-blue-950 font-semibold hover:text-white py-1 px-4 border hover:border-none border-blue-950 rounded"
              @click="togleWeldingForm"
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
              v-if="welding.status"
              class="text-white bg-green-700 p-1 px-2 rounded-md"
              >COMPLETATO</span
            >
            <span v-else class="text-white bg-yellow-400 p-1 px-2 rounded-md"
              >DA COMPLETARE</span
            >
          </h1>
        </div>
        <hr class="my-4" />


        <h1 class="text-xl text-center font-semibold mt-4">Macchinari e programmi</h1>
        <div class="flex justify-between p-4 bg-gray-100 rounded-lg mt-2">
          <h1 class="text-blue-800 text-sm font-semibold">Macchina:</h1>
          <h1 class="text-sm">
            <span
              v-if="welding.soldering_type"
              class="text-white bg-cyan-600 p-1 px-2 rounded-md"
              >Saldatrice Selettiva</span
            >
            <span v-else class="text-white bg-orange-600 p-1 px-2 rounded-md"
              >Saldatrice ad Onda</span
            >
          </h1>
        </div>

          
          <div class="mt-4 bg-gray-100 p-4 rounded-md">
          <h4 class="text-blue-800 text-sm font-semibold">
          Programma di saldatura:
          </h4>
          <hr class="my-1" />
          <p>{{ welding.soldering_program }}</p>
        </div>
        

      

        <h1 class="text-xl text-center font-semibold mt-4">Info</h1>
        <div class="mt-4 bg-gray-100 p-4 rounded-md">
          <h4 class="text-blue-800 text-sm font-semibold">
            Componenti mancanti:
          </h4>
          <hr class="my-1" />
          <p>{{ welding.missing_component }}</p>
        </div>
        <div class="mt-4 bg-gray-100 p-4 rounded-md">
          <h4 class="text-blue-800 text-sm font-semibold">Note:</h4>
          <hr class="my-1" />
          <p>{{ welding.note }}</p>
        </div>
        <div class="mt-4 bg-gray-100 p-4 rounded-md">
          <h4 class="text-blue-800 text-sm font-semibold mb-4">Firma operatore:</h4>
          <p class="">{{ welding.firma }}</p>
          <hr>
        </div>
       
    
      </div>

    <WeldingForm
      v-show="showForm"
      @close-modal="togleWeldingForm"
      @save-data="updateWelding"
      v-if="isLoading"
      :welding="welding"
    />
  </main>
</template>
<script setup>

import { endpoints } from "../common/endpoints";
import { axios } from "../common/api.service";
import { ref, onMounted, computed } from "vue";
import WeldingForm from "../components/WeldingForm.vue";
import CardCheck from "../components/CardCheck.vue";


const welding = ref({});



const showForm = ref(false);
const isLoading = ref(false);


const props = defineProps({
  welding_number: String,
});



async function callApi() {
  const endpoint = `${endpoints["weldingCRUD"]}${props.welding_number}/`;

  try {
    const response = await axios.get(endpoint);

    welding.value = response.data;
    console.log(response.data);
    isLoading.value = true

  } catch (error) {
    alert(error);
  }
}



function updateWelding(value) {
  togleWeldingForm();
  welding.value = value;
}


function togleWeldingForm() {
  showForm.value = !showForm.value;
}


// lifecycle hooks
onMounted(() => {
  callApi();

});
</script>
