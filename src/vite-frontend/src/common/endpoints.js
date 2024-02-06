const baseEndpoint = "/api/v1/";

const endpoints = {
  boardsCRUD: `${baseEndpoint}board/`,
  ordersCRUD: `${baseEndpoint}order/`,
  shippingCRUD: `${baseEndpoint}shipping/`,
  productionstepCRUD: `${baseEndpoint}productionstep/`,
  testCRUD: `${baseEndpoint}test/`,
  smtCRUD: `${baseEndpoint}smt/`,
  verifyCRUD: `${baseEndpoint}verify/`,
  updateImgBoard: `${baseEndpoint}boardImgUpdate/`,
  production: `${baseEndpoint}production/`,
  usersDetail: "/auth/users/me/",
};

export { endpoints };