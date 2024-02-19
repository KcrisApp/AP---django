<template>
  <main>


    
      <div class="p-4 w-full">

       
        <!-- <OrderForm v-show="showModal" v-bind:board_id="b.id" @close-modal="togleModal" @save-data="updateOrder"/> -->
        
        <div class="flex justify-between my-4 flex-wrap">
          <h1 class="text-2xl mb-4">
            <font-awesome-icon icon="hard-drive" class="text-blue-950" />
            Bacheca
          </h1>
          

        <hr class="my-2" />
      </div>
      <div class="bg-slate-50 p-4 gap-4 rounded-xl">
      <p class="mb-2">{{ announcement.created_at }}</p>  
      <h1 class="text-lg font-bold">{{ announcement.announcement_title }}</h1>

      <div class="mt-5" v-html="announcement.html"></div>
      <p class="mt-5 font-medium text-right">La direzione</p>
    
      </div>
      
      </div>

   
  <div>
   
  </div>

  <QuillEditor  :content="myContent"  contentType="html"/>



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
// access the `store` 
const store = useStoreUser()
console.log(store.first_name)


const announcement = ref({});
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
