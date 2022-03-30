num = float(input("점수는 100점 만점입니다. 점수 입력 :"))

if 90 <= num <= 100:
    print("당신은 에이스!")

elif 80 <= num <= 89:
    print("학점 : B")

elif 70 <= num <= 79:
    print("교수님의 C뿌리기!")

elif 60 <= num <= 69:
    print("너는 D졌다!")

else:
    print("총살")
