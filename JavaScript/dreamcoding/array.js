'use strict';
// Array 배열과 관련된 필수 APIs!!!!🎉

// 당근과 토끼가 엄청 많으면 당근바구니 토끼바구니.. 끼리 분류할 수도 있고
// 그렇게 담은.. 그런걸.. 자료구조....? 이게.... 자료구조...? ㅋㅋㅋㅋ
// 자료구조는 어떤 방식, 어떤 형식으로 담느냐에 따라 굉장히 다양한 타입이 있다.

// Q. Object와 자료구조의 차이는?

// obj ex. 토끼와 당근
// * 토끼의 특징 : 동물
// - 귀 2개 : 프로퍼티
// - 뛴다: 함수, 메소드
// - 먹는다: 함수, 메소드
// * 당근 : 채소
// - 비타민A : 프로퍼티
// - 주황색 : 프로퍼티
// ㄴobj는 뭘 할 수 없는 프로퍼티만 구성될 수도 있다!

// >> 이런 obj들을 또 obj끼리 묶은 건 자료구조라고 할 수 있음.
// 보통 다른 언어에서는 같은? 종류의 obj끼리만 자료구조로 묶을 수 있는데,
// js는 타입이 dynamically type language.. 쓰까가 된다..
// 물론.. 하면 안좋다.. ㅋㅋㅋㅋㅋㅋ 2:55 뚝배기 머야ㅠㅠ

// 나중에 자료구조와 알고리즘 꼭 공부해봐요!
// 검색, 삽입, 정렬, 삭제 etc.. big o 머시기..


// 1️⃣. Declaration 배열을 선언하는 방법
const arr1 = new Array(); // 이렇게도 되고
const arr2 = [1, 2]; // []; 속에 넣는 것도 되고


// 2️⃣. Index position
const fruits = ['🍎', '🍌'];
console.log('index', fruits);
console.log(fruits.length);
console.log(fruits[0]);
console.log(fruits[1]);
console.log('last index', fruits[fruits.length - 1]); // 보통 마지막 찾을 땐 일케..


// 3️⃣. Looping over an array
// print all fruits

// [1] 그냥 단순 for loop
console.log('for loop');
for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i]);
}

// [2] for (a of b) {} :: 파이썬 for i in range 느낌이네..
console.log('for (a of b) {}');
for (let fruit of fruits) { // 조건문 () 속에 let 잊지 말도록
  console.log(fruit);
}

// [3] forEach !!!!!!!!!!
console.log('forEach?');
fruits.forEach(function (fruit, index, array) {
  console.log(fruit, index, array);
}); // forEach <-- Ctrl click하면 내장함수 설명 볼 수 있음

console.log('Arrow==>');
// 여기서 이름 없는 함수는 화살함수 쓸 수 있었죠??
fruits.forEach((fruit, index, array) => {
  console.log(fruit, index, array);
});

console.log('간단쓰');
// 한 줄 짜리는 {};도 생략되쥬?
fruits.forEach((fruit, index, array) => console.log(fruit, index, array));

console.log('더 간단쓰');
fruits.forEach((fruit) => console.log(fruit));


// 4️⃣. Array Add, Del, Copy
// push: add an item to the end
console.log(fruits, 'push ⬇');
fruits.push('🍓', '🍑')
console.log(fruits);

// pop: remove an item from the end
console.log(fruits, 'pop ⬇');
fruits.pop(); // 맨 끝에 있는 것을 알아서 pop 날림 = 복숭아 pop
fruits.pop(); // 현재 기준 끝자락은 레몬이므로 레몬 pop
console.log(fruits); // 둘다 pop됐죠?

// unshift: add an item to the beginning
console.log(fruits, 'unshift ⬇');
fruits.unshift('🍋', '🍑')
console.log(fruits);

// shift: remove an item from the beginning
console.log(fruits, 'shift ⬇');
fruits.shift();
console.log(fruits);
fruits.shift();

// Warning!!!! :: unshift & shift are slower than pop, push !!

// splice: remove an item by index position
fruits.push('🍓', '🍑', '🍋');
console.log('all fruits', fruits);
// fruits.splice(몇번째부터, 몇 개); 몇 개 지울지는 쓸지말지 맘대루
// 지우려는 개수 설정을 하지 않으면? fruits.splice(1); 이후 다 날린다..
fruits.splice(1, 1);
console.log('- spliced array', fruits);
fruits.splice(1, 1, '🍏', '🍉');
console.log('+ spliced array', fruits);

// concat: combine two arrays
const fruits2 = ['🍍', '🥭'];
fruits.concat(fruits2);
console.log('concat', fruits.concat(fruits2));


// 5️⃣. Searching
// indexOf: 대상의 인덱스는 모르지만, 대상의 철자(생김새?)를 알면 찾아줌
const newFruits = fruits.concat(fruits2);
console.log(newFruits.indexOf('🍎'));
console.log(newFruits.indexOf('🥭'));
console.log(newFruits.indexOf('🍍'));
console.log(newFruits.indexOf('🍋'));
console.log(newFruits);
console.log(newFruits[6]);
console.log(newFruits[-1]);  // js는 역순 -1, -2 안 되나..?
// js에서는 undefined == -1로 말하는군요..

// includes: 이거 포함했어? <-- 를 boolean으로 알려준당
console.log(newFruits.includes('🍏'));
console.log(newFruits.includes('🍇'));

// lastIndexOf: 만약 배열에 같은 값이 또 있을 경우?
// 그냥 indexOf는 첫빠따로 나오면 알려주고 종료
// lastIndexOf는 뒤에서부터 알려주고 종료 ㅎㅎ
newFruits.push('🍎');
console.log('양쪽 사과', newFruits);
console.log('index', newFruits.indexOf('🍎'));
console.log('lastindex', newFruits.lastIndexOf('🍎'));