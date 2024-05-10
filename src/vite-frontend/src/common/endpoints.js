const productionEndPoint = "/api/v1/production/";
const adminEndPoint = "/api/v1/administration/";

const endpoints = {
  boardsCRUD: `${productionEndPoint}board/`,
  ordersCRUD: `${productionEndPoint}order/`,
  orderStatus: `${productionEndPoint}order_status/`,
  shippingCRUD: `${productionEndPoint}shipping/`,
  productionstepCRUD: `${productionEndPoint}productionstep/`,
  testCRUD: `${productionEndPoint}test/`,
  smtCRUD: `${productionEndPoint}smt/`,
  weldingCRUD: `${productionEndPoint}welding/`,
  verifyCRUD: `${productionEndPoint}verify/`,
  updateImgBoard: `${productionEndPoint}boardImgUpdate/`,
  updateImgBoardBot: `${productionEndPoint}boardImgUpdateBot/`,
  updateTopographicFile: `${productionEndPoint}topographicOrder/`,
  updateGerberFile: `${productionEndPoint}gerberOrder/`,
  updateSchematicsFile: `${productionEndPoint}schematicsOrder/`,
  updateOdbFile: `${productionEndPoint}odbOrder/`,
  production: `${productionEndPoint}production/`,
  
};

const userEndPoints = {
  usersDetail: "/auth/users/me/",
  usersList: "/auth/users/",
}

const administrationEndpoint = {
  announcementCRUD: `${adminEndPoint}announcement/`,
}

export { endpoints, administrationEndpoint, userEndPoints };