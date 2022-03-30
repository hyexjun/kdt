# 인스턴스 변수 : travelCode(str), cityName(str), flight(str), travelType(int), maxPeole(int), reserved(int)
# maxPeople(int), reserved(int)

class Travel:
    INDIVIDUAL = 0
    PACKAGE = 1

    def __init__(self, travelCode, cityName, flight, travelType, maxPeople, reserved=0):
        self.travelCode = travelCode
        self.cityName = cityName
        self.flight = flight
        self.travelType = travelType
        self.maxPeople = maxPeople
        self.reserved = 0

    def __str__(self):
        if self.travelType == Travel.INDIVIDUAL:
            return "{0: <6}         {1: <4}        {2: <5}   {3: <6}   {4: <3}명   {5: <2}명".format(self.travelCode, self.cityName, self.flight, "개별자유여행", self.maxPeople, self.reserved)
        else:
            return "{0: <6}         {1: <4}        {2: <5}   {3: <6}   {4: <3}명   {5: <2}명".format(self.travelCode, self.cityName, self.flight, "패키지여행", self.maxPeople, self.reserved)


########################################################################
travels = [Travel("TRV001", "뮌헨   ", "독일항공 ", Travel.INDIVIDUAL, 10),
           Travel("TRV002", "프라하 ", "에어프랑스", Travel.INDIVIDUAL, 20),
           Travel("TRV003", "LA     ", "델타항공 ", Travel.PACKAGE, 12),
           Travel("TRV004", "후쿠오카", "대한항공 ", Travel.INDIVIDUAL, 15),
           Travel("TRV005", "상해   ", "남방항공 ", Travel.PACKAGE, 10)]
########################################################################


class TravelBiz:
    def __init__(self, travels):  # travels 리스트 객체
        self.travels = travels

    def printAllTravels(self):  # 모든 여행 정보 출력 메소드
        for t in self.travels:
            print(t)

    def printIndividyalTravels(self):  # 개인 여행 정보 출력
        for t in self.travels:
            if t.travelType == Travel.INDIVIDUAL:
                print(t)

    def printPackageTravels(self):  # 패키지 여행 정보 출력
        for t in self.travels:
            if t.travelType == Travel.PACKAGE:
                print(t)

    def reserveTravels(self, travelCode, reserveCount):  # 여행 예약
        reservedTravel = None
        for t in self.travels:
            if t.travelCode == travelCode:
                if (t.maxPeople - t.reserved) >= reserveCount:
                    t.reserved += reserveCount
                    reservedTravel = t
                    print("예약이 완료 되었습니다.")
                else:
                    print("예약 가능 인원이 초과되었습니다. (예약 가능 인원 : {0}명".format(
                        t.maxPeople - t.reserved))
        return reservedTravel

    @staticmethod
    def printTravelListTitle():
        print("----------------------------------------------------------------------------------")
        print(" 여행코드\t도시명\t       항공편\t    여행유형\t최대예약가능인원\t예약")
        print("----------------------------------------------------------------------------------")

    @staticmethod
    def printMenu():  # 메뉴출력
        print("======= < 메뉴 > =======")
        print("1. 전체 여행 상품 조회")
        print("2. 개별 자유여행 상품 조회")
        print("3. 패키지여행 상품 조회")
        print("4. 여행 상품 예약")
        print("9. 종료")
        print("========================")

    @staticmethod
    def getMenuInput():
        return input(" ")

    # @staticmethod
    # def getMenuInput() :
    #     return int(input("## 메뉴 입력 :"))


biz = TravelBiz(travels)
print("Welcome~ 안녕하세요~ 000 여행사입니다.")

while True:
    TravelBiz.printMenu()
    print("## 메뉴 입력 :")
    menu = int(TravelBiz.getMenuInput())
    if menu == 9:
        print("프로그램을 종료합니다. Bye~ Bye~")
        break
    elif menu == 1:
        TravelBiz.printTravelListTitle()
        biz.printAllTravels()
        print("----------------------------------------------------------------------------------")
    elif menu == 2:
        TravelBiz.printTravelListTitle()
        biz.printIndividyalTravels()
        print("----------------------------------------------------------------------------------")
    elif menu == 3:
        TravelBiz.printTravelListTitle()
        biz.printPackageTravels()
        print("----------------------------------------------------------------------------------")
    elif menu == 4:
        print("여행 상품을 예약합니다.")
        print("여행 코드 입력", end=" ")
        tCode = biz.getMenuInput()
        print("여행 인원 입력:", end=" ")
        tCount = int(biz.getMenuInput())
        reserved = biz.reserveTravels(tCode, tCount)
        if reserved:
            TravelBiz.printTravelListTitle()
            print(reserved)
            print(
                "----------------------------------------------------------------------------------")
    else:
        print("메뉴를 잘못 입력하였습니다.")
        break
