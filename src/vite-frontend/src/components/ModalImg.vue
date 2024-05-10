<template>
   <form>
   <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
  <!--
    Background backdrop, show/hide based on modal state.

    Entering: "ease-out duration-300"
      From: "opacity-0"
      To: "opacity-100"
    Leaving: "ease-in duration-200"
      From: "opacity-100"
      To: "opacity-0"
  -->
  <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>

  <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
    <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
      <!--
        Modal panel, show/hide based on modal state.

        Entering: "ease-out duration-300"
          From: "opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
          To: "opacity-100 translate-y-0 sm:scale-100"
        Leaving: "ease-in duration-200"
          From: "opacity-100 translate-y-0 sm:scale-100"
          To: "opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
      -->
      <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
        <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4 text-center">
          
         
           
            <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
              <h2 class="font-semibold text-xl leading-6 text-gray-900" id="modal-title">Immagine scheda</h2>
              <div class="mt-2">
                
                  <div>
                  <img :src="previewImage" class="uploading-image" />
                  <input type="file" accept="image/jpeg" id="fileInput" @change=uploadImage>
                </div>
                
              </div>
            </div>
          </div>
        
        <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6 gap-2">
         
          <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-green-500 px-3 py-2 text-sm font-semibold text-white shadow-sm ring-1 ring-inset  hover:bg-red-900 sm:mt-0 sm:w-auto" @click="postImg">Save</button>
          <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md  px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset  hover:bg-gray-200 sm:mt-0 sm:w-auto" @click="closeModal">Cancel</button>
        </div>
      </div>
    </div>
  </div>
</div>
</form>
</template>



<script setup>
import { endpoints } from "../common/endpoints";
import { axios } from "../common/api.service";
import { ref, defineEmits } from "vue";

const props = defineProps({
    board_id: {
        type: Number,
        required: true
            },
    side: {
        type: Boolean,
        required: true
            },
    
}
)
const previewImage = ref(null)
const image = ref(null)
const emit = defineEmits(["close-alert", "save-img"]);

function closeModal() {
  emit("close-alert")
}
function reset() {
  document.getElementById('fileInput').value = null;
}


function uploadImage(e){
    image.value = e.target.files[0];
    const reader = new FileReader();
    reader.readAsDataURL(image.value);
    reader.onload = e =>{
        previewImage.value = e.target.result;
          console.log(previewImage.value);
        }
      }

async function postImg() {
        var fd = new FormData();

        var sideImg = "board_img"

        fd.append("board_img", image.value);
        let endpoint = endpoints["updateImgBoard"]+`${props.board_id}`;

        if (props.side) {

          sideImg = "board_img_bot"
          endpoint = endpoints["updateImgBoardBot"]+`${props.board_id}`;
        }

        fd.append(sideImg, image.value);
        
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
            previewImage.value = null
            reset()
            emit("save-img", response.data);
          
        } catch (error) {
          alert(error)
        }
        
      }

</script>

