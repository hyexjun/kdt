const images = ['0.png', '1.png', '2.png'];
// 이미지 목록으로 배열 만들기

const chosenImage = images[Math.floor(Math.random() * images.length)];
// 랜덤으로 사진 번호 고르기

const bgImage = document.createElement('img');
// html에 넣을 dom요소 만들기

bgImage.src = `img/${chosenImage}`;

document.body.appendChild(bgImage);
