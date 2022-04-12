import './App.css';
import DiaryEditor from './DiaryEditor';
import DiaryList from './DiaryList';
import { useCallback, useState, useRef, useEffect, useMemo } from 'react';
// import OptimizeTest from './OptimizeTest';

function App() {
  const [data, setData] = useState([]);
  const dataId = useRef(1);

  const getData = async () => {
    const res = await fetch(
      'https://jsonplaceholder.typicode.com/comments' // json 가져온 데이터 샘플로 활용하기
    ).then((res) => res.json());

    const initData = res.slice(0, 20).map((item) => {
      return {
        author: item.email,
        content: item.body, // 일기장 틀에 맞게 데이터 변경처리 해주는 과정
        emotion: Math.floor(Math.random() * 5) + 1, // 가져올 데이터 없으므로 랜덤생성
        created_date: new Date().getTime(),
        id: dataId.current++,
      };
    });

    setData(initData);
  };

  useEffect(() => {
    getData();
  }, []);

  const onCreate = useCallback((author, content, emotion) => {
    const created_date = new Date().getTime();
    const newItem = {
      author,
      content,
      emotion,
      created_date,
      id: dataId.current,
    };
    dataId.current += 1;
    setData((data) => [newItem, ...data]);
  }, []);

  // const onRemove = (targetId) => {
  //   const newDiaryList = data.filter((it) => it.id !== targetId);
  //   console.log(`${targetId}번 일기가 삭제되었습니다.`);
  //   setData(newDiaryList);
  // };   ⬇ useCallback 사용한 최적화 ver.
  const onRemove = useCallback((targetId) => {
    setData((data) => data.filter((item) => item.id !== targetId));
  }, []);

  const onEdit = useCallback((targetId, newContent) => {
    setData(
      data.map((item) =>
        item.id === targetId ? { ...item, content: newContent } : item
      )
    );
  }, []);

  const getDiaryAnalysis = useMemo(() => {
    const goodCount = data.filter((item) => item.emotion >= 3).length;
    const badCount = data.length - goodCount;
    const goodRatio = (goodCount / data.length) * 100;
    return { goodCount, badCount, goodRatio };
  }, [data.length]);

  const { goodCount, badCount, goodRatio } = getDiaryAnalysis;
  // ⭐ useMemo와 React.memo 차이? 복습 필요!!

  return (
    <div className='App'>
      {/* <OptimizeTest /> */}
      <DiaryEditor onCreate={onCreate} />
      <div className='Ratio'>
        <div>전체 일기 : {data.length}개</div>
        <div>좋은 날 : {goodCount}개</div>
        <div>안 좋은 날 : {badCount}개</div>
        <div>좋은 비율 : {goodRatio}%</div>
      </div>
      <DiaryList onEdit={onEdit} onRemove={onRemove} diaryList={data} />
    </div>
  );
}

export default App;
