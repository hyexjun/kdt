import DiaryItem from './DiaryItem';

// 신병 받아라.. onRemove 이후에도 onEdit 만들었으니 props로 받아야겠지요? 💎
const DiaryList = ({ diaryList, onRemove, onEdit }) => {
  return (
    <div className='DiaryList'>
      <h2>누가 내 🧀 먹었냐고</h2>
      <h4>{diaryList.length}개의 일기가 있습니다.</h4>
      <div>
        {diaryList.map((item, idx) => (
          // <div key={item.id}>  <-->  <div key={idx}>
          // 이렇게 해도 되긴 하는데 글 삭제해서 idx 순서가 변경될 경우 꼬일 수 있음!!
          // 정확한 id가 있는 경우 웬만하면 id 쓰자 이건 ^^
          //   <div>작성자 : {item.author}</div>
          //   <div>내용 : {item.content}</div>
          //   <div>감정 : {item.emotion}</div>
          //   <div>작성 시각 : {item.created_date}</div>
          // </div>
          // 열심히 쳤지만 결국 컴포넌트로 분리작업 들어가버리고
          <DiaryItem key={item.id} {...item} onRemove={onRemove} onEdit={onEdit}/> // 💎 요기에 넣어줍니다. 그리고.. item.js로 가자..
          // it 객체에 포함된 모든 데이터가 ...item 쫘라락 전달
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
