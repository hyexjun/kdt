# for i in 'abcdefghijk':
# print(i)

for odd in range(1, 11):
    if odd % 2 > 0:
        print(odd)

total = 0  # 1~10 정수를 누적 저장할 변수 선언과 초기화
for num in range(1, 37):
    total += num
print("1~10까지의 합은", total, "입니다.")

# 랜덤공식
k = int(input("정수 k를 입력하면, 약수의 합을 알려주마!"))

total = 0
for i in range(1, k+1):
    if k % i == 0:
        print(i)
        total += i
print("k의 약수의 합은..", total, "이거다..")
