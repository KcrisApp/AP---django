<template>
  <div
    class="relative z-10"
    aria-labelledby="modal-title"
    role="dialog"
    aria-modal="true"
  >
    <div
      class="fixed inset-0 bg-gray-900 bg-opacity-75 transition-opacity"
    ></div>

    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div
        class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0"
      >
        <div
          class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-3xl"
        >
          <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
            <div class="">
              <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">

                <div class="flex justify-between my-4">

                  <h2
                  class="text-base font-semibold leading-6 p-2 text-gray-900"
                  id="modal-title"
                >
                  <b class="text-blue-900">Aggiungi step</b>
                </h2>

                  <div class="flex items-center">
                    <label for="color" class="block mr-2 text-md font-medium  dark:text-white">Step color:</label>
                    <input
                        id="color"
                        type="color"
                        v-model="step_color"
                        class=""
                      />
                    </div>
                </div>
                

               
                <hr class="my-5">
                <div class="mt-4">
                  <div>
                    <div class="mb-6">
                      <label
                        for="orderNumber"
                        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                        >Step name</label
                      >
                      <input
                        type="text"
                        id="orderNumber"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        placeholder=""
                        required
                        v-model="step_name"
                      />
                    </div>

                    <div class="mb-6">
                      <label
                        for="orderNumber"
                        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                        >Ordine del processo</label
                      >
                      <input
                        type="number"
                        id="orderNumber"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        placeholder=""
                        required
                        v-model="step_order"
                      />
                    </div>
                    
                    <div class="mb-6">
                      <label
                        for="procesNote"
                        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                        >Descrizione del processo</label
                      >
                      <textarea
                        v-model="step_description"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        name="procesNote"
                        id="procesNote"
                        cols="30"
                        rows="3"
                      ></textarea>
                  
                    </div>
                    <div class="mb-6">
                      <label
                        for="procesNote"
                        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                        >Zona del process</label
                      >
                      <select v-model="step_type" id="countries" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                        <option selected value="Verifica">Verifica</option>
                        <option value="Smt">Smt</option>
                        <option value="Collaudo">Collaudo</option>
                        <option value="Saldatura Onda">Saldatura Onda</option>
                        <option value="Saldatura selettiva">Saldatura selettiva</option>
                        <option value="Preformatura">Preformatura</option>
                      </select>
                  
                    </div>
                   
                

                    <div class="px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                      <button
                       @click="sentData"
                        class="mt-3 inline-flex w-full justify-center mx-2 rounded-md px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-green-500 hover:text-white sm:mt-0 sm:w-auto"
                      >
                        Save
                      </button>
                      <button
                     
                        class="mt-3 inline-flex w-full justify-center rounded-md px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-red-800 hover:text-white sm:mt-0 sm:w-auto"
                        @click="triggerCloseModal"
                      >
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
  </div>
</template>

<script setup>
import { ref, defineEmits } from "vue";
import { endpoints } from "../common/endpoints";
import { axios } from "../common/api.service";


const props = defineProps({
 
  steps: {
    type: Object,
    required: false,
  },
  board: {
    type: Number,
    required: true,
  },
});

const step_color = ref("#B41F1F");
const step_order = ref(1);
const step_description = ref("");
const step_name = ref("");
const step_type = ref("Verifica");



// const note = ref(props.tests.note);
// const non_compliance = ref(props.tests.non_compliance);
// const missing_component = ref(props.tests.missing_component);
// const serialnumber = ref(props.tests.serialnumber);

// const ict = ref(props.tests.ict);
// const aoi = ref(props.tests.aoi);
// const xray = ref(props.tests.xray);
// const functional = ref(props.tests.functional);
// const status = ref(props.tests.status);

const emit = defineEmits(["close-modal", "save-data"]);

if(props.steps){
  console.log(props.steps)
        step_type.value = props.steps.step_type
        step_name.value = props.steps.step_name
        step_description.value = props.steps.step_description
        step_color.value = props.steps.step_color
        step_order.value = props.steps.step_order
}

async function sentData() {

  try {
    let method = "POST";
    let endpoint = endpoints["productionstepCRUD"];

    if (props.steps) {
    
    endpoint = endpoints["productionstepCRUD"]+`${props.steps.uuid}/`;
    method = "PATCH";

  }


    const response = await axios({
      method: method,
      url: endpoint,
      data: {
        step_type: step_type.value,
        step_name: step_name.value,
        step_description: step_description.value,
        step_color: step_color.value,
        step_order: step_order.value,
        board: props.board
      },

    });
    emit("save-data", response.data);

   
  } catch (error) {
    error = error;
    alert(error);
  }
}
function triggerCloseModal() {
  // emit an event to delete an answer instance
  emit("close-modal");
}

 


</script>
