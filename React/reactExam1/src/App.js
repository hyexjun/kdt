import './App.css';
import React from 'react';
import Counter from './Counter';
import MyHeader from './MyHeader';
import Container from './Container';

// 특정 props를 까먹으면 안 될 때,
Counter.defaultProps = {
  initialValue: 0,
};

function App() {
  const counterProps = {
    a: 1,
    b: 2,
    c: 3,
    d: 4,
    e: 5,
    // initialValue: 0, 앗 실수로 날려먹었다면?
  };

  return (
    <Container>
      <div>
        <MyHeader />
        {/* <Counter a={1} initialValue={'basic'} /> */}
        {/* 몇 개를 보내든 객체로 넘어간당
      그런데 너무 길어지면 보기가 안 좋으니까.. */}
        {/* <Counter a={1} b={2} c={3} d={4} e={5} initialValue={'values'} /> */}
        <Counter {...counterProps} />
      </div>
    </Container>
  );
}

export default App;
