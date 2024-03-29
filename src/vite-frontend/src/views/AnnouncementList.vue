<template>
  <main>
    <div class="p-4 w-full">
      <section class="my-2 mx-5">
        <!-- Bacheca -->

        <div class="flex justify-between gap-2 flex-wrap">
          <h1 class="text-2xl flex-1">
            <font-awesome-icon icon="hard-drive" class="text-blue-950" />
            Comunicati
          </h1>
          <div class="flex-2">
            <form class="">
              <div class="relative">
                <div
                  class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none"
                ></div>
                <input
                  type="search"
                  id="default-search"
                  class="block w-full p-2 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="Cerca per nome scheda"
                  v-model="search"
                />
              </div>
            </form>
          </div>
          <button
            class="hover:bg-blue-500 text-blue-950 font-semibold hover:text-white py-1 px-6 border border-blue-950 rounded"
            @click="togleModal"
          >
            <font-awesome-icon icon="folder-plus" /> Add
          </button>
        </div>
        <hr class="my-5" />
        <div v-for="an in paginatedData" :key="an.uuid">
          <Annuncement class="my-4" :annuncements="an" />
        </div>
      </section>

      <!-- Testpagination -->
      <div class="text-center mt-4">
        <nav aria-label="Page navigation example">
          <ul class="inline-flex -space-x-px text-sm">
            <li v-show="pageNumber !== 0">
              <a
                @click.prevent="prevPage"
                class="disabled flex items-center justify-center px-3 h-8 ms-0 leading-tight text-gray-500 bg-white border border-e-0 border-gray-300 rounded-s-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
                >Previous</a
              >
            </li>
            <li v-for="p in pageCounter">
              <a
                @click.prevent="setPage(p)"
                class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
                >{{ p }}</a
              >
            </li>

            <li v-show="pageNumber < pageCounter - 1">
              <a
                @click.prevent="nextPage"
                class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 rounded-e-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
                >Next</a
              >
            </li>
          </ul>
        </nav>
      </div>
      <!-- Testpagination -->
    </div>
    <AnnouncementForm 
    v-show="showModal"
    @close-modal="togleModal"
    @save-data="updateAnnouncement"
    />
  </main>
</template>
<script setup>
import { administrationEndpoint } from "../common/endpoints";
import { axios } from "../common/api.service";
import { ref, onMounted, computed } from "vue";
import { useStoreUser } from "../stores/storeUsers";
import AnnouncementForm from "../components/AnnouncementForm.vue";
import Annuncement from "../components/Annuncement.vue";

// access the `store`
const store = useStoreUser();
// console.log(store.first_name);

const announcement = ref([]);
const search = ref("");

const iconType = ref(false);
const msg = ref("");

const showModal = ref(false);
const showForm = ref(false);


// Pagination
const pageCounter = ref(0);
const size = ref(15);
const pageNumber = ref(0);

const paginatedData = computed(() => {
  const start = pageNumber.value * size.value;
  const end = start + size.value;

  let a = announcement.value.filter((annuncement_value) =>
    annuncement_value.announcement_title
      .toLowerCase()
      .includes(search.value.toLowerCase())
  );

  pageCounter.value = Math.ceil(a.length / size.value);
  console.log(pageCounter.value);

  return a.slice(start, end);
});

const setPage = (page) => {
  pageNumber.value = page - 1;
};

const nextPage = () => {
  pageNumber.value++;
};

const prevPage = () => {
  pageNumber.value === 0 ? (pageNumber.value = 0) : pageNumber.value--;
};

const props = defineProps({
  uuid: String,
});

// a computed ref
const orderCount = computed(() => {
  return order.value.length;
});

async function callApi() {
  let endpoint = administrationEndpoint["announcementCRUD"];
  try {
    const response = await axios.get(endpoint);
    announcement.value.push(...response.data);
    console.log(response.data);
  } catch (error) {
    alert(error);
  }
}

function updateAnnouncement(value) {
  togleModal();
  if (typeof value === "number") {
    msg.value = "Aggiornametno non riuscito";
    iconType.value = false;
  } else {
    console.log(value);
    announcement.value.push(value);
    msg.value = "Aggiornametno avvenuto con successo";
    iconType.value = true;
  }

  setTimeout(() => (msg.value = ""), 5000);
}

function togleAlert() {
  showAlert.value = !showAlert.value;
}
function togleModal() {
  showModal.value = !showModal.value;
}

function togleForm() {
  showForm.value = !showForm.value;
}

// lifecycle hooks
onMounted(() => {
  callApi();
});
</script>
