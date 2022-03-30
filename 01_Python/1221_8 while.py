i = 0
while i < 10:
    print(i)
    i = i+1             # i += 1


i = 0
k = 0

while i < 10:           # i는 0부터 10미만까지 반.복.을 하겠다 와일은 반복.. 와일은 반복..
    if i % 2 == 0:      # 만약 i의 나머지가 0이라면=(짝수라면)
        print(i)        # 위의 값들을 출력해라
    i = i+1
    k = k+i             # print(i)의 합을
print(k)                # 출력해라


for row in range(1, 6):                      # 행을 1부터 5까지 반복
    for col in range(1, 6):                  # 열을 1부터 5까지 반복
        print("(", row, ",", col, ")", end=" ")  # 그걸 ( 행, 렬 ) 이라는 틀로
    print()                                  # 이거 엔드 무슨 의미였지..


for row in range(0, 3):
    for col in range(0, 3):
        if (col == 1):
            break
        print("(", row, ",", col, ")", end=" ")
    print()

    # 아래 두 종류의 미묘한 차이가 궁금한디..

for row in range(1, 6):
    for col in range(1, 6):
        if row >= col:
            print("(", row, ",", col, ")", end=" ")
    print()


for row in range(1, 6):
    for col in range(1, row+1):
        print("(", row, ",", col, ")", end=" ")
    print()
