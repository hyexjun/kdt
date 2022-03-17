// const loginForm = document.getElementById("login-form");
// const loginInput = loginForm.querySelector("input");
// const loginButton = loginForm.querySelector("button");

const loginInput = document.querySelector("#login-form input");
const loginButton = document.querySelector("#login-form button");
// 위 세 줄이랑 같은 두 줄


function onLoginBtnClick() {
    // console.log(`hello!! ${loginInput.value}`);
    // console.log("click!!!")
    const username = loginInput.value;
    if (username === "") {
        alert("Please write your name");
    } else if (username.length > 15) {
        alert("your name is too long!");
    }
}

loginButton.addEventListener("click", onLoginBtnClick);