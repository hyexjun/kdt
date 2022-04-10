const add = (a, b) => a + b;
const sub = (a, b) => a - b;

// 여기 있는 함수를 다른 파일에서 쓰려면 모듈화 해야함
module.exports = {
  moduleName: 'calc module',
  add: add,
  sub: sub,
};
