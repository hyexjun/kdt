import './App.css';
import MyHeader from './MyHeader';
import MyFooter from './MyFooter';
import React from 'react'; // [2] App 대신 포장할 React import

function App() {
  const name = 'hyju';
  const number = 5;

  return (
    // [1] 최상단껍데기 App 죽이면 대체할 다른 최고껍데기 필요..
    <div className='App'>
      {/* <React.Fragment> */}
      {/*[3] className App을 대신하는 껍데기*/}
      <MyHeader />
      <header className='App-header'>
        <h2>안녕 리액트 {name}</h2>{' '}
        {/* jsx의 {} 안에는 num, str만 넘겨줄 수 있음 */}
      </header>
      <p> {/* 조건부 렌더링ㅎㅎㅎ */}
        {number}는 : {number % 2 === 0 ? '짝수' : '홀수'}
      </p>
      <MyFooter />
      {/* </React.Fragment> */}
      {/* 'React.Fragment'만 쏙 지우고 텅 비워놔도 된다 */}
    </div>
  );
}

export default App;
