// spread 연산자 : ...
const cookie = {
  base: 'cookie',
  madeIn: 'korea',
};

const chocochipCookie = {
  ...cookie,
  toping: 'chocochip',
};

const blueberryCookie = {
  ...cookie,
  toping: 'blueberry',
};

const strawberryCookie = {
  ...cookie,
  toping: 'strawberry',
};

console.log(chocochipCookie);
console.log(blueberryCookie);
console.log(strawberryCookie);
console.log('---------');

// concat을 써도 되지만 암튼 ... <-- 스프레드연산자로도 간단하게 가능.
const cookiesA = ['바나나', '딸기', '포도'];
const cookiesB = ['초콜릿', '커피', '아몬드'];
const allCookies = [...cookiesA, ...cookiesB];
console.log(allCookies);
