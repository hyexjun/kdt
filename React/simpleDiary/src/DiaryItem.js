import { useState, useRef } from 'react';

const DiaryItem = ({
  onEdit, // 💎 js 파일을 타고 타고 여기까지 스며들어줍니다..
  onRemove,
  id,
  author,
  content,
  emotion,
  created_date,
}) => {
  const [isEdit, setIsEdit] = useState(false);
  // 수정중이냐 아니냐 boolean으로 값을 보관해놓을 state?
  // state 만들었으면 이제 토글 함수를 만들어봅니다..
  const toggleIsEdit = () => setIsEdit(!isEdit); // 이 함수가 호출이 되면 isEdit을 반전시켜버리는.. 용..

  const [localContent, setLocalContent] = useState(content);
  // 수정창에서 열릴 contents의 기본값(useState(요거))을 찐 컨텐츠로 해두면,
  // 수정 클릭해서 열릴 때 이전 써둔 그 데이터 고대로 나오겠쥬?

  const localContentInput = useRef();
  // 뭐가 이렇게 많아.. 싶지만,
  // 수정창 말고 본문창에서도ㅜㅜ 해놓은 기능이니까 완성도를 위해 참고 해줍니다..

  const handleRemove = () => {
    if (window.confirm(`${id}번 일기를 정말 삭제하시겠습니까?`)) {
      onRemove(id); // 확인을 누르면 id를 전달..
    }
  };

  const handleQuitEdit = () => {
    // 수정 취소 누를 때 실행될 함수
    setIsEdit(false); // 편집 상태를 false로 돌릴거고
    setLocalContent(content); // 내가 입력해놨던 수정내용도 걍 원래 내용으로 복원
  };

  // 대망의 CRUD 중 update(수정)입니다..
  const handleEdit = () => {
    if (localContent.length < 5) {
      localContentInput.current.focus();
      return;
    }

    // if (window.confirm(`${id}번 일기를 수정하시겠습니까?`)) {
    //   onEdit(id, localContent); // 저는 그냥 안 물어볼래요..
    //   toggleIsEdit();
    // }

    onEdit(id, localContent); // 여기까지는 수정창 입력 데이터를 바꿔치기해주지만
    toggleIsEdit(); // 요기까지 실행돼야 수정창도 닫히고, 내용물도 보여주는 화면으로 바뀐다!!
  };

  return (
    <div className='DiaryItem'>
      <div className='info'>
        <span>
          « 작성자 : {author} 🍟 오늘의 별점 : {emotion} »
        </span>
        <br />
        <span className='date'>{new Date(created_date).toLocaleString()}</span>
      </div>
      {/* <div className='content'>{content}</div> */}
      <div className='content'>
        {isEdit ? (
          <>
            <textarea
              ref={localContentInput}
              value={localContent}
              onChange={(event) => {
                setLocalContent(event.target.value);
              }}
            />
          </>
        ) : (
          <>{content}</>
        )}
        {/* 와 여기서 삼항연산자로 깔끔처리가 되는구나.. 감탄.. */}
      </div>
      {isEdit ? (
        <>
          <button onClick={handleEdit}>저장</button>
          <button onClick={handleQuitEdit}>취소</button>
        </>
      ) : (
        <>
          <button onClick={toggleIsEdit}>수정</button>
          {/* 이제 수정하기를 누르면 isEdit의 state가
      기본값 false에서 true로, 이후엔 또 반대로 반전처리 먹힘
      이제 isEdit이 true일땐 수정창? 나오도록 하는 함수를 짜볼거예요 */}
          <button onClick={handleRemove}>삭제</button>
        </>
      )}
    </div>
  );
};

export default DiaryItem;
