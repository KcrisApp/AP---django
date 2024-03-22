<template>
  <NavBar v-if="onLoad" />
</template>

<script setup>

import { endpoints } from "./common/endpoints";
import { axios } from "./common/api.service";
import { onMounted, ref } from "vue";
import { useStoreUser } from './stores/storeUsers'
import NavBar from "./components/NavBar.vue";

// access the `store` 
const store = useStoreUser()
const onLoad = ref(false)


async function callApi() {
  onLoad.value = false
  let endpoint = endpoints["usersDetail"];
  try {
    const response = await axios.get(endpoint);
  

    // Update storeUser
    store.$patch({ userData: response.data })
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



