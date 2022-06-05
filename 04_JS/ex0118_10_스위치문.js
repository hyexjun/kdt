// 100, 90점 등급 A
// 80점 B, 70점 C, 60점 D 그 외에는 F
let jumso = prompt('몇 점?');

switch (jumso) {
  case '100':
  case '90': // 스위치 or 조건은 요런 느낌
    document.write('A');
    break;
  case '80':
    document.write('B');
    break;
  case '70':
    document.write('C');
    break;
  case '60':
    document.write('D');
    break;
  default:
    alert('총살이다.');
    break;
}
