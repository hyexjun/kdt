function checkAge() {
    let data1 = document.getElementById("age").value;
    alert("당신의 나이 : "+data1);
}

function checkAge() {
    // let checkData = confirm("당신은 성인입니까?");
    let age = prompt("당신의 나이는?", "입력해주세요.")
    // if(checkData) { document.write("당신은 성인입니다.") }
    if(age >= 20) { document.write("당신은 성인입니다.") }
    else {alert("당신은 미성년자입니다.")}   
}

console.log('Hello World!');