<template>
    <main>
      <div class="container-fluid flex min-h-screen">
        <NavBar />

       

        <div class="m-4 w-full" v-for="o in order">

          <Alert
          v-show="showAlert"
          icon-type="error"
          title="Attenzione"
          message="Sei sicuro di voler eliminare la scheda?"
          @close-alert="togleAlert"
          @confirm="deleteOrder(o.order_number)"
        />
          <OrderForm v-show="showModal" v-bind:order_id="o.board" v-bind:order="o" @close-modal="togleModal" @save-data="updateOrder"/>
          <div class="flex justify-between my-4">
        
         
            <h1 class="text-2xl" >
              <font-awesome-icon icon="hard-drive" class="text-blue-950" />
              Ordine: {{ o.order_number }}
                
            </h1>

            <div class="flex gap-2">
              <button
            class="hover:bg-amber-400 text-blue-950 font-semibold hover:text-white py-1 px-6 border border-blue-950 rounded" 
            @click="togleModal"
          >
            <font-awesome-icon icon="folder-plus" /> Modifica ordine
          </button>
          <button
            class="bg-red-600 hover:bg-red-900 text-white font-semibold hover:text-white py-1 px-6 border  rounded" 
            @click="togleAlert"
          >
           Elimina
          </button>
            </div>
            
          </div>
  
          <hr class="my-2" />
          <div class="flex bg-slate-100 p-4 gap-3
          flex-wrap">
            <div class="flex-none">
              <qrcode-vue class="my-2" :value="o.order_number" size="60" level="H" />
            </div>
        
                <div class="flix-1">
                    <p>Numero d'ordine: <b> {{ o.order_number }}</b></p>
                    <p>Serial number: <b> {{ o.order_serialnumber }}</b></p>
                    <p>Quantità: <b> {{ o.order_quantity }}</b></p>
           
                </div>
                <div class="flex-1">
                    <p>Data di creazione: <b> {{ o.created_at }}</b></p>
                    <p>Cliente: <b> {{ o.customer }}</b></p>
                   
                </div>
            </div>
            <div class="bg-gray-100 my-2 p-4">
              <p><b>Note di processo:</b></p>
              <hr class="my-1">
              <p>{{ o.order_process_note }}</p>
              
            </div>
           
            <hr class="my-2">

            <h1 class="text-xl mt-4" > 
              Reparti
            </h1>
        
            <div class="flex gap-2 mt-4 ">
              <router-link
                  :to="{ name: 'board-details', params: { uuid: o.uuid } }"
                  class="py-2 px-6 border border-blue-950 rounded-md bg-gray-50 hover:bg-blue-900 hover:text-white"
                >
                SMT
                </router-link>
                <router-link
                  :to="{ name: 'board-details', params: { uuid: o.uuid } }"
                  class="py-2 px-6 border border-blue-950 rounded-md bg-gray-50 hover:bg-blue-900 hover:text-white"
                >
                Verifica
                </router-link>
                <router-link
                  :to="{ name: 'board-details', params: { uuid: o.uuid } }"
                  class="py-2 px-6 border border-blue-950 rounded-md bg-gray-50 hover:bg-blue-900 hover:text-white"
                >
                Collaudi
                </router-link>
                <router-link
                  :to="{ name: 'board-details', params: { uuid: o.uuid } }"
                  class="py-2 px-6 border border-blue-950 rounded-md bg-gray-50 hover:bg-blue-900 hover:text-white"
                >
                Spedizione
                </router-link>
            </div>
        </div>
      </div>
    </main>
  </template>
  <script setup>

  import NavBar from "../components/NavBar.vue";
  import { endpoints } from "../common/endpoints";
  import { axios } from "../common/api.service";
  import { ref, onMounted } from "vue";
  import Alert from "../components/Alert.vue";
  import { useRouter, useRoute } from "vue-router";
  import OrderForm from "../components/OrderForm.vue";

  import QrcodeVue from 'qrcode.vue'

  const router = useRouter();
  const route = useRoute();

  const order = ref([]);
  const showAlert = ref(false);
  const showModal = ref(false);

  const props = defineProps({
            order_number: String,

        })
  

  
  async function callApi() {
    const endpoint = `${endpoints["ordersCRUD"]}${props.order_number}/`;

try {
  const response = await axios.get(endpoint);
  console.log(response)

      order.value.push(response.data);
  

      console.log(response.data);
    } catch (error) {
      alert(error);
    }
  }

  async function deleteOrder(order_number) {
    let endpoint = `${endpoints["ordersCRUD"]}${order_number}/`;

    try {
      const response = await axios.delete(endpoint);
      togleAlert();
      router.push({ name: "ordini" });
    } catch (error) {
      alert(error);
    }
  }

function updateOrder(value) {
  togleModal()
 
  order.value[0].order_number = value.order_number
  order.value[0].order_process_note = value.order_process_note
  order.value[0].order_quantity = value.order_quantity
  order.value[0].order_serialnumber = value.order_serialnumber
  

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
  