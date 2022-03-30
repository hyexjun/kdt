const quotes = [
  {
    quote: '위로가 돼요',
    author: 'HA:TFELT',
  },
  {
    quote: '이름에게',
    author: 'IU',
  },
  {
    quote: 'Feel My Rhythm',
    author: 'Red Velvet',
  },
  {
    quote: 'Line',
    author: '안예은',
  },
  {
    quote: 'SAME SAME',
    author: 'STAYC',
  },
  {
    quote: 'TOMBOY',
    author: '(G)I-DLE',
  },
  {
    quote: '대화가 필요해',
    author: '자두',
  },
  {
    quote: 'How You Like That',
    author: 'Black Pink',
  },
  {
    quote: '깊은 우리 젊은 날',
    author: 'We are the Night',
  },
  {
    quote: 'Hey Child',
    author: 'X Ambassadors',
  },
];
// 보기에 멋진 긴 영어문장 말한 사람까지 찾기가 힘들어서 노래로 대체함ㅎ

const quote = document.querySelector('#quote span:first-child');
const author = document.querySelector('#quote span:last-child');
const todaysQuote = quotes[Math.floor(Math.random() * quotes.length)];

// quote.innerText = '🎧'+todaysQuote.quote;
quote.innerText = `🎧 ${todaysQuote.quote}`;
// author.innerText = '🎤'+todaysQuote.author;
author.innerText = `🎤 ${todaysQuote.author}`;
