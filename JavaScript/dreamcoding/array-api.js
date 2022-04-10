// Q1. make a string out of an array
{
	const fruits = ['apple', 'banana', 'orange'];
	const result = fruits.join(); // join(구분자 안 넣으면 자동으로 , 으로 됨)
	console.log(result);
}

// Q2. make an array out of a string
{
	const fruits = '🍎, 🥝, 🍌, 🍒';

	// 저의 시도..
	const arrFruits = new Array(fruits);
	console.log(fruits);
	console.log('arr', arrFruits);
	// 이건 한줄 통째로인데용;; 이걸 바라진 않았을것인디..ㅋㅋ
	const realArrFruits = [];
	for (let i = 0; i < fruits.length; i++) {
		realArrFruits.push(fruits[i]);
	}
	console.log('realArrFruits', realArrFruits);
	// 뭔 split, 반점 replace, slicing ㅇㅈㄹ해서
	// forloop으로 배열에 append?하기?.. 이렇게 더럽게..? 해야되나?

	// 엘리님 정답..
	const result = fruits.split(','); // , 단위로 나눌 거니까
	console.log(result); // zz split 자체가 걍 바로 되는 함수였네 ㅎ..
	// split() 안에 구분자 전달하지 않으면 한줄 통째로 배열화 되고 끝남
	// 마치 new Array 통째로 변환했던 저것처럼요.......
}

// Q3. make this array look like this: [5, 4, 3, 2, 1]
{
	const array = [1, 2, 3, 4, 5];
	const result = array.reverse();
	// ..이미 잘 된 api를 모르니까 함수를 자꾸 만드려고 용을 쓰는 나 자신을 발견..
	console.log(result);
	console.log(array); // reverse 자체가 이미 return 포함이라 array만 봐도 적용돼있음
}

// Q4. make new array without the first two elements
{
	const array = [1, 2, 3, 4, 5];
	// const result = array.splice(0, 2);
	// console.log('splice(0, 2)', result);
	// console.log('splice가 적용된 찐 array', array);
	// 문제는 새로운 배열을 만들라고 했으니까? 필요한 게 [3, 4, 5]긴 하지만?..
	console.log('array', array);

	const result1 = array.slice(0, 3);
	console.log('array.slice(0, 3)', result1);

	const result2 = array.slice(2, 5);
	console.log('array.slice(2, 5)', result2);

	// splice는 배열 자체를 수정
	// slice는 배열에서 수정한 새로운 값을 리턴
}

class Student {
	constructor(name, age, enrolled, score) {
		this.name = name;
		this.age = age;
		this.enrolled = enrolled;
		this.score = score;
	}
}
const students = [
	new Student('A', 29, true, 45),
	new Student('B', 28, false, 80),
	new Student('C', 30, true, 90),
	new Student('D', 40, false, 66),
	new Student('E', 18, true, 88),
];

// Q5. find a student with the score 90
{
	// const result = students.find(function (student, index) {
	//   return student.score === 90;
	// });
	const result = students.find((student) => student.score === 90);
	console.log('90점인 학생', result);
}

// Q6. make an array of enrolled students
{
	const result = students.filter((student) => student.enrolled);
	console.log(result);
}

// Q7. make an array containing only the students' scores
// result should be: [45, 80, 90, 66, 88]
{
	const result = students.map((student) => student.score);
	console.log('student.score : map', result);
	// 배열 안에 있는 요소를 다른 방식?으로 다시 만들고 싶을 때 map! ⭐⭐⭐
}

// Q8. check if there is a student with the score lower than 50
{
	const result1 = students.some((student) => student.score < 50);
	console.log('some > 50', result1);
	// 배열 안에 조건 맞는 게 하나라도 있으면 true 반환! some!!!!!

	const result2 = students.every((student) => student.score < 50);
	console.log('every > 50', result2);
	// every는 모두 조건에 맞아야 됨
}

// 🚩🚩🚩 복습 재개 지점입니다. 여기서부터 다시 시작하면 됩니다.
// 아 마크다운으로 폰트 엄청크게 하고싶다..
// Q9. compute students' average score
{
	const result = students.reduce((prev, curr) => {
		// console.log('----------');
		// console.log('prev', prev);
		// console.log('curr', curr);
		return prev + curr.score;
	}, 0);
	console.log(result / students.length);
	// reduce는 값을 돌면서 누적하는 무언가를 구할 때 사용
	// 평균구하는 함수..? 다른 데서 쓰는 avg랑 mean이랑 헷갈리고 난리났다..
}

// Q10. make a string containing all the scores
// result should be: '45, 80, 90, 66, 88'
{
	const result = students.map((student) => student.score).join();
	console.log(result); // 다시 한번 map 복습.
	// student는 여러 속성 종합세트니까 필요한 점수속성만 있는 걸로 재생성
	// mapping 후에 join 함수를 통해 string으로 변환
}

// Bonus! do Q10 sorted in ascending order
// result should be: '45, 66, 80, 88, 90'
{
	const result = students.map((student) => student.score).sort();
	console.log(`점수 정렬 : ${result}`);
	console.log(typeof result);
	result.join();
  console.log(typeof result);
}