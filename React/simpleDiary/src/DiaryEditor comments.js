import { useState, useRef } from 'react';

const DiaryEditor = ( {onCreate}) => {
  const [author, setAuthor] = useState(''); // [1]
  const [content, setContent] = useState(''); // [2]
  // 둘다 문자열이고 구성도 비슷하면 state 두개로 쓸 것 없이 객체로 만들어도 된담

  const [state, setState] = useState({
    // [3] : 1, 2번을 요로코롬 합쳤어야
    author: '',
    content: '',
    test: '',
    emotion: '⭐⭐⭐',
  });

  const authorInput = useRef(); // useRef() : 함수 호출해서 반환값을 상수에 저장
  const contentInput = useRef(); // textarea 이하동문

  const handleChangeState = (event) => {
    console.log(event.target.name); // 얘는 뭐 사실 보는 용이고..
    console.log(event.target.value);

    setState({
      ...state, // 이 녀석이 의미하는 바를 다시 한 번 곱씹어보기
      [event.target.name]: event.target.value,
    });
  };

  const handleSubmit = () => {
    if (state.author.length < 1) {
      // alert('작성자명은 최소 한 글자 이상 입력해주세요.');
      authorInput.current.focus();
      return;
    }

    if (state.content.length < 5) {
      // alert('본문은 최소 다섯 글자 이상 작성해주세요.');
      contentInput.current.focus();
      return;
    }

    // 둘 다 비어있으면 두 if문중에 어떤 것부터 실행하나 싶었는데
    // 그냥 스크립트 언어 특성 상 위에 있는 거 먼저 하나봄 ㅎㅎ

    onCreate(state.author, state.content, state.emotion);
    alert('저장 완료!'); // 일기가 잘 저장되었다면
    setState({
      // 초기화해줍니다.
      author: '',
      content: '',
      test: '',
      emotion: '⭐⭐⭐',
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
            // ⬇ setAuthor(event.target.value);
            setState({
              author: event.target.value,
              content: state.content,
            });
            // state를 객체st로 만들었기 때문에 여기에도 객체로.
            // 하지만 프로퍼티 별 세부조정하지 않으면 나머지도 불필요하게 바뀌므로
            // 꼭 프로퍼티 별 설정을 해주도록 해요

            // 그럼 여기서 생기는 의문 : 코드 더 길어졌잖아요..
            // 이걸 위해서 스프레드 연산자를 배웠다..
          }}
        />
      </div>
      <div>
        <textarea
          ref={contentInput}
          name='content'
          value={state.content}
          onChange={(event) => {
            // ⬇ setContent(event.target.value);
            setState({
              // author: state.author,
              // content: event.target.value,
              ...state,
              content: event.target.value,
              // 순서 중요합니다.. 위에서부터 아래로 읽는 스크립트니께..
              // content: event.target.value,
              // ...state,  <-- 이런 순서면 위 타겟을 아래 스프레드가 덮어씌워버리니까 몬주알지??
            });
          }}
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
          <option value={'⭐'}>⭐</option>
          <option value={'⭐⭐'}>⭐⭐</option>
          <option value={'⭐⭐⭐'}>⭐⭐⭐</option>
          <option value={'⭐⭐⭐⭐'}>⭐⭐⭐⭐</option>
          <option value={'⭐⭐⭐⭐⭐'}>⭐⭐⭐⭐⭐</option>
        </select>
      </div>
      <div>
        <button onClick={handleSubmit}>💻 저! 장! 💾</button>
      </div>
    </div>
  );
};
export default DiaryEditor;
