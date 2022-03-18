// const loginForm = document.getElementById("login-form");
// const loginInput = loginForm.querySelector("input");
// const loginButton = loginForm.querySelector("button");

const loginInput = document.querySelector("#login-form input");
// const loginButton = document.querySelector("#login-form button");
// 위 세 줄이랑 같은 두 줄
const loginForm = document.querySelector("#login-form")

function onLoginSubmit(event) {
    // console.log(`hello!! ${loginInput.value}`);
    // console.log("click!!!")

    event.preventDefault();
    // const username = loginInput.value;
    // console.log(username);
    console.log(loginInput.value);
}


// loginButton.addEventListener("click", onLoginBtnClick);
loginForm.addEventListener('submit', onLoginSubmit);
// 일종의 조건문처럼 addEventListener(A, B);
// A라는 조건에 걸릴 때, B를 실행하겠음 이기 때문에 B()라고 쓰지 않는다
// B()는 걍 바로 함수 호출이니까..
