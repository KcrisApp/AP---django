<template>
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-900 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div
          class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-3xl">
          <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
            <div class="">
              <div class="my-5 text-center sm:ml-4 sm:mt-0 sm:text-left">
                <h2 class="text-base font-semibold leading-6 mb-4 text-gray-900" id="modal-title">
                  <b class="text-blue-900"><font-awesome-icon icon="camera" /> Qrcode scanner</b>
                </h2>
                <div class="mb-4">
                  <p class="error">{{ error }}</p>
                  <qrcode-stream :paused="false" @detect="onDetect" @error="onError" :track="paintOutline" />
                </div>
                <div class="flex gap-4 justify-center">
                  <button @click="emit('update:modelValue', false)"
                    class="mt-4  rounded-md px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm  ring-gray-300 hover:bg-red-800 hover:text-white sm:mt-0 sm:w-auto">
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
</template>

<script setup lang="ts">
import { ref } from "vue";
import { QrcodeStream } from "vue-qrcode-reader";
import { useRouter } from 'vue-router';

const router = useRouter();
// data
const result = ref("");
const error = ref("");
const goToOrder = ref(false);

const props = defineProps({
  modelValue: {
    type: Boolean,
    required: true
  }
}
)
const emit = defineEmits(['update:modelValue'])

// methods
const onDetect = (detectedCodes) => {
  // console.log(detectedCodes);

  const [firstCode] = detectedCodes;
  result.value = firstCode.rawValue;
  console.log(goToOrder.value)


  router.push({ name: 'order-details', params: { order_number: result.value } })

};

const onError = (err) => {
  error.value = `[${err.name}]: `;

  if (err.name === "NotAllowedError") {
    error.value += "you need to grant camera access permission";
  } else if (err.name === "NotFoundError") {
    error.value += "no camera on this device";
  } else if (err.name === "NotSupportedError") {
    error.value += "secure context required (HTTPS, localhost)";
  } else if (err.name === "NotReadableError") {
    error.value += "is the camera already in use?";
  } else if (err.name === "OverconstrainedError") {
    error.value += "installed cameras are not suitable";
  } else if (err.name === "StreamApiNotSupportedError") {
    error.value += "Stream API is not supported in this browser";
  } else if (err.name === "InsecureContextError") {
    error.value +=
      "Camera access is only permitted in secure context. Use HTTPS or localhost rather than HTTP.";
  } else {
    error.value += err.message;
  }
};


function paintOutline(detectedCodes, ctx) {
  for (const detectedCode of detectedCodes) {
    const [firstPoint, ...otherPoints] = detectedCode.cornerPoints

    ctx.strokeStyle = 'red'

    ctx.beginPath()
    ctx.moveTo(firstPoint.x, firstPoint.y)
    for (const { x, y } of otherPoints) {
      ctx.lineTo(x, y)
    }
    ctx.lineTo(firstPoint.x, firstPoint.y)
    ctx.closePath()
    ctx.stroke()
  }
}

</script>

<style scoped>
.error {
  font-weight: bold;
  color: red;
}
</style>
