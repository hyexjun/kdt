import './App.css';
import DiaryEditor from './DiaryEditor';
import DiaryList from './DiaryList';
import React, {
  useCallback,
  useRef,
  useEffect,
  useMemo,
  useReducer,
} from 'react';

const reducer = (state, action) => {
  switch (action.type) {
    case 'INIT': {
      return action.data;
    }
    case 'CREATE': {
      const created_date = new Date().getTime();
      const newItem = {
        ...action.data,
        created_date,
      };
      return [newItem, ...state];
    }
    case 'REMOVE': {
      return state.filter((item) => item.id !== action.targetId);
    }
    case 'EDIT': {
      return state.map((item) =>
        item.id === action.targetId
          ? { ...item, content: action.newContent }
          : item
      );
    }
    default:
      return state;
  }
};

export const DiaryStateContext = React.createContext();
export const DiaryDispatchContext = React.createContext();

function App() {
  const [data, dispatch] = useReducer(reducer, []);
  const dataId = useRef(0);

  const getData = async () => {
    const res = await fetch(
      'https://jsonplaceholder.typicode.com/comments'
    ).then((res) => res.json());

    const initData = res.slice(0, 20).map((item) => {
      return {
        author: item.email,
        content: item.body,
        emotion: Math.floor(Math.random() * 5) + 1,
        created_date: new Date().getTime(),
        id: dataId.current++,
      };
    });

    dispatch({ type: 'INIT', data: initData });
  };

  useEffect(() => {
    getData();
  }, []);

  const onCreate = useCallback((author, content, emotion) => {
    dispatch({
      type: 'CREATE',
      data: { author, content, emotion, id: dataId.current },
    });
    dataId.current += 1;
  }, []);

  const onRemove = useCallback((targetId) => {
    dispatch({ type: 'REMOVE', targetId });
  }, []);

  const onEdit = useCallback((targetId, newContent) => {
    dispatch({ type: 'EDIT', targetId, newContent });
  }, []);

  const memoizedDispatches = useMemo(() => {
    return { onCreate, onRemove, onEdit };
  }, []);

  const getDiaryAnalysis = useMemo(() => {
    const goodCount = data.filter((item) => item.emotion >= 3).length;
    const badCount = data.length - goodCount;
    const goodRatio = (goodCount / data.length) * 100;
    return { goodCount, badCount, goodRatio };
  }, [data.length]);

  const { goodCount, badCount, goodRatio } = getDiaryAnalysis;

  return (
    // [1] 최상위 컴포넌트를 공급자 컴포넌트로 변경
    <DiaryStateContext.Provider value={data}>
      {/* [2]
          Q. 데이터 전달하는 context에 onCreate, onRemove, onEdit도 같이 태워보내면 안되나요?
          A. 네 안됩니다. 글작성, 삭제 등 이벤트 발생으로 prop이 바뀌면 리렌더링 발생함.
              그러면 기껏 불필요한 리렌더링 줄이려고 최적화한 것들이 말짱 도로묵이 된다(?)는듯..
            Q. 그럼 얘네들은 어떻게 태워보내요?
            A. state를 변화시키는 함수(dispatch)들은 새로 context를 또 만들어라! */}
      <DiaryDispatchContext.Provider value={memoizedDispatches}>
        <div className='App'>
          <DiaryEditor />
          <div className='Ratio'>
            <div>🌈 Total Diaries : {data.length} days</div>
            <div>Good 🌞 Days : {goodCount} days</div>
            <div>Bad 🌚 Days : {badCount} days</div>
            <div>How is your last? : 🍀 {goodRatio.toFixed(1)}%</div>
          </div>
          {/* <DiaryList onEdit={onEdit} onRemove={onRemove} diaryList={data} /> */}
          <DiaryList />
          {/* [1] context로 전달하므로 컴포넌트로 전달 불필요 */}
        </div>
      </DiaryDispatchContext.Provider>
    </DiaryStateContext.Provider>
  );
}

export default App;
