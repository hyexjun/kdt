class Book:                           # 클래스 정의

    def __init__(self, title, price):  # 멤버변수(인스턴스변수) 선언 및 초기화
        self.title = title
        self.price = price

    def __str__(self):                # Book클래스로부터 생성된 객체의 상태를 표현하는 문자열 리턴
        pass


class Magazine(Book):  # 클래스 정의

    def __init__(self, title, price, category, description):  # 멤버변수(인스턴스변수) 선언 및 초기화
        super().__init__(title, price)
        self.category = category
        self.description = description

    def __str__(self):                # Magazine클래스로부터 생성된 객체의 상태를 표현하는 문자열 리턴
        return "[제목]{0:<15}   [분류]{1:<15}    [가격] {2:>5}   [비고]{3:<15}".format(self.title, self.category, self.price, self.description)


class Novel(Book):

    def __init__(self, title, price, author):  # 멤버변수(인스턴스변수) 선언 및 초기화
        super().__init__(title, price)
        self.author = author

    def __str__(self):                # Novel클래스로부터 생성된 객체의 상태를 표현하는 문자열 리턴
        return "[제목]{0:<15}   [저자]{1:<15}    [가격] {2:>5} ".format(self.title, self.author, self.price)


class BookBiz:

    def __init__(self, magazines, novels):  # 멤버변수(인스턴스변수) 선언 및 초기화
        magazines.extend(novels)
        self.books = magazines

    def printAllBooks(self):          # 모든 도서 정보 출력하는 메소드
        for idx, bk in enumerate(self.books):
            print("{0}.{1}".format(idx+1, bk))

    def printAllMagazines(self):      # 도서중 잡지만 출력하는 메소드
        for idx, bk in enumerate(self.books):
            if isinstance(bk, Magazine):
                print("{0}.{1}".format(idx+1, bk))

    def printAllNovels(self):         # 도서중 소설만 출력하는 메소드
        idx = 1
        for bk in self.books:
            if isinstance(bk, Novel):
                print("{0}.{1}".format(idx, bk))
                idx += 1

    def printMagazineOneYearSubscription(self):  # 잡지의 1년 구독료를 출력하는 메소드
        idx = 1
        for bk in self.books:
            if isinstance(bk, Magazine):
                print("{0}.{1}:{2}원".format(idx, bk.title,
                      self.calculateOneYearSubscriptionPrice(bk.price)))
                idx += 1

    def searchNovelByAuthor(self, author):      # 소설중 작가로 검색된 소설객체를 출력하는 메소드
        idx = 1
        for bk in self.books:
            if isinstance(bk, Novel) and bk.author == author:
                print("{0}.{1}".format(idx, bk))
                idx += 1

    # 소설중 최대가격과 최소가격사이의 소설 검색 후 결과를 출력하는 메소드
    def searchNovelByPrice(self, minPrice, maxPrice):
        idx = 1
        for bk in self.books:
            if isinstance(bk, Novel) and bk.price >= minPrice and bk.price <= maxPrice:
                print("{0}.{1}".format(idx, bk))
                idx += 1

    # 잡지의 가격을 파라미터로 받아서 1년 구독료 계산해서 리턴하는 메소드
    def calculateOneYearSubscriptionPrice(self, price):
        return price * 12

    @staticmethod
    def getUserInput():               # 사용자로부터 키보드 입력을 받아서 리턴하는 메소드
        return input('')

    @staticmethod
    def printHead():                  # 도서정보 출력할때 heading만 출력하는 메소드
        print("-------------------------------------도서 정보 -------------------------------------------")

    @staticmethod
    def printTail():                  # 모든 도서정보 출력후 밑줄 출력하는 메소드
        print("------------------------------------------------------------------------------------------")

    @staticmethod
    def printMenu():                  # 메뉴 출력하는 메소드
        print("==== << 도서 정보 프로그램 >> ====")
        print("1. 전체 도서 정보 조회 ")
        print("2. 전체 잡지 조회 ")
        print("3. 전체 소설 조회")
        print("4. 잡지 연간 구독료 조회 ")
        print("5. 소설 저자명 검색 ")
        print("6. 소설 가격 검색 (최소값 ~ 최대값)")
        print("9. 시스템 종료 ")
        print("==================================")


# 객체 생성하고 메서드 호출하는 실행코드 (Sample Run 참고)

magazines = [Magazine('Cooking Light', 15000, "living, cooking", "America Cooking"),
             Magazine('Auto Bild', 16000, 'science, car', 'Germany Car')]
novels = [Novel('The Confession', 10500, 'Grisham, John'),
          Novel('Les Miserables', 17500, 'Hugo, Victor'),
          Novel('Breakthrough', 47200, 'Ifill, Gwen'),
          Novel('The Racketeer', 38000, 'Grisham, John')]


biz = BookBiz(magazines, novels)

while True:
    BookBiz.printMenu()
    print("## 메뉴 입력:", end=" ")
    menu = int(biz.getUserInput())
    if menu == 9:
        print("=================================")
        print("프로그램을 종료합니다. Bye~ Bye~")
        print("=================================")
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
        print("------------------------------.")
        biz.printMagazineOneYearSubscription()
        print("------------------------------.")
    elif menu == 5:
        print("검색할 저자명을 입력하세요 : ", end=" ")
        author = biz.getUserInput()
        BookBiz.printHead()
        biz.searchNovelByAuthor(author)
        BookBiz.printTail()
    elif menu == 6:
        print("검색할 소설 가격의 최소값을 입력하세요 : ", end=" ")
        minPrice = int(biz.getUserInput())
        print("검색할 소설 가격의 최대값을 입력하세요 : ", end=" ")
        maxPrice = int(biz.getUserInput())
        BookBiz.printHead()
        biz.searchNovelByPrice(minPrice, maxPrice)
        BookBiz.printTail()
