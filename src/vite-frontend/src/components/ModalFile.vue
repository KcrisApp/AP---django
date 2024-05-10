<template>
   <div>
   <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">

  <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>

  <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
    <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">

      <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
        <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4 text-center">
          
         
           
            <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
              <h2 class="font-semibold text-xl leading-6 text-gray-900" id="modal-title">File {{file_type}}</h2>
              <div class="mt-2">
                
                  <div>
                  <input type="file" @change=uploadFile id="fileInput">
                </div>
                
              </div>
            </div>
          </div>
        
        <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6 gap-2">
         
          <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-green-500 px-3 py-2 text-sm font-semibold text-white shadow-sm ring-1 ring-inset  hover:bg-red-900 sm:mt-0 sm:w-auto" @click="postFile">Save</button>
          <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md  px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset  hover:bg-gray-200 sm:mt-0 sm:w-auto" @click="closeModal">Cancel</button>
          <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md  px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset  hover:bg-gray-200 sm:mt-0 sm:w-auto" @click="reset">reset</button>
        </div>
      </div>
    </div>
  </div>
</div>
</div>
</template>



<script setup>
import { endpoints } from "../common/endpoints";
import { axios } from "../common/api.service";
import { ref, defineEmits } from "vue";

const props = defineProps({
    order_id: {
        type: Number,
        required: true
            },

    file_type: {
        type: String,
        required: true
            },
    
}
)

const file = ref()
const emit = defineEmits(["close-alert", "save-file"]);

function closeModal() {
  emit("close-alert")
}
function reset() {
  document.getElementById('fileInput').value = null;
}



function uploadFile(e){
    file.value = e.target.files[0];
      }


async function postFile() {

        var fd = new FormData();
        let endpoint = ""

        switch (props.file_type) {

          case 'topographic':
            console.log(props.file_type)
            fd.append("order_file_topographic", file.value);
            endpoint = endpoints["updateTopographicFile"]+`${props.order_id}`;

            break;

          case 'odb':
            console.log(props.file_type)
            fd.append("order_file_odb", file.value);
            endpoint = endpoints["updateOdbFile"]+`${props.order_id}`;

            break;

          case 'gerber':

            console.log(props.file_type)
          fd.append("order_file_gerber", file.value);
            endpoint = endpoints["updateGerberFile"]+`${props.order_id}`;

            break;

          case 'schematic':

            console.log(props.file_type)
          fd.append("order_file_schematics", file.value);
            endpoint = endpoints["updateSchematicsFile"]+`${props.order_id}`;

            break;
          
        }



        // fd.append("order_filetopographic", file.value);
        // let endpoint = endpoints["updateTopographicFile"]+`${props.order_id}`;
        console.log(endpoint)

        try {
          const response = await axios({
                    method: "put",
                    url: endpoint,
                    data: fd,
                    headers: {
                      "content-type": `multipart/form-data; boundary=${fd._boundary}`,
                    },
                  })
            console.log(response)

            emit("save-file", response.data);
            reset()
          
        } catch (error) {
          alert(error)
        }
         
      }

</script>

