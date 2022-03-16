// doSomething(add);
// 오.. 진짜 함수 선언(때 함수명 적은 애들)은.. 호이스팅이.. 되네.....
// dodo(add);
// 이건 함수 선언때는 노네임인데 const로 이름을 표현한 거라 호이스팅 안됨


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

const dodo = function (add) {
    console.log(add);
    const result = add(5, 3);
    console.log(result);
}


// 함수 호출

doSomething(add);
dodo(add);