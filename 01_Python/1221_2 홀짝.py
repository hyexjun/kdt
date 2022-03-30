import sys

num = int(input("1~100 사이의 정수 입력 : "))

if num <= 0 or num > 100:
    print("1~100 사이의 정수가 아닙니다.")
    sys.exit()  # 프로그램 종료. 선생님이 알려준 정답

if num % 2 == 0:
    print(num, "는 짝수입니다.")
else:
    print(num, "는 홀수입니다.")


x = int(input("1~100 사이의 정수를 입력하세요. :"))

if x <= 0 or x > 100:
    print("범위 밖입니다.")  # 내가 상상한 것

if x % 2 == 0:
    print("짝수")
else:
    print("홀수")


x = input()
print(type(x))          # 위에서 input 받을 때 int처리 하지 않아서 타입 str로 나옴..
if x % 2 == 0:              # 애초에 정수가 아니므로 2로 나눌 수 없음.. 그래서 오류다..
    print("짝수")
else:
    print("홀수")  # 시도한 것
