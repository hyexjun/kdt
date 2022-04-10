'use strict';
// JavaScript is synchronous. 자바스크립트는 동기적이다.
// Excute the code block by orger after hoisting.
// hoisting: var, function declaration

// 동기적이란 건 걍 뭐.. 쓴 순서대로 나온다..? 당연한..?
console.log('1');
console.log('2');
console.log('3');


// 비동기적(async)이란 것은? - 언제 코드가 실행될지 예측 어려운?
console.log('1');
setTimeout(() => console.log('2'), 1000);
// 브라우저 API를 요청(조건 맞을 때 실행해=Call Back)해두고 걍 넘어가버림
console.log('3');
// 실행하자마자 1, (1000 뒤에) 2, 3 따닥 나올 줄 알았는데
// 1, 3 따닥 나오고 1000 뒤에 2 나옴.. 이것이 비동기다..


// Q. 콜백은 그러면 항상 비동기인가요? Nope.

// [1] Sync Callback
function printImmediately(print) {
	print();
}
printImmediately(() => console.log('hello'));

// [2] Async Callback
function printWithDelay(print, timeout) {
	setTimeout(print, timeout);
}
printWithDelay(() => console.log('async callback'), 2000);



// 🚀🚀 Callback Hell example
class UserStorage {
	loginUser(id, password, onSuccess, onError) {
		setTimeout(() => {
			if (
				(id === 'ellie' && password === 'dream') ||
				(id === 'coder' && password === 'academy')
			) {
				onSuccess(id);
			} else {
				onError(new Error('not found'));
			}
		}, 2000);
	}

	getRoles(user, onSuccess, onError) {
		setTimeout(() => {
			if (user === 'ellie') {
				onSuccess({ name: 'ellie', role: 'admin' });
			} else {
				onError(new Error('no access'));
			}
		}, 1000);
	}
}

const userStorage = new UserStorage();
const id = prompt('enter your id');
const password = prompt('enter your password');
userStorage.loginUser(
	id,
	password,
	(user) => {
		userStorage.getRoles(
			user,
			(userWithRole) => {
				alert(
					`Hello ${userWithRole.name}, you have a ${userWithRole.role} role`
				);
			},
			(error) => {
				console.log(error);
			}
		);
	},
	(error) => {
		console.log(error);
	}
);
