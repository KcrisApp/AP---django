<template>
  <!-- card 1 -->
  <div class="p-2 w-100">
    <div class="flex rounded-lg h-xs dark:bg-gray-800 p-2 flex-col">
      <div class="flex items-center">
        <div
          v-if="status"
          class="w-6 h-6 mr-3 inline-flex items-center justify-center rounded-full dark:bg-indigo-500 bg-green-500 text-white flex-shrink-0"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            x="0px"
            y="0px"
            width="100"
            height="100"
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
        <div
          v-else
          class="w-6 h-6 mr-3 inline-flex items-center justify-center rounded-full dark:bg-indigo-500 bg-white text-white flex-shrink-0"
        >
          <svg
            fill="red"
            height="800px"
            width="800px"
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

        <h2 class="text-gray-600 dark:text-white text-sm font-medium">
          {{ text }}
        </h2>
      </div>
    </div>
  </div>
</template>
<script setup>
const props = defineProps({
  status: {
    type: Boolean,
    required: true,
    default: false,
  },
  text: {
    type: String,
    required: true,
  },
});
</script>
