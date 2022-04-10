import React, { useEffect, useState } from 'react';

const Lifecycle = () => {
  const [count, setCount] = useState(0); // 카운트에 사용될 state
  const [text, setText] = useState(''); // input에 쓰일 state

  // 이펙트 사용 문법
  // useEffect((params)=>{func}, [dependency array])
  // 🎯 뎁스에 변화가 발생하는 순간, 첫번째 인자인 콜백함수가 실행된다.

  useEffect(() => {
    console.log('Mount!');
  }, []); // [1] 컴포넌트가 마운트된 시점에 뭔가 하고 싶으면,
  // 두번째 인자인 뎁스?를 빈 배열로 줘라..

  useEffect(() => {
    console.log('Update..');
  }); // [2] 버튼 눌러서 숫자 증가한다거나 하는 이벤트 발생?
  // 컴포넌트 업데이트를 제어할 경우에는 뎁스를.. 날려버려요..?

  useEffect(() => {
    console.log(`text is update : ${text}`);
  }, [text]);

  // [3] 이펙트 근본 🎯
  // 요녀석을 잘 활용하면 원하는 값만 감지해서 함수를 실행시킬 수 있다 ^^
  useEffect(() => {
    console.log(`count is update : ${count}`);
    if (count > 5) {
      alert('5개를 초과하여 구매할 수 없으므로 구매 수량을 초기화합니다.');
      setCount(1);
    }
  }, [count]);

  return (
    <div style={{ padding: 20 }}>
      <div>
        {count}
        <button onClick={() => setCount(count + 1)}>+</button>
      </div>
      <div>
        <input value={text} onChange={(event) => setText(event.target.value)} />
      </div>
    </div>
  );
};

export default Lifecycle;
