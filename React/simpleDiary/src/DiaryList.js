import { useContext } from 'react';
import DiaryItem from './DiaryItem';
import { DiaryStateContext } from './App'; // 컴포넌트 트리로 데이터 가져올 곳

// const DiaryList = ({ diaryList, onRemove, onEdit }) => {
  // 이제 더이상 diaryList를 프롭으로 받아올 필요 X

const DiaryList = ({ onRemove, onEdit }) => {
  // onRemove, onEdit 프롭 받아왔으니 💎

  const diaryList = useContext(DiaryStateContext)

  return (
    <div className='DiaryList'>
      <h2>누가 내 🧀 먹었냐고</h2>
      <h4>{diaryList.length}개의 일기가 있습니다.</h4>
      <div>
        {diaryList.map((item) => (
          <DiaryItem
            key={item.id}
            {...item}
            onRemove={onRemove} // 💎 써준다
            onEdit={onEdit} // 💎 받아온 프롭 써주기
          />
        ))}
      </div>
    </div>
  );
};

// 게시글 0개일 때? length 받아올 거 없다고 오류 나오는 거 방지를 위한 default로 빈 배열 정해주기
DiaryList.defaultProps = {
  diaryList: [],
};
export default DiaryList;
