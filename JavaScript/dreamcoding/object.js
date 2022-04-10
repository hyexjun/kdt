// Objects
// one of JS's data types.
// a collection of related data and/or functionality.
// Nearly all objects in JS are instances of Object.
// ⁂ Object = { key : value };  !!!!!!!



// 1️⃣. Literals and properties
const obj1 = {}; // [1] 'object literal' syntax
// js에서는 class(붕어빵틀)가 없어도 1번 방법으로 오브젝트 생성 가능
const obj2 = new Object(); // [2] 'object constructor' syntax


// [A]
function print(name, age) {
  console.log(name); // 이렇게 할 경우 params가 많으면 굉장히 더러워진다..
  console.log(age); // params 5개면 줄줄줄 쓸거야..? 그래서 [A]는 사실 방법도 아님 ㅎㅎ
}
const name = 'ellie';
const age = 4;
print(name, age);


// [B]부터가 방법이라고 할 수 있습니다.
function print1(person) {
  console.log(person.name);
  console.log(person.age);
}
const ellie = { name: 'ellie', age: 4 }; // 하지만 이렇게 정리해주면? == [1] 방법으로 만든 것
print1(ellie); // [2] 방법으로 객체 생성한 건 안 나왔음


// 사람이라는 객체는 이름과 나이라는 속성이면 충분해! 하고 만들었다가
ellie.hasJob = true; // 뒤늦게 일을 하는지 아닌지 추가하고 싶어지면?
console.log(ellie.hasJob); // 이렇게 { name: 'ellie', age: 4, hasJob: true } 처럼 할 수 있음
// 하지만 자주 있는 경우는 아니고, 이렇게 동적으로 코딩하는 것은 좋지 못하므로 지양할 것!

console.log(ellie); // log 확인 시 { name: 'ellie', age: 4, hasJob: true } 나오죠?
delete ellie.hasJob; // 삭제도 된다는 놀라운 사실..
console.log(ellie); // 다시 log 보면 없어졌다 ㅎㅎ



// 2️⃣. Computed properties
// key should be always string
console.log(ellie['name']); // = console.log(ellie.name);
// 단 인덱스처럼? 대괄호에 넣을 때 key는 꼭 string으로 인식되도록 ''에 property명을 적어줘야함

console.log(ellie.hasJob); // 아까 위에서 삭제한 속성이라 안 나오쥬?
ellie['hasJob'] = true; // 다시 computed prop으로 지정하고
console.log(ellie.hasJob); // 나온다.


// 그럼 질문 : ellie.hasJob vs ellie['hasJob'] ???
function printValue(obj, key) {
  console.log(obj.key);
  console.log(obj[key]);
}
printValue(ellie, 'name');
printValue(ellie, 'age');



// 3️⃣. Property value shorthand
const person1 = { name: 'bob', age: 2 };
const person2 = { name: 'steve', age: 3 };
const person3 = { name: 'dave', age: 4 };


// Q. 만약 person4를 만들고 싶어지면? 어떻게 하는 게 좋을까요?
// A. 함수를 만들어서 써요!
function makePerson(a, b) {
  return {
    name: a,
    age: b,
  };
}
const person4 = makePerson('ellie', 30);
console.log(person4);


// 맞는데, JS에서 제공하는 ShortHand!
function makeSaram(name, age) {
  // 파라미터는 뭘 써도 상관 없는데
  return {
    // 원활한 의미파악을 위해 사용한 워딩이 같다면
    name: name, // ==>  name,
    age: age, // ==> age,  로 생략? 합치기 가능합니다.
  };
}


// 이렇게까지 줄여진다..
function makeIngan(name, age) {
  return {
    name,
    age,
  };
}
const person5 = makeIngan('ellie', 15);
console.log(person5);


// ⭐비구조화 할당 : 알아두기
let object = { one: 1, two: 2, three: 3, name: 'olla' }; // 오브젝트
let { name: myname, one: oneOne, two, three, abc = 'four' } = object;
// let { key: new varName, newVar='객체에 없을 경우 설정할 기본값 설정 가능' }
console.log('비구조화 할당 :', myname, oneOne, two, abc, three);



// 4️⃣. Constructor Function
// 가만 보면 func도 붕어빵틀처럼? 오브젝트 찍어내기가 가능하죠?
// 그래서 JS가 class를 지원하기 이전, 다른 계산을 하는 함수가 아니라
// 순수하게 오브젝트 생성용 함수는 이런 식으로 썼고.. 사실상 class 생성 문법과 거의 비슷
function Person(name, age) {
  // this = {};
  this.name = name;
  this.age = age;
  // return this;   가 생략된 것.
}
const person6 = new Person('ellie', 20);
console.log(person6); // 오 이건 또 앞에 함수명이 나오네요?



// 5️⃣. in operator: property existence check (key in obj)
// 프로퍼티가 그 오브젝트의 키로 있는지 아닌지 체크합니다.
console.log('name' in ellie);
console.log('age' in ellie);
console.log('job' in ellie); // key in ojb : 이건 boolean
console.log(ellie.job); // 이건 없는 속성이므로 출력해봐야 당연히 undefined



// 6️⃣. for..in vs for..of
// for (key in 객체명)
for (key in ellie) {
  console.log(key);
}

// 배열 보는 기존 방법 1
const array1 = [1, 2, 3, 4, 5];
for (let i = 0; i < array1.length; i++) {
  console.log(array1[i]);
}
// 방법 2 : for (value of 배열명)
const array2 = [6, 7, 8, 9, 10];
for (value of array2) {
  console.log(value);
}



// 7️⃣. Fun Cloning
// object.assign(dest, [obj1, obj2, obj3 ...])
const user = { name: 'ellie', age: 25 };
const user2 = user;
// 이러면 user의 메모리에 할당된 레퍼런스, user2에도 같은 레퍼런스가 할당되어 같다.


// Q. user2의 속성을 바꾸면 user에도 영향을 미칠까?
user2.name = 'coder';
// user2의 이름 속성을 바꾼 거면, user2는 당연히 바뀌어도 user는 그대로여야 할 것 같은데.
console.log(user); // 와 user가 바뀌는기고..
// 이게 복사되었지만 서로 다른 being 객체가 아니고..
// user2 = { name: 'ellie', age: 25 } << -- 복사된 데이터가 아니고..
// user2 = { name: user꺼 네임 데이터를 끌어오는 포털?, age: 쌤쌤 } 같은 느낌인가벼..


// Q. 그럼 진짜 복제는 어떻게 하나요?
// 방법 1 :
const user3 = {}; // 텅텅 빈 객체를 하나 만들고
for (key in user) {
  user3[key] = user[key];
}
console.log(user3);
user2.name = 'origin';
user3.name = 'num333';
console.log(user);
console.log(user2);
console.log(user3);

// 방법 2 : 기본적으로 내장된 모듈..?
// Object.assign(복사본명, 원본객체명);
const user4 = {};
Object.assign(user4, user);
console.log(user4);

// 이렇게 해도.. 된다.... 허어..
const user5 = Object.assign({}, user3);
console.log(user5);

// another sample
const fruit1 = { color: 'red'};
const fruit2 = { color: 'blue', size: 'big' };
const mixed = Object.assign({}, fruit1, fruit2); // 뒤에 쓰인 객체가 제일 세다 !!!
console.log(mixed.color);
console.log(mixed.size);