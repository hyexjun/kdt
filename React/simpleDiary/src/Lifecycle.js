import React, { useEffect, useState } from 'react';

const UnmountTest = () => {
  useEffect(() => {
    console.log('Mount!');
    // [2] 아래 return으로 unmount 나오는 이유 모르겠는디요..
    return () => console.log('Unmount!');
  }, []); // [1] 이것 자체는 컴포넌트가 실행될때(mount) 나오는 로그니까
  // on 눌러서 아래 div가 생성될 때만 로그 찍히고, off할땐 안 나옴
  return <div>Unmount Testing Component</div>;
};

// 하나의 컴포넌트 당 파일 하나 <-- 이래야만 하는 건 아니니까,
// 이 파일에 컴포넌트를 또 만들어볼게요? 위로 갑니다~

const Lifecycle = () => {
  const [isVisible, setIsVisible] = useState(false);
  const toggle = () => setIsVisible(!isVisible);

  return (
    <div style={{ padding: 20 }}>
      <button onClick={toggle}>ON/OFF</button>
      {isVisible && <UnmountTest />}
      {/* isVisible이 true면 UnmountTest 컴포넌트가 나오고,
      다시 누르면 toggle에 의해 false가 되어 사라짐
      ㄴ> 이건 알겠는데 && 연산자 저 한줄 자체 단락회로평가 아직 몰겟음..*/}
    </div>
  );
};

export default Lifecycle;
