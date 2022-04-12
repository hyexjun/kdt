import './App.css';
import DiaryEditor from './DiaryEditor';
import DiaryList from './DiaryList';
import { useCallback, useState, useRef, useEffect, useMemo } from 'react';
// import OptimizeTest from './OptimizeTest';

// https://jsonplaceholder.typicode.com/comments

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
        emotion: Math.floor(Math.random() * 5) + 1, // 이건 써먹을 게 없어서 랜덤으로 만든다
        created_date: new Date().getTime(),
        id: dataId.current++,
      }; // 별점 랜덤인데 별모양으로 보이고 싶으면.. 난수*'⭐'이 안 먹히니까
    }); // switch나 forloop 같은 걸로 경우 설정해서 출력으로 꽂아야되니..?

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

  const onRemove = (targetId) => {
    const newDiaryList = data.filter((it) => it.id !== targetId);
    // console.log(newDiaryList); 확인용 log는 웬만하면 지우자
    console.log(`${targetId}번 일기가 삭제되었습니다.`);
    setData(newDiaryList);
  };

  const onEdit = (targetId, newContent) => {
    setData(
      data.map((item) =>
        item.id === targetId ? { ...item, content: newContent } : item
      )
    );
  };

  const getDiaryAnalysis = useMemo(() => {
    const goodCount = data.filter((item) => item.emotion >= 3).length;
    const badCount = data.length - goodCount;
    const goodRatio = (goodCount / data.length) * 100;
    return { goodCount, badCount, goodRatio };
  }, [data.length]);

  const { goodCount, badCount, goodRatio } = getDiaryAnalysis;
  // useMemo 쓰면 getDiaryAnalysis는 더이상 함수가 아니라는데 이 부분 다시 봐야할듯
  // 뭔가 그 기능?을 모르겠다기보단 문법? 굴러가는 회로를 몰겠음..ㅡㅡ useRef도 마찬가지다 ㅋㅋ

  return (
    <div className='App'>
      {/* <OptimizeTest /> */}
      {/* 최적화테스트 실습용이니 끝나면 꼭 지워주자 */}
      <DiaryEditor onCreate={onCreate} />
      <div>전체 일기 : {data.length}</div>
      <div>좋은 날 : {goodCount}</div>
      <div>안 좋은 날 : {badCount}</div>
      <div>좋은 비율 : {goodRatio}%</div>
      <DiaryList onEdit={onEdit} onRemove={onRemove} diaryList={data} />
    </div>
  );
}

export default App;
