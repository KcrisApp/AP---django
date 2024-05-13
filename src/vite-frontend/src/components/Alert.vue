<template>
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">

    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>

    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">

        <div
          class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
          <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4 text-center">
            <div v-if="props.iconType == 'error'"
              class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-red-100 sm:mx-0 sm:h-10 sm:w-10">
              <font-awesome-icon icon="exclamation" />
            </div>

            <div v-else-if="props.iconType == 'success'"
              class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-green-700 text-white sm:mx-0 sm:h-10 sm:w-10">
              <font-awesome-icon icon="circle-check" />
            </div>


            <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
              <h2 class="font-semibold text-xl leading-6 text-gray-900" id="modal-title">{{ props.title }}</h2>
              <div class="mt-2">
                <p class=" text-gray-500">{{ props.message }}</p>
              </div>
            </div>
          </div>

          <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6 gap-2">

            <button type="button"
              class="mt-3 inline-flex w-full justify-center rounded-md bg-red-500 px-3 py-2 text-sm font-semibold text-white shadow-sm ring-1 ring-inset  hover:bg-red-900 sm:mt-0 sm:w-auto"
              @click="confirm">Elimina</button>
            <button type="button"
              class="mt-3 inline-flex w-full justify-center rounded-md  px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset  hover:bg-gray-200 sm:mt-0 sm:w-auto"
              @click="closeModal">Cancel</button>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>



<script setup>

// Import
import { defineEmits } from "vue";

// Definition of Props
const props = defineProps({
  iconType: {
    type: String,
    required: true
  },
  title: {
    type: String,
    required: true
  },
  message: {
    type: String,
    required: true
  }
}
)

//  Signal
const emit = defineEmits(["close-alert", "confirm"]);

// Function
function closeModal() {
  emit("close-alert")
}
function confirm() {
  emit("confirm")
}

</script>