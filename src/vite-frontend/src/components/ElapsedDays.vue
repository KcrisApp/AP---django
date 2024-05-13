<template>
  <span class="text-red-800 mx-4 font-semibold" v-if="useDateOrderCheck(dateTime) >= 0">
    {{ useDateOrderCheck(dateTime) }} Giorni fa
  </span>
  <span class="text-yellow-500 mx-4 font-semibold" v-else="useDateOrderCheck(dateTime) <= -2">
    Restano {{ useDateOrderCheck(dateTime) }} giorni
  </span>
  <span class="text-green-600 mx-4 font-semibold" v-else="useDateOrderCheck(dateTime) <= -5">
    Restano {{ Math.abs(useDateOrderCheck(dateTime)) }} giorni
  </span>
</template>

<script setup>
import { useDateOrderCheck } from "../use/useDateOrderCheck"

const props = defineProps({
  dateTime: {
    type: String,
    required: true,
  },
});
</script>
