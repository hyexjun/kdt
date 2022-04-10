function taskA(a, b) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const res = a + b;
      resolve(res);
    }, 3000);
  });
}

// 같은 거
/* function taskA(a, b, c) {
  const executorA = (resolve, reject) => {
    setTimeout(() => {
      const res = a + b;
      c(res);
    }, 3000);
  };
  return new Promise(executorA);
} */

function taskB(a) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const res = a * 2;
      resolve(res);
    }, 1000);
  });
}

function taskC(a) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const res = a * -1;
      resolve(res);
    }, 2000);
  });
}

/* taskA(3, 4, (a_res) => {
  console.log('A Task result :', a_res);
  taskB(a_res, (b_res) => {
    console.log('B Task result :', b_res);
    taskC(b_res, (c_res) => {
      console.log('C Task result :', c_res);
    });
  });
}); */

taskA(5, 1)
  .then((a_res) => {
    console.log('A Task result :', a_res);
    return taskB(a_res);
  })
  .then((b_res) => {
    console.log('B Task result :', b_res);
    return taskC(b_res);
  })
  .then((c_res) => {
    console.log('C Task result :', c_res);
  });

/* callback이 직관적으로 와닿는건 winterlood인데
확실히 더 설명을 잘 하는 건 ellie네.. 복습은 엘리로 갑니다.. */