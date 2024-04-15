<template>
  <main>

    <div class="p-4 w-full">
      <Alert
        v-show="showAlert"
        icon-type="error"
        title="Attenzione"
        message="Sei sicuro di voler eliminare la scheda?"
        @close-alert="togleAlert"
        @confirm="deleteBoard(board.uuid)"
      />

      <div v-if="isLoading">
        <BoardForm
          v-show="showForm"
          @close-modal="togleForm"
          @save-data="updateBoard"
          v-bind:boardArr="board"
        />
        <OrderForm
          v-show="showModal"
          v-bind:board_id="board.id"
          @close-modal="togleModal"
          @save-data="updateOrder"
        />
        <ModalImg
          v-show="showFormImg"
          @close-alert="togleImgForm"
          v-bind:board_id="board.id"
          v-bind:side="sideType"
          @save-img="imgUpdate"
        />
      </div>

      <div class="flex flex-wrap gap-4 justify-between my-4">
        <h1 class="text-2xl">
          <font-awesome-icon icon="hard-drive" class="text-blue-950" />
          Scheda: {{ board.board_name }}
        </h1>
        <div
        v-if="store.permissionAccess"
          class="flex gap-2"
         
        >
          <button
            class="hover:bg-blue-400 hover:border-blue-400 text-blue-950 font-semibold hover:text-white py-1 px-6 border border-blue-950 rounded"
            @click="togleModal"
          >
            <!-- <font-awesome-icon icon="folder-plus" /> Add order -->
            Add order
          </button>
          <button
            class="hover:bg-amber-400 hover:border-amber-400 text-blue-950 font-semibold hover:text-white py-1 px-4 border border-blue-950 rounded"
            @click="togleForm"
          >
            <!-- <font-awesome-icon icon="folder-plus" /> Modifica -->
            Modifica
          </button>
          <button
            class="hover:bg-red-900 bg-red-600 text-white font-semibold py-1 px-4 rounded"
            @click="togleAlert"
          >
            Elimina
          </button>
        </div>
      </div>
      

      <div 
      v-if="board.alert_info"
      class="  text-lg  rounded-xl mt-4 bg-red-50 text-red-700 shadow-md">
     
       <div class="flex flex-wrap items-center px-4 pt-4 gap-2 ">
        <font-awesome-icon icon="bell" class=" text-red-700"/>
        <span class="inline-flex items-center rounded-md bg-red-50 px-2 py-1 text-sm font-medium text-red-700 ring-1 ring-inset ring-red-600/10">Alert</span>
       
       </div>
       
       <p class="px-4 py-2 text-sm font-medium">
        <hr class="pb-2">
            {{ board.alert_info }} 
        </p>
         
      </div> 
      <hr class="my-2">
      <div class="flex bg-slate-50 p-4 gap-4 rounded-xl flex-wrap">
       
       
          <p>
            Codice: <b> {{ board.board_code }}</b>
          </p>
          <p >
            Revisione: <b> {{ board.board_rev }}</b>
          </p>

          <p>
            Data di creazione: <b> {{ useDateFormatted(board.created_at) }}</b>
          </p>
          <p>
            Cliente: <b> {{ board.customer }}</b>
          </p>
      
      </div> 


      
      <hr class="my-2" />
      <div class=" bg-slate-50 p-4 rounded-xl">
        <h3 class="text-xl font-semibold mb-4">Immagini</h3>
     
      <div class="flex gap-4  flex-wrap justify-start">
        <div class="col">
          <h5 class="font-semibold">TOP side</h5>
          <img class="h-auto max-w-xs" :src="board.board_img" />
          <button
          v-if="store.permissionAccess"
            class="hover:bg-slate-500 hover:border-slate-500 text-blue-950 font-semibold hover:text-white py-1 px-4 border border-blue-950 rounded mt-4"
            @click="togleImgForm(false)"
          >
            Carica/Modifica
          </button>
        </div>
        <div class="col">
          <h5 class="font-semibold">BOT side</h5>
        
          <img class="h-auto max-w-xs" :src="board.board_img_bot" />
          <button
          v-if="store.permissionAccess"
            class="hover:bg-slate-500 hover:border-slate-500 text-blue-950 font-semibold hover:text-white py-1 px-4 border border-blue-950 rounded mt-4"
            @click="togleImgForm(true)"
          >
            Carica/Modifica
          </button>
        </div>
      </div>
      </div>
      <div class="flex justify-between mt-4">
        <h4 class="text-2xl">Ordini</h4>
        <p
          class="bg-s-100 text-blue-800 text-sm font-medium mr-2 px-2.5 py-0.5 rounded dark:bg-slate-300 dark:text-blue-300"
        >
          Numero ordini: {{ orderCount }}
        </p>
      </div>

      <hr class="my-2" />
      <table class="text-left text-sm font-light flex-wrap w-full">
        <thead class="border-b font-medium dark:border-neutral-500">
          <tr>
            <th scope="col" class="px-6 py-4">Numero ordine</th>
            <th scope="col" class="px-6 py-4">Quantità</th>
            <th scope="col" class="px-6 py-4">Data di consegna</th>
            <th scope="col" class="px-6 py-4">Revisione</th>
          </tr>
        </thead>
        <tbody>
          <tr
            class="border-b dark:border-neutral-500"
            v-for="o in order"
            :key="order.uuid"
          >
            <td class="whitespace-nowrap px-6 py-2">
              <router-link
                :to="{
                  name: 'order-details',
                  params: { order_number: o.order_number },
                }"
                class="hover:text-green-600"
              >
                {{ o.order_number }}
              </router-link>
            </td>
            <td class="whitespace-nowrap px-6 py-2">
              {{ o.order_quantity }}
            </td>
            <td class="whitespace-nowrap px-6 py-2">{{ useDateFormatted(o.shipping_date) }}</td>
            <td class="whitespace-nowrap px-6 py-2">{{ o.order_customization }}</td>
          </tr>
        </tbody>
      </table>
      <hr class="my-5" />

      <div class="flex justify-center mt-5">
        <button
          class="hover:border-blue-500 text-blue-950 font-semibold hover:text-white py-1 px-4 rounded"
          :class="
            showSteps
              ? 'hover:bg-red-500'
              : 'bg-green-700 text-white hover:bg-blue-900'
          "
          @click="togleStepView"
        >
          {{
            showSteps ? "Nascondi fasi produttive" : "Mostra fasi produttive"
          }}
          <span
            v-show="!showSteps"
            class="bg-gray-100 text-gray-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded dark:bg-gray-700 dark:text-gray-400 border border-gray-500"
            >{{ stepCount }}</span
          >
        </button>
      </div>
      <p class="text-center" v-if="!showSteps">...</p>

      <div v-if="showSteps">
        <hr class="my-5" />

        <div class="flex justify-between my-4">
          <h4 class="text-xl ml-5 text-blue-900 font-bold">Fasi produttive</h4>

          <div class="flex gap-2">
            <button
            v-if="store.permissionAccess"
              class="hover:bg-blue-500 hover:border-blue-500 text-blue-950 font-semibold hover:text-white py-1 px-4 border border-blue-950 rounded"
              @click="togleStepForm"
            >
              <font-awesome-icon icon="folder-plus" /> Aggiungi fase
            </button>
          </div>
        </div>

        <div>
          <draggable
            class="flex flex-wrap justify-center mt-10"
            v-model="steps"
            group="step"
            item-key="id"
            tag="ul"
            drag-class="drag"
            ghost-class="ghost"
            @change="onChangeStepOrder"
            :disabled="!store.permissionAccess"
          >
            <template #item="{ element, index }">
              <StepCard
                :id="element.uuid"
                :step="element"
                @delete-step="deleteStep(element.uuid)"
                @mod-step="modStep(element)"
                :index="index"
              />
            </template>
          </draggable>

          <!-- <StepCard id="s.uuid" :color="s.step_color" :title="s.step_name"
            :content="s.step_description" :order="s.step_order" :rep="s.step_type" :key="s.uuid"
            @delete-step="deleteStep(s.uuid)" @mod-step="modStep(s)" />  -->
        </div>
        <StepForm
          v-show="showStepsForm"
          :board="orderNumber"
          @close-modal="togleStepForm"
          @save-data="saveDataStep"
        />

        <StepForm
          v-if="showModStepsForm"
          :steps="singleStep"
          :board="orderNumber"
          @close-modal="showModStepsForm = false"
          @save-data="updateSingleStep"
        />
      </div>
    </div>
  </main>
</template>
<script setup>
import { endpoints } from "../common/endpoints";
import { axios } from "../common/api.service";
import { ref, onMounted, computed } from "vue";
import Alert from "../components/Alert.vue";
import OrderForm from "../components/OrderForm.vue";
import StepForm from "../components/StepForm.vue";
import BoardForm from "../components/BoardForm.vue";
import ModalImg from "../components/ModalImg.vue";
import StepCard from "../components/StepCard.vue";
import { useDateFormatted } from "../use/useDateFormatted";
import { useRouter } from "vue-router";
import Info from "../components/Info.vue";
import draggable from "vuedraggable";

import { useStoreUser } from "../stores/storeUsers";
// access the `store`
const store = useStoreUser();


const board = ref({});
const order = ref([]);
const steps = ref([]);
const iconType = ref(false);
const msg = ref("");

const showAlert = ref(false);
const showModal = ref(false);
const showForm = ref(false);
const showFormImg = ref(false);
const showSteps = ref(false);
const showStepsForm = ref(false);
const showModStepsForm = ref(false);
const isLoading = ref(false);
const dragDisable = ref(false);
const sideType = ref(false);
const singleStep = ref({});
const router = useRouter();


const props = defineProps({
  uuid: String,
});

// gestione drag and drop delle card per gli step di produzione
async function onChangeStepOrder(e) {
  let item = e.moved || e.added;
  if (!item) return;

  let index = item.newIndex;

  let currentStep = steps.value[index];
  let prevStep = steps.value[index - 1];
  let nextStep = steps.value[index + 1];

  let position = Math.round(currentStep.step_order);

  if (prevStep && nextStep) {
    // console.log('pre  + next')
    // console.log('pre',prevStep.step_order)
    // console.log('next',nextStep.step_order)
    position = Math.round((prevStep.step_order + nextStep.step_order) / 2);
  } else if (prevStep) {
    // console.log("pre")
    // console.log('pre',prevStep.step_order)

    position = Math.round(prevStep.step_order + prevStep.step_order / 2);
  } else if (nextStep) {
    // console.log("next")
    // console.log('next',nextStep.step_order)
    position = Math.round(nextStep.step_order / 2);
  }

  // console.log(currentStep)
  // console.log(prevStep)
  // console.log(nextStep)
  console.log(position);
  try {
    let response = await axios.patch(
      endpoints["productionstepCRUD"] + `${currentStep.uuid}/`,
      { step_order: position }
    );
    // console.log(response)
    currentStep.step_order = position;
  } catch (error) {
    console.log(error);
  }
}
// a computed ref
const orderCount = computed(() => {
  return order.value.length;
});
const stepCount = computed(() => {
  return steps.value.length;
});

const orderNumber = computed(() => {
  return board.value.id;
});
// const orderSteps = computed(() => {
//   return steps.value.sort((a, b) => a.step_order - b.step_order);
// }
// )

const modStep = (step) => {
  singleStep.value = step;
  showModStepsForm.value = true;
};

const updateSingleStep = (value) => {
  const upd_obj = steps.value.findIndex((obj) => obj.uuid == value.uuid);
  console.log(value);

  steps.value[upd_obj].step_type = value.step_type;
  steps.value[upd_obj].step_name = value.step_name;
  steps.value[upd_obj].step_description = value.step_description;
  steps.value[upd_obj].step_color = value.step_color;
  steps.value[upd_obj].step_order = value.step_order;
  showModStepsForm.value = false;
};

async function callApiBoard() {
  isLoading.value = false;
  try {
    // Test axios all
    axios
      .all([
        axios.get(`${endpoints["boardsCRUD"]}${props.uuid}/`),
        axios.get(`${endpoints["productionstepCRUD"]}?board=${props.uuid}`),
      ])
      .then(
        axios.spread((data1, data2) => {
          // output of req.
          board.value = data1.data;
          order.value = data1.data.order;

          data2.data.forEach((element) => {
            steps.value.push(element);
          });
          isLoading.value = true;
        })
      );
  } catch (error) {
    alert(error);
  }
}

async function deleteBoard() {
  let endpoint = `${endpoints["boardsCRUD"]}${props.uuid}/`;

  try {
    const response = await axios.delete(endpoint);
    togleAlert();
    router.push({ name: "boards" });
  } catch (error) {
    alert(error);
  }
}

async function deleteStep(uuid) {
  let endpoint = `${endpoints["productionstepCRUD"]}${uuid}/`;

  try {
    const response = await axios.delete(endpoint);

    console.log(response);
    updateDeleteStep(uuid);
  } catch (error) {
    alert(error);
  }
}

const saveDataStep = (newStep) => {
  togleStepForm();
  steps.value.push(newStep);
};
const updateDeleteStep = (uuidDelete) => {
  steps.value = steps.value.filter((step) => {
    return step.uuid !== uuidDelete;
  });
};

function updateOrder(value) {
  togleModal();
  order.value.unshift(value);
}

function updateBoard(value) {
  togleForm();
  if (typeof value === "number") {
    msg.value = "Aggiornametno non riuscito";
    iconType.value = false;
  } else {
    console.log(value);
    board.value = value;
    msg.value = "Aggiornametno avvenuto con successo";
    iconType.value = true;
  }

  setTimeout(() => (msg.value = ""), 5000);
}
function imgUpdate(value) {
  console.log(value)
  togleImgForm(sideType.value);

  if (sideType.value) {
    board.value.board_img_bot = value.board_img_bot;
   
 
  }
  else{

    board.value.board_img = value.board_img;
   
  }
  
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
function togleStepView() {
  showSteps.value = !showSteps.value;
}
function togleStepForm() {
  showStepsForm.value = !showStepsForm.value;
}
function togleImgForm(sideValue) {
  sideType.value = sideValue
  showFormImg.value = !showFormImg.value;
}
const chekUserPermission = () => {
  if (store.company_role == "M") {
    dragDisable.value = false;
  }
};
// lifecycle hooks
onMounted(() => {
  callApiBoard();
  chekUserPermission();
});
</script>
