import { useState, useRef } from 'react';

const DiaryEditor = ({ onCreate }) => {
  const [state, setState] = useState({
    author: '',
    content: '',
    test: '',
    emotion: 3,
  });

  const authorInput = useRef();
  const contentInput = useRef();

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

    onCreate(state.author, state.content, state.emotion);
    alert('저장 완료!'); // 일기가 잘 저장되었다면
    setState({
      // 초기화해줍니다.
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
          placeholder={'테스트하느라고 만든 별도 공간\n입력해도 데이터가 저장되지 않습니다 :)'}
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
export default DiaryEditor;
