import './App.css';
import DiaryEditor from './DiaryEditor';
import DiaryList from './DiaryList';
import { useCallback, useRef, useEffect, useMemo, useReducer } from 'react';
// import OptimizeTest from './OptimizeTest';

const reducer = (state, action) => {
  switch (action.type) {
    case 'INIT': {
      return action.data; // 새로운 state가 됨?
    }
    case 'CREATE': {
      const created_date = new Date().getTime();
      const newItem = {
        ...action.data, // = data: { author, content, emotion, id: dataId.current }
        created_date,
      };
      return [newItem, ...state];
    }
    case 'REMOVE': {
      return state.filter((item) => item.id !== action.targetId);
    }
    case 'EDIT': {
      // edit type의 액션 발생 시 targetId와 newContent가 전달됨
      return state.map(
        (item) =>
          item.id === action.targetId // tergetId와 일치하는 요소를 찾은 뒤
            ? { ...item, content: action.newContent } // 일치하면 newContent로 수정
            : item // 아니면 원래 내용 그대로.
      );
    }
    default:
      return state;
  }
};

function App() {
  // const [data, setData] = useState([]);
  const [data, dispatch] = useReducer(reducer, []); // reducer는 내장함수 아님

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

    dispatch({ type: 'INIT', data: initData });
    // setData(initData);  <-- 이 문장이 할 일을 reducer가 할 예정
  };

  useEffect(() => {
    getData();
  }, []);

  const onCreate = useCallback((author, content, emotion) => {
    dispatch({
      type: 'CREATE',
      data: { author, content, emotion, id: dataId.current },
    });
    // created_date는 reducer에서 선언 예정
    dataId.current += 1;
    // setData((data) => [newItem, ...data]);
  }, []);

  const onRemove = useCallback((targetId) => {
    dispatch({ type: 'REMOVE', targetId });
    // setData((data) => data.filter((item) => item.id !== targetId));
  }, []);

  const onEdit = useCallback((targetId, newContent) => {
    dispatch({ type: 'EDIT', targetId, newContent });
    // setData(
    //   data.map((item) =>
    //     item.id === targetId ? { ...item, content: newContent } : item
    //   )
    // );
  }, []);

  const getDiaryAnalysis = useMemo(() => {
    const goodCount = data.filter((item) => item.emotion >= 3).length;
    const badCount = data.length - goodCount;
    const goodRatio = (goodCount / data.length) * 100;
    return { goodCount, badCount, goodRatio };
  }, [data.length]);

  const { goodCount, badCount, goodRatio } = getDiaryAnalysis;

  return (
    <div className='App'>
      {/* <OptimizeTest /> */}
      <DiaryEditor onCreate={onCreate} />
      <div className='Ratio'>
        <div>🌈 Total Diaries : {data.length} days</div>
        <div>Good 🌞 Days : {goodCount} days</div>
        <div>Bad 🌚 Days : {badCount} days</div>
        <div>How is your last? : 🍀 {goodRatio.toFixed(1)}%</div>
      </div>
      <DiaryList onEdit={onEdit} onRemove={onRemove} diaryList={data} />
    </div>
  );
}

export default App;
