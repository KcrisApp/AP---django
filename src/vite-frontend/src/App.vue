<template>
  <NavBar />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { endpoints } from "./common/endpoints";
import { axios } from "./common/api.service";
import { ref, onMounted, computed } from "vue";
import {useDateFormat } from "./use/useDateFormat"
import { useStoreUser } from './stores/storeUsers'
import NavBar from "./components/NavBar.vue";
// access the `store` 
const store = useStoreUser()

console.log(store.first_name)

async function callApi() {
  let endpoint = endpoints["usersDetail"];
  try {
    const response = await axios.get(endpoint);
    console.log(response.data);

    // Update storeUser
    store.$patch({
        username: response.data.username, 
        name:  response.data.name,
        first_name: response.data.first_name,
        last_name:  response.data.last_name,
        company_role: response.data.company_role,
        last_login: response.data.last_login
    })


  } catch (error) {
    alert(error);
  }
}
// lifecycle hooks
onMounted(() => {
  callApi();
});

</script>



