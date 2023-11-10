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

                <div class="flex justify-around my-4">

                  <h2
                  class="text-base font-semibold leading-6 text-gray-900"
                  id="modal-title"
                >
                  <b>Aggiorna test</b>
                </h2>

                  <div class="flex items-center">
                      <input
                        id="vue-checkbox-list"
                        type="checkbox"
                        value=""
                        class="w-4  text-blue-600 bg-gray-100 border-gray-300 rounded  dark:ring-offset-gray-700   dark:bg-gray-600 dark:border-gray-500"
                      />
                      <label
                        for="vue-checkbox-list"
                        class="w-full ms-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                        >STATUS</label
                      >
                    </div>
                </div>
                




                <hr class="mb-4" />

                <h3 class="mb-4 font-semibold text-gray-900 dark:text-white text-center">
                  Test
                </h3>
                <ul
                  class="items-center w-full text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg sm:flex dark:bg-gray-700 dark:border-gray-600 dark:text-white"
                >
                  <li
                    class="w-full border-b border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600"
                  >
                    <div class="flex items-center ps-3">
                      <input
                        id="vue-checkbox-list"
                        type="checkbox"
                        value=""
                        class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded  dark:ring-offset-gray-700   dark:bg-gray-600 dark:border-gray-500"
                      />
                      <label
                        for="vue-checkbox-list"
                        class="w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                        >Ict</label
                      >
                    </div>
                  </li>
                  <li
                    class="w-full border-b border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600"
                  >
                    <div class="flex items-center ps-3">
                      <input
                        id="react-checkbox-list"
                        type="checkbox"
                        value=""
                        class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500"
                      />
                      <label
                        for="react-checkbox-list"
                        class="w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                        >AOI</label
                      >
                    </div>
                  </li>
                  <li
                    class="w-full border-b border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600"
                  >
                    <div class="flex items-center ps-3">
                      <input
                        id="angular-checkbox-list"
                        type="checkbox"
                        value=""
                        class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500"
                      />
                      <label
                        for="angular-checkbox-list"
                        class="w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                        >X-ray</label
                      >
                    </div>
                  </li>
                  <li class="w-full dark:border-gray-600">
                    <div class="flex items-center ps-3">
                      <input
                        id="laravel-checkbox-list"
                        type="checkbox"
                        value=""
                        class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500"
                      />
                      <label
                        for="laravel-checkbox-list"
                        class="w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                        >FT</label
                      >
                    </div>
                  </li>
                </ul>
                <hr class="my-5">
                <div class="mt-4">
                  <form @submit.prevent="sentData">
                    <div class="mb-6">
                      <label
                        for="orderNumber"
                        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                        >Serial number testati</label
                      >
                      <input
                        type="text"
                        id="orderNumber"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        placeholder=""
                        required
                        v-model="order_number"
                      />
                    </div>

                   
                    
                    <div class="mb-6">
                      <label
                        for="procesNote"
                        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                        >Note di processo</label
                      >
                      <textarea
                        v-model="order_process_note"
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
                        >Componenti mancanti</label
                      >
                      <textarea
                        v-model="order_process_note"
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
                        >Non conformita</label
                      >
                      <textarea
                        v-model="order_process_note"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        name="procesNote"
                        id="procesNote"
                        cols="30"
                        rows="3"
                      ></textarea>
                  
                    </div>

                    <div class="px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                      <button
                        type="submit"
                        class="mt-3 inline-flex w-full justify-center mx-2 rounded-md px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-green-500 hover:text-white sm:mt-0 sm:w-auto"
                      >
                        Save
                      </button>
                      <button
                        type="button"
                        class="mt-3 inline-flex w-full justify-center rounded-md px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-red-800 hover:text-white sm:mt-0 sm:w-auto"
                        @click="triggerCloseModal"
                      >
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
import { ref, defineEmits } from "vue";
import { endpoints } from "../common/endpoints";
import { axios } from "../common/api.service";
import { useRouter, useRoute } from "vue-router";

const props = defineProps({
  test_uuid: {
    type: String,
    required: false,
  },
  order: {
    type: Object,
    required: false,
  },
});
const note = ref("");
const non_compliance = ref("");
const missing_component = ref("");
const serialnumber = ref("");

const ict = ref(false);
const aoi = ref(false);
const xray = ref(false);
const functional = ref(false);

const router = useRouter();
const route = useRoute();

const emit = defineEmits(["close-modal", "save-data"]);

if (props.order) {
  order_number.value = props.order.order_number;
  order_quantity.value = props.order.order_quantity;
  order_process_note.value = props.order.order_process_note;
  order_serialnumber.value = props.order.order_serialnumber;
}

async function sentData() {
  let endpoint = endpoints["ordersCRUD"];
  let method = "POST";

  if (props.order) {
    endpoint += `${props.order.order_number}/`;
    method = "PUT";
  }
  try {
    const response = await axios({
      method: method,
      url: endpoint,
      data: {
        order_number: order_number.value,
        order_quantity: order_quantity.value,
        order_process_note: order_process_note.value,
        order_serialnumber: order_serialnumber.value,
        board: props.board_id,
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
