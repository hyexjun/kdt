import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 시리즈 = 1차원 데이터 (정수, 실수, 문자열 등)
temp = pd.Series([-20, -10, 10, 20], index=['Jan', 'Feb', 'Mar', 'Apr'])
print(temp)

# x = [1,2,3]
# y = [2,4,8]
# plt.plot(x, y)
# plt.title('Line Graph')
# plt.show()