const clock = document.querySelector("h2#clock");

function getClock() {
    const date = new Date();
    // date.getHours() 상태로는 num type이기 때문에 padStart 적용 불가
    
    const hours = String(date.getHours()).padStart(2, "0");
    const minutes = String(date.getMinutes()).padStart(2, "0");
    const seconds = String(date.getSeconds()).padStart(2, "0");
    clock.innerText = `${hours}:${minutes}:${seconds}`;
}

getClock();  // 함수 호출 해놔야 처음부터 시계가 바로 보인다
setInterval(getClock, 1000);

// Memo
// padStart(원하는 글자수, "추가할 문자열")
// padStart는 앞에 붙이는 함수, padEnd는 뒤에 붙이는 함수