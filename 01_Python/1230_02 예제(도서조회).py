class Book:

    def __init__(self, title, category, writer, price=0, etc):
        self.title = title
        self.category = category
        self.writer = writer
        self.price = price
        self.etc = etc

    def __str__(self):
        if self.category == Book.category:
            return "[제목]{0: <6} [분류]{1: <4} {2: <5} [가격]{3: <6} [비고]{4: <3}".format(self.title, self.category, self.writer, self.price, self.etc)
        elif self.writer == Book.writer:
            return "[제목]{0: <6} {1: <4} [저자]{2: <5} [가격]{3: <6} {4: <3}".format(self.title, self.category, self.writer, self.price, self.etc)


class BookBiz:
    def __init__(self, Books):  # Books 리스트 객체
        self.Books = Books

    def printAllBooks(self):  # 모든 도서 정보 출력 메소드
        for b in self.Books:
            print(b)

    def printcategoryBooks(self):  # 잡지 정보 출력
        for b in self.Books:
            if b.category == Book.category:
                print(b)

    def printwriterBooks(self):  # 소설 여행 정보 출력
        for b in self.Books:
            if b.writer == Book.writer:
                print(b)

    def searchwriterBooks(self):  # 저자 검색 기능
        x = input("> 검색할 저자명을 입력하세요. :")
        if x in self.writer:

    def searchpriceBooks(self):  # 가격 검색 기능

    @staticmethod
    def printBookListTitle():
        print("--------------------------------도서 정보----------------------------------")

    @staticmethod
    def printMenu():  # 메뉴 출력
        print("====<< 도서 정보 프로그램 >>====")
        print("1. 전체 도서 정보 조회")
        print("2. 전체 잡지 조회")
        print("3. 전체 소설 조회")
        print("4. 잡지 연간 구독료 조회")
        print("5. 소설 저자명 검색")
        print("6. 소설 가격 검색 (최소값~최대값")
        print("9. 시스템 종료")
        print("===============================")

    @staticmethod
    def getMenuInput():
        return input(" ")

    # @staticmethod
    # def getMenuInput() :
    #     return int(input("## 메뉴 입력 :"))


########################################################################
Books = [Book("Cooking Light", "livig, cooking", "", 15000, "America Cooking"),
         Book("Auto Bild", "science, car", "", 16000, "Germany Car"),
         Book("The Confession", "", "Grisham, John", 10500, ""),
         Book("Les Miserables", "", "Hugo, Victor", 17500, ""),
         Book("Breakthrough", "", "Ifill, Gwen", 47200, ""),
         Book("The Racketeer", "", "Grisham, John", 38000, "")]
########################################################################

biz = BookBiz(Books)
while True:
    BookBiz.printMenu()
    print("## 메뉴 입력 :")
    menu = int(BookBiz.getMenuInput())
    if menu == 9:
        print("프로그램을 종료합니다. Bye~ Bye~")
        break
    elif menu == 1:
        BookBiz.printBookListTitle()
        biz.printAllBooks()
        print("--------------------------------------------------------------------------")
    elif menu == 2:
        BookBiz.printBookListTitle()
        biz.printcategoryBooks()
        print("--------------------------------------------------------------------------")
    elif menu == 3:
        BookBiz.printBookListTitle()
        biz.printwriterBooks()
        print("--------------------------------------------------------------------------")
    elif menu == 4:
        print("---------------------------")
        print("1. Cooking Light : 180000원")
        print("2. Auto Bild : 192000원")
        print("---------------------------")
    elif menu == 5:
        BookBiz.printBookListTitle()
        biz.searchwriterBooks()
        print("--------------------------------------------------------------------------")
    elif menu == 6:
        BookBiz.printBookListTitle()
        biz.searchpriceBooks()
        print("--------------------------------------------------------------------------")
    else:
        print("메뉴를 잘못 입력하였습니다.")
        break
