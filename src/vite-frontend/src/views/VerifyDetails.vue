<template>
  <main>
    <div class="container-fluid flex min-h-screen">
      <NavBar />

      <div class="m-4 w-full">
        <div class="flex justify-between my-4">
          <div>
            <h1 class="text-2xl">
              <font-awesome-icon icon="magnifying-glass" />

              Verifica
            </h1>
            <p class="mt-2">Data: {{ verify.created_at }}</p>
            <p class="mt-2">Ordine: {{ verify.order_number }}</p>
          </div>

          <div class="flex gap-2">
            <button
              class="hover:bg-amber-400 max-h-8 text-blue-950 font-semibold hover:text-white  px-4 border hover:border-none text-sm border-blue-950 rounded"
              @click="togleVerifyForm"
            >
              Aggiorna
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

      </div>
    </div>
    <VerifyForm
      v-show="showForm"
      @close-modal="togleVerifyForm"
      @save-data="updateTest"
      v-if="isLoading"
      :verify="verify"
    />
  </main>
</template>

<script setup>
import NavBar from "../components/NavBar.vue";
import { endpoints } from "../common/endpoints";
import { axios } from "../common/api.service";
import { ref, onMounted, computed } from "vue";
import Alert from "../components/Alert.vue";
import VerifyForm from "../components/VerifyForm.vue";
import { useRouter, useRoute } from "vue-router";

const verify = ref({});

const isLoading = ref(false);
const showForm = ref(false);


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
    isLoading.value = true
  } catch (error) {
    alert(error);
  }
}



function updateVerify(value) {
  togleVerifyForm();
  verify.value = value
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
