const productionEndPoint = "/api/v1/production/";
const adminEndPoint = "/api/v1/administration/";

const endpoints = {
  boardsCRUD: `${productionEndPoint}board/`,
  ordersCRUD: `${productionEndPoint}order/`,
  shippingCRUD: `${productionEndPoint}shipping/`,
  productionstepCRUD: `${productionEndPoint}productionstep/`,
  testCRUD: `${productionEndPoint}test/`,
  smtCRUD: `${productionEndPoint}smt/`,
  weldingCRUD: `${productionEndPoint}welding/`,
  verifyCRUD: `${productionEndPoint}verify/`,
  updateImgBoard: `${productionEndPoint}boardImgUpdate/`,
  updateImgBoardBot: `${productionEndPoint}boardImgUpdateBot/`,
  updateTopographicFile: `${productionEndPoint}topographicOrder/`,
  production: `${productionEndPoint}production/`,
  usersDetail: "/auth/users/me/",
};

const administrationEndpoint = {
  announcementCRUD: `${adminEndPoint}announcement/`,
}

export { endpoints, administrationEndpoint };