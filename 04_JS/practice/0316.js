
// 함수 선언

function add(a, b) {
    const sum = a + b;
    return sum;
}

function doSomething(add) {
    console.log(add);
    const result = add(2, 3);
    console.log(result);
}


// 함수 호출

doSomething(add);