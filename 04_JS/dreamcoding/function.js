// doSomething(add);
// dodo(add);
// 오.. 진짜 함수 선언(때 함수명 적은 애들)은.. 호이스팅이.. 되네.....
// 이건 함수 선언때는 노네임인데 const로 이름을 표현한 거라 호이스팅 안됨

// 함수 선언

function add(a, b) {
  const sum = a + b;
  return sum;
}

function doSomething(add) {
  console.log(add);
  const result = add(2, 3);
  console.log(result);
}

// 이건 함수를 무명으로 선언한 뒤에 const로 선언
// 엄밀히 함수는 무명이고 그 함수를 변수에 할당한 것
const dodo = function (add) {
  console.log(add);
  const result = add(5, 3);
  console.log(result);
};

function showMessage(message, from) {
  if (from === undefined) {
    from = "unknown";
  }
  console.log(`${message} by ${from}`);
}

function printAll(...args) {
  for (let i = 0; i < args.length; i++) {
    console.log(args[i]);
  }
}

// 함수 호출 맨 위에 호이스팅 되나 안 되나 호출한 것과 차이 알아두기
doSomething(add);
dodo(add);

// 확인용 함수 호출
printAll("dream", "coding", "eliie");
showMessage("hi");

// Callback func using function expression
// 두 가지의 콜백 함수가 파라미터로 전달됨
function randomQuiz(answer, printYes, printNo) {
  if (answer === "love you") {
    printYes();
  } else {
    printNo();
  }
}

const printYes = function () {
  console.log("yes!");
};
const printNo = function print() {
  console.log("no!");
};

randomQuiz("wrong", printYes, printNo);
randomQuiz("love you", printYes, printNo);

// Arrow Function
// always anonymous 항상 이름이 없는 함수

// const simplePrint = function () {
//     console.log('simplePrint!');
// }

const simplePrint = () => console.log("simplePrint!");
// example
const multi = (a, b) => {
  return a * b;
};