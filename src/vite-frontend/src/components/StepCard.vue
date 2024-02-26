<template>
<li>


<div class="p-2 max-w-sm ">
        <div 
        class="border border-slate-100 flex rounded-lg h-full bg-slate-50 dark:bg-gray-800  flex-col">
        <div 
       
        class="py-2 rounded-md bg-blue-950 text-white">
        <h5 class="px-2 text-md font-medium">
          {{ step.step_name }}
       
        </h5>
        
        </div>
        <div class=" p-2">
          
          <div class="flex flex-col justify-between flex-grow">
              <p class="leading-relaxed text-base dark:text-gray-300">
                {{ step.step_description }}
              </p>
            
          </div>
          <div class="p-2" @mouseenter="togleActionBtn" @mouseleave="togleActionBtn">
                <div  v-show="showActionBtn"  class="flex mt-2 justify-end gap-4">
                <font-awesome-icon icon="pen-to-square"  class="text-blue-950 hover:text-green-500" @click="modSignal"/>
                <font-awesome-icon icon="trash"  class="text-red-900 hover:text-red-500" @click="deleteSignal"/>
                </div>
        </div>
          <div class="flex flex-col justify-between flex-grow mt-4">
       
            <span 
            :style="{ 'background-color': step.step_color }"
            class="text-black text-xs font-medium me-2 px-2.5 py-0.5 rounded dark:bg-blue-900 dark:text-blue-300">          {{ step.step_type }}</span>
           
          </div>
        </div>

        </div>
      
    </div>
</li>
</template>

<script setup>
import { ref, defineEmits } from "vue";

const emit = defineEmits(["mod-step", "delete-step"]);

const props = defineProps({
  step: {
    type:Object,
    required:true
}
});

const showActionBtn = ref(false)

const togleActionBtn = () => {
    showActionBtn.value = !showActionBtn.value
}
const deleteSignal = () => {
   emit("delete-step")
}
const modSignal = () => {
   emit("mod-step")
}



</script>

<style scoped>
.drag > div{
    transform: rotate(5deg);

}
.ghost{

    border-radius: 6px;
 
    border: 2px rgb(19, 44, 65) ;
    border-style: dashed;
}
.ghost > div{
    visibility: hidden;
}
</style>