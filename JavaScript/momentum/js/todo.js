const toDoForm = document.querySelector('#todo-form');
const toDoInput = toDoForm.querySelector('input');
// const toDoInput = document.querySelector('#todo-form input'); 같은 거 알지?
const toDoList = document.querySelector('#todo-list');
// const toDos = [];
let toDos = []; // 58번쯤 있는 toDos = parsedToDos; 를 위한 빌드업
// 여러 바퀴 돌 때마다 빈 배열로 시작하면 새로고침할 때 증발해보이는 요소들이 있음
// 이전 todo들도 덧씌워주기? 위해서 상수에서 변수로 바꿈
const TODOS_KEY = 'toDos';


function saveToDos() {
  localStorage.setItem(TODOS_KEY, JSON.stringify(toDos));
  // stringify : todos array를 string으로 변환하는 콜백함수
  // parse : 반대로 string을 array로 변환처리하는 콜백함수
}


function deleteToDo(event) {
  const li = event.target.parentElement; // 할일목록 중 어떤 li를 지워야하는지 설정
  // html에서 삭제버튼 클릭 시 li 삭제도 삭제지만 DB에서 좌표 찍는 것도 중요함
  // 그러려면 할일목록 생성 및 리스트업 시 배열이나 문자열로 저장 X
  // 정확한 좌표를 주기 위해 객체(ex. {id:random, text: "할일1"})로 생성 추천
  li.remove();
  toDos = toDos.filter(toDo => toDo.id !== parseInt(li.id));  // toDo.id는 number, 그냥 li.id는 string
  saveToDos();
}


function paintTodo(newTodo) {
  const li = document.createElement('li');
  li.id = newTodo.id;
  const span = document.createElement('span');
  span.innerText = newTodo.text; // 넘겨받은 객체에서 text만 쏙 보여주도록 가다듬기
  const button = document.createElement('button');
  button.innerText = '❌';
  button.addEventListener('click', deleteToDo);
  li.appendChild(span); // X.appendChild(Y);
  li.appendChild(button); // X에 Y를 추가함
  toDoList.appendChild(li); // 여기까지 해야 실제 li 요소가 html에 들어가겠져
} // append는 마지막에 있어야 함 . 이유는 다시 생각해보세요.


function handleToDoSubmit(event) {
  event.preventDefault(); // 복습! 새로고침? 막는 함수?
  const newTodo = toDoInput.value; // 입력됐던 값을 변수에 할당하고
  toDoInput.value = ''; // 그 담에 비우기예요^^
  console.log(`newTodo : ${newTodo}, toDoInput.value : ${toDoInput.value}`);
  // 인풋박스가 비워지는 거지 이전 입력했던 값은 newTodo에 가있는거지..

  // toDos.push(newTodo);  <-- 빈 배열(toDos)에 input Value(newTodo)가 담기는 지점
  // 초반에는 그냥 string만 담았지만 지금은 obj를 담기로 했으니까 바꿔줍니다..
  const newTodoObj = {
    text: newTodo,
    id: Date.now(),  // 삭제를 위한 고유한 좌표 id 생성요소
  }
  toDos.push(newTodoObj);
  paintTodo(newTodoObj); // 여기부터 newTodoObj.text로 줘버리면 html에 id가 안 넘어간다..?
  saveToDos();
}

toDoForm.addEventListener('submit', handleToDoSubmit);


const savedToDos = localStorage.getItem(TODOS_KEY);
// console.log('savedToDos', savedToDos);
if (savedToDos !== null) {
  const parsedToDos = JSON.parse(savedToDos);
  // console.log('parsedToDos', parsedToDos);
  toDos = parsedToDos;
  parsedToDos.forEach(paintTodo); // forEach(a) : array의 요소 하나마다 a를 실행
}
