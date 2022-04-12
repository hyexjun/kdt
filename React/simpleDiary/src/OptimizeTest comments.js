import React, { useState, useEffect } from 'react';

const Countview = ({ count }) => {
  useEffect(() => {
    // 리렌더링 될때 프롭스가 어떻게 되는지 보자
    console.log(`Update Count ${count}`);
  });
  return <div>{count}</div>;
};

// useEffect로 log 확인 시, count만 이벤트 발생하는데도
// text까지 리렌더링되는 것을 확인할 수 있다..
// text : 저는 왜요.. <-- 를 방지하기 위한 컴포넌트 재사용 익히기.

const Textview = React.memo(({ text }) => { // 메모이제이션? 그거 적용
  useEffect(() => {
    console.log(`Update Text ${text}`);
  });
  return <div>{text}</div>;
});

const OptimizeTest = () => {
  const [count, setCount] = useState(0);
  const [text, setText] = useState('');

  return (
    <div style={{ padding: 50 }}>
      <div>
        <h2>count</h2>
        <Countview count={count} />
        <button
          onClick={() => {
            setCount(count + 1);
          }}
        >
          +
        </button>
      </div>
      <div>
        <h2>text</h2>
        <Textview text={text} />
        <input
          value={text}
          onChange={(event) => {
            setText(event.target.value);
          }}
        />
      </div>
    </div>
  );
};

export default OptimizeTest;
