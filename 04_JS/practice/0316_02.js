'use strict';

class Person {
    constructor(name, age) {
        // fields
        this.name = name;
        this.age = age;
    }

    // method
    speak() {
        console.log(`${this.name}: hello!`);
    }
}

const ellie = new Person('ellie', 20);
console.log(ellie.name);
console.log(ellie.age);
ellie.speak();



// getter and setters

class User {
    constructor(firstName, lastName, age) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
    }

    get age() {
        return this._age;
    }
    
    set age(value) {
        // if (value < 0) {
        //     throw Error('age can not be negative');
        // }          -- 입력값이 음수라면 에러메시지 던져
        // this._age = value;
        this._age = value < 0 ? 0 : value;
        // 위 에러문구 혹은 아래 삼항식으로 value가 음수면 0으로 치환, 아니면 value 사용
    }
}

const user1 = new User('Steve', 'Jobs', -3);
console.log(user1.age);



// 상속

class Shape {
    constructor(width, height, color) {
        this.width = width;
        this.height = height;
        this.color = color;
    }

    draw() {
        console.log(`drawing ${this.color} color!`);
    }

    getArea() {
        return this.width * this.height;
    }
}

const randomDicd = new Shape(30, 5, 'red');
randomDicd.draw();


class Rectangle extends Shape {}   // 기존의 shape 클래스에 확장추가?
class Triangle extends Shape {
    draw() {
        // 원래 아래의 shape draw 함수였는데
        // console.log(`drawing ${this.color} color!`);
        console.log('🧀');   // 이걸로 재설정
        // 근데 그러다보면 draw랑 getarea랑 다 바꾼거라
        // 원래 엄빠 draw 보고 싶으면 아래의 super. 사용해준다!
        super.draw();
    }

    getArea() {
        return (this.width * this.height) / 2;
    }   // 삼각형의 면적 함수는 shape getarea 함수에서 변형 필요
        // 필요한 함수명 따다가 그것만 재설정해주면 재사용 가능
}

const rectangle = new Rectangle(20, 20, 'blue');
rectangle.draw();
console.log(rectangle.getArea());

const triangle = new Triangle(30, 15, 'pink');
triangle.draw();
console.log(triangle.getArea());