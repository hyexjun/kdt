import React, { useState } from 'react';
import OddEvenResult from './OddEvenResult';

// 🌷 const Counter = (props) => {
//   console.log(props); 🌷

const Counter = ({ initialValue }) => { // 🥞

  // 동적으로 바뀌는 요소들이 있는 것을 state(비구조화 할당)로 활용
  // [0, 1] = a, b ;일 때 a는 초기값, b는 변화용 박스(투명..?)
  // const [count, setCount] = useState(0);

  // 🌷 const [count, setCount] = useState(props.initialValue); 🌷
  const [count, setCount] = useState(initialValue); // 🥞
  // 비구조화 할당으로 이렇게 받아올수도 있단게 몬말이예요!!

  const onIncrease = () => {
    setCount(count + 1);
  };

  const onDecrease = () => {
    setCount(count - 1);
  };

  return (
    <div>
      <h2>{count}</h2>
      <button onClick={onIncrease}>+</button>
      <button onClick={onDecrease}>-</button>
      <OddEvenResult count={count} />
    </div>
  );
};

export default Counter;
