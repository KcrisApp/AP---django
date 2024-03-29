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
                    <b class="text-blue-900">Nuovo comunicato</b>
                  </h2>

        
                </div>

                <hr class="my-5" />
                <div class="mt-4">
             
                    <div class="mb-6">
                      <label
                      for="status"
                      class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                      >Tipo di annuncio:</label
                    >
                    <select
                    v-model="type"
                      id="status"
                      class="p-2 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 block w-full dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    >
                      <option selected value="avviso">Avviso</option>
                      <option value="comunicato">Comunicato</option>
                    </select>
                    </div>

                    <hr class="mb-4" />

                    <div class="mb-6 mt-4">
                      <label
                        for="titleForm"
                        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                        >Titolo</label
                      >
                      <input
                        type="titleForm"
                        id="orderNumber"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        placeholder=""
                        required
                        v-model="title"
                      />
                    </div>

                    <div class="mb-6 mt-4">
                      <label
                        for="content"
                        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                        >Testo</label
                      >
                      <textarea
                        type="text"
                        id="content"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        placeholder=""
                        required
                        v-model="text_content"
                      />
                    </div>
             
              
                
                    <div class="px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                      <button
                        @click="sentData"
                        class="mt-3 inline-flex w-full justify-center mx-2 rounded-md px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-blue-900 hover:text-white sm:mt-0 sm:w-auto"
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
</template>

<script setup>

// Import
import { ref, defineEmits } from "vue";
import { axios } from "../common/api.service";
import { administrationEndpoint } from "../common/endpoints";

const props = defineProps({

  announcement: {
    type: Object,
    required: false,
  },
});


const text_content = ref("")
const title = ref("")
const type = ref("Avviso")
const emit = defineEmits(["close-modal", "save-data"]);

if (props.announcement) {
  text_content.value = props.announcement.announcement_content
  title.value = props.announcement.announcement_title
  type.value = props.announcement.announcement_type
}
// Function

async function sentData() {

  let endpoint = administrationEndpoint["announcementCRUD"];
  let method = "POST" 

  if (props.announcement) {
    endpoint += `${props.announcement.uuid}/`;
    method = "PATCH";
  }

  let data = {
    announcement_type:type.value,
    announcement_title:title.value,
    announcement_content:text_content.value 
  }
  try {
    const response = await axios({
      method: method,
      url: endpoint,
      data: data
    });
    emit("save-data", response.data);
  } catch (error) {
    console.log(error)
    emit("save-data", error.response.status);
  }
}
function triggerCloseModal() {
  // emit an event to delete an answer instance
  emit("close-modal");
}
</script>
