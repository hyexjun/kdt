import sys

x = int(input("정수 x를 입력하세요 :"))
y = int(input("정수 y를 입력하세요 :"))
z = input("연산자 입력(*,/,+,-) 중 택 1:")


if z == "*":
    print(x*y, "은(는) 곱셈의 결과입니다.")

elif z == "/":
    print(x/y, "은(는) 나눗셈의 결과입니다.")

elif z == "+":
    print(x+y, "은(는) 덧셈의 결과입니다.")

elif z == "-":
    print(x+y, "은(는) 뺄셈의 결과입니다.")

else:
    print("다 틀렸다!")
    sys.exit()


# if xzy = x*y :
# 아래는 대충 비슷했음..
# 그냥 x랑 y를 위로 인형뽑기하면 정답에 가까워짐..
# 안되는 이유 xzy= <는 하나인데 x*y, x/y, 변수 하나에 4종류 주기 힘듦..
# 추가 포인트는 z값이 문자열이므로 if문에서 문자열z라고 알도록 ""써주기


# 아래는 선생님정답

x = int(input("정수 1을 입력하세요 :"))
y = int(input("정수 2를 입력하세요 :"))
z = input("연산자(*,/,+,-)를 선택하세요:")


if z == "*":
    print(x, str(z), y, "=", (x*y))
elif z == "/":
    print(x, str(z), y, "=", (x/y))
elif z == "+":
    print(x, str(z), y, "=", (x+y))
elif z == "-":
    print(x, str(z), y, "=", (x-y))
else:
    print("수식이 안 맞습니다.")
