import React, { useEffect, useState, useRef } from 'react';
// 최적화 이전 주석은 별도 파일에서 확인!

const DiaryItem = ({
  onEdit, // 상태변화 가능 + 더불어 함수 컴포넌트
  onRemove, // 상태변화 가능 + 더불어 함수 컴포넌트
  // onCreate 최적화 했던 것처럼 useCallback 쓰러 갑쉬다
  id,
  author,
  content, // 상태변화 가능
  emotion,
  created_date,
}) => {
  useEffect(() => {
    console.log(`${id}번 아이템 렌더`);
  });

  const [isEdit, setIsEdit] = useState(false);
  const toggleIsEdit = () => setIsEdit(!isEdit);

  const [localContent, setLocalContent] = useState(content);
  const localContentInput = useRef();

  const handleRemove = () => {
    if (window.confirm(`${id}번 일기를 정말 삭제하시겠습니까?`)) {
      onRemove(id);
    }
  };

  const handleQuitEdit = () => {
    setIsEdit(false);
    setLocalContent(content);
  };

  const handleEdit = () => {
    if (localContent.length < 5) {
      localContentInput.current.focus();
      return;
    }

    onEdit(id, localContent);
    toggleIsEdit();
  };

  return (
    <div className='DiaryItem'>
      <div className='info'>
        <span>
          « 작성자 : {author} 🍟 오늘의 점수 : {emotion} »
        </span>
        <br />
        <span className='date'>{new Date(created_date).toLocaleString()}</span>
      </div>
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
      </div>
      {isEdit ? (
        <>
          <button onClick={handleEdit}>저장</button>
          <button onClick={handleQuitEdit}>취소</button>
        </>
      ) : (
        <>
          <button onClick={toggleIsEdit}>수정</button>
          <button onClick={handleRemove}>삭제</button>
        </>
      )}
    </div>
  );
};

export default React.memo(DiaryItem);
