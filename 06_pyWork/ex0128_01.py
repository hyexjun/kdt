import requests


url="https://www.melon.com/chart/index.htm"
res = requests.get(url)   # 정보 요청
res.raise_for_status()                         # 에러코드이면 프로그램 종료
# print("응답 코드", res.status_code)             # 코드 지위? 상태를 알려줌


if res.status_code==requests.codes.ok:
    print("정상출력")

else :
    print("비정상출력")