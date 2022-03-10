import requests
import re

# res = requests.get('http://www.naver.com')
# res.raise_for_status() #정상 200 코드 일 때 계속 진행

p = re.compile('ca.e') # 정규 표현식 지정
m = p.match('careful') # 매칭이 되었는지 확인

if m:
    print('매칭되었습니다.')
    print('m.group --> 일치한 단어 출력 : ', m.group())  #매칭 검사한 단어를 출력시켜줌.
    print('m.string --> 입력한 단어 출력 : ', m.string)  #매칭 검사한 단어를 출력시켜줌.
    print('m.start() --> 일치하는 문자열의 시작 index : ', m.start())  #매칭 검사한 단어를 출력시켜줌.
    print('m.end() --> 일치하는 문자열의 시작 index : ', m.end())  #매칭 검사한 단어를 출력시켜줌.
    print('m.span() --> 일치하는 문자열의 시작과 마지막 index : ', m.span())  #매칭 검사한 단어를 출력시켜줌.
else :
    print('매치 되지 않음')

