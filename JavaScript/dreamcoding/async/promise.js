'use strict';

// Promise is a JS obj for async operation.
// [1] State
// promise가 만들어져 지정한 operation을 수행중일 때 : pending -->
// 수행을 성공적으로 마치면 'fulfilled state' || 파일을 못 찾거나 네트워크 문제가 있거나 등 'rejected state'
// [2] Producer & Consumer 차이를 아는 것?



// 1️⃣. Producer
const promise = new Promise((resolve, reject) => {
	// 네트워크에서 데이터를 받거나, 파일에서 큰 데이터를 읽는 것은 시간 걸림
	// 이런 걸 동기적으로 처리하면 받아오는 동안 다음 라인의 코드가 실행되지 않기 때문에
	// 비동기식으로 처리하는 게 좋다ㅑ
	// promise를 선언하자마자 콜백함수가 바로 실행돼버림
	// 만약 프로미스 안에 네트워크 통신 함수를 만들면, 그와 동시에 네트워크 통신도 풀악셀..
	// 사용자가 요구했을 때(ex 버튼)만 통신해야 하는 거라면 이런 식으로는 하면 안되겠쥬 ❌❌
	// 한줄요약 : promise는 선언과 동시에 실행 때려버리니 유의합시다.
	console.log('doing something...');
	setTimeout(() => {
		// resolve('ellie');
		reject(new Error('no network'));
	}, 2000);
});



// 2️⃣. Consumers : then, catch, finally
promise
	.then((value) => {
		console.log(value); // 약속내용(정상적으로 성공하면 ellie가 넘어옴)
	})
	.catch((error) => {
		console.log(error); // 정상적으로?ㅋㅋ 실패하면 이 코드 실행
	})
	.finally(() => {
		console.log('finally'); // 기든 아니든 무조건 실행되는 코드
	}); // cf. 어쩌구().저쩌구().함수() 이렇게 줄줄이 이어져 실행되는거 == method chaining



// 3️⃣. ⚡ Promise Chaining ⚡
const fetchNumber = new Promise((resolve, reject) => {
	setTimeout(() => resolve(1), 1000); // 1000(1초) 뒤에 1을 넘겨주세요
});

fetchNumber // 니콜라스 js때 fetch then 사용했었지용? 거긴 설명은 생략됐지만..ㅋㅋ
	.then((num) => num * 2)
	.then((num) => num * 3)
	.then((num) => {
		return new Promise((resolve, reject) => {
			setTimeout(() => resolve(num - 1), 1000);
		});
	})
	.then((num) => console.log(num));



// 4️⃣. Error Handling
const getHen = () =>
	new Promise((resolve, reject) => {
		setTimeout(() => resolve('🐔'), 1000);
	});

// 🌟 resolve Ver.🌟
// const getEgg = (hen) =>
// 	new Promise((resolve, reject) => {
// 		setTimeout(() => resolve(`${hen} -> 🥚`), 1000);
// 	});

// 🔔 reject Ver.🔔
const getEgg = (hen) =>
new Promise((resolve, reject) => {
	setTimeout(() => reject(new Error(`error! ${hen} -> 🥚`)), 1000);
});

const cook = (egg) =>
	new Promise((resolve, reject) => {
		setTimeout(() => resolve(`${egg} -> 🍳`), 1000);
	});

// 🌟 resolve Ver.🌟  cf. then((a) => func(a)) 일 경우 then(func)으로
// getHen()
// 	.then((hen) => getEgg(hen))
// 	.then((egg) => cook(egg))
// 	.then((meal) => console.log(meal));

// 🔔 reject Ver.🔔
getHen()
  .then(getEgg)
  .catch(error => {
    return '🥓';
  })
  .then(cook)
  .then(console.log)
  .catch(console.log);