'use strict';
// class: template
// object: instance of a class
// Javascript classes
// - introduced in ES6
// - syntactical sugar over prototype-based inheritance

// 1️⃣. Class declarations
class Person {
  // constructor
  constructor(name, age) {
    // fields
    this.name = name;
    this.age = age;
  }
  // methods
  speak() {
    console.log(`${this.name}: hello!`);
  }
}

const helli = new Person('hllie', 20);
console.log(helli.name);
console.log(helli.age);
helli.speak();

// 2️⃣. Getter and Setter
class User {
  constructor(firstName, lastName, age) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age; // [6] 그런데 age라는 getter를 정의하는 순간
    // this.age는 = age 가 아니라 get age() => return this.age를 호출함
    // 동일하게 setter를 정의하는 순간, 32번줄에서 할당한 = age의 메모리?가 아니라
    // setter....... 동영상 12:55 도대체 몬소리고.. 암튼 무한루프로 굴러가서 콜스택 초과함
  }

  // [3] get을 이용해서 값을 리턴하고
  get age() {
    return this._age; // [7] 그래서 그걸 방지하고자 this.age가 아니라 this._age로 한대..
  } // [5] if 사용자가 get을 호출하면, 바로 age를 그대로 리턴

  // [4] set을 이용해서 값을 설정합니다. 대신 set은 값을 설정하니까? value 필요
  set age(value) {
    // if (value < 0) {
    //     throw Error('age can not be negative');
    // }          -- 입력값이 음수라면 에러메시지 던져
    // this._age = value;
    this._age = value < 0 ? 0 : value;
    // 위 에러문구 혹은 아래 삼항식으로 value가 음수면 0으로 치환, 아니면 value 사용
  }
}

const user1 = new User('Steve', 'Jobs', -1); // [1] 객체지향적 언어에서 사람의 나이는 음수 X
console.log(user1.age); // [2] 그래서 이럴 때 조정?해주기 위해 게터, 세터 필요 --> 35번으로 가자

// 3️⃣. Public & Private Fields  : 이건 최신 문법이라 아직 널리 쓰이진 않음
class Experiment {
  publicField = 2;
  #privateField = 0; // 사용법은 앞에 해시태그 붙이기..
}

const experiment = new Experiment();
console.log(experiment.publicField); // 콘솔창에서 출력값 보면 퍼블릭은 보이지만
console.log(experiment.privateField); // 프라이빗은 undefined로 나오는 것을 볼 수 있음!

// 4️⃣. Static properties and methods  : 이것도 최신이라 아직은 쫌..
class Article {
  static publisher = 'Dream Coding';
  constructor(articleNumber) {
    this.articleNumber = articleNumber;
  }

  static printPublisher() {
    console.log(Article.publisher); // 와 이거 뭔소린지 몰겟는디??
  }
}

const article1 = new Article(1);
const article2 = new Article(2);
console.log(article1.publisher);

// 5️⃣. Inheritance ✨
// a way for one class to extend another class.

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

class Rectangle extends Shape {}
// 기존의 shape 클래스에 확장추가? shape를 확장하여 class Rectangle을 만든다~
class Triangle extends Shape {
  draw() {
    // 원래 draw()는 아래의 함수였는데
    // console.log(`drawing ${this.color} color!`); == 102번줄
    console.log('🧀'); // 이 내용으로 draw()의 함수정의를 다시 해줌
    // 원래의 엄빠 draw 보고 싶으면 아래의 super.를 앞에 사용해준다!
    super.draw();
  }

  getArea() {
    return (this.width * this.height) / 2;
  } // 삼각형의 면적 함수는 shape getarea 함수에서 변형 필요
  // 필요한 함수명 따다가 그것만 재설정해주면 재사용 가능
}

const rectangle = new Rectangle(20, 20, 'blue');
rectangle.draw();
console.log(rectangle.getArea());

const triangle = new Triangle(30, 15, 'pink');
triangle.draw();
console.log(triangle.getArea());

// 6️⃣. Class checking: instanceOf  ::: 아래 내용의 boolean을 맞혀보세요~!
console.log(rectangle instanceof Rectangle);
console.log(triangle instanceof Rectangle);
console.log(triangle instanceof Triangle);
console.log(triangle instanceof Shape);
console.log(triangle instanceof Object);
