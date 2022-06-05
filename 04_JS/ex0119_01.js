// let num = 0 ;
// for (let i=0 ; i<=1000 ; i++) {
//     if (i%3==0) {
//         num += i
//         if (num>200) {
//         document.write(num);
//         break;
//         }
//     }
// }

let num = 0;
while (i <= 1000) {
  if (i % 3 == 0) {
    num += i;
    if (num > 200) {
      document.write(num);
      break;
      i++;
    }
  }
}
