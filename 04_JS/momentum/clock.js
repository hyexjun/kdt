const clock = document.querySelector("h2#clock");

function getClock() {
    const date = new Date();
    clock.innerText = `${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`;
}

getClock();  // 이걸 지우면 처음엔 비어있다가 시작하게 됨
setInterval(getClock, 1000);