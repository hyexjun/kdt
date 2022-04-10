// callback 복습
function taskA(a, b, c) {
    setTimeout(() => {
      const res = a + b;
      c(res);
    }, 3000);
  }
  
  function taskB(a, b) {
    setTimeout(() => {
      const res = a * 2;
      b(res);
    }, 1000);
  }
  
  function taskC(a, b) {
    setTimeout(() => {
      const res = a * -1;
      b(res);
    }, 2000);
  }
  
  
  // taskA(3, 4, (res) => {console.log('A Task 3000 result :', res);});
  // // c = (res) => {console.log('A Task result :', res);}
  // // 세번째 인자인 콜백함수가 함수명 자체가 없어서 순간 헷갈림..
  // taskB(7, (res) => {
  //   console.log('B Task 1000 result :', res);
  // });
  // taskC(14, (res) => {
  //   console.log('C Task 2000 result :', res);
  // });
  
  taskA(4, 5, (a_res) => {
    console.log('A Task result :', a_res);
    taskB(a_res, (b_res) => {
      console.log('B Task result :', b_res);
      taskC(b_res, (c_res) => {
        console.log('C Task result :', c_res);
      });
    });
  });  // 간이 callbackhell 생성 ㅎㅎ... 이거 뭐 내성발톱이냐..? 계속 파고드네ㅜ
