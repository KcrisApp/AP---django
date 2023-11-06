<template>
  <main>
    <div class="container-fluid flex min-h-screen">
      <NavBar />
      <div class="m-4 w-full">
     

        <section class="">
          <div
            class="mx-auto max-w-screen-xl px-4 py-32 lg:flex lg:h-screen lg:items-center"
          >
            <div class="mx-auto max-w-xl text-center">
              <h1 class="text-3xl font-extrabold sm:text-5xl">
                Benvenuto sul portale 
                <strong class="font-extrabold text-blue-800 sm:block">
                Mce - AP
                </strong>
              </h1>

              <p class="mt-4 sm:text-xl/relaxed">
                Da qui potrai accedere agli ordini in produzione e a tutte le info sulle schede.
              </p>

              <div class="mt-8 flex flex-wrap justify-center gap-4">
                <RouterLink to="/ordini"  class="block w-full rounded bg-blue-600 px-12 py-3 text-sm font-medium text-white shadow hover:bg-blue-800 focus:outline-none focus:ring active:bg-red-500 sm:w-auto"
                  >Ordini</RouterLink>
                  <RouterLink to="/boards"  class="block w-full rounded px-12 py-3 text-sm font-medium text-blue-600 shadow hover:text-blue-700 hover:bg-slate-100 focus:outline-none focus:ring active:text-red-500 sm:w-auto"
                  >Schede</RouterLink>
        
              </div>
            </div>
          </div>
        </section>
      </div>
    </div>
  </main>
</template>
<script setup>
import NavBar from "../components/NavBar.vue";
import { endpoints } from "../common/endpoints";
import { axios } from "../common/api.service";
import { ref, onMounted } from "vue";

const boards = ref([]);

async function callApi() {
  let endpoint = endpoints["boardsCRUD"];
  try {
    const response = await axios.get(endpoint);
    boards.value.push(...response.data);
    console.log(response.data);
  } catch (error) {
    alert(error);
  }
}
// lifecycle hooks
onMounted(() => {
  callApi();
});
</script>
