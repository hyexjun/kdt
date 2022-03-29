import imp
import requests
import re

p = re.compile('ca.e') #정규표현식 형태 지정
# m = p.match('good care') #ca로 시작하고 1개의 문자가 있는지 비교
m = p.search('good care') #문자열 중에 ca가 있고, 1개의 문자가 있는지 비교

if m:
    print('매칭성공')
else :
    print('매칭 실패')