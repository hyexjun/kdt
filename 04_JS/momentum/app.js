const loginInput = document.querySelector("#login-form input");
const loginForm = document.querySelector("#login-form");
const greeting = document.querySelector("#greeting");

const HIDDEN_CLASSNAME = "hidden";
// 아래 class add 혹은 remove 시 "hidden"을 여러번 쓰니까 변수 지정했다는데
// 그게 뭔 상관인지 몰겠음.......

function onLoginSubmit(event) {

    event.preventDefault();  // 막아주기..? 이거 토마토..
    const username = loginInput.value;  // 인풋 입력값 변수 할당
    localStorage.setItem("username", username);
    // js용 미니DB라고 보면 되고 f12 앱쪽에서 볼수있음

    loginForm.classList.add(HIDDEN_CLASSNAME);
    // submit 제출 실행 시 hidden 클래스 추가로 form 숨겨버리기
    greeting.innerText = `No sibal Keep going, ${username}!!`;
    greeting.classList.remove(HIDDEN_CLASSNAME);

}

loginForm.addEventListener("submit", onLoginSubmit);