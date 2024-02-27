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

<script>
import { ref, onMounted } from "vue";
import { read, utils, writeFileXLSX } from 'xlsx';

export default {
    methods: {
      onChange(event) {
        this.file = event.target.files ? event.target.files[0] : null;
        if (this.file) {
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
            console.log(data)
          }
  
          reader.readAsBinaryString(this.file);
        }
      },
    }
  };
</script>
<!-- <template>
    <input type="file" @change="onChange" />
  <table><thead><tr><th>Name</th><th>Index</th></tr></thead><tbody>
    <tr v-for="(row, idx) in rows" :key="idx">
      <td>{{ row.Name }}</td>
      <td>{{ row.Index }}</td>
    </tr>
  </tbody><tfoot><td colSpan={2}>
    <button @click="exportFile">Export XLSX</button>
  </td></tfoot></table>
</template> -->


<template>
    <div id="app">
      <input type="file" @change="onChange" />
    </div>
  </template>