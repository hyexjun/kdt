import './App.css';
import DiaryEditor from './DiaryEditor';
import DiaryList from './DiaryList';
import { useState, useRef, useEffect } from 'react';
import Lifecycle from './Lifecycle';

function App() {
  const [data, setData] = useState([]); // 일기 데이터의 배열을 저장할 곳이므로 빈 배열로 초기값 설정
  const dataId = useRef(1); // 🎄 useRef 뭔지 다시 공부하십쇼..

  const onCreate = (author, content, emotion) => {
    const created_date = new Date().getTime(); // onCreate 실행되는 시각을 상수에 저장
    const newItem = {
      author,
      content,
      emotion,
      created_date,
      id: dataId.current,
    };
    dataId.current += 1; // 🎄 0으로 설정했으니 이후 생성 시 +1 해주기

    // setData([...data, newItem]);
    // 원래 data에 newItem을 추가한 배열 생성!
    // 근데 우린 최신글이 상단에 올라오게 해야되므로 순서를 반대로 해줍니다
    setData([newItem, ...data]);
  };

  const onRemove = (targetId) => {
    console.log(`${targetId}번 일기가 삭제되었습니다.`);
    const newDiaryList = data.filter((it) => it.id !== targetId);
    console.log(newDiaryList); // fillter 함수 조건 맞게 추출해서 새로운 배열 만드는거 기억나지요
    setData(newDiaryList); // 새로운 배열을 다시 setData로 바꿔치기!
  };

  // 수정 최종완료 버튼 눌렀을 때 아무 데이터로 매칭돼서 바뀌면 안되니까요
  const onEdit = (targetId, newContent) => {
    setData(
      data.map((item) =>
        item.id === targetId ? { ...item, content: newContent } : item
      ) // 수정대상이 맞으면 ? item 쫘라락에서 content --> newContent로 바꿔줘!
    );
  }; // 이렇게 만든 함수가 타고 타고 가서 실행되려면 🎁

  return (
    <div className='App'>
      <Lifecycle />
      <DiaryEditor onCreate={onCreate} />
      {/* 게시글생성 함수를 에디터 컴포넌트에 프롭으로 전달.. ??? */}
      <DiaryList onEdit={onEdit} onRemove={onRemove} diaryList={data} />
      {/* 🎁 요기로. onEdit함수가 쓰일 item의 부모인 요 컴포넌트로 갑쉬다 */}
    </div>
  );
}

export default App;
