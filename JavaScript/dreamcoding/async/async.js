// async & await  1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣
// clear style of using promise :)


// 1️⃣. async

function fetchUser() {
  return new Promise((resolve, reject) => {
    // ex. 네트워크 통신에 10초쯤 걸리는 통신 어쩌구
    resolve('ellie');
  });
}

const user = fetchUser(); // 여기서
console.log(user); // 여기까지 최소 그 함수에 걸리는 시간 이상 걸리겠쥬
// 더불어 이 아래에 웹페이지를 구현하는 코드가 있다면?
// 당연히 먼저 실행"중"인 코드(시간 소요중..)가 끝나기 전까진 아래에 있는 코드들도 같이 대기
// 그래서 앞서 얘기했듯 시간 좀 소요되는 수행들은 비동기식으로 처리하는 것이 좋다.. UX를 위해..

user.then(console.log);

async function fetchUser1() {
  return 'ellie';
}
// Q. async라는 키워드를 함수 앞에 쓰면 자동으로 promise화 되는 건가요?
// A. 기존에 있던 것에서 조금 더 달달하게 처리하도록(?ㅋㅋ) 돕는 syntatic Sugar


// 2️⃣. await : async Func 안에서만 사용 가능!!

function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
  // 함수 delay : ms가 지나면 resolve를 호출하는 프로미스를 반환
}

async function getApple() {
  await delay(1000);
  return '🍎';
}

async function getBanana() {
  await delay(1000);
  return '🍌';  // 아래 함수와 동일한 기능 수행
}
// function getBanana() {
//   return delay(3000).then(() => '🍌');
// }

function pickFruits() {
  return getApple().then(apple => {
    return getBanana().then(banana => `pickFruits ${apple} + ${banana}`);
  });
}
pickFruits().then(console.log); // 이런 식이면 콜백지옥과 다를 게 없다......

async function pickFruits1() {
  const apple = await getApple();
  const banana = await getBanana();
  return `pickFruits1 ${apple} + ${banana}`;
}
pickFruits1().then(console.log);


// 3️⃣. error 처리하는 다른 방식

// error 처리도 .then().catch() 가 아닌
async function getApple1() {
  await delay(1000);
  throw 'error';  // 에러 발생용 복사본
  return '🍎';
}
// try{} & catch{} 를 사용할 수 있음!
async function pickFruits2() {
  try {
    const apple = await getApple1();
    const banana = await getBanana();
    return `${apple} + ${banana}`;
  } catch {
    // 에러 처리 내용
    return 'pickFruits2 error';
  }
}
pickFruits2().then(console.log);


// 4️⃣. 시간 단축이 필요할 때

// async function pickFruits3() {
//   const apple = await getApple(); <-- 여기서 1초 소요
//   const banana = await getBanana(); <-- 사과 처리 후 여기서도 1초 소요
//   return `pickFruits3 ${apple} + ${banana}`;
// }
// pickFruits3().then(console.log);

// 이걸 기다려줄 필요 없이
async function pickFruits3() {
  const applePromise = getApple(); // promise는 선언 동시 실행인 점을 활용해서
  const bananaPromise = getBanana(); // 동시에 병렬로 처리해버리기
  const apple = await applePromise;
  const banana = await bananaPromise;
  return `pickFruits3 ${apple} + ${banana}`; // 출력까지 시간이 단축된다
}
pickFruits3().then(console.log); // console 확인 시 과일따기 1,2보다 3이 빨리 출력됨

// 근데 좀 지저분한 코드를 정리해주는 promise APIs : all()💝
// promise 배열을 전달하게 되면, 모든 promise들을 병렬로 다 받아줌
function pickAllFruits() {
  return Promise.all([getApple(), getBanana()]).then(fruits => fruits.join(' + '));
}
pickAllFruits().then(item => console.log(`pickAllFruits ${item}`));
// 위 함수들과 출력되는 순서(시간 차이) 비교 가능~~!


// 5️⃣. 번외.. 1등만 기억하는 세상 : race() ㅋㅋ
function pickFirstOne() {
  return Promise.race([getApple(), getBanana()]);
}
pickFirstOne().then(item => console.log(`pickFirstOne ${item}`));


// 6️⃣. async & await을 써서 'callback -> promise'를 more clean code로!
