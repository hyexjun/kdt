let new_arr = [, , , ,];

new_arr[0] = 5;
new_arr[1] = 6;
new_arr[2] = 7;
new_arr[3] = 8;
new_arr[4] = 9;

// for (let i=5 ; i<10 ; i++) {
//     let inputArr = Number(prompt("추가할 배열을 입력하세요."))
//     new_arr[i] = inputArr;
// }
// console.log(new_arr)
// 이건 정상작동 잘 되는거..

for (let i = 5; i < 10; i++) {
  let inputArr = Number(prompt('추가할 배열을 입력하세요.'));
  new_arr.push(inputArr);
}
console.log(new_arr);
