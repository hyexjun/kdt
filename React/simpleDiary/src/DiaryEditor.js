import React, { useState, useRef, useEffect, useContext } from 'react';
import { DiaryDispatchContext } from './App';

// Q. 리렌더링이 발생하는 경우?
// A. 본인 상태 변화, 부모 컴포넌트에 변화 발생, 자신이 받은 프롭이 변경된 경우 등

// const DiaryEditor = ({ onCreate }) => {
const DiaryEditor = () => { // <-- onCreate 컴포넌트로 안 받으니까 지워준다
  // 근데 onCreate를 받아오긴 해야되니까요
  const { onCreate } = useContext(DiaryDispatchContext); // 이렇게 가져옴

  useEffect(() => {
    console.log('DiaryEditor render');
  });

  const authorInput = useRef();
  const contentInput = useRef();

  const [state, setState] = useState({
    author: '',
    content: '',
    test: '',
    emotion: 3,
  });

  const handleChangeState = (event) => {
    setState({
      ...state,
      [event.target.name]: event.target.value,
    });
  };

  const handleSubmit = () => {
    if (state.author.length < 1) {
      authorInput.current.focus();
      return;
    }

    if (state.content.length < 5) {
      contentInput.current.focus();
      return;
    }

    console.log(state.author, state.content, state.emotion);
    onCreate(state.author, state.content, state.emotion);
    alert('저장 완료!');
    setState({
      author: '',
      content: '',
      test: '',
      emotion: 3,
    });
  };

  return (
    <div className='DiaryEditor'>
      <h2>오늘의 일기 📖</h2>
      <div>
        <input
          ref={authorInput}
          name='author'
          value={state.author}
          onChange={(event) => {
            setState({
              author: event.target.value,
              content: state.content,
              emotion: state.emotion,
            });
          }}
          placeholder={'당신의 이름을 입력해주세요.'}
        />
      </div>
      <div>
        <textarea
          ref={contentInput}
          name='content'
          value={state.content}
          onChange={(event) => {
            setState({
              ...state,
              content: event.target.value,
            });
          }}
          placeholder={'무슨 일이 일어나고 있나요?'}
        />
      </div>
      <div>
        <textarea
          name='test'
          value={state.test}
          onChange={handleChangeState}
          placeholder={
            '테스트하느라고 만든 별도 공간\n입력해도 데이터가 저장되지 않습니다 :)'
          }
        />
      </div>
      <div>
        <select
          name='emotion'
          value={state.emotion}
          onChange={handleChangeState}
        >
          <option value={1}>1</option>
          <option value={2}>2</option>
          <option value={3}>3</option>
          <option value={4}>4</option>
          <option value={5}>5</option>
        </select>
      </div>
      <div>
        <button onClick={handleSubmit}>💻 저! 장! 💾</button>
      </div>
    </div>
  );
};
export default React.memo(DiaryEditor);
