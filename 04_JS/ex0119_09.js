let tv = new Object();
tv.color = 'white';
tv.price = 2000000;
tv.info = function () {
  document.write('색상 : ', this.color, '<br>');
  document.write('가격 : ', this.price, '<br>');
};

let car = {
  color: 'black',
  price: 30000000,
  info: function () {
    document.write('색상 : ', this.color, '<br>');
    document.write('가격 : ', this.price, '<br>');
  },
  // this를 써야 변수선언 블럭? 내에서 저 컬러가 이 컬러구나를 인식할 수 있다나..?
  // 근데 this를 안 써도 같은 블럭 내에서만 인식하는 지역변수 아님? 질문..!
};
document.write(tv.color, tv.price, '<br>');
tv.info();
