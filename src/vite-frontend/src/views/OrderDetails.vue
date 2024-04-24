<template>
  <main>

      <div
        v-if="onLoad" 
       class="p-4 w-full" v-for="o in order">

        <Alert
          v-show="showAlert"
          icon-type="error"
          title="Attenzione"
          message="Sei sicuro di voler eliminare la scheda?"
          @close-alert="togleAlert"
          @confirm="deleteOrder(o.order_number)"
        />
        <OrderForm
          v-show="showModal"
          v-bind:order_id="o.board"
          v-bind:order="o"
          @close-modal="togleModal"
          @save-data="updateOrder"
        />
        <ModalFile
          v-show="showFormFile"
          @close-alert="togleModalFile"
          v-bind:order_id="o.id"
          @save-file="fileUpdate"
        />
        <div class="flex flex-wrap gap-4 justify-between my-4">
          <h1 class="text-2xl">
            <font-awesome-icon icon="hard-drive" class="text-blue-950" />
            Ordine: {{ o.order_number }}
          </h1>
         
          <div class="flex gap-2"  v-if="store.permissionAccess">
            <button
              class="hover:bg-amber-400 hover:border-amber-400 text-blue-950 font-semibold hover:text-white py-1 px-6 border border-blue-950 rounded"
              @click="togleModal"
            >
              <font-awesome-icon icon="folder-plus" /> Modifica ordine
            </button>
            <button
              class="bg-red-600 hover:bg-red-900 text-white font-semibold hover:text-white py-1 px-6 border rounded"
              @click="togleAlert"
            >
              Elimina
            </button>
          </div>
        </div>
        <div class="">
        <router-link
                  :to="{
                    name: 'board-details',
                      params: { uuid: o.board },
                  }"
                  class="hover:text-green-600"
                >
                <font-awesome-icon icon="arrow-left-long" /> Back to {{ o.board_name }}
                
                </router-link>
            
        </div>

        
        <hr class="my-5" />
        <div class="flex bg-slate-100 p-4  gap-10 flex-wrap rounded-md shadow-md">
          <div class="flex-0">
            <qrcode-vue
              class="my-2"
              :value="o.order_number"
              :size="60"
              level="H"
            />
          </div>

          <div class="flex-1 ">
            <p>
              Scheda: <b>{{ o.board_name }}</b>
            </p>
            <p>
              Numero d'ordine: <b> {{ o.order_number }}</b>
            </p>
            <p>
              Serial number: <b> {{ o.order_serialnumber }}</b>
            </p>
            <p>
              Quantità: <b> {{ o.order_quantity }}</b>
            </p>
          </div>
          <div class="flex-1">
            <p>
              Data di creazione: <b>{{ useDateFormatted(o.created_at) }} </b>
            </p>
            <p>
              Cliente: <b> {{ o.customer }}</b>
            </p>
            <p>
              Personalizzazione: <b> {{ o.order_customization }}</b>
            </p>
          </div>

 
         
        </div>
        <div class="bg-gray-100 my-4 p-4 rounded-md text-sm">
          <p><b>Moduli:</b></p>
          <hr class="my-2" />
          <div class="flex gap-6">
          <router-link
          v-if="store.isOfficeUser"
              :to="{
                name: 'foglio-caratterizzazione',
                params: { uuid: o.uuid },
              }"
            >
              <h3 class="text-xl hover:text-blue-800">
                <font-awesome-icon icon="passport" /> Foglio caratterizzazione
              </h3>
            </router-link>
            <router-link
              :to="{
                name: 'foglio-cestello',
                params: { uuid: o.uuid },
              }"
            >
            
              <h3 class="text-xl hover:text-blue-800">
                <font-awesome-icon icon="passport" />
                Cartellino 
              </h3>
            </router-link>
          </div>
        </div>



        <!-- Section topographic file -->
        <div class="bg-gray-100 my-2 p-4 rounded-md text-sm">
          <div class="flex justify-between">
            <p><b>File:</b></p>
            <font-awesome-icon v-if="store.permissionAccess"  icon="circle-plus" class="text-2xl hover:text-green-700" @click="togleModalFile"/>
          </div>
         
          <hr class="my-2" />
          <p
          v-if="o.order_filetopographic"
          >
          <a :href="o.order_filetopographic" target=”_blank” class="text-red-700">
            <font-awesome-icon icon="file-pdf" class="text-2xl"/>
            Topographic
          </a>
           </p>
        </div>







        <div class="bg-gray-100 my-2 p-4 rounded-md text-sm">
          <p><b>Note di processo:</b></p>
          <hr class="my-1" />
          <p>{{ o.order_process_note }}</p>
        </div>

        <hr class="my-2" />
        <p><b>Stato ordine:</b></p>
        
          <div>
              <div class="text-lg p-4 bg-slate-100 rounded-md ">
              
              <p class="flex justify-center text-sm">
                Data di spedizione: 
              </p>
              <p class="flex justify-center text-sm">
                <b>  {{ useDateFormatted(o.shipping_date) }}</b>
              </p>
              <p class="flex justify-center">
                <hr>
                <ElapsedDays :dateTime="o.shipping_date" />
              </p>

            </div>
          </div>
      
          <div class="">
            <OrderStatusBar :order_number="o.order_number " :minimal_view="true" />
          </div>
    
       
        <hr class="" />

        <h1 class="text-xl mt-4">Reparti</h1>

        <div class="flex gap-2 mt-4 flex-wrap">
          <router-link
            :to="{ name: 'smt-details', params: { smt_number: o.order_smt } }"
            class="py-2 px-6 border border-blue-950 rounded-md bg-gray-50 hover:bg-blue-900 hover:text-white"
          >
            SMT
          </router-link>
          <router-link
            :to="{ name: 'welding-details', params: { welding_number: o.order_welding } }"
            class="py-2 px-6 border border-blue-950 rounded-md bg-gray-50 hover:bg-blue-900 hover:text-white"
          >
            Saldatura
          </router-link>
          <router-link
            :to="{
              name: 'verify-details',
              params: { verify_number: o.order_verify },
            }"
            class="py-2 px-6 border border-blue-950 rounded-md bg-gray-50 hover:bg-blue-900 hover:text-white"
          >
            Verifica
          </router-link>
          <router-link
            :to="{
              name: 'test-details',
              params: { test_number: o.order_test },
            }"
            class="py-2 px-6 border border-blue-950 rounded-md bg-gray-50 hover:bg-blue-900 hover:text-white"
          >
            Collaudi
          </router-link>
          <router-link
            :to="{ name: 'shipping-details', params: { order_id: o.id, order_qta:o.order_quantity }}"
            class="py-2 px-6 border border-blue-950 rounded-md bg-gray-50 hover:bg-blue-900 hover:text-white"
          >
            Spedizioni
          </router-link>
        </div>
      </div>

  </main>
</template>
<script setup>

import { endpoints } from "../common/endpoints";
import { axios } from "../common/api.service";
import { ref, onMounted } from "vue";
import Alert from "../components/Alert.vue";
import { useRouter } from "vue-router";
import OrderForm from "../components/OrderForm.vue";
import ModalFile from "../components/ModalFile.vue";
import  ElapsedDays  from '../components/ElapsedDays.vue'
import  OrderStatusBar  from '../components/OrderStatusBar.vue'
import QrcodeVue from "qrcode.vue";
import { useStoreUser } from '../stores/storeUsers'
import { useDateFormatted } from "../use/useDateFormatted"
// access the `store` 
const store = useStoreUser()

const router = useRouter();









const order = ref([]);
const showAlert = ref(false);
const showModal = ref(false);
const showFormFile = ref(false);

const onLoad = ref(false);

const props = defineProps({
  order_number: String,
});


async function callApi() {
  
  onLoad.value = false
  const endpoint = `${endpoints["ordersCRUD"]}${props.order_number}/`;

  try {
    const response = await axios.get(endpoint);
    console.log(response);

    order.value.push(response.data);

    console.log(response.data);
    onLoad.value = true
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
  togleModal();

  order.value[0].order_number = value.order_number;
  order.value[0].order_process_note = value.order_process_note;
  order.value[0].order_quantity = value.order_quantity;
  order.value[0].order_serialnumber = value.order_serialnumber;
  order.value[0].order_customization = value.order_customization;
  order.value[0].shipping_date = value.shipping_date;
}

function togleAlert() {
  showAlert.value = !showAlert.value;
}
function togleModal() {
  showModal.value = !showModal.value;
}
function togleModalFile() {
  showFormFile.value = !showFormFile.value;
}


function fileUpdate(value) {
  console.log(value)
  togleModalFile();
  order.value[0].order_filetopographic = value.order_filetopographic;

  
}
// lifecycle hooks
onMounted(() => {
  callApi();
});
</script>
