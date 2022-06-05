// for (let i=2 ; i<=9 ; i++) {
//     for (let j=1 ; j<=9 ; j++) {
//         document.write(i,"*",j,"=",i*j,"<br>")
//     }
//     document.write("<br>")
// }

let whatNum = prompt('몇 단? ex. 2단, 3단 등');
switch (whatNum) {
  case '2단':
    for (let j = 1; j <= 9; j++) {
      document.write(2, '*', j, '=', 2 * j, '<br>');
      break;
    }
  case '3단':
    for (let j = 1; j <= 9; j++) {
      document.write(3, '*', j, '=', 3 * j, '<br>');
      break;
    }
  case '4단':
    for (let j = 1; j <= 9; j++) {
      document.write(4, '*', j, '=', 4 * j, '<br>');
      break;
    }
  case '5단':
    for (let j = 1; j <= 9; j++) {
      document.write(5, '*', j, '=', 5 * j, '<br>');
      break;
    }
  case '6단':
    for (let j = 1; j <= 9; j++) {
      document.write(6, '*', j, '=', 6 * j, '<br>');
      break;
    }
  case '7단':
    for (let j = 1; j <= 9; j++) {
      document.write(7, '*', j, '=', 7 * j, '<br>');
      break;
    }
  case '8단':
    for (let j = 1; j <= 9; j++) {
      document.write(8, '*', j, '=', 8 * j, '<br>');
      break;
    }
  case '9단':
    for (let j = 1; j <= 9; j++) {
      document.write(9, '*', j, '=', 9 * j, '<br>');
      break;
    }
}
