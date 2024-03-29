<template>
  <main>
    <div class="container-fluid flex min-h-screen">
      <div class="w-full">
        <section class="shadow-md px-4 py-16 rounded-md border bg-gray-100">
          <div class="mb-4">
            <div class="mx-auto max-w-xl text-center">
              <!-- <img src="http://127.0.0.1:8000/static/img/logo.png" alt="Mce logo"  width="150"> -->

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

        <!-- Bacheca -->
        <section class="my-4 shadow-md p-4 rounded-md border">
          <h1 class="text-md font-semibold sm:text-2xl my-5 text-blue-900">
            Bacheca:
            <span
              class="bg-green-100 text-green-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded dark:bg-green-900 dark:text-green-300"
              >{{ annuncementsCount }}</span
            >
          </h1>

          <hr class="my-5" />
          <div v-for="an in firstFiveAnnouncement">
            <Annuncement class="my-4" :annuncements="an" />
          </div>
        </section>

        <!-- Ultimi ordini -->
        <section class="my-4 shadow-md p-4 rounded-md border">
          <div class="flex justify-between">
          <h1 class="text-md font-semibold sm:text-2xl  text-lime-600">
            Ultimi 5 ordini:
            
          </h1>
          <span
              class="bg-green-100 text-green-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded dark:bg-green-900 dark:text-green-300"
              >Totale ordini: {{ ordersCount }}</span
            >
            <RouterLink
                  to="/ordini"
                  class="text-sm font-medium hover:text-green-700 underline"
                  >Tutti gli ordini</RouterLink
                >
        </div>
          <hr class="my-5" />
          <div v-for="o in firstFiveOrder">
            <OrderCard class="my-4" :order="o"/>
          </div>
        </section>
      </div>
    </div>

    <QrcodeScan v-if="showScanModal" v-model="showScanModal" />
  </main>
</template>

<script setup>
import QrcodeScan from "../components/QrcodeScan.vue";
import { administrationEndpoint, endpoints } from "../common/endpoints";
import { axios } from "../common/api.service";
import { ref, onMounted, computed } from "vue";
import Annuncement from "../components/Annuncement.vue";
import OrderCard from "../components/OrderCard.vue";

const showScanModal = ref(false);
const isLoading = ref(false);
const announcement = ref([]);
const orders = ref([]);

const togleModalScan = () => {
  showScanModal.value = !showScanModal.value;
};



// Computed
const firstFiveAnnouncement = computed(() => {
  return announcement.value.slice(0, 3);
});
const firstFiveOrder = computed(() => {
  return orders.value.slice(0, 3);
});

const annuncementsCount = computed(() => {
  return announcement.value.length;
});
const ordersCount = computed(() => {
  return orders.value.length;
});
async function callApiTest() {
  let endpoint = administrationEndpoint["announcementCRUD"];
  try {
    const response = await axios.get(endpoint);
    announcement.value.push(...response.data);
    console.log(response.data);
  } catch (error) {
    alert(error);
  }
}




async function callApi() {
  isLoading.value = false;
  try {
    // Test axios all
    axios
      .all([
        axios.get(`${endpoints["ordersCRUD"]}`),
        axios.get(administrationEndpoint["announcementCRUD"]),
      ])
      .then(
        axios.spread((data1, data2) => {
          // output of req.
          orders.value.push(... data1.data);
          announcement.value.push(... data2.data);
         
    
          isLoading.value = true;
        })
      );
  } catch (error) {
    alert(error);
  }
}

// lifecycle hooks
onMounted(() => {
  callApi();
});
</script>
