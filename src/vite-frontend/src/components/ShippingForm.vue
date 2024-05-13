<template>
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-900 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div
          class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
          <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
            <div class="">
              <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                <h2 class="text-base font-semibold leading-6 text-gray-900 mb-6" id="modal-title">
                  <b>Aggiungi spedizione </b>
                </h2>
                <hr class="mb-4" />
                <div class="mt-2">
                  <form @submit.prevent="sentData">
                    <div class="mb-6">
                      <input id="shipping_check" name="shipping_check" type="checkbox" v-model="shipping_check"
                        class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500" />
                      <label for="shipping_check"
                        class="w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">Collaudo</label>
                    </div>

                    <div class="mb-6">
                      <label for="qta"
                        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Quantità</label>
                      <input type="number" min="0" :max="max_board" step="1" id="qta"
                        class="text-center bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        required v-model="shipping_quantity" />
                    </div>
                    <div class="mb-6">
                      <label for="shipping_date"
                        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Data</label>
                      <input id="shipping_date" name="shipping_date" type="datetime-local"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        placeholder="Select date" v-model="shipping_date">
                    </div>
                    <div class="mb-6">
                      <label for="shipping_missing_components"
                        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Componenti mancanti</label>
                      <textarea v-model="shipping_missing_components"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        name="shipping_missing_components" id="shipping_missing_components" cols="30"
                        rows="3"></textarea>
                    </div>
                    <hr>
                    <div class="mb-6 mt-4">
                      <label for="firma" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Firma
                        operatore</label>
                      <input type="text" id="firma"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        placeholder="" required v-model="firma" />
                    </div>
                    <div class=" px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                      <button type="submit"
                        class="mt-3 inline-flex w-full justify-center mx-2 rounded-md px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-green-500 hover:text-white sm:mt-0 sm:w-auto">
                        Save
                      </button>
                      <button type="button"
                        class="mt-3 inline-flex w-full justify-center rounded-md px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-red-800 hover:text-white sm:mt-0 sm:w-auto"
                        @click="triggerCloseModal">
                        Cancel
                      </button>
                    </div>
                  </form>
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
import { ref, defineEmits, computed } from "vue";
import { endpoints } from "../common/endpoints";
import { axios } from "../common/api.service";


const props = defineProps({

  order: {
    type: String,
    required: false,
  },
  ship: {
    type: Object,
    required: false
  },
  max_shipping_board: {
    type: Number,
    required: true
  },
});


var tzoffset = (new Date()).getTimezoneOffset() * 60000;
const date = new Date(Date.now() - tzoffset).toISOString().slice(0, 16)



const shipping_quantity = ref(0);
const shipping_date = ref(date);
const shipping_check = ref(false);
const shipping_missing_components = ref("");
const firma = ref("");

const max_board = ref(props.max_shipping_board)


const emit = defineEmits(["close-modal", "save-data"]);


if (props.ship) {

  const d = (new Date(props.ship.shipping_date).getTime()) - tzoffset
  const date = new Date(d).toISOString().slice(0, 16)

  shipping_quantity.value = props.ship.shipping_qta
  shipping_date.value = date
  shipping_check.value = props.ship.shipping_check
  shipping_missing_components.value = props.ship.shipping_missing_components
  firma.value = props.ship.firma

  max_board.value = props.max_shipping_board + shipping_quantity.value
}


async function sentData() {
  let endpoint = endpoints["shippingCRUD"];
  let method = "POST";

  if (props.ship) {
    endpoint += `${props.ship.uuid}/`;
    method = "PUT"
  }


  try {
    const response = await axios({
      method: method,
      url: endpoint,
      data: {
        shipping_qta: shipping_quantity.value,
        shipping_check: shipping_check.value,
        shipping_date: shipping_date.value,
        shipping_missing_components: shipping_missing_components.value,
        firma: firma.value,
        order: props.order,

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
