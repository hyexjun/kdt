def get_web(url) :
    import urllib.request                           # urllib이라는 라이브러리?를 가져온다
    response = urllib.request.urlopen(url)          # 받은 url을 여는 urlopen 함수 사용
    data = response.read()                          # 바로 윗줄의 리스폰을 읽어서 = 데이터라 명명
    decoded = data.decode('utf-8')                  # 국제표준머시기의 utf8로 디코딩을 한 걸 decoded라고 명명
    return decoded                                  # 그게 최종 return 값이다!

url = input("웹 페이지 주소를 입력하세요 :")          # url을 입력하면
content = get_web(url)                              # get_web 함수를 실행한 결과를 content라고 하겠음
print(content)                                      # 출력!!