import React, { useState, useEffect } from 'react';

const CounterA = React.memo(({ count }) => {
  useEffect(() => {
    console.log(`CounterA Update : ${count}`);
  });
  return <div>{count}</div>;
});
// 이 상태에서 버튼을 눌러도 count 계속 1 상태라 바뀐 게 없음
// 그러므로 노 업데이트 노 리렌더

// 그런데 객체로 설정한 이 녀석은 리렌더링이 발생한다! --> 얕은 비교 때문
// const CounterB = React.memo(({ obj }) => {
//   useEffect(() => {
//     console.log(`CounterB Update : ${obj.count}`);
//   });
//   return <div>{obj.count}</div>;
// });

// 메모를 제거해주고 areEqual 사용합니다.
const CounterB = ({ obj }) => {
  useEffect(() => {
    console.log(`CounterB Update : ${obj.count}`);
  });
  return <div>{obj.count}</div>;
};

// 공식문서 참고, 깊은 비교를 통해 boolean 결과 반환
  // return true : 이전 프롭스와 현재 프롭스가 같을 경우 -> 리렌더링 X
  // false의 경우 이전과 현재가 다르므로 리렌더링 O
const areEqual = (prevProps, nextProps) => {
  // if (prevProps.obj.count === nextProps.obj.count) {
  //   return true;
  // }
  // return false;

  return prevProps.obj.count === nextProps.obj.count
};



const MemoizedCounterB = React.memo(CounterB, areEqual);

const OptimizeTest = () => {
  const [count, setCount] = useState(1);
  const [obj, setObj] = useState({ count: 1 });

  return (
    <div style={{ padding: 50 }}>
      <div>
        <h2>Counter A</h2>
        <CounterA count={count} />
        <button onClick={() => setCount(count)}>A button</button>
      </div>
      <div>
        <h2>Counter B</h2>
        {/* <CounterB obj={obj} /> */}
        <MemoizedCounterB obj={obj} />
        <button onClick={() => setObj({ count: obj.count })}>B button</button>
      </div>
    </div>
  );
};

export default OptimizeTest;
