<!-- <script setup>
import { ref, onMounted } from "vue";
import { read, utils, writeFileXLSX } from 'xlsx';

const rows = ref([]);

onMounted(async() => {
  /* Download from https://sheetjs.com/pres.numbers */
  const f = await fetch("https://sheetjs.com/pres.numbers");
  const ab = await f.arrayBuffer();

  /* parse workbook */
  const wb = read(ab);

  /* update data */
  rows.value = utils.sheet_to_json(wb.Sheets[wb.SheetNames[0]]);
});

/* get state data and export to XLSX */
function exportFile() {
  const ws = utils.json_to_sheet(rows.value);
  const wb = utils.book_new();
  utils.book_append_sheet(wb, ws, "Data");
  writeFileXLSX(wb, "SheetJSVueAoO.xlsx");
}
</script> -->

<script setup>
import { ref, onMounted } from "vue";
import { read, utils, writeFileXLSX } from 'xlsx';
const datatable = ref([])
const file = ref(null)
const colNumber = ref(0)
const rowSelectArray = ref([])
const onLoad = ref(false)
const selected = ref([])
// const classSelector = ref(['border-red-500 border-solid border-4','border-green-500 border-solid border-4','border-blue-500 border-solid border-4'])
const classSelector = ref([])
const typeCol = ['','border-red-500 border-solid border-4','border-orange-500 border-solid border-4','border-grey-500 border-solid border-4','border-blue-500 border-solid border-4','border-purple-500 border-solid border-4']


  function onChange(event) {
        onLoad.value = true
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
      }

const addToList = (id) =>{
    console.log(id)
    rowSelectArray.value = datatable.value.slice(id)
    console.log(rowSelectArray.value)
   
    // evt.currentTarget.classList.add('bg-green-500');
}



const selCol = (evt) =>{
    // numero della colonna
    console.log(evt.target.id)
    console.log(evt.target.value)
    console.log(classSelector.value)


    classSelector.value[evt.target.id] = typeCol[evt.target.value]

}


</script>



<template>
 
<!-- TW Elements is free under AGPL, with commercial license required for specific uses. See more details: https://tw-elements.com/license/ and contact us for queries at tailwind@mdbootstrap.com --> 
<div class="mb-3">
  <label
    for="formFile"
    class="mb-2 inline-block text-neutral-700 dark:text-neutral-200"
    >Import .xlsx file</label
  >
  <input
    class="relative m-0 block w-full min-w-0 flex-auto rounded border border-solid border-neutral-300 bg-clip-padding px-3 py-[0.32rem] text-base font-normal text-neutral-700 transition duration-300 ease-in-out file:-mx-3 file:-my-[0.32rem] file:overflow-hidden file:rounded-none file:border-0 file:border-solid file:border-inherit file:bg-neutral-100 file:px-3 file:py-[0.32rem] file:text-neutral-700 file:transition file:duration-150 file:ease-in-out file:[border-inline-end-width:1px] file:[margin-inline-end:0.75rem] hover:file:bg-neutral-200 focus:border-primary focus:text-neutral-700 focus:shadow-te-primary focus:outline-none dark:border-neutral-600 dark:text-neutral-200 dark:file:bg-neutral-700 dark:file:text-neutral-100 dark:focus:border-primary"
    type="file" 
    @change="onChange"
    id="formFile" />
</div>




<div
v-if="onLoad" 
class="my-5">
    <div class="flex justify-between mb-1">
  <span class="text-base font-medium text-blue-700 dark:text-white">Import file</span>
  <span class="text-sm font-medium text-blue-700 dark:text-white">45%</span>
</div>
<div class="w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-700">
  <div class="bg-blue-600 h-2.5 rounded-full" style="width: 45%"></div>
</div>
</div>


<!-- <pre>
  {{ datatable }}
</pre> -->
<div>
    {{ selected }}
</div>

<div class="relative overflow-x-auto shadow-md sm:rounded-lg">
    <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 overflow-x-auto over">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
                <th v-for="n in colNumber" scope="col" class="px-6 py-3">
                    <select  @change="selCol($event)" :id="n-1" :ref="n-1">
                      <option value="0">-</option>
                      <option value="1">Partnumber</option>
                      <option value="2">Drawing ref</option>
                      <option value="3">Qta</option>
                      <option value="4">Description</option>
                      <option value="5">Value</option>
                    </select>
                </th>
              
            </tr>
        </thead>
        <tbody>
          <tr 
          v-for="(row, idx) in datatable" 
          :key="idx" 
          @click="addToList(idx)"
          
         >
         <!-- :class = "id == 2 ?'border-red-500 border-solid border-4':''" -->
            <td 
            :class = "rowSelectArray.includes(row) ?'bg-green-600 text-white':'text-gray-900 '"
            class=" border-b dark:border-gray-700" 
            v-for="(r, id) in row">
             
                <th 
                :id="id"
                :class="rowSelectArray.includes(row) ? classSelector[id] :''"
                scope="row" 
                class="px-6 py-4 font-medium  whitespace-nowrap dark:text-white0">{{ r }}</th>
            
            </td>
            
          </tr>
          
        </tbody>
    </table>
</div>

  </template>