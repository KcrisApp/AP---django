<template>
  <main>
    <div class="container-fluid flex min-h-screen">
      <div class="my-32 w-full">
        <section class="">
          <div class="mb-4">
            <div class="mx-auto max-w-xl text-center">
              <lottie-animation
                path="../assets/lottie/home.json"
             
              />

              <h1 class="text-3xl font-extrabold sm:text-5xl">
                Benvenuto sul portale
                <strong class="font-extrabold text-blue-800 sm:block">
                  Mce - AP
                </strong>
              </h1>

              <p class="mt-4 sm:text-xl/relaxed">
                Da qui potrai accedere agli ordini in produzione e alle relative
                schede.
              </p>

              <div class="mt-8 flex flex-wrap justify-center gap-4">
                <RouterLink
                  to="/ordini"
                  class="block w-full rounded bg-blue-600 px-12 py-3 text-sm font-medium text-white shadow hover:bg-blue-800 focus:outline-none focus:ring sm:w-auto"
                  >Ordini</RouterLink
                >
                <RouterLink
                  to="/boards"
                  class="block w-full rounded px-12 py-3 text-sm font-medium text-blue-600 shadow hover:text-blue-700 bg-slate-300 hover:bg-slate-400 focus:outline-none focus:ring sm:w-auto"
                  >Schede</RouterLink
                >
                <button
                  @click="togleModalScan"
                  class="block w-full rounded bg-green-600 px-12 py-3 text-sm font-medium text-white shadow hover:bg-green-800 focus:outline-none focus:ring sm:w-auto"
                >
                  QRcode Scan
                </button>
              </div>
            </div>
          </div>
        </section>

        <section class="my-28 mx-5">
          <!-- Bacheca -->

          <h1 class="text-lg font-semibold sm:text-3xl my-5 text-blue-900">
            Bacheca
          </h1>
          <hr class="my-5" />
          <div v-for="an in announcement">
            <Annuncement class="my-4" :annuncements="an" />
          </div>
        </section>
      </div>
    </div>

    <QrcodeScan v-if="showScanModal" v-model="showScanModal" />
  </main>
</template>

<script setup>
import QrcodeScan from "../components/QrcodeScan.vue";
import { administrationEndpoint } from "../common/endpoints";
import { axios } from "../common/api.service";
import { ref, onMounted, computed } from "vue";
import { useDateFormat } from "../use/useDateFormat";
import Annuncement from "../components/Annuncement.vue";

const showScanModal = ref(false);
const announcement = ref([]);

const togleModalScan = () => {
  showScanModal.value = !showScanModal.value;
};

async function callApi() {
  let endpoint = administrationEndpoint["announcementCRUD"];
  try {
    const response = await axios.get(endpoint);
    announcement.value.push(...response.data);
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
