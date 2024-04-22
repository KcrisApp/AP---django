<template>
  <div class="my-4">
    <div 
    v-show="minimal_view"
    class="flex gap-4 my-4">

        <div class="flex items-center p-2 rounded-md bg-slate-100 gap-2 text-xs">
            <div v-if="order_status.order_smt">
            <svg
                xmlns="http://www.w3.org/2000/svg"
                x="0px"
                y="0px"
                width="20"
                height="20"
                viewBox="0 0 48 48"
            >
                <path
                fill="#c8e6c9"
                d="M44,24c0,11.045-8.955,20-20,20S4,35.045,4,24S12.955,4,24,4S44,12.955,44,24z"
                ></path>
                <path
                fill="#4caf50"
                d="M34.586,14.586l-13.57,13.586l-5.602-5.586l-2.828,2.828l8.434,8.414l16.395-16.414L34.586,14.586z"
                ></path>
            </svg>
            </div>
            <div v-else>
            <svg
                fill="red"
                height="15"
                width="15"
                version="1.1"
                id="Layer_1"
                xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink"
                viewBox="0 0 300.003 300.003"
                xml:space="preserve"
            >
                <g>
                <g>
                    <path
                    d="M150,0C67.159,0,0.001,67.159,0.001,150c0,82.838,67.157,150.003,149.997,150.003S300.002,232.838,300.002,150
                C300.002,67.159,232.839,0,150,0z M206.584,207.171c-5.989,5.984-15.691,5.984-21.675,0l-34.132-34.132l-35.686,35.686
                c-5.986,5.984-15.689,5.984-21.672,0c-5.989-5.991-5.989-15.691,0-21.68l35.683-35.683L95.878,118.14
                c-5.984-5.991-5.984-15.691,0-21.678c5.986-5.986,15.691-5.986,21.678,0l33.222,33.222l31.671-31.673
                c5.986-5.984,15.694-5.986,21.675,0c5.989,5.991,5.989,15.697,0,21.678l-31.668,31.671l34.13,34.132
                C212.57,191.475,212.573,201.183,206.584,207.171z"
                    />
                </g>
                </g>
            </svg>
            </div>
            Smt
    </div>
    <div class="flex items-center p-2 rounded-md bg-slate-100 gap-2 text-xs">
            <div v-if="order_status.order_welding">
            <svg
                xmlns="http://www.w3.org/2000/svg"
                x="0px"
                y="0px"
                width="20"
                height="20"
                viewBox="0 0 48 48"
            >
                <path
                fill="#c8e6c9"
                d="M44,24c0,11.045-8.955,20-20,20S4,35.045,4,24S12.955,4,24,4S44,12.955,44,24z"
                ></path>
                <path
                fill="#4caf50"
                d="M34.586,14.586l-13.57,13.586l-5.602-5.586l-2.828,2.828l8.434,8.414l16.395-16.414L34.586,14.586z"
                ></path>
            </svg>
            </div>
            <div v-else>
            <svg
                fill="red"
                height="15"
                width="15"
                version="1.1"
                id="Layer_1"
                xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink"
                viewBox="0 0 300.003 300.003"
                xml:space="preserve"
            >
                <g>
                <g>
                    <path
                    d="M150,0C67.159,0,0.001,67.159,0.001,150c0,82.838,67.157,150.003,149.997,150.003S300.002,232.838,300.002,150
                C300.002,67.159,232.839,0,150,0z M206.584,207.171c-5.989,5.984-15.691,5.984-21.675,0l-34.132-34.132l-35.686,35.686
                c-5.986,5.984-15.689,5.984-21.672,0c-5.989-5.991-5.989-15.691,0-21.68l35.683-35.683L95.878,118.14
                c-5.984-5.991-5.984-15.691,0-21.678c5.986-5.986,15.691-5.986,21.678,0l33.222,33.222l31.671-31.673
                c5.986-5.984,15.694-5.986,21.675,0c5.989,5.991,5.989,15.697,0,21.678l-31.668,31.671l34.13,34.132
                C212.57,191.475,212.573,201.183,206.584,207.171z"
                    />
                </g>
                </g>
            </svg>
            </div>
            Saldatura
    </div>
    <div class="flex items-center p-2 rounded-md bg-slate-100 gap-2 text-xs">
            <div v-if="order_status.order_verify">
            <svg
                xmlns="http://www.w3.org/2000/svg"
                x="0px"
                y="0px"
                width="20"
                height="20"
                viewBox="0 0 48 48"
            >
                <path
                fill="#c8e6c9"
                d="M44,24c0,11.045-8.955,20-20,20S4,35.045,4,24S12.955,4,24,4S44,12.955,44,24z"
                ></path>
                <path
                fill="#4caf50"
                d="M34.586,14.586l-13.57,13.586l-5.602-5.586l-2.828,2.828l8.434,8.414l16.395-16.414L34.586,14.586z"
                ></path>
            </svg>
            </div>
            <div v-else>
            <svg
                fill="red"
                height="15"
                width="15"
                version="1.1"
                id="Layer_1"
                xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink"
                viewBox="0 0 300.003 300.003"
                xml:space="preserve"
            >
                <g>
                <g>
                    <path
                    d="M150,0C67.159,0,0.001,67.159,0.001,150c0,82.838,67.157,150.003,149.997,150.003S300.002,232.838,300.002,150
                C300.002,67.159,232.839,0,150,0z M206.584,207.171c-5.989,5.984-15.691,5.984-21.675,0l-34.132-34.132l-35.686,35.686
                c-5.986,5.984-15.689,5.984-21.672,0c-5.989-5.991-5.989-15.691,0-21.68l35.683-35.683L95.878,118.14
                c-5.984-5.991-5.984-15.691,0-21.678c5.986-5.986,15.691-5.986,21.678,0l33.222,33.222l31.671-31.673
                c5.986-5.984,15.694-5.986,21.675,0c5.989,5.991,5.989,15.697,0,21.678l-31.668,31.671l34.13,34.132
                C212.57,191.475,212.573,201.183,206.584,207.171z"
                    />
                </g>
                </g>
            </svg>
            </div>
            Verifica
    </div>
    <div class="flex items-center p-2 rounded-md bg-slate-100 gap-2 text-xs">
            <div v-if="order_status.order_test">
            <svg
                xmlns="http://www.w3.org/2000/svg"
                x="0px"
                y="0px"
                width="20"
                height="20"
                viewBox="0 0 48 48"
            >
                <path
                fill="#c8e6c9"
                d="M44,24c0,11.045-8.955,20-20,20S4,35.045,4,24S12.955,4,24,4S44,12.955,44,24z"
                ></path>
                <path
                fill="#4caf50"
                d="M34.586,14.586l-13.57,13.586l-5.602-5.586l-2.828,2.828l8.434,8.414l16.395-16.414L34.586,14.586z"
                ></path>
            </svg>
            </div>
            <div v-else>
            <svg
                fill="red"
                height="15"
                width="15"
                version="1.1"
                id="Layer_1"
                xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink"
                viewBox="0 0 300.003 300.003"
                xml:space="preserve"
            >
                <g>
                <g>
                    <path
                    d="M150,0C67.159,0,0.001,67.159,0.001,150c0,82.838,67.157,150.003,149.997,150.003S300.002,232.838,300.002,150
                C300.002,67.159,232.839,0,150,0z M206.584,207.171c-5.989,5.984-15.691,5.984-21.675,0l-34.132-34.132l-35.686,35.686
                c-5.986,5.984-15.689,5.984-21.672,0c-5.989-5.991-5.989-15.691,0-21.68l35.683-35.683L95.878,118.14
                c-5.984-5.991-5.984-15.691,0-21.678c5.986-5.986,15.691-5.986,21.678,0l33.222,33.222l31.671-31.673
                c5.986-5.984,15.694-5.986,21.675,0c5.989,5.991,5.989,15.697,0,21.678l-31.668,31.671l34.13,34.132
                C212.57,191.475,212.573,201.183,206.584,207.171z"
                    />
                </g>
                </g>
            </svg>
            </div>
            Collaudo
    </div>
 
    </div>
    
    <div class="w-full bg-gray-200 rounded-full dark:bg-gray-700">
        
      <div
        class="bg-green-600 text-xs font-medium text-blue-100 text-center p-0.5 leading-none rounded-full"
        :style="{ 'width': percentValueBar  + '%' }"
      >
        {{ percentValueBar }}%
      </div>
    </div>
  </div>
</template>
<script setup>

  import { endpoints } from "../common/endpoints";
  import { ref, onMounted, computed } from "vue";
  import { axios } from "../common/api.service";
  const order_status = ref({})
  const onLoad = ref(false)


const props = defineProps({
        order_number:{
            type: String,
            required: true
        },
        minimal_view:{
            type: Boolean,
            required: true
        },
        })


const percentValueBar = computed(() => {

        let percent = [0,0,0,0]
    
        order_status.value.order_smt ? percent[0] = 25 : percent[0] = 0
        order_status.value.order_verify ? percent[1] = 25 : percent[1] = 0
        order_status.value.order_test ? percent[2] = 25 : percent[2] = 0
        order_status.value.order_welding ? percent[3] = 25 : percent[3] = 0

        return percent.reduce((a, b) => a + b, 0)

    });



  async function callApi() {

  onLoad.value = false
  const endpoint = `${endpoints["orderStatus"]}${props.order_number}/`;

  try {
    const response = await axios.get(endpoint);
    order_status.value = response.data;

    onLoad.value = true
  } catch (error) {
    alert(error);
  }
}



    // lifecycle hooks
    onMounted(() => {
    callApi();
    });
</script>
