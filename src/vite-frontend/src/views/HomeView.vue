<template>
  <main>
    <div class="container-fluid flex min-h-screen">
      <div class="my-32 w-full">
        <section class="">
          <div class="mb-4">
            <div class="mx-auto max-w-xl text-center">
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
                  class="block w-full rounded px-12 py-3 text-sm font-medium text-blue-600 shadow hover:text-blue-700 hover:bg-slate-100 focus:outline-none focus:ring sm:w-auto"
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
          <div
            class="block rounded-lg bg-white shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)] dark:bg-neutral-700"
          >
            <div
              class="border-b-2 border-neutral-100 px-6 py-3 dark:border-neutral-600 dark:text-neutral-50"
            >
            <div class="flex">

              <font-awesome-icon
                    icon="circle-info"
                    class="text-4xl text-blue-800"
                  />
                  <p class="text-sm font-semibold leading-6 text-gray-900 ml-4 pt-2">
                    COMUNICATO
                  </p>
            </div>
            </div>
            <div class="p-6">
              <h5
                class="mb-2 text-xl font-medium leading-tight text-neutral-800 dark:text-neutral-50"
              >
                Special title treatment
              </h5>
              <p class="mb-4 text-base text-neutral-600 dark:text-neutral-200">
                With supporting text below as a natural lead-in to additional
                content.
              </p>
              <p class="font-semibold leading-6 text-gray-900 text-sm">
                 Data: <time datetime="2023-01-23T13:23Z">10-12-2023</time>
                </p>
              <button
                class="mt-4 block w-full rounded bg-green-600 px-6 py-2 text-sm font-medium text-white shadow hover:bg-green-800 focus:outline-none focus:ring sm:w-auto"
              >
                Leggi
              </button>
            </div>
          </div>
        </section>
      </div>
    </div>

    <QrcodeScan v-if="showScanModal" v-model="showScanModal" />
  </main>
</template>
<script setup>
import QrcodeScan from "../components/QrcodeScan.vue";
import { ref } from "vue";

const showScanModal = ref(false);

const togleModalScan = () => {
  showScanModal.value = !showScanModal.value;
};
</script>
