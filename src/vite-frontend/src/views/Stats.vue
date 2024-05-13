<template>
  <main>
    <div class="container m-4">
      <h1 class="text-2xl">Statistiche</h1>
      <div class="flex">
        <Chart v-if="onLoad" :label="label" :data_qta="data" />
      </div>
    </div>
  </main>
</template>
<script setup>

import { endpoints } from "../common/endpoints";
import { axios } from "../common/api.service";
import { ref, onMounted } from "vue";
import Chart from "../components/Chart.vue";



const boards = ref([]);
const onLoad = ref(false);

const label = ref([])
const data = ref([])

async function callApi() {
  let endpoint = endpoints["ordersCRUD"];
  try {
    const response = await axios.get(endpoint);
    boards.value.push(...response.data);
    console.log(response.data)

    response.data.forEach(element => {
      data.value.push(element.order_quantity)
      label.value.push(element.created_at)

      var dateString = element.created_at;

      var date = new Date(element.created_at);

      console.log(date.getMonth());

    });

    console.log(data.value);
    console.log(label.value);
    onLoad.value = true

  } catch (error) {
    alert(error);
  }
}
// lifecycle hooks
onMounted(() => {
  callApi();
});
</script>