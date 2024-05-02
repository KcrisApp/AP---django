<template>
  <NavBar v-if="onLoad" />
</template>

<script setup>

import { onMounted, ref } from "vue";
import { useStoreUser } from './stores/storeUsers'
import NavBar from "./components/NavBar.vue";

// access the `store` 
const store = useStoreUser()
const onLoad = ref(false)

async function callApi() {
  onLoad.value = false
  try {

    await store.getUserData()
    const user = store.userInfo

    if (user) {
      
      onLoad.value = true
    }

  } catch (error) {
    alert(error);
  }
}

        

// lifecycle hooks
onMounted(() => {
  callApi();
});

</script>



