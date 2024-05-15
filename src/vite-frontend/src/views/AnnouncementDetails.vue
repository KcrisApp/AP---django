<template>
  <main>
    <Info v-show="msg" :message="msg" :icon-type="iconType" />
    <div class="px-4 w-full">
      <div class="flex justify-between my-4 flex-wrap">
        <h1 class="text-2xl mb-2">
          <font-awesome-icon icon="hard-drive" class="text-blue-950" />
          Notifiche
        </h1>
        <div v-if="store.permissionAccess" class="flex gap-2">
          <button
            class="hover:bg-amber-400 hover:border-amber-400 text-blue-950 font-semibold hover:text-white py-1 px-6 border border-blue-950 rounded"
            @click="togleModal">
            Modifica
          </button>
          <button class="bg-red-600 hover:bg-red-900 text-white font-semibold hover:text-white py-1 px-6 border rounded"
            @click="togleAlert">
            Elimina
          </button>
        </div>
      </div>
      <router-link :to="{
        name: 'announcement-list'
      }" class="hover:text-green-600">
        <font-awesome-icon icon="arrow-left-long" /> Back to list
      </router-link>
      <hr class="my-6" />
      <div class="bg-slate-50 p-4 gap-4 rounded-xl">
        <div class="flex mb-4">
          <font-awesome-icon v-if="announcement.announcement_type === 'comunicato'" icon="circle-info"
            class="text-4xl text-blue-800" />
          <font-awesome-icon v-if="announcement.announcement_type === 'avviso'" icon="triangle-exclamation"
            class="text-3xl text-yellow-500" />
          <p class="text-sm font-semibold leading-6 text-gray-900 ml-4 pt-1">
            {{ announcement.announcement_type }}
          </p>
        </div>
        <p class="mb-2">{{ useDateFormatted(announcement.created_at) }}</p>
        <h1 class="text-lg font-bold">{{ announcement.announcement_title }}</h1>
        <div class="mt-5" v-html="announcement.announcement_content"></div>
        <p class="mt-5 font-medium text-right">La direzione</p>
      </div>
    </div>
    <div>
    </div>
    <Alert v-show="showAlert" icon-type="error" title="Attenzione" message="Sei sicuro di voler eliminare l'annuncio"
      @close-alert="togleAlert" @confirm="deleteAnnouncement" />
    <AnnouncementForm v-if="isLoading" v-show="showModal" @close-modal="togleModal" @save-data="updateAnnouncement"
      :announcement="announcement" />
  </main>
</template>
<script setup>

import { administrationEndpoint } from "../common/endpoints";
import { axios } from "../common/api.service";
import { ref, onMounted } from "vue";
import Alert from "../components/Alert.vue";
import AnnouncementForm from "../components/AnnouncementForm.vue";
import Info from "../components/Info.vue";
import { useDateFormatted } from "../use/useDateFormatted";
import { useRouter } from "vue-router";
import { useStoreUser } from '../stores/storeUsers'

// access the `store` 
const store = useStoreUser()


const announcement = ref({});
const iconType = ref(false);
const msg = ref("");
const showModal = ref(false);
const showForm = ref(false);
const showAlert = ref(false);
const isLoading = ref(false)

const router = useRouter();


const props = defineProps({
  uuid: String,
});

// Async function

async function callApi() {
  isLoading.value = false
  const endpoint = `${administrationEndpoint["announcementCRUD"]}${props.uuid}/`;

  try {
    const response = await axios.get(endpoint);

    announcement.value = response.data;
    console.log(response.data);
    isLoading.value = true

  } catch (error) {
    alert(error);
  }
}

async function deleteAnnouncement() {
  let endpoint = `${administrationEndpoint["announcementCRUD"]}${props.uuid}/`;

  try {
    const response = await axios.delete(endpoint);
    togleAlert();
    router.push({ name: "announcement-list" });
  } catch (error) {
    alert(error);
  }
}

function updateAnnouncement(value) {
  togleModal()
  if (typeof value === 'number') {
    msg.value = "Aggiornametno non riuscito"
    iconType.value = false
  }
  else {
    console.log(value)
    announcement.value = value
    msg.value = "Aggiornametno avvenuto con successo"
    iconType.value = true
  }
  setTimeout(() => msg.value = "", 5000)
}

function togleAlert() {
  showAlert.value = !showAlert.value;
}
function togleModal() {
  showModal.value = !showModal.value;
}

// lifecycle hooks
onMounted(() => {
  callApi();

});
</script>
