<template>
  <main>


    
      <div class="p-4 w-full">

       
      

        
        <section class="my-2 mx-5">
          <!-- Bacheca -->

          <h1 class="text-lg font-semibold sm:text-3xl my-5 text-blue-900">
            Bacheca
          </h1>
          <hr class="my-5" />
          <div v-for="an in announcement">
            <Annuncement class="my-4" :annuncements="an" />
          </div>
        </section>
        

   
  </div>





  </main>
</template>
<script setup>

import { administrationEndpoint } from "../common/endpoints";
import { axios } from "../common/api.service";
import { ref, onMounted, computed } from "vue";

// import OrderForm from "../components/OrderForm.vue";

import { useRouter, useRoute } from "vue-router";
import { useStoreUser } from '../stores/storeUsers'
import  Info from "../components/Info.vue"
import Annuncement from "../components/Annuncement.vue";
// access the `store` 
const store = useStoreUser()
console.log(store.first_name)


const announcement = ref([]);
const myContent = ref("")

const iconType = ref(false);
const msg = ref("");

const showModal = ref(false);
const showForm = ref(false);


const isLoading = ref(false)

const router = useRouter();
const route = useRoute();

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





function updateBoard(value) {
  togleForm()
  if (typeof value === 'number') {
      msg.value =  "Aggiornametno non riuscito"
      iconType.value =  false
  }
  else{
  console.log(value)
  board.value = value
  msg.value =  "Aggiornametno avvenuto con successo"
  iconType.value =  true
  }
  

  setTimeout(() => msg.value = "", 5000)



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
function togleImgForm() {
  showFormImg.value = !showFormImg.value;
}
// lifecycle hooks
onMounted(() => {
  callApi();

});
</script>
