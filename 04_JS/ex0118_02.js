const num1 = 15;
const num2 = 3; //document에 출력(write)하라는 의미와 비슷

num3 = num2++;
document.write(num3, '<br/>'); // 3
document.write(num2, '<br/>'); // 4

num3 = num2++;
document.write(num3, '<br/>'); // 4
document.write(num2, '<br/>'); // 5

num3 = ++num2;
document.write(num3, '<br/>'); // 6
document.write(num2, '<br/>'); // 6
