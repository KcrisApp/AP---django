<template>
  <div
    class="relative z-10"
    aria-labelledby="modal-title"
    role="dialog"
    aria-modal="true"
  >
    <!--
      Background backdrop, show/hide based on modal state.
  
      Entering: "ease-out duration-300"
        From: "opacity-0"
        To: "opacity-100"
      Leaving: "ease-in duration-200"
        From: "opacity-100"
        To: "opacity-0"
    -->
    <div
      class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"
    ></div>

    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div
        class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0"
      >
        <!--
          Modal panel, show/hide based on modal state.
  
          Entering: "ease-out duration-300"
            From: "opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
            To: "opacity-100 translate-y-0 sm:scale-100"
          Leaving: "ease-in duration-200"
            From: "opacity-100 translate-y-0 sm:scale-100"
            To: "opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
        -->
        <div
          class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg"
        >
          <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
            <div class="sm:flex sm:items-start">
              <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                <h2
                  class="text-base font-semibold leading-6 text-gray-900 mb-6"
                  id="modal-title"
                >
                  <b>NUOVA SCHEDA</b>
                </h2>
                <hr class="mb-4" />
                <div class="mt-2">
                  <form class="w-full max-w-lg" @submit.prevent="sentData">
                    <div class="flex flex-wrap -mx-3 mb-6">
                      <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                        <label
                          class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
                          for="grid-first-name"
                        >
                          Cliente
                        </label>
                        <input
                          class="appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"
                          type="text"
                          placeholder=""
                          v-model="customer"
                        />
                        <!-- <p class="text-red-500 text-xs italic">
                          Please fill out this field.
                        </p> -->
                      </div>

                      <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                        <label
                          class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
                          for="grid-first-name"
                        >
                          Nome scheda
                        </label>
                        <input
                          class="appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"
                          type="text"
                          placeholder=""
                          v-model="board_name"
                        />
                        <!-- <p class="text-red-500 text-xs italic">
                          Please fill out this field.
                        </p> -->
                      </div>
                      <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                        <label
                          class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
                          for="grid-first-name"
                        >
                          Codice
                        </label>
                        <input
                          class="appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"
                          type="text"
                          placeholder=""
                          v-model="board_code"
                        />
                        <!-- <p class="text-red-500 text-xs italic">
                          Please fill out this field.
                        </p> -->
                      </div>

                      <div class="w-full md:w-1/2 px-3">
                        <label
                          class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
                          for="grid-last-name"
                        >
                          Revisione
                        </label>
                        <input
                          class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                          type="text"
                          placeholder=""
                          v-model="board_rev"
                        />
                      </div>
                    </div>

                    <div
                      class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6"
                    >
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
import { axios } from "../common/api.service"
import { useRouter, useRoute } from 'vue-router'


const props = defineProps({
    boardArr: {
        type: Object,
        required: false
            }
}
)




const customer = ref();
const board_name = ref("");
const board_code = ref("");
const board_rev = ref("");

const router = useRouter()
const route = useRoute()

const emit = defineEmits(["close-modal", "save-data"]);

if (props.boardArr) {
  customer.value = props.boardArr.customer
  board_name.value = props.boardArr.board_name
  board_code.value = props.boardArr.board_code
  board_rev.value = props.boardArr.board_rev
}


async function sentData(){
 
  let endpoint = endpoints["boardsCRUD"];
      let method = "POST";
      if (props.boardArr) {
        endpoint += `${props.boardArr.uuid}/`;
        method = "PUT";
      }
      try {

        
        const response = await axios({
          method: method,
          url: endpoint,
          data: { customer: customer.value,
                  board_name: board_name.value,
                  board_code: board_code.value,
                  board_rev: board_rev.value
          },
        });
      
        emit("save-data", response.data);
        customer.value = ""
        board_code.value = ""
        board_name.value = ""
        board_rev.value = ""

      } catch (error) {
        error = error;
        alert(error)
      }
}
function triggerCloseModal() {
  // emit an event to delete an answer instance

  if (props.boardArr) {
    
    console.log(props.boardArr.id)
  }
  emit("close-modal");
}
</script>
