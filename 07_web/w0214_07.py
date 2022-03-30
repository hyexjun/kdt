# lo.e 정규표현식 형태
# search 비교
# i love you, you live, lofffe, loke, loaeful, live love, from loveless
import re

m_list = ['i love you', 'you live', 'lofffe', 'loke', 'loaeful', 'live love', 'from loveless']

p = re.compile('lo.e')
for m_word in m_list:
    m = p.search(m_word)
    if m:
        print('성공')
        print(m.group())
    else:
        print('실패')
        