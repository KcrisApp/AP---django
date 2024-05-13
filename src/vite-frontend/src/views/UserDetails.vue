<template>
  <main>
    <div class="p-4 w-full">
      <div class="flex justify-between gap-2">
        <h1 class="text-2xl">
          <font-awesome-icon icon="table-list" class="text-blue-950" />
          Utente
        </h1>
      </div>
      <hr class="my-4" />
      <div class="bg-white overflow-hidden shadow rounded-lg border">
        <div class="px-4 py-5 sm:px-6">
          <h3 class="text-lg leading-6 font-medium text-blue-900">
            Profilo utente
          </h3>
        </div>
        <div class="border-t border-gray-200 px-4 py-5 sm:p-0">
          <dl class="sm:divide-y sm:divide-gray-200">
            <div class="py-3 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
              <dt class="text-sm font-medium text-gray-500">
                Nome
              </dt>
              <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                {{ user.first_name }}
              </dd>
            </div>
            <div class="py-3 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
              <dt class="text-sm font-medium text-gray-500">
                Cognome
              </dt>
              <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                {{ user.last_name }}
              </dd>
            </div>
            <div class="py-3 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
              <dt class="text-sm font-medium text-gray-500">
                Email address
              </dt>
              <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                {{ user.email }}
              </dd>
            </div>
            <div class="py-3 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
              <dt class="text-sm font-medium text-gray-500">
                Ruolo
              </dt>
              <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                {{ user.company_role }}
              </dd>
            </div>
            <div class="py-3 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
              <dt class="text-sm font-medium text-gray-500">
                Reparto
              </dt>
              <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                {{ user.department }}
              </dd>
            </div>
            <div class="py-3 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
              <dt class="text-sm font-medium text-gray-500">
                Data inserimento
              </dt>
              <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                {{ user.date_joined }}
              </dd>
            </div>
            <div class="py-3 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
              <dt class="text-sm font-medium text-gray-500">
                <b>Ultimo accesso</b>
              </dt>
              <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                <b>{{ user.last_login }}</b>
              </dd>
            </div>
          </dl>
        </div>
      </div>
    </div>
  </main>
</template>
<script setup>


import { ref, onMounted, computed } from "vue";
import { userEndPoints } from "../common/endpoints";
import { axios } from "../common/api.service";



const props = defineProps({
  username: {
    type: String,
    required: true
  },



});


const user = ref({});
const onLoad = ref(false);

async function callApi() {
  onLoad.value = false
  let endpoint = `${userEndPoints["usersList"]}${props.username}/`;
  try {
    const response = await axios.get(endpoint);

    user.value = response.data
    // Update storeUser

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
