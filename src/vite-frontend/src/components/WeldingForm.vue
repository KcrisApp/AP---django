<template>
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-900 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div
          class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-3xl">
          <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
            <div class="">
              <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                <div class="flex justify-between my-4">
                  <h2 class="text-base font-semibold leading-6 p-2 text-gray-900" id="modal-title">
                    <b class="text-blue-900">Aggiorna saldatura</b>
                  </h2>
                  <div class="flex items-center">
                    <label for="status" class="block mr-2 text-md font-medium  dark:text-white">Status:</label>
                    <select v-model="status" id="status"
                      class="p-2 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 block w-full dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                      <option selected value=false>Da completare</option>
                      <option value=true>Completate</option>
                    </select>
                  </div>
                </div>
                <hr class="mb-4" />
                <h3 class="mb-4 font-semibold text-gray-900 dark:text-white text-center">
                  Macchina
                </h3>
                <div class="flex items-center">
                  <label for="soldering_type" class="block mr-2 text-md font-medium  dark:text-white">Macchina:</label>
                  <select v-model="soldering_type" id="soldering_type"
                    class="p-2 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 block w-full dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                    <option selected value=false>Saldatrice selettiva</option>
                    <option value=true>Saldatrice ad onda</option>
                  </select>
                </div>
                <hr class="my-5">
                <div class="mt-4">
                  <div class="mb-6">
                    <label for="soldering_program"
                      class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Programma di
                      saldatura</label>
                    <input type="text" id="soldering_program"
                      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                      placeholder="" required v-model="soldering_program" />
                  </div>
                  <h3 class="mb-4 font-semibold text-gray-900 dark:text-white text-center">
                    Info
                  </h3>
                  <hr class="my-5">
                  <div class="mb-6">
                    <label for="note" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Note di
                      processo</label>
                    <textarea v-model="note"
                      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                      name="note" id="note" cols="30" rows="3"></textarea>
                  </div>
                  <div class="mb-6">
                    <label for="missing_component"
                      class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Componenti mancanti</label>
                    <textarea v-model="missing_component"
                      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                      name="missing_component" id="missing_component" cols="30" rows="3"></textarea>
                  </div>
                  <hr>
                  <div class="mb-6 mt-4">
                    <label for="firma" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Firma
                      operatore</label>
                    <input type="text" id="firma"
                      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                      placeholder="" required v-model="firma" />
                  </div>
                  <div class="px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                    <button @click="sentData"
                      class="mt-3 inline-flex w-full justify-center mx-2 rounded-md px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-green-500 hover:text-white sm:mt-0 sm:w-auto">
                      Save
                    </button>
                    <button
                      class="mt-3 inline-flex w-full justify-center rounded-md px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-red-800 hover:text-white sm:mt-0 sm:w-auto"
                      @click="triggerCloseModal">
                      Cancel
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, defineEmits } from "vue";
import { endpoints } from "../common/endpoints";
import { axios } from "../common/api.service";


const props = defineProps({

  welding: {
    type: Object,
    required: false,
  },
});

const note = ref(props.welding.note);
const missing_component = ref(props.welding.missing_component);
const firma = ref(props.welding.firma);
const soldering_type = ref(props.welding.soldering_type);
const soldering_program = ref(props.welding.soldering_program)
const status = ref(props.welding.status);

const emit = defineEmits(["close-modal", "save-data"]);



async function sentData() {

  let endpoint = endpoints["weldingCRUD"] + `${props.welding.uuid}/`;
  let method = "PATCH";

  try {
    const response = await axios({
      method: method,
      url: endpoint,
      data: {
        soldering_type: soldering_type.value,
        soldering_program: soldering_program.value,
        note: note.value,
        missing_component: missing_component.value,
        firma: firma.value,
        status: status.value,
      },

    });
    emit("save-data", response.data);


  } catch (error) {

    emit("save-data", error.response.status);

  }
}
function triggerCloseModal() {
  // emit an event to delete an answer instance
  emit("close-modal");
}




</script>
