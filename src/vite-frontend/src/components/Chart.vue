<template>
  <Line
    id="my-chart-id"
    :options="chartOptions"
    :data="chartData"
  />
  
</template>

<script setup>
  import { Line } from 'vue-chartjs'
  import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js'

  import { ref, onMounted, computed } from "vue";

  ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
)


const props = defineProps({
  label: {
    type: Object,
    required: false,
  },
  data_qta: {
    type: Object,
    required: false,
  },
});



const chartData = ref({
    
        labels: props.label,
        datasets: [ { 
            label: 'Boards',
            backgroundColor: '#2A71DB',
            borderColor: '#2A71DB',
            data: props.data_qta },
            
          ]
      })

const  chartOptions = ref({
        responsive: true
      })

</script>