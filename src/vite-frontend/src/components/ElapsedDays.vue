<template>
  <span
    class="text-red-800 mx-4 font-semibold"
    v-if="useDateOrderCheck(dateTime) >= 0"
  >
    {{ useDateOrderCheck(dateTime) }} Giorni fa
    <!-- <font-awesome-icon icon="rocket" /> -->
  </span>
  <span
    class="text-yellow-500 mx-4 font-semibold"
    v-else="useDateOrderCheck(dateTime) <= -2"
  >
    Restano {{ useDateOrderCheck(dateTime) }} giorni
    <!-- <font-awesome-icon icon="rocket" /> -->
  </span>

  <span
    class="text-green-600 mx-4 font-semibold"
    v-else="useDateOrderCheck(dateTime) <= -5"
  >
    Restano {{ Math.abs(useDateOrderCheck(dateTime)) }} giorni
    <!-- <font-awesome-icon icon="rocket" /> -->
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
