<template>
  <main>
    <Info v-show="msg" :message="msg" :icon-type="iconType" />
    <div class="p-4 w-full">
      <div class="" v-if="isLoading">
        <router-link :to="{
          name: 'order-details',
          params: { order_number: verify.order_number },
        }" class="hover:text-green-600">
          <font-awesome-icon icon="arrow-left-long" /> Back to {{ verify.order_number }}
        </router-link>
        <hr class="my-4">
      </div>
      <div class="flex justify-between my-4">
        <div>
          <h1 class="text-2xl mb-4 text-blue-900">
            <font-awesome-icon icon="magnifying-glass" />
            Verifica
          </h1>
          <p class="mt-2">Data: {{ useDateFormatted(verify.created_at) }}</p>
          <p class="mt-2">Ordine: {{ verify.order_number }}</p>
        </div>
        <div class="flex gap-2">
          <button v-if="store.isVerifyUser"
            class="hover:bg-amber-400 max-h-8 text-blue-950 font-semibold hover:text-white  px-4 border hover:border-none text-sm border-blue-950 rounded"
            @click="togleVerifyForm">
            Aggiorna
          </button>
        </div>
      </div>
      <hr class="my-2" />
      <div class="flex justify-between my-4">
        <h1 class="text-md font-semibold">Status:</h1>
        <h1 class="text-md">
          <span v-if="verify.status" class="text-white bg-green-700 p-1 px-2 rounded-md">COMPLETATO</span>
          <span v-else class="text-white bg-yellow-400 p-1 px-2 rounded-md">DA COMPLETARE</span>
        </h1>
      </div>
      <hr class="my-4" />
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
      <div class="mt-4 bg-gray-100 p-4 rounded-md">
        <h4 class="text-blue-800 text-sm font-semibold mb-4">Firma operatore:</h4>
        <p class="">{{ verify.firma }}</p>
        <hr>
      </div>
    </div>
    <VerifyForm v-show="showForm" @close-modal="togleVerifyForm" @save-data="updateVerify" v-if="isLoading"
      :verify="verify" />
  </main>
</template>

<script setup>

import { endpoints } from "../common/endpoints";
import { axios } from "../common/api.service";
import { ref, onMounted } from "vue";
import VerifyForm from "../components/VerifyForm.vue";
import Info from "../components/Info.vue"
import { useDateFormatted } from "../use/useDateFormatted";
import { useStoreUser } from "../stores/storeUsers";
// access the `store`
const store = useStoreUser();
const verify = ref({});

const isLoading = ref(false);
const showForm = ref(false);

const iconType = ref(false);
const msg = ref("");


const props = defineProps({
  verify_number: String,
});

async function callApi() {
  const endpoint = `${endpoints["verifyCRUD"]}${props.verify_number}/`;

  try {
    const response = await axios.get(endpoint);

    verify.value = response.data;
    console.log(response.data);
    isLoading.value = true
  } catch (error) {
    alert(error);
  }
}



function updateVerify(value) {
  togleVerifyForm();
  console.log(value)


  if (typeof value === 'number') {
    msg.value = "Aggiornametno non riuscito"
    iconType.value = false
  }
  else {
    verify.value = value
    msg.value = "Aggiornametno avvenuto con successo"
    iconType.value = true
  }


  setTimeout(() => msg.value = "", 5000)
}


function togleVerifyForm() {
  showForm.value = !showForm.value;
}

// lifecycle hooks
onMounted(() => {
  callApi();
  console.log(props.uuid);
});
</script>
