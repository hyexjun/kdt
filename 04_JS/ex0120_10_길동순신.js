// 함수 파라미터로 돌리기
function calBmi1(csName, weight, height) {
    document.querySelector("#textBox").innerText = `${csName}의 BMI는 ${calBmi3(weight, height)}입니다.`;
}

// 인풋 가져와서 돌리기
function calBmi2() {
    let height = Number(document.getElementById("cm").value);
    let weight = Number(document.querySelector("#kg").value);
    let bmi = calBmi3(weight, height);

    if ((height=="") || (weight=="")) {
        alert("빈 항목을 입력해주세요.");
        if (height=="") {
            document.getElementById("cm").focus();
        } else {
            document.querySelector("#kg").focus();
        }
    } else {
        document.querySelector("#final").innerText = `당신의 bmi는 ${bmi}입니다.`;
    }
    // document.getElementById("final").innerText = "당신의 bmi는 " + bmi + "입니다.";
    
    // let final = (document.getElementById("final").innerText=bmi);
    // let x = print(a); << 이거랑 같은 짓이다....
}


// function calBmi3(a, b) {
//     return (a / ((b * 0.01) ** 2)).toFixed(2);
// }

// let calBmi3 = function (a, b) {
//     return (a / ((b * 0.01) ** 2)).toFixed(2);
// }

let calBmi3 = (a, b) => (a / ((b * 0.01) ** 2)).toFixed(2);