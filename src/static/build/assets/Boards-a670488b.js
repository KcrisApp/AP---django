import{r as u,o as w,a as h,b as p,c as _,d as e,e as a,k as f,v as g,f as b,l as k,F as C,g as B,i as D,N as L,t as l,w as N,j as S}from"./index-dcd3e5f1.js";import{_ as M}from"./BoardForm-5f361ad1.js";const V={class:"container-fluid flex min-h-screen"},j={class:"m-4 w-full"},F={class:"flex justify-between gap-2"},A={class:"text-2xl"},R={class:"flex-1"},T={class:""},U={class:"relative"},z=e("div",{class:"absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none"},null,-1),E=e("hr",{class:"mt-2"},null,-1),$={class:"text-left text-sm font-light flex-wrap w-full"},q=e("thead",{class:"border-b font-medium dark:border-neutral-500"},[e("tr",null,[e("th",{scope:"col",class:"px-6 py-4"},"Scheda"),e("th",{scope:"col",class:"px-6 py-4"},"Codice"),e("th",{scope:"col",class:"px-6 py-4"},"Data creazione"),e("th",{scope:"col",class:"px-2 py-4"},"Revisione"),e("th",{scope:"col",class:"px-2 py-4"})])],-1),G={class:"whitespace-nowrap px-6 py-4 font-medium"},H={class:"whitespace-nowrap px-6 py-4"},I={class:"whitespace-nowrap px-6 py-4"},J={class:"whitespace-nowrap px-4 py-4"},K={class:"px-2 py-4"},O={class:"flex justify-center gap-4"},X={__name:"Boards",setup(P){const r=u([]),n=u(!1),c=u("");function d(){n.value=!n.value}function x(t){console.log(t),d(),r.value.unshift(t)}function m(){return r.value.filter(t=>t.board_name.toLowerCase().includes(c.value.toLowerCase()))}async function v(){let t=S.boardsCRUD;try{const o=await D.get(t);r.value.push(...o.data),console.log(o.data)}catch(o){alert(o)}}return w(()=>{v()}),(t,o)=>{const i=h("font-awesome-icon"),y=h("router-link");return p(),_("main",null,[e("div",V,[a(L),f(a(M,{onCloseModal:d,onSaveData:x},null,512),[[g,n.value]]),e("div",j,[e("div",F,[e("h1",A,[a(i,{icon:"hard-drive",class:"text-blue-950"}),b(" Schede ")]),e("div",R,[e("form",T,[e("div",U,[z,f(e("input",{type:"search",id:"default-search",class:"block w-full p-2 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",placeholder:"Cerca per ordine o nome scheda","onUpdate:modelValue":o[0]||(o[0]=s=>c.value=s)},null,512),[[k,c.value]])])])]),e("button",{class:"hover:bg-blue-500 text-blue-950 font-semibold hover:text-white py-1 px-6 border border-blue-950 rounded",onClick:d},[a(i,{icon:"folder-plus"}),b(" Add ")])]),E,e("table",$,[q,e("tbody",null,[(p(!0),_(C,null,B(m(),s=>(p(),_("tr",{class:"border-b dark:border-neutral-500",key:s.uuid},[e("td",G,l(s.board_name),1),e("td",H,l(s.board_code),1),e("td",I,l(s.created_at),1),e("td",J,l(s.board_rev),1),e("td",K,[e("div",O,[a(y,{to:{name:"board-details",params:{uuid:s.uuid}},class:""},{default:N(()=>[a(i,{icon:"fa-eye",class:"text-blue-950 hover:text-green-500"})]),_:2},1032,["to"])])])]))),128))])])])])])}}};export{X as default};
