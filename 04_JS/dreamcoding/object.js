// Object 알아보기~~
const name = 'mille';
const age = 4;
print1(name, age);

function print1(name, age) {
  console.log(name);
  console.log(age);
}
// 이렇게 할 경우 params가 많으면 굉장히 더러워진다..
// params 5개면 줄줄줄 쓸거야..?

const ellie = { name: 'ellie', age: 5 }; // object 만드는 방법1 : obj literal syntax
function print2(person) {
  console.log(person.name);
  console.log(person.age);
}
print2(ellie);

// object 만드는 방법2 : obj constructor syntax
const ojb2 = new Object(); // 클래스 object를 이용해서 ㅎ
// 암튼 클래스방법 2 없어도 1번으로 만들수 있음

ellie.hasJob = true; // 뒤늦게 obj 추가가 가능함.. 다른 언어에선 잘 안됨
console.log(ellie.hasJob);
print2(ellie); // 근데 여기선 ellie, 5, true로 나오진 않음

delete ellie.hasJob; // 이렇게 프로퍼티 삭제도 됨...
print2(ellie);
