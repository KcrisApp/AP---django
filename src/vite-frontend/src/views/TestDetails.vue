<template>
  <main>
    <div class="container-fluid flex min-h-screen">
      <NavBar />

      <div class="m-4 w-full">
        <div class="flex justify-between my-4">
          <div>
            <h1 class="text-2xl">
              <font-awesome-icon icon="laptop-code" class="text-blue-950" />

              Collauo: {{ tests.order_number }}
            </h1>
            <p class="mt-2">Data: {{ tests.created_at }}</p>
          </div>

          <div class="flex gap-2">
            <button
              class="hover:bg-amber-400 max-h-8 text-sm text-blue-950 font-semibold hover:text-white py-1 px-4 border hover:border-none border-blue-950 rounded"
              @click="togleTestForm"
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
              v-if="tests.status"
              class="text-white bg-green-700 p-1 px-2 rounded-md"
              >COMPLETATO</span
            >
            <span v-else class="text-white bg-red-700 p-1 px-2 rounded-md"
              >DA COMPLETARE</span
            >
          </h1>
        </div>
        <hr class="my-2" />

        <div class="flex flex-wrap justify-center mt-5">
          <CardCheck :status="tests.ict" text="ICT" />
          <CardCheck :status="tests.aoi" text="AOI" />
          <CardCheck :status="tests.xray" text="X-Ray" />
          <CardCheck :status="tests.functional" text="Funzionale" />
        </div>

        <div class="mt-4 bg-gray-100 p-4 rounded-md">
          <h4 class="text-blue-800 text-sn font-semibold">Non conformita:</h4>
          <hr class="my-1" />
          <p>{{ tests.non_compliance }}</p>
        </div>
        <div class="mt-4 bg-gray-100 p-4 rounded-md">
          <h4 class="text-blue-800 text-sm font-semibold">
            Componenti mancanti:
          </h4>
          <hr class="my-1" />
          <p>{{ tests.missing_component }}</p>
        </div>
        <div class="mt-4 bg-gray-100 p-4 rounded-md">
          <h4 class="text-blue-800 text-sm font-semibold">Note:</h4>
          <hr class="my-1" />
          <p>{{ tests.note }}</p>
        </div>
        <div class="mt-4 bg-gray-100 p-4 rounded-md">
          <h4 class="text-blue-800 text-sm font-semibold">Serial number:</h4>
          <hr class="my-1" />
          <p>{{ tests.serialnumber }}</p>
        </div>

     
      </div>
    </div>
    <TestForm
      v-show="showForm"
      @close-modal="togleTestForm"
      @save-data="togleTestForm"
      v-if="isLoading"
      :tests="tests"
    />
  </main>
</template>
<script setup>
import NavBar from "../components/NavBar.vue";
import { endpoints } from "../common/endpoints";
import { axios } from "../common/api.service";
import { ref, onMounted, computed } from "vue";
import Alert from "../components/Alert.vue";
import TestForm from "../components/TestForm.vue";
import BoardForm from "../components/BoardForm.vue";
import ModalImg from "../components/ModalImg.vue";
import CardCheck from "../components/CardCheck.vue";
import { useRouter, useRoute } from "vue-router";

const tests = ref({});
const showForm = ref(false);

const props = defineProps({
  test_number: String,
});

const isLoading = ref(false);

async function callApi() {
  const endpoint = `${endpoints["testCRUD"]}${props.test_number}/`;

  try {
    const response = await axios.get(endpoint);

    tests.value = response.data;
    isLoading.value = true;
  } catch (error) {
    alert(error);
  }
}

console.log(tests);

function updateTest(value) {
  togleTestForm();
  tests.value=value
}


function togleTestForm() {
  showForm.value = !showForm.value;
}

// lifecycle hooks
onMounted(() => {
  callApi();
});
</script>
