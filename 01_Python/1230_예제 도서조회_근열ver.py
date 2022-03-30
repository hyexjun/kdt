###############도서정보 조회 workshop###########################
# 클래스 정의
class Book:
    def __init__(self, title, price):
        # 멤버변수(인스턴스변수) 선언 및 초기화
        self.title = title
        self.price = price

    def __str__(self):
        # Book클래스로부터 생성된 객체의 상태를 표현하는 문자열 리턴
        pass


# 클래스 정의
class Magazine(Book):
    def __init__(self, title, category, price, description):
        # 멤버변수(인스턴스변수) 선언 및 초기화
        super().__init__(title, price)
        self.category = category
        self.description = description

    def __str__(self):
        # Magazine클래스로부터 생성된 객체의 상태를 표현하는 문자열 리턴
        return "[제목]{0:<15}   [분류]{1:<15}    [가격] {2:>5}   [비고]{3:<15}".format(self.title, self.category, self.price, self.description)


# 클래스 정의
class Novel(Book):
    def __init__(self, title, price, author):
        # 멤버변수(인스턴스변수) 선언 및 초기화
        super().__init__(title, price)
        self.author = author

    def __str__(self):
        # Novel클래스로부터 생성된 객체의 상태를 표현하는 문자열 리턴
        return "[제목]{0:<15}   [저자]{1:<15}    [가격] {2:>5} ".format(self.title, self.author, self.price)

# 클래스 정의


class BookBiz:
    def __init__(self, magazines, novels):
        self.magazines = magazines
        self.novels = novels

    def printAllBooks(self):
        # 모든 도서 정보 출력하는 메서드
        cnt = 1
        for m in self.magazines:
            print("{0}. {1}".format(cnt, m))
            cnt += 1
        for n in novels:
            print("{0}. {1}".format(cnt, n))
            cnt += 1

    def printAllMagazines(self):
        # 도서중 잡지만 출력하는 메서드
        cnt = 1
        for m in self.magazines:
            print("{0}. {1}".format(cnt, m))
            cnt += 1

    def printAllNovels(self):
        # 도서중 소설만 출력하는 메서드
        cnt = 1
        for n in self.novels:
            print("{0}. {1}".format(cnt, n))
            cnt += 1

    def printMagazineOneYearSubscription(self):
        # 잡지의 1년 구독료를 출력하는 메서드
        cnt = 1
        for i in self.magazines:
            if isinstance(i, Magazine):
                print("{0}. {1} : {2}원".format(cnt, i.title,
                      self.calculateOneYearSubscriptionPrice(i.price)))
                cnt += 1

    def searchNovelByAuthor(self, author):
        # 소설중 작가로 검색된 소설객체를 리턴하는 메서드
        cnt = 1
        for n in self.novels:
            if n.author == author:
                print("{0}. {1}".format(cnt, n))

    def searchNovelByPrice(self, minPrice, maxPrice):
        # 소설중 최대가격과 최소가격사이의 소설 검색 후 결과를 리턴하는 메서드
        cnt = 1
        for i in self.novels:
            if int(i.price) >= int(minPrice) and int(i.price) <= int(maxPrice):
                print("{0}. {1}".format(cnt, i))

    def calculateOneYearSubscriptionPrice(self, price):
        # 잡지의 가격을 파라미터로 받아서 1년 구독료 계산해서 리턴하는 메서드
        return price * 12

    @staticmethod
    def getUserInput():
        # 사용자로부터 키보드 입력을 받아서 리턴하는 메서드
        return input(" ")

    @staticmethod
    def printHead():
        # 도서정보 출력할때 heading만 출력하는 메서드
        print("---------------------------- 도서 정보 ------------------------")

    @staticmethod
    def printTail():
        # 모든 도서정보 출력후 밑줄 출력하는 메서드
        print("--------------------------------------------------------------")

    @staticmethod
    def printMenu():
        # 메뉴 출력하는 메서드
        print("=== << 도서 정보 프로그램 >> ===")
        print("1. 전체 도서 정보 조회")
        print("2. 전체 잡지 조회")
        print("3. 전체 소설 조회")
        print("4. 잡지 연간 구독료 조회")
        print("5. 소설 저자명 검색")
        print("6. 소설 가격 검색 (최소값 ~ 최대값)")
        print("9. 시스템 종료")
        print("==============================")


################################################################################
magazines = [
    Magazine("Cooking Light", "Living, cooking", 15000, "America Cooking"),
    Magazine("Auto Bild    ", "science, car   ", 16000, "Germany Car")
]

novels = [
    Novel("The Confession", 10500, "Grisham, John"),
    Novel("Les Miserables", 17500, "Hugo, Victor "),
    Novel("Breakthrough  ", 47200, "Ifill, Gwen  "),
    Novel("The Racketeer ", 38000, "Grisham, John")
]
################################################################################

# 객체 생성하고 메서드 호출하는 실행코드(Sample Run 참고)
biz = BookBiz(magazines, novels)
while True:
    BookBiz.printMenu()
    print("##메뉴 입력 :")
    menu = int(BookBiz.getUserInput())
    if menu == 9:
        print("프로그램을 종료합니다. Bye~")
        break
    elif menu == 1:
        BookBiz.printHead()
        biz.printAllBooks()
        BookBiz.printTail()
    elif menu == 2:
        BookBiz.printHead()
        biz.printAllMagazines()
        BookBiz.printTail()
    elif menu == 3:
        BookBiz.printHead()
        biz.printAllNovels()
        BookBiz.printTail()
    elif menu == 4:
        print("-------------------------")
        biz.printMagazineOneYearSubscription()
        print("-------------------------")
    elif menu == 5:
        print("검색할 저자명을 입력하세요 :")
        author = biz.getUserInput()
        BookBiz.printHead()
        biz.searchNovelByAuthor(author)
        BookBiz.printTail()
    elif menu == 6:
        print(">검색할 소설 가격의 최소값을 입력하세요 :")
        minPrice = biz.getUserInput()
        print(">검색할 소설 가격의 최대값을 입력하세요 :")
        maxPrice = biz.getUserInput()
        BookBiz.printHead()
        biz.searchNovelByPrice(minPrice, maxPrice)
        BookBiz.printTail()
