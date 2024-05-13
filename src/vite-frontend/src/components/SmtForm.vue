<template>
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-900 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div
          class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-3xl">
          <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
            <div class="">
              <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                <div class="flex justify-between my-4">
                  <h2 class="text-base font-semibold leading-6 p-2 text-gray-900" id="modal-title">
                    <b class="text-blue-900">Aggiorna SMT</b>
                  </h2>
                  <div class="flex items-center">
                    <label for="status" class="block mr-2 text-md font-medium dark:text-white">Status:</label>
                    <select v-model="status" id="status"
                      class="p-2 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 block w-full dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                      <option selected value="false">Da completare</option>
                      <option value="true">Completate</option>
                    </select>
                  </div>
                </div>
                <hr class="mb-4" />
                <h3 class="my-4 text-md-body-1 font-semibold text-blue-900 dark:text-white text-center">
                  Controlli
                </h3>
                <ul
                  class="items-center w-full text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg sm:flex dark:bg-gray-700 dark:border-gray-600 dark:text-white">
                  <li class="w-full border-b border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600">
                    <div class="flex items-center ps-3">
                      <input id="fridge_temperature" type="checkbox" v-model="fridge_temperature"
                        class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded dark:ring-offset-gray-700 dark:bg-gray-600 dark:border-gray-500" />
                      <label for="fridge_temperature"
                        class="w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">Temperatura
                        frigo</label>
                    </div>
                  </li>
                  <li class="w-full border-b border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600">
                    <div class="flex items-center ps-3">
                      <input id="cream_expiration" type="checkbox" v-model="cream_expiration"
                        class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500" />
                      <label for="cream_expiration"
                        class="w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">Scadenza
                        crema</label>
                    </div>
                  </li>
                  <li class="w-full border-b border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600">
                    <div class="flex items-center ps-3">
                      <input id="cream_deposit" type="checkbox" v-model="cream_deposit"
                        class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500" />
                      <label for="cream_deposit"
                        class="w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">Deposito
                        crema</label>
                    </div>
                  </li>
                  <li class="w-full dark:border-gray-600">
                    <div class="flex items-center ps-3">
                      <input id="pick_and_place_setup" type="checkbox" v-model="pick_and_place_setup"
                        class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500" />
                      <label for="pick_and_place_setup"
                        class="w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">PeP setup</label>
                    </div>
                  </li>
                </ul>
                <ul
                  class="mt-2 items-center w-full text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg sm:flex dark:bg-gray-700 dark:border-gray-600 dark:text-white">
                  <li class="w-full border-b border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600">
                    <div class="flex items-center ps-3">
                      <input id="frame_status" type="checkbox" v-model="frame_status"
                        class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded dark:ring-offset-gray-700 dark:bg-gray-600 dark:border-gray-500" />
                      <label for="frame_status"
                        class="w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">Controllo
                        lamina</label>
                    </div>
                  </li>
                  <li class="w-full border-b border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600">
                    <div class="flex items-center ps-3">
                      <input id="board_check" type="checkbox" v-model="board_check"
                        class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500" />
                      <label for="board_check"
                        class="w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">Controllo
                        scheda</label>
                    </div>
                  </li>
                  <li class="w-full border-b border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600">
                    <div class="flex items-center ps-3">
                      <input id="oven_parameters" type="checkbox" v-model="oven_parameters"
                        class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500" />
                      <label for="oven_parameters"
                        class="w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">Parametri
                        forno</label>
                    </div>
                  </li>
                  <li class="w-full dark:border-gray-600">
                    <div class="flex items-center ps-3">
                      <input id="check_status" type="checkbox" v-model="check_status"
                        class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500" />
                      <label for="check_status"
                        class="w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">Controllo
                        parametri</label>
                    </div>
                  </li>
                </ul>
                <hr class="my-5" />
                <div class="mt-4">

                  <div class="mb-6">
                    <label for="mydata_program"
                      class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Programma MyData</label>
                    <input type="text" id="mydata_program"
                      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                      placeholder="" required v-model="mydata_program" />
                  </div>
                  <hr class="mb-4" />
                  <h3 class="my-4 text-md-body-1 font-semibold text-blue-900 dark:text-white text-center">
                    Forni
                  </h3>
                  <div class="my-5 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
                    <div class="sm:col-span-3">
                      <label for="oven_top" class="block text-sm font-medium leading-6 text-gray-900">Forno TOP</label>
                      <div class="mt-2">
                        <input type="text" name="oven_top" id="oven_top" v-model="oven_top"
                          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" />
                      </div>
                    </div>
                    <div class="sm:col-span-3">
                      <label for="oven_bot" class="block text-sm font-medium leading-6 text-gray-900">Forno BOT</label>
                      <div class="mt-2">
                        <input type="text" name="oven_bot" id="oven_bot" v-model="oven_bot"
                          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" />
                      </div>
                    </div>
                  </div>
                  <div class="my-5 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
                    <div class="sm:col-span-3">
                      <label for="recast_profile_top" class="block text-sm font-medium leading-6 text-gray-900">Profilo
                        forno TOP</label>
                      <div class="mt-2">
                        <input type="text" name="recast_profile_top" id="recast_profile_top"
                          v-model="recast_profile_top"
                          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" />
                      </div>
                    </div>
                    <div class="sm:col-span-3">
                      <label for="recast_profile_bot" class="block text-sm font-medium leading-6 text-gray-900">Profilo
                        forno BOT</label>
                      <div class="mt-2">
                        <input type="text" name="recast_profile_bot" id="recast_profile_bot"
                          v-model="recast_profile_bot"
                          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" />
                      </div>
                    </div>
                  </div>
                  <hr class="mb-4" />
                  <h3 class="my-4 text-md-body-1 font-semibold text-blue-900 dark:text-white text-center">
                    Serigrafia
                  </h3>
                  <div class="my-5 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
                    <div class="sm:col-span-3">
                      <label for="my500_top" class="block text-sm font-medium leading-6 text-gray-900">My500 TOP</label>
                      <div class="mt-2">
                        <input type="text" name="my500_top" id="my500_top" v-model="my500_top"
                          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" />
                      </div>
                    </div>
                    <div class="sm:col-span-3">
                      <label for="my500_bot" class="block text-sm font-medium leading-6 text-gray-900">My500 BOT</label>
                      <div class="mt-2">
                        <input type="text" name="my500_bot" id="my500_bot" v-model="my500_bot"
                          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" />
                      </div>
                    </div>
                  </div>
                  <div class="my-5 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
                    <div class="sm:col-span-3">
                      <label for="screen_printer_top" class="block text-sm font-medium leading-6 text-gray-900">Telaio
                        serigrafico TOP</label>
                      <div class="mt-2">
                        <input type="text" name="screen_printer_top" id="screen_printer_top"
                          v-model="screen_printer_top"
                          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" />
                      </div>
                    </div>
                    <div class="sm:col-span-3">
                      <label for="screen_printer_bot" class="block text-sm font-medium leading-6 text-gray-900">Telaio
                        serigrafico BOT</label>
                      <div class="mt-2">
                        <input type="text" name="screen_printer_bot" id="screen_printer_bot"
                          v-model="screen_printer_bot"
                          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" />
                      </div>
                    </div>
                  </div>
                  <div class="my-5 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
                    <div class="sm:col-span-3">
                      <label for="cream_type" class="block text-sm font-medium leading-6 text-gray-900">Tipo
                        crema</label>
                      <div class="mt-2">
                        <input type="text" name="cream_type" id="cream_type" v-model="cream_type"
                          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" />
                      </div>
                    </div>
                    <div class="sm:col-span-3 p-10">
                      <input checked id="cream_test" type="checkbox" v-model="cream_test"
                        class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />
                      <label for="cream_test"
                        class="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">Controllo crema</label>
                    </div>
                  </div>
                  <hr class="mb-4" />
                  <h3 class="my-4 text-md-body-1 font-semibold text-blue-900 dark:text-white text-center">
                    Info
                  </h3>
                  <div class="mb-6">
                    <label for="note" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Note di
                      processo</label>
                    <textarea v-model="note"
                      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                      name="note" id="note" cols="30" rows="3"></textarea>
                  </div>
                  <div class="mb-6">
                    <label for="missing_component"
                      class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Componenti mancanti</label>
                    <textarea v-model="missing_component"
                      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                      name="missing_component" id="missing_component" cols="30" rows="3"></textarea>
                  </div>
                  <div class="mb-6 mt-4">
                    <label for="firma" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Firma
                      operatore</label>
                    <input type="text" id="firma"
                      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                      placeholder="" required v-model="firma" />
                  </div>
                  <div class="px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                    <button @click="sentData"
                      class="mt-3 inline-flex w-full justify-center mx-2 rounded-md px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-blue-900 hover:text-white sm:mt-0 sm:w-auto">
                      Save
                    </button>
                    <button
                      class="mt-3 inline-flex w-full justify-center rounded-md px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-red-800 hover:text-white sm:mt-0 sm:w-auto"
                      @click="triggerCloseModal">
                      Cancel
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, defineEmits } from "vue";
import { endpoints } from "../common/endpoints";
import { axios } from "../common/api.service";

const props = defineProps({
  smt: {
    type: Object,
    required: false,
  },
});

const fridge_temperature = ref(props.smt.fridge_temperature);
const cream_expiration = ref(props.smt.cream_expiration);
const cream_deposit = ref(props.smt.cream_deposit);
const pick_and_place_setup = ref(props.smt.pick_and_place_setup);
const frame_status = ref(props.smt.frame_status);
const board_check = ref(props.smt.board_check);
const oven_parameters = ref(props.smt.oven_parameters);
const check_status = ref(props.smt.check_status);

const mydata_program = ref(props.smt.mydata_program);
const oven_top = ref(props.smt.oven_top);
const oven_bot = ref(props.smt.oven_bot);
const recast_profile_top = ref(props.smt.recast_profile_top);
const recast_profile_bot = ref(props.smt.recast_profile_bot);
const my500_top = ref(props.smt.my500_top);
const my500_bot = ref(props.smt.my500_bot);
const screen_printer_top = ref(props.smt.screen_printer_top);
const screen_printer_bot = ref(props.smt.screen_printer_bot);
const cream_type = ref(props.smt.cream_type);
const cream_test = ref(props.smt.cream_test);
const missing_component = ref(props.smt.missing_component);
const note = ref(props.smt.note);
const status = ref(props.smt.status);
const firma = ref(props.smt.firma);

const emit = defineEmits(["close-modal", "save-data"]);

async function sentData() {
  let endpoint = endpoints["smtCRUD"] + `${props.smt.uuid}/`;
  let method = "PATCH";
  let data = {
    fridge_temperature: fridge_temperature.value,
    cream_expiration: cream_expiration.value,
    cream_deposit: cream_deposit.value,
    pick_and_place_setup: pick_and_place_setup.value,
    frame_status: frame_status.value,
    board_check: board_check.value,
    oven_parameters: oven_parameters.value,
    check_status: check_status.value,
    mydata_program: mydata_program.value,
    oven_top: oven_top.value,
    oven_bot: oven_bot.value,
    recast_profile_top: recast_profile_top.value,
    recast_profile_bot: recast_profile_bot.value,
    my500_top: my500_top.value,
    my500_bot: my500_bot.value,
    screen_printer_top: screen_printer_top.value,
    screen_printer_bot: screen_printer_bot.value,
    cream_type: cream_type.value,
    cream_test: cream_test.value,
    note: note.value,
    firma: firma.value,
    status: status.value,
  }
  try {
    const response = await axios({
      method: method,
      url: endpoint,
      data: data
    });
    emit("save-data", response.data);
  } catch (error) {
    emit("save-data", error.response.status);
  }
}
function triggerCloseModal() {
  // emit an event to delete an answer instance
  emit("close-modal");
}
</script>
