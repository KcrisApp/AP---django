import { defineStore } from 'pinia'


export const useStoreUser = defineStore('storeUser', {
  state:  () => {
    return{
      userData: null
    }
 },
 getters:{

  userInfo(state){
    return state.userData
  },
  permissionAccess(state){
    return state.userData.company_role === "M"   ?  true :  false
  },

  isTestingUser(state){
    return state.userData.department === "T" || state.userData.company_role === "M" ?  true :  false
  },

  isOfficeUser(state){
    return state.userData.department === "O" || state.userData.company_role === "M" ?  true :  false
  },

  isSmtUser(state){
    return state.userData.department === "S" || state.userData.company_role === "M" ?  true :  false
  },

  isWeldingUser(state){
    return state.userData.department === "W" || state.userData.company_role === "M" ?  true :  false
  },

  isShippingUser(state){
    return state.userData.department === "A" || state.userData.company_role === "M" ?  true :  false
  },

  isVerifyUser(state){
    return state.userData.department === "V" || state.userData.company_role === "M" ?  true :  false
  }
 }

})
