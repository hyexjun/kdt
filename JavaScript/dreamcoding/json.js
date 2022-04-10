// HTTP : hypertext transfer Protocal
// 클라이언트와 서버 간의 통신 규약? 프로토콜?
// AJAX : asynchronous JS And Xml
// JSON : JS Object Notation


// 1️⃣. Object --> JSON   :  stringfy(obj)
let json = JSON.stringify(true);
console.log(json);

json = JSON.stringify(['apple', 'banana']);
// 여기엔 싱글쿼트인데 콘솔에는 더블쿼트로 보이는 것.. 그것이 json형식이다..
console.log(json);

const rabbit = {
	name: 'tory',
	color: 'white',
	size: null,
	birthDate: new Date(),
	jump: () => {
		console.log(`${name} can jump!`);
	},
};

console.log(rabbit);                // 보면 알겠지만 메소드는 json화가 안 됨
json = JSON.stringify(rabbit);      // 뭐도 안됨.. 52번과 같은 맥락
console.log(json);


// 만약 json으로 바꿀 때 조금 더 통제?하고 싶다면,
// 토끼 obj에서 원하는 프로퍼티만 json으로 바꾸고 싶다면
json = JSON.stringify(rabbit, ['name', 'color', 'size']); // 이런 식으로
console.log(json);

// 아니면 콜백함수를 통해
json = JSON.stringify(rabbit, (key, value) => {
	console.log(`key: ${key}, value: ${value}`);
	return key === 'name' ? 'ellie' : value;
	// a 어쩌구 조건식 ? b : c ;  ==  a가 조건식에 맞으면 b를 처리, else는 c로 처리
	// key가 name이면 value를 ellie로 설정하고, 그게 아닌 나머지 key가 들어오면 원래 value로!
});
console.log(json);



// 2️⃣. JSON --> Object   :  parse(json)
console.log('----------');
json = JSON.stringify(rabbit);
// 마찬가지로 좀더 세밀한 조정을 하고싶으면 내장된 콜백함수 사용!
const obj = JSON.parse(json, (key, value) => {
	console.log(`key: ${key}, value: ${value}`);
	return key === 'birthDate' ? new Date(value) : value;
});
console.log(obj);
console.log(`obj로 얍! ${obj}`); // 근데 여기는 obj 양식?으로 안나오넹ㅎ
rabbit.jump();
// obj.jump();  // 그니까 애초에 존재하지 않는 obj.jump()인 것이다

console.log(rabbit.birthDate.getDate());
console.log(obj.birthDate.getDate());