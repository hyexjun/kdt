// Callback
function isPositive(number, resolve, reject) {
  setTimeout(() => {
    if (typeof number === 'number') {
      // 성공 --> resolve
      resolve(number >= 0 ? '양수' : '음수');
    } else {
      // 실패 --> reject
      reject('주어진 값이 숫자형이 아닙니다.');
    }
  }, 2000);
}

isPositive(
  // number
  [],
  // resolve
  (res) => {console.log('성공 :', res);},
  // reject
  (err) => {console.log('실패 :', err);}
);


// Promise
function isPositiveP(number) {
  const executor = (resolve, reject) => {
    setTimeout(() => {
      if (typeof number === 'number') {
        // 성공 --> resolve
        resolve(number >= 0 ? '양수' : '음수');
      } else {
        // 실패 --> reject
        reject('주어진 값이 숫자형이 아닙니다.');
      }
    }, 2000);
  };

  const asyncTask = new Promise(executor);
  return asyncTask;
}

const res = isPositiveP(101);
res
  .then((res) => {
    console.log('작업 성공 :', res);
  })
  .catch((err) => {
    console.log('작업 실패 :', err);
  });