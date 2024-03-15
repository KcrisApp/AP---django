import{r as o,b as c,d as u,e,w as g,br as F,v as w,k as A,bK as N,q as L,bH as R,bI as q,c as C,o as z,a as B,f as y,g as $,u as E,p as H,F as M,h as j,i as _,j as k,bL as I,t as K}from"./index-aa10096d.js";const O={class:"relative z-10","aria-labelledby":"modal-title",role:"dialog","aria-modal":"true"},G=e("div",{class:"fixed inset-0 bg-gray-900 bg-opacity-75 transition-opacity"},null,-1),J={class:"fixed inset-0 z-10 w-screen overflow-y-auto"},Q={class:"flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0"},W={class:"relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-3xl"},X={class:"bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4"},Y={class:""},Z={class:"mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left"},ee=e("div",{class:"flex justify-between my-4"},[e("h2",{class:"text-base font-semibold leading-6 p-2 text-gray-900",id:"modal-title"},[e("b",{class:"text-blue-900"},"Nuovo comunicato")])],-1),te=e("hr",{class:"my-5"},null,-1),oe={class:"mt-4"},ae={class:"mb-6"},se=e("label",{for:"status",class:"block mb-2 text-sm font-medium text-gray-900 dark:text-white"},"Tipo di annuncio:",-1),re=e("option",{selected:"",value:"avviso"},"Avviso",-1),le=e("option",{value:"comunicato"},"Comunicato",-1),ne=[re,le],de=e("hr",{class:"mb-4"},null,-1),ie={class:"mb-6 mt-4"},ce=e("label",{for:"titleForm",class:"block mb-2 text-sm font-medium text-gray-900 dark:text-white"},"Titolo",-1),ue={class:"mb-6 mt-4"},ge=e("label",{for:"content",class:"block mb-2 text-sm font-medium text-gray-900 dark:text-white"},"Titolo",-1),me={__name:"AnnouncementForm",emits:["close-modal","save-data"],setup(S,{emit:m}){const n=o(""),d=o(""),b=o("Avviso");o(null);async function h(){let i=N.announcementCRUD,a="POST",t={announcement_type:b.value,announcement_title:d.value,announcement_content:n.value};try{const v=await A({method:a,url:i,data:t});m("save-data",v.data)}catch(v){console.log(v),m("save-data",v.response.status)}}function x(){m("close-modal")}return(i,a)=>(c(),u("div",O,[G,e("div",J,[e("div",Q,[e("div",W,[e("div",X,[e("div",Y,[e("div",Z,[ee,te,e("div",oe,[e("div",ae,[se,g(e("select",{"onUpdate:modelValue":a[0]||(a[0]=t=>b.value=t),id:"status",class:"p-2 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 block w-full dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"},ne,512),[[F,b.value]])]),de,e("div",ie,[ce,g(e("input",{type:"titleForm",id:"orderNumber",class:"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",placeholder:"",required:"","onUpdate:modelValue":a[1]||(a[1]=t=>d.value=t)},null,512),[[w,d.value]])]),e("div",ue,[ge,g(e("textarea",{type:"text",id:"content",class:"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",placeholder:"",required:"","onUpdate:modelValue":a[2]||(a[2]=t=>n.value=t)},null,512),[[w,n.value]])]),e("div",{class:"px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6"},[e("button",{onClick:h,class:"mt-3 inline-flex w-full justify-center mx-2 rounded-md px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-blue-900 hover:text-white sm:mt-0 sm:w-auto"}," Save "),e("button",{class:"mt-3 inline-flex w-full justify-center rounded-md px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-red-800 hover:text-white sm:mt-0 sm:w-auto",onClick:x}," Cancel ")])])])])])])])])]))}},be={class:"p-4 w-full"},ve={class:"my-2 mx-5"},he={class:"flex justify-between gap-2 flex-wrap"},xe={class:"text-2xl flex-1"},fe={class:"flex-2"},ye={class:""},pe={class:"relative"},_e=e("div",{class:"absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none"},null,-1),ke=e("hr",{class:"my-5"},null,-1),we={class:"text-center mt-4"},Ce={"aria-label":"Page navigation example"},$e={class:"inline-flex -space-x-px text-sm"},Me=["onClick"],je=["onClick"],Ae=["onClick"],Te={__name:"AnnouncementList",props:{uuid:String},setup(S){const m=L();console.log(m.first_name);const n=o([]),d=o(""),b=o(!1),h=o(""),x=o(!1);o(!1),o(!1),R(),q();const i=o(0),a=o(15),t=o(0),v=C(()=>{const s=t.value*a.value,r=s+a.value;let f=n.value.filter(l=>l.announcement_title.toLowerCase().includes(d.value.toLowerCase()));return i.value=Math.ceil(f.length/a.value),console.log(i.value),f.slice(s,r)}),T=s=>{t.value=s-1},V=()=>{t.value++},D=()=>{t.value===0?t.value=0:t.value--};C(()=>order.value.length);async function U(){let s=N.announcementCRUD;try{const r=await A.get(s);n.value.push(...r.data),console.log(r.data)}catch(r){alert(r)}}function P(s){p(),typeof s=="number"?(h.value="Aggiornametno non riuscito",b.value=!1):(console.log(s),n.value.push(s),h.value="Aggiornametno avvenuto con successo",b.value=!0),setTimeout(()=>h.value="",5e3)}function p(){x.value=!x.value}return z(()=>{U()}),(s,r)=>{const f=B("font-awesome-icon");return c(),u("main",null,[e("div",be,[e("section",ve,[e("div",he,[e("h1",xe,[y(f,{icon:"hard-drive",class:"text-blue-950"}),$(" Comunicati ")]),e("div",fe,[e("form",ye,[e("div",pe,[_e,g(e("input",{type:"search",id:"default-search",class:"block w-full p-2 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",placeholder:"Cerca per nome scheda","onUpdate:modelValue":r[0]||(r[0]=l=>d.value=l)},null,512),[[w,d.value]])])])]),E(m).company_role=="M"?(c(),u("button",{key:0,class:"hover:bg-blue-500 text-blue-950 font-semibold hover:text-white py-1 px-6 border border-blue-950 rounded",onClick:p},[y(f,{icon:"folder-plus"}),$(" Add ")])):H("",!0)]),ke,(c(!0),u(M,null,j(v.value,l=>(c(),u("div",null,[y(I,{class:"my-4",annuncements:l},null,8,["annuncements"])]))),256))]),e("div",we,[e("nav",Ce,[e("ul",$e,[g(e("li",null,[e("a",{onClick:k(D,["prevent"]),class:"disabled flex items-center justify-center px-3 h-8 ms-0 leading-tight text-gray-500 bg-white border border-e-0 border-gray-300 rounded-s-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"},"Previous",8,Me)],512),[[_,t.value!==0]]),(c(!0),u(M,null,j(i.value,l=>(c(),u("li",null,[e("a",{onClick:k(Ne=>T(l),["prevent"]),class:"flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"},K(l),9,je)]))),256)),g(e("li",null,[e("a",{onClick:k(V,["prevent"]),class:"flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 rounded-e-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"},"Next",8,Ae)],512),[[_,t.value<i.value-1]])])])])]),g(y(me,{onCloseModal:p,onSaveData:P},null,512),[[_,x.value]])])}}};export{Te as default};
