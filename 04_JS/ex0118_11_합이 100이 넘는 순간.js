// // data = range [1, 10]
// // for i in date :
// // print (i)

// let data=[0, 1, 2, 3, 4, 5] ;

// for (let i=0 ; i<=10 ; i++) {
//     document.write(i, "<br>")
// }

// let j=0 ;
// for (j in data) {
//     document.write(j, "<br>")
// }

// 1~100까지의 합 중 100이 넘어가는 순간은 몇 까지의 합인지?
let num = 0;
for (let i = 0; i <= 100; i++) {
  num += i;
  if (num > 100) {
    document.write(i);
    break;
  }
}
