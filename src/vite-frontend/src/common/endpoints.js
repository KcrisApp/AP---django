const baseEndpoint = "/api/v1/";

const endpoints = {
  boardsCRUD: `${baseEndpoint}board/`,
  ordersCRUD: `${baseEndpoint}order/`,
  testCRUD: `${baseEndpoint}test/`,
  smtCRUD: `${baseEndpoint}smt/`,
  verifyCRUD: `${baseEndpoint}verify/`,
  updateImgBoard: `${baseEndpoint}boardImgUpdate/`,
  usersDetail: "/auth/users/me/",
};

export { endpoints };