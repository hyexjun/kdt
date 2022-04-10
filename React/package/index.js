const randomColor = require('randomcolor');
// 원래는 require(경로 설정) 해줘야하는데 외부에서 설치한 npm은 알아서 인식한대요..

let color1 = randomColor();
let color2 = randomColor();
let color3 = randomColor();

console.log(color1, color2, color3);