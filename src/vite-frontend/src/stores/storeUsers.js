import { defineStore } from 'pinia'


export const useStoreUser = defineStore('storeUser', {
  state:  () => {
    return{
      userData: null
    }
 },
 getters:{
  permissionAccess(state){
    return state.userData.company_role === "M" ?  true :  false
  }
 }

})
