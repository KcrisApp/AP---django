<script setup>
import { ref, computed, onMounted } from "vue";
import { read, utils, writeFileXLSX } from 'xlsx';
import { endpoints } from "../common/endpoints";
import { axios } from "../common/api.service";
import NoteForm from "../components/NoteForm.vue"
import { useStoreUser } from "../stores/storeUsers";
import { useRouter } from "vue-router";

const props = defineProps({
  order_number: String,
});

const router = useRouter();


const onLoad = ref(false)
const colOrder_bom = ref([])
const order_bom = ref([])
const order = ref(null)
const showEditNote = ref(false)
const store = useStoreUser();
const note = ref("")
const showModalOption = ref(false)
const filterSmt = ref(false)
const filterTht = ref(false)
const sortDrw = ref(false)
const search = ref("");





// Filtri  di ricerca
const filterSearch = () =>{
  
  colOrder_bom.value =  order_bom.value.filter((order_b) =>
  order_b.drw.toLowerCase().includes(search.value.toLowerCase()) 
  );
}

const filterThtActive = () =>{

  filterTht.value =!filterTht.value

  if (filterTht.value) {
    colOrder_bom.value =  order_bom.value.filter((order_b) =>
  
  order_b.value.toLowerCase() == "tht" || order_b.value.toLowerCase() == "pth"
  );
  }
  else{
    colOrder_bom.value =  order_bom.value
  }

  
}


const filterSmdActive = () =>{

  filterSmt.value =!filterSmt.value
  if (filterSmt.value) {
  
      colOrder_bom.value =  order_bom.value.filter((order_b) =>
      order_b.value.toLowerCase() == "smd"
      );
      }

else{
    colOrder_bom.value =  order_bom.value
  }

}
const resetFilter = () =>{

filterSmd.value =!filterSmd.value
colOrder_bom.value =  order_bom.value

}

const filterSortByDrowing = () =>{

  sortDrw.value =!sortDrw.value
  if (sortDrw.value) {
    colOrder_bom.value.sort(function (a, b) {
      if (a.drw < b.drw) {
        return -1;
      }
      if (a.drw > b.drw) {
        return 1;
      }
      return 0;
    }); 
  }
  else{
    colOrder_bom.value.sort(function (a, b) {
      if (a.drw > b.drw) {
        return -1;
      }
      if (a.drw > b.drw) {
        return 1;
      }
      return 0;
    }); 
  }

   

}



const trigModal = () => showModalOption.value = !showModalOption.value

// Conteggio codici
const codeCount = computed(()=>{
  return colOrder_bom.value.length
})
const codeCheckedItem = computed(()=>{
  let counter = 0;
  for (const obj of colOrder_bom.value) {
    if (obj.check) counter++;
}
return counter
})

const codeToBeCheckedItem = computed(()=>{
  let counter = 0;
  for (const obj of order_bom.value) {
    if (!obj.check) counter++;
}
return counter
})
// Create xlsx order_bom
  function exportFile() {

    const ws = utils.json_to_sheet(order_bom.value);
    const wb = utils.book_new();
    utils.book_append_sheet(wb, ws, "Data");
    writeFileXLSX(wb, `bom_${order.value}.xlsx`);
    

  }
                                                                                                                                                                                                                                                                                                                             

  const addToList = (id) =>{
    console.log(id)

    for (const obj of colOrder_bom.value) {

      if(obj.id == id){
      
        obj.check = !obj.check
        console.log(obj)
        for (const obj_bom of order_bom.value) {

        if(obj_bom.id == id){

          obj_bom.check =  obj.check

        }
        }
  
      }}

 
      
    updateData()
}

// const addNoteToItem = (id) => {
//   note.value =  order_bom.value[id].note
//   selectId.value = id
//   showEditNote.value = true

// }


// const closeModal = () =>{
//   order_bom.value[ selectId.value].note = note.value
//   showEditNote.value = false
//   selectId.value = null

//   updateData()
// }


// Conteggio codici
// const codeCount = computed(()=>{
//   return order.order_order_bom_pick_and_place.value.length
// })

const goBack = () =>{
  router.back()
}

const resetAll = () =>{
  for (const obj of colOrder_bom.value) {
    obj.check = false
}
  for (const obj of order_bom.value) {
      obj.check = false
  }
updateData()
}
const checkAll = () =>{
  for (const obj of colOrder_bom.value) {
    obj.check = true
}
for (const obj of order_bom.value) {
    obj.check = true
}
updateData()
}



async function callApi() {
  
  onLoad.value = false
  const endpoint = `${endpoints["ordersCRUD"]}${props.order_number}/`;

  try {
    const response = await axios.get(endpoint);
    console.log(response);

    if (response.data.order_bom) {
      
      order_bom.value = JSON.parse(response.data.order_bom)
      colOrder_bom.value = JSON.parse(response.data.order_bom)
    }
    order.value = response.data.order_number

    console.log(response.data.order_bom);
    onLoad.value = true
  } catch (error) {
    alert(error);
  }
}


async function updateData() {
  
  const endpoint = `${endpoints["ordersCRUD"]}${props.order_number}/`;
  let method = "PATCH";
  try {
    const response = await axios({
      method: method,
      url: endpoint,
      data: {
        order_bom: JSON.stringify(order_bom.value),
      },

    });
   
  } catch (error) {
    alert(error.response);
  }
}

onMounted(()=>{
  callApi()
})

</script>



<template>
   <h1 class="text-2xl mb-4 text-blue-900">
              <font-awesome-icon icon="laptop-code" class="text-blue-950" />

             BOM 
    </h1>
    <div class="flex gap-2 justify-between">

      <p
    class="hover:text-green-600"
    @click="goBack"
    >
      
      <font-awesome-icon icon="arrow-left-long" /> Back
                
    </p>
 <!-- <pre>
  {{ placement }}
 </pre> -->




<div class="flex">
  <div class="m-2">
            <div class="relative">
              <div
                class=" inset-y-0 left-0 flex items-center pl-3 pointer-events-none"
              ></div>
              <input
                type="search"
                id="default-search"
                class="block w-full p-2 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder="Cerca drawing ref..."
                v-model="search"
                @keyup="filterSearch"
                required
              />
            </div>
      </div>


      <button
  @click="trigModal"
 class="btn bg-slate-300 hover:bg-slate-400 px-4 py-2 rounded-md m-2 text-sm">Filter
</button>
  <button
  @click="exportFile"
 class="btn bg-emerald-500 hover:bg-emerald-800 px-4 py-2 rounded-md m-2 text-white text-sm">Download
</button>
  <button
 @click="resetAll"
 class="bg-transparent m-2 hover:bg-blue-500 text-blue-700 hover:text-white text-sm py-2 px-4 border border-blue-500 hover:border-transparent rounded-md">Reset all
</button> 
<button
 @click="checkAll"
 class="bg-transparent m-2 hover:bg-green-500 text-green-700 hover:text-white text-sm py-2 px-4 border border-green-500 hover:border-transparent rounded-md">Check all
</button> 
</div>


    </div>
   
<!-- Idea si può usare la barra per vedere la percentuale di completamento -->

<!-- <div
v-if="onLoad" 
class="my-5">
    <div class="flex justify-between mb-1">
  <span class="text-base font-medium text-blue-700 dark:text-white">Import file</span>
  <span class="text-sm font-medium text-blue-700 dark:text-white">45%</span>
</div>
<div class="w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-700">
  <div class="bg-blue-600 h-2.5 rounded-full" style="width: 45%"></div>
</div>
</div> -->
<div
v-show="showModalOption"
class="bg-slate-100 my-2 p-4 rounded-md text-sm border shadow-md">
          <div class="flex justify-between">
            <p><b>Filter:</b></p>
            
            <p
            @click="resetFilter"
            class="underline cursor-pointer"
            >reset filter</p>
          </div>
         
          <hr class="my-2" />
          <div class="flex justify-start gap-2">
            <button
@click="filterSmdActive"
:class="filterSmt ? 'bg-blue-700 text-white':''"
 class="bg-transparent  hover:bg-blue-500 text-blue-700 hover:text-white text-sm  px-4 border border-blue-500 hover:border-transparent rounded-md">SMT
</button> 
<button
 @click="filterThtActive"
 :class="filterTht ? 'bg-green-600 text-white':''"
 class=" hover:bg-green-500 text-green-700 hover:text-white text-sm  px-4 border border-green-500 hover:border-transparent rounded-md">THT
</button> 
<button

 @click="filterSortByDrowing"
 class="bg-transparent  hover:bg-slate-500 text-slate-700 hover:text-white text-sm  px-4 border border-slate-500 hover:border-transparent rounded-md">Ordina 

  <span v-if="sortDrw">
    <font-awesome-icon icon="arrow-up-a-z" />
  </span>
  <span v-else>
    <font-awesome-icon icon="arrow-down-a-z" />
  </span>



 
</button> 

          </div>
       
           
        </div>




<hr class="my-2">
<div class="flex gap-2">
        <span
          class="bg-blue-100 text-blue-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded dark:bg-blue-900 dark:text-blue-300"
          >Codici totali: {{ codeCount }}</span
        >

        <!-- <span
          class="bg-red-100 text-red-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded dark:bg-red-900 dark:text-red-300"
          >Posizioni da verificare: {{ codeToBeCheckedItem }}</span
        > -->
        <span
          class="bg-green-100 text-green-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded dark:bg-green-900 dark:text-green-300"
          >Righe selezionate: {{ codeCheckedItem }}</span
        >
      </div>

<div class="relative overflow-x-auto shadow-md sm:rounded-lg mt-4">

  <!-- <NoteForm v-model="note"  v-if="showEditNote" @close-modal="closeModal"/> -->

    <table 
   
    class="w-full divide-y divide-gray-200 dark:divide-neutral-700 text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 overflow-x-auto over mt-4">
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
          <tr 
          v-for="(row, idx) in colOrder_bom" 
          :key="idx" 
          @dblclick ="addToList(row.id)"
          class="hover:text-white hover:bg-gray-400"
          :class = "row.check ?' text-white bg-blue-950 font-bold':''"  
         >

            <td 

            class=" border-b dark:border-gray-700">
            
                <th 
                
                scope="row" 
                class="px-6 py-4 font-medium  whitespace-nowrap dark:text-white0">{{ row.drw }}
              </th>
            </td>
            <td 
            class=" border-b dark:border-gray-700">
            
              <th 
                
                scope="row" 
                class="px-6 py-4 font-medium  whitespace-nowrap dark:text-white0">{{ row.pn }}
              </th>
            </td>
              <td 
            class=" border-b dark:border-gray-700">
            
              <th 
                
                scope="row" 
                class="px-6 py-4 font-medium  whitespace-nowrap dark:text-white0">{{ row.qta }}
              </th>
            </td>
              <td 

              
            class=" border-b dark:border-gray-700">
            
              <th 
                
                scope="row" 
                class="px-6 py-4 font-medium  whitespace-wrap dark:text-white ">
                  {{ row.desc }}
             
              </th>
            </td>
              <td 
            class=" border-b dark:border-gray-700">
              <th 
                scope="row" 
                class="px-6 py-4 font-medium  whitespace-nowrap dark:text-white0">
                {{ row.value}}
              </th>
            </td>
          </tr>
          
        </tbody>
    </table>
    
</div>

  </template>