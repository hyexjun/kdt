const site = prompt(
  '원하는 사이트 이름을 입력하세요.\n 네이버, 다음, 네이트, 구글 등'
);

switch (site) {
  case '네이버':
    url = 'http://www.naver.com';
    break;
  case '다음':
    url = 'http://www.daum.net';
    break;
  case '네이트':
    url = 'http://www.nate.com';
    break;
  case '구글':
    url = 'http://www.google.com';
    break;
  default:
    alert('해당이 되지 않는 사이트입니다.');
    break;
}

if (url) {
  location.href = url;
}
