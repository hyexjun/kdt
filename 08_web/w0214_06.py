# s.t 정규표현식 형태
# match 으로 비교
# start, sat, ssen, sin, son, sot

import re

m_list = ['sat', 'start', 'ssen', 'sin', 'son', 'sot']
p = re.compile('s.t')
for m_word in m_list:
    m = p.match(m_word)
    if m:
        print('성공')
        print(m.group())
        print(m.string)
        print(m.start())
        print(m.end())
        print(m.span())
    else :
        print('실패')
        