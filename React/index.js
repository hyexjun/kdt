// 반대로 모듈화한 다른 js파일을 불러오는 작업이 필요
const calc = require('./calc');

console.log(calc);
console.log(calc.add(1, 2));
console.log(calc.add(4, 5));
console.log(calc.sub(10, 2));
