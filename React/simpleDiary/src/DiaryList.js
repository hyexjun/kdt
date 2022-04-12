import DiaryItem from './DiaryItem';

// onRemove 이후에도 onEdit 만들었으니 props로 받아야겠지요? 💎
const DiaryList = ({ diaryList, onRemove, onEdit }) => {
  return (
    <div className='DiaryList'>
      <h2>누가 내 🧀 먹었냐고</h2>
      <h4>{diaryList.length}개의 일기가 있습니다.</h4>
      <div>
        {diaryList.map((item) => (
          <DiaryItem
            key={item.id}
            {...item}
            onRemove={onRemove}
            onEdit={onEdit}
          /> // 💎 요기에 넣어줍니다. 그리고.. item.js로 가자..
          // id가 일치하는 객체에 포함된 모든 데이터가 ...item 쫘라락 전달
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
