<template>
  <h1 class="text-2xl mb-4 text-blue-900">
    <font-awesome-icon icon="laptop-code" class="text-blue-950" />
    BOM Creator
  </h1>
  <p class="hover:text-green-600 my-2" @click="goBack">
    <font-awesome-icon icon="arrow-left-long" /> Back
  </p>
  <div v-if="tableShow" class="mb-3 border rounded-md bg-gray-100 p-5">
    <label for="formFile" class="mb-2 inline-block text-blue-900 font-semibold text-xl dark:text-neutral-200 ">Import
      .xlsx file</label>
    <input
      class="relative m-0 block w-full min-w-0 flex-auto rounded border border-solid border-neutral-300 bg-clip-padding px-3 py-[0.32rem] text-base font-normal text-neutral-700 transition duration-300 ease-in-out file:-mx-3 file:-my-[0.32rem] file:overflow-hidden file:rounded-none file:border-0 file:border-solid file:border-inherit file:bg-neutral-100 file:px-3 file:py-[0.32rem] file:text-neutral-700 file:transition file:duration-150 file:ease-in-out file:[border-inline-end-width:1px] file:[margin-inline-end:0.75rem] hover:file:bg-neutral-200 focus:border-primary focus:text-neutral-700 focus:shadow-te-primary focus:outline-none dark:border-neutral-600 dark:text-neutral-200 dark:file:bg-neutral-700 dark:file:text-neutral-100 dark:focus:border-primary"
      type="file" @change="onChange" id="formFile" />
  </div>
  <button v-if="tableShow" @click="createBom" class="btn bg-green-600 px-4 py-2 rounded-md m-2 text-white">Crea
  </button>
  <button v-if="!tableShow" @click="backToFile" class="btn bg-red-600 px-4 py-2 rounded-md m-2 text-white">Indietro
  </button>
  <button v-if="!tableShow" @click="exportFile"
    class="btn bg-yellow-500 px-4 py-2 rounded-md m-2 text-white text-sm">Download BOM
  </button>
  <button v-if="!tableShow" @click="expandedBom"
    class="btn bg-cyan-600 px-4 py-2 rounded-md m-2 text-white text-sm">Download BOM expand
  </button>
  <button v-if="!tableShow" @click="save" class="btn bg-green-600 px-4 py-2 rounded-md m-2 text-white text-sm">Save
  </button>
  <div v-if="onLoad" class="my-5">
    <div class="flex justify-between mb-1">
      <span class="text-base font-medium text-blue-700 dark:text-white">Import file</span>
      <span class="text-sm font-medium text-blue-700 dark:text-white">45%</span>
    </div>
    <div class="w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-700">
      <div class="bg-blue-600 h-2.5 rounded-full" style="width: 45%"></div>
    </div>
  </div>
  <div class="relative overflow-x-auto shadow-md sm:rounded-lg mt-4">
    <h5>Numero codici: {{ codeCount }}</h5>
    <table v-if="tableShow"
      class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 overflow-x-auto over">
      <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
        <tr>
          <th v-for="n in colNumber" scope="col" class="px-6 py-3 text-lg">
            <select @change="selCol($event)" :id="n - 1" :ref="n - 1">
              <option value="0">-</option>
              <option value="1">Drawing ref</option>
              <option value="2">Partnumber</option>
              <option value="3">Qta</option>
              <option value="4">Description</option>
              <option value="5">Value</option>
            </select>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, idx) in datatable" :key="idx" @click="addToList(idx)">
          <td :class="rowSelectArray.includes(row) ? 'bg-green-600 text-white' : 'text-gray-900 '"
            class=" border-b dark:border-gray-700" v-for="(r, id) in row">
          <th :id="id" :class="rowSelectArray.includes(row) ? classSelector[id] : ''" scope="row"
            class="px-6 py-4 font-medium  whitespace-nowrap dark:text-white0">{{ r }}</th>
          </td>
        </tr>
      </tbody>
    </table>
    <table v-if="!tableShow"
      class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 overflow-x-auto over mt-4">
      <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
        <tr>
          <th scope="col" class="px-6 py-3">Drowing Ref</th>
          <th scope="col" class="px-6 py-3">Partnumber</th>
          <th scope="col" class="px-6 py-3">Qta</th>
          <th scope="col" class="px-6 py-3">Description</th>
          <th scope="col" class="px-6 py-3">Value</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, idx) in bomResult" :key="idx">
          <td class=" border-b dark:border-gray-700" v-for="(r, id) in row">
          <th :id="id" scope="row" class="px-6 py-4 font-medium  whitespace-nowrap dark:text-white0">{{ r }}
          </th>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>

import { ref, computed } from "vue";
import { read, utils, writeFileXLSX } from 'xlsx';
import { useRouter } from "vue-router";
import { endpoints } from "../common/endpoints";
import { axios } from "../common/api.service";


const datatable = ref([])
const file = ref(null)
const colNumber = ref(0)
const rowSelectArray = ref([])
const jsonToSave = ref(null)
const onLoad = ref(false)
const tableShow = ref(true)

const classSelector = ref([])
const colOrder = ref([])
const typeCol = ['', 'border-red-500 border-solid border-4', 'border-orange-500 border-solid border-4', 'border-grey-500 border-solid border-4', 'border-blue-500 border-solid border-4', 'border-purple-500 border-solid border-4']
const bomResult = ref([])


const props = defineProps({
  order_number: String,
});

const router = useRouter();


function onChange(event) {
  onLoad.value = true
  try {

    let colArray = []

    file.value = event.target.files ? event.target.files[0] : null;
    if (file.value) {
      const reader = new FileReader();

      reader.onload = (e) => {
        /* Parse data */
        const bstr = e.target.result;
        const wb = read(bstr, { type: 'binary' });
        /* Get first worksheet */
        const wsname = wb.SheetNames[0];
        const ws = wb.Sheets[wsname];
        /* Convert array of arrays */
        const data = utils.sheet_to_json(ws, { header: 1 });
        datatable.value = data
        console.log(data)

        datatable.value.forEach(element => {
          colArray.push(element.length)
        });

        colNumber.value = Math.max(...colArray)

      }

      reader.readAsBinaryString(file.value);
    }
    onLoad.value = false
    tableShow.value = true
  } catch (error) {
    alert(error)
  }

}

// Create xlsx BOM
function exportFile() {

  const ws = utils.json_to_sheet(bomResult.value);
  const wb = utils.book_new();
  utils.book_append_sheet(wb, ws, "Data");
  writeFileXLSX(wb, "BOM_normalized.xlsx");


}


const addToList = (id) => {
  console.log(id)
  rowSelectArray.value = datatable.value.slice(id)
  console.log(rowSelectArray.value)

}



const selCol = (evt) => {
  // numero della colonna
  console.log(evt.target.id)
  console.log(evt.target.value)
  console.log(classSelector.value)


  classSelector.value[evt.target.id] = typeCol[evt.target.value]
  colOrder.value[evt.target.id] = evt.target.value

}


const createBom = () => {
  rowSelectArray.value.forEach(element => {
    // console.log(`Drowing ref: ${element[colOrder.value.indexOf('1')]}`)
    // console.log(`Partnumber: ${element[colOrder.value.indexOf('2')]}`)
    // console.log(`Qta: ${element[colOrder.value.indexOf('3')]}`)
    // console.log(`Description: ${element[colOrder.value.indexOf('4')]}`)
    // console.log(`Value: ${element[colOrder.value.indexOf('5')]}`)
    let arrToPush = [element[colOrder.value.indexOf('1')], element[colOrder.value.indexOf('2')], element[colOrder.value.indexOf('3')], element[colOrder.value.indexOf('4')], element[colOrder.value.indexOf('5')]]
    bomResult.value.push(arrToPush)
    tableShow.value = false
  })

}

// Create expanded BOM
const expandedBom = () => {

  let tempArr = []
  bomResult.value.forEach(ele => {

    let arrPart = ele.slice(1)
    const singleDrowingArr = ele[0].split(" ");

    singleDrowingArr.forEach(d => {
      let arr = [d, ...arrPart]
      tempArr.push(arr)
    })



  })
  console.log(tempArr)

  const ws = utils.json_to_sheet(tempArr);
  const wb = utils.book_new();
  utils.book_append_sheet(wb, ws, "Data");
  writeFileXLSX(wb, "BOM_exp.xlsx");

}


const save = () => {
  let arr_to_save = []
  rowSelectArray.value.forEach((element, index) => {
    // console.log(`Drowing ref: ${element[colOrder.value.indexOf('1')]}`)
    // console.log(`Partnumber: ${element[colOrder.value.indexOf('2')]}`)
    // console.log(`Qta: ${element[colOrder.value.indexOf('3')]}`)
    // console.log(`Description: ${element[colOrder.value.indexOf('4')]}`)
    // console.log(`Value: ${element[colOrder.value.indexOf('5')]}`)
    let jsonToPush = { 'id': index, 'drw': element[colOrder.value.indexOf('1')], 'pn': element[colOrder.value.indexOf('2')], 'qta': element[colOrder.value.indexOf('3')], 'desc': element[colOrder.value.indexOf('4')], 'value': element[colOrder.value.indexOf('5')] }
    arr_to_save.push(jsonToPush)

  })

  sentData(arr_to_save)
}


// Conteggio codici
const codeCount = computed(() => {
  return bomResult.value.length
})

const backToFile = () => {
  bomResult.value = []
  tableShow.value = !tableShow.value
}

async function sentData(arr_to_save) {

  const endpoint = `${endpoints["ordersCRUD"]}${props.order_number}/`;
  let method = "PATCH";
  try {
    const response = await axios({
      method: method,
      url: endpoint,
      data: {
        order_bom: JSON.stringify(arr_to_save),
      },

    });
    console.log(response.data);
    jsonToSave.value = response.data.order_placement_pick_and_place
    goBack()

  } catch (error) {
    alert(error.response.status);
  }
}

const goBack = () => {
  router.back()
}
</script>

