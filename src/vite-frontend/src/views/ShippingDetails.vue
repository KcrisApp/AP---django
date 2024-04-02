<template>
  <main>
    <Info v-show="msg" :message="msg" :icon-type="iconType" />
    <div class="p-4 w-full">
      <div class="">
        <router-link
          v-if="orderNumber"
          :to="{
            name: 'order-details',
            params: { order_number: orderNumber },
          }"
          class="hover:text-green-600"
        >
          <font-awesome-icon icon="arrow-left-long" /> Back to {{ orderNumber }}
        </router-link>

        <hr class="my-4" />
      </div>

      <div class="flex justify-between my-4">
        <div>
          <h1 class="text-2xl mb-4 text-blue-900">
            <font-awesome-icon icon="truck-fast" />
            Dettaglio Spedizioni
          </h1>
        </div>

        <div class="flex gap-2">
          <button
            
            v-if="orderQta !== orderQtaDelivered && store.isShippingUser"
            class="hover:bg-amber-400 max-h-8 text-sm text-blue-950 font-semibold hover:text-white py-1 px-4 border hover:border-none border-blue-950 rounded"
            @click="togleModal"
          >
            Add
          </button>
        </div>
      </div>
      <div class="flex gap-2">
        <span
          class="bg-blue-100 text-blue-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded dark:bg-blue-900 dark:text-blue-300"
          >Quantità totale: {{ orderQta }} pz</span
        >
        <span
          class="bg-red-100 text-red-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded dark:bg-red-900 dark:text-red-300"
          >Da spedire: {{ orderQtaDelivery }} pz</span
        >
        <span
          class="bg-green-100 text-green-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded dark:bg-green-900 dark:text-green-300"
          >Spedite: {{ orderQtaDelivered }} pz</span
        >
      </div>
      <hr class="mt-2" />
      <table class="text-left text-sm font-light flex-wrap w-full">
        <thead class="border-b font-medium dark:border-neutral-500">
          <tr>
            <th scope="col" class="px-6 py-4">Ordine</th>
            <th scope="col" class="px-6 py-4">Collaudo</th>
            <th scope="col" class="px-6 py-4">Qtà</th>
            <th scope="col" class="px-2 py-4">Data</th>
            <th scope="col" class="py-4">Componenti mancanti</th>
            <th scope="col" class="py-4">Firma operatore</th>
            <th scope="col" class="py-4"></th>
          </tr>
        </thead>

        <tbody>
          <tr
            class="border-b dark:border-neutral-500"
            v-for="s in shipping"
            :key="s.uuid"
            ref="modalRef"
          >
            <td class="whitespace-nowrap px-6 py-4 font-medium">
              {{ s.order_number }}
            </td>
            <td class="whitespace-nowrap px-6 py-4">
              <CardCheck :status="s.shipping_check" text="" />
            </td>
            <td class="whitespace-nowrap px-6 py-4">
              {{ s.shipping_qta }}
            </td>

            <td class="whitespace-nowrap py-4">
              {{ useDateFormat(s.shipping_date) }}
            </td>
            <td class="whitespace-nowrap px-6 py-4">
              {{
                s.shipping_missing_components
                  ? s.shipping_missing_components
                  : "Nessuno"
              }}
            </td>
            <td class="whitespace-nowrap py-4">
              {{ s.firma }}
            </td>
            <td 
            v-if="store.isShippingUser"
            class="py-4">
              <div
                class="flex justify-center gap-4"
                @click="openModShipping(s)"
              >
                <font-awesome-icon
                  icon="pen-to-square"
                  class="text-blue-950 hover:text-green-500"
                />
              </div>
            </td>
            <td 
            v-if="store.isShippingUser"
            class="py-4">
              <div class="flex justify-center gap-4" @click="togleAlert">
                <font-awesome-icon
                  icon="trash"
                  class="text-red-900 hover:text-red-500"
                />
              </div>
              <Alert
                v-show="showAlert"
                icon-type="error"
                title="Attenzione"
                :message="`Sei sicuro di voler eliminare la spedizione per l'ordine ${s.order_number}?`"
                @close-alert="togleAlert"
                @confirm="deleteShipping(s.uuid)"
              />
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <ShippingForm
      v-show="showForm"
      @close-modal="togleModal"
      @save-data="updateShipping"
      :order="props.order_id"
      :max_shipping_board="orderQtaDelivery"
    />

    <ShippingForm
      v-if="showModModal"
      @close-modal="togleModifyForm"
      :ship="singleShip"
      :order="props.order_id"
      @save-data="updateSingleShip"
      :max_shipping_board="orderQtaDelivery"
    />
  </main>
</template>
<script setup>
import { endpoints } from "../common/endpoints";
import { axios } from "../common/api.service";
import { ref, onMounted, computed } from "vue";
import CardCheck from "../components/CardCheck.vue";
import ShippingForm from "../components/ShippingForm.vue";
import Alert from "@/components/Alert.vue";
import Info from "../components/Info.vue";
import {useDateFormat } from "../use/useDateFormat"
import { useStoreUser } from "../stores/storeUsers"

const store = useStoreUser();

const shipping = ref([]);
const showForm = ref(false);
const showAlert = ref(false);
const showModModal = ref(false);
const singleShip = ref({});
const iconType = ref(false);
const msg = ref("");

const props = defineProps({
  order_id: String,
});

const orderQta = computed(() => {
  let val = 0;
  shipping.value.forEach((element, index) => {
    if (index == 0) {
      val = element.order_quantity;
    }
  });

  return val;
});
const orderQtaDelivery = computed(() => {
  let val = 0;
  let orderDelivery = 0;
  let orderToDelivery = 0;
  shipping.value.forEach((element, index) => {
    orderDelivery += element.shipping_qta;
    if (index == 0) {
      val = element.order_quantity;
    }
  });

  orderToDelivery = val - orderDelivery;
  return orderToDelivery;
});

const orderQtaDelivered = computed(() => {
 
  let orderDelivery = 0;

  shipping.value.forEach((element, index) => {
    orderDelivery += element.shipping_qta;
  });

  return orderDelivery;
});

const orderNumber = computed(() => {
  let val = 0;
  shipping.value.forEach((element, index) => {
    if (index == 0) {
      val = element.order_number;
    }
  });

  return val;
});


const updateSingleShip = (value) => {
  const upd_obj = shipping.value.findIndex((obj) => obj.id == value.id);

  shipping.value[upd_obj].shipping_qta = value.shipping_qta;
  shipping.value[upd_obj].shipping_check = value.shipping_check;
  shipping.value[upd_obj].shipping_date = value.shipping_date;

  togleModifyForm();
};

function updateShipping(value) {
  togleModal();

  if (typeof value === "number") {
    msg.value = "Aggiornametno non riuscito";
    iconType.value = false;
  } else {
    shipping.value.unshift(value);
    msg.value = "Aggiornametno avvenuto con successo";
    iconType.value = true;
  }
  setTimeout(() => (msg.value = ""), 5000);
}

const updateDeleteShipping = (uuidDelete) => {
  shipping.value = shipping.value.filter((ship) => {
    return ship.uuid !== uuidDelete;
  });
};

const togleModal = () => {
  showForm.value = !showForm.value;
};

const togleModifyForm = () => {
  showModModal.value = !showModModal.value;
};
const openModShipping = (uuid) => {
  togleModifyForm();
  singleShip.value = uuid;
};

const togleAlert = () => {
  showAlert.value = !showAlert.value;
};

async function callApi() {
  // http://127.0.0.1:8000/api/v1/shipping/?order=12
  // `string text ${expression} string text`
  let endpoint = `${endpoints["shippingCRUD"]}?order=${props.order_id}`;

  try {
    const response = await axios.get(endpoint);
    shipping.value.push(...response.data);
  } catch (error) {
    alert(error);
  }
}

async function deleteShipping(uuid) {
  let endpoint = `${endpoints["shippingCRUD"]}${uuid}/`;

  try {
    const response = await axios.delete(endpoint);
    togleAlert();
    console.log(response);
    updateDeleteShipping(uuid);
  } catch (error) {
    alert(error);
  }
}

// lifecycle hooks
onMounted(() => {
  callApi();
});
</script>
