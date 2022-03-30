a = float(input("A과목 점수를 입력하세요."))
b = float(input("B과목 점수를 입력하세요."))
c = float(input("C과목 점수를 입력하세요."))
d = (a+b+c)/3

if 60 <= d:
    print("총점은", a+b+c, "입니다. 평균이", d, "이므로 합격입니다!")

elif d < 60:
    print("총점은", a+b+c, "입니다. 평균이", d, "이므로 집에 가세요..")
