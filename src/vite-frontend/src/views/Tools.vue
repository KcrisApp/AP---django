<template>
  <main>

      <div class="p-4 w-full">
        <h1 class="text-3xl my-4 text-blue-900"><font-awesome-icon icon="toolbox"/> Tools</h1>

        <hr class="my-2"/>

        <div class="grid gap-4 grid-cols-1 xl:grid-cols-4">

     
          <div
            class="max-w-sm p-6 bg-slate-100 border border-gray-100 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700"
          >
          
              <h5
                class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white"
              >
                QR-code scanner
              </h5>
      
            <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">
              Scansiona il QR code per ricercare l'ordine di produzione 
            </p>
            <button @click="togleModalScan"  class="block w-full rounded bg-green-600 px-12 py-3 text-sm font-medium text-white shadow hover:bg-green-800 focus:outline-none focus:ring sm:w-auto"
                  >QRcode Scan</button>
          </div>





          <div
            class="max-w-sm p-6 bg-slate-100 border border-gray-100 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700"
          >
          
              <h5
                class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white"
              >
                BOM Creator
              </h5>
      
            <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">
              Permette di formattare ed esplodere una BOM partendo da un file .xlsx 
            </p>
            <button 
            class="block w-full rounded bg-green-600 px-12 py-3 text-sm font-medium text-white shadow hover:bg-green-800 focus:outline-none focus:ring sm:w-auto">
            <router-link
                  :to="{
                    name: 'test-page',
                   }"
                
                >
                Crea BOM
                
                </router-link>
  

          </button>
          </div>






          
          <div
            class="max-w-sm p-6 bg-slate-100 border border-gray-100 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700"
          >
          
              <h5
                class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white"
              >
                Powatec calculator
              </h5>
      
            <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">
              Permette capire la fattibilita di una scheda sulla P&P manuale
            </p>
            <button 
            class="block w-full rounded bg-green-600 px-12 py-3 text-sm font-medium text-white shadow hover:bg-green-800 focus:outline-none focus:ring sm:w-auto">
            <router-link
                  :to="{
                    name: 'powatec',
                   }"
                
                >
                Powatec
                
                </router-link>
  

          </button>
          </div>
          

        </div>

    </div>
    <QrcodeScan v-if="showScanModal" v-model="showScanModal"/>
  </main>
</template>
<script setup>

import QrcodeScan from "../components/QrcodeScan.vue"
import { ref } from "vue";

const showScanModal = ref(false)

const togleModalScan = () => {
  showScanModal.value = !showScanModal.value
}


</script>
