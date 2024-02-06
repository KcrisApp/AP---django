import { defineStore } from 'pinia'

export const useStoreUser = defineStore('storeUser', {
  state:  () => {
    return { 
    username: '', 
    name: '',
    first_name:'Cristiano',
    last_name:'',
    company_role:'',
    last_login: null
  }},
  
})