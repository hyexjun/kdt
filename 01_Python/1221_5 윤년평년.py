moon = int(input("xxxx년은 윤년일까요 평년일까요? :"))

if moon % 4 == 0:
    if moon % 400 == 0:
        print(moon, "년은 윤년입니다.")
    elif moon % 100 == 0:
        print(moon, "년은 평년입니다.")
    else:
        print(moon, "년은 평년입니다.")
else:
    print(moon, "년은 평년입니다.")
