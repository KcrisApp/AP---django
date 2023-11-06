const baseEndpoint = "/api/v1/";

const endpoints = {
  boardsCRUD: `${baseEndpoint}board/`,
  ordersCRUD: `${baseEndpoint}order/`,
  testCRUD: `${baseEndpoint}test/`,
  updateImgBoard: `${baseEndpoint}boardImgUpdate/`,
  usersDetail: "/auth/users/me/",
};

export { endpoints };