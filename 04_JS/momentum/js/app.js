const loginInput = document.querySelector('#login-form input');
const loginForm = document.querySelector('#login-form');
const greeting = document.querySelector('#greeting');

const HIDDEN_CLASSNAME = 'hidden';
const USERNAME_KEY = 'username';
// 아래 class add 혹은 remove 시 "hidden"을 여러번 쓰니까 변수 지정했다는데
// 그게 뭔 상관인지 몰겠음.......
// 아 함수() 속 객체 쓸때 "어쩌구"는 자동완성이 안되니까
// "어쩌구" 자체를 변수명으로 선언하고 자동완성 쓰는건가봄..

function onLoginSubmit(event) {
  event.preventDefault(); // 막아주기..? 이거 토마토..
  const username = loginInput.value; // 인풋 입력값 변수 할당
  localStorage.setItem(USERNAME_KEY, username);
  // js용 미니DB라고 보면 되고 f12 앱쪽에서 볼수있음

  loginForm.classList.add(HIDDEN_CLASSNAME);
  // submit 제출 실행 시 hidden 클래스 추가로 form 숨겨버리기
  paintGreetings(username);
}

function paintGreetings(username) {
  greeting.innerText = `Hello, ${username}.`;
  greeting.classList.remove(HIDDEN_CLASSNAME);
}

loginForm.addEventListener('submit', onLoginSubmit);
// 일종의 조건문처럼 addEventListener(A, B);
// A라는 조건에 걸릴 때, B를 실행하겠음 이기 때문에 B()라고 쓰지 않는다
// B()는 걍 바로 함수 호출이니까..

const saveUsername = localStorage.getItem(USERNAME_KEY);

if (saveUsername === null) {
  // show the form
  loginForm.classList.remove(HIDDEN_CLASSNAME);
  loginForm.addEventListener('submit', onLoginSubmit);
} else {
  // shwo the greeting
  paintGreetings(saveUsername);
}
