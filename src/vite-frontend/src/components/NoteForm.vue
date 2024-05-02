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
          class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-2xl"
        >
          <div class="bg-white px-2 pb-2 pt-2 sm:p-6 sm:pb-4">
            <div class="">
              <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">

                <div class="flex justify-between my-2">

                  <h2
                  class="text-base font-semibold leading-6 p-2 text-gray-900"
                  id="modal-title"
                >
                  <b class="text-blue-900">Aggiungi / Modifica nota</b>
                </h2>

                </div>

           

               
                <div class="mt-4">
                    <div class="mb-6">
               
                      <textarea
                      :value="modelValue"
                       @input="$emit('update:modelValue', $event.target.value)"
                      
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        name="note"
                        id="note"
                        cols="30"
                        rows="3"
                        ref="textareaRef"
                      ></textarea>
                  
                    </div>
                   
                    
                    <div class="px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                     
                      <button
                     
                        class="mt-3 inline-flex w-full justify-center rounded-md px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-red-800 hover:text-white sm:mt-0 sm:w-auto"
                        @click="triggerCloseModal"
                      >
                        Close
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



const props = defineProps({
 
  modelValue: {
    type: String,
    required: true,
  },

});


const emit = defineEmits(["close-modal", "update:modelValue"]);
const  textareaRef = ref("");

const sentData = () => {
    console.log(textareaRef.name)
    
}
const triggerCloseModal =() => {
  // emit an event to delete an answer instance
  emit("close-modal");
}

 


</script>
