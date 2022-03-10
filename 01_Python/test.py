price=input("가격을 입력하세요:")
num=input("개수를 입력하세요:")
#sum=price*num
sum=int(price)*int(num)
print('총금액은 ',sum,'원입니다.')

import keyword
import pprint

pprint.pprint(keyword.kwlist, width=60, compact=True)
help(pprint)
      
from keyword import kwlist
from pprint import pprint
pprint(kwlist, width=60, compact=True)
