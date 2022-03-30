class Book:
    book_list0 = [["[제목]Cooking Light      ", "[분류]living, cooking", 15000, "[비고]America Cooking"],
                  ["[제목]Auto Bild          ", "[분류]science, car   ",
                      16000, "[비고]Germany Car    "],
                  ["[제목]The Confession     ", "[저자]Grisham, John  ",
                      10500, "                     "],
                  ["[제목]Les Miserables     ", "[저자]Hugo, Victor   ",
                      17500, "                     "],
                  ["[제목]Breakthrough       ", "[저자]Ifill, Gwen    ",
                      47200, "                     "],
                  ["[제목]The Racketeer      ", "[저자]Grisham, John  ", 38000, "                     "]]

    def __init__(self, book_list0):
        self.book_list = book_list0

    @staticmethod
    def getMenu():
        print("=== << 도서 정보 프로그램 >> ===\n1.전체 도서 정보 조회\n2.전체 잡지 조회\n3.전체 소설 조회\n4.잡지 연간 구독료 조회\n5.소설 저자명 검색\n6.소설 가격 검색 (최소값 ~ 최대값)\n9.종료\n================================")

    @staticmethod
    def getUserInput():
        return int(input("## 메뉴 입력:"))

    def Book_info(self):  # 1. 전체 도서 정보 조회
        for i in self.book_list:
            box = []
            for j in range(4):
                box.append(i[j])
            box[2] = str(box[2])
            box[2] = "[가격]" + box[2]
            print("           ".join(map(str, box)))

    def Book_magazine_serch(self):  # 2. 전체 잡지 조회
        for i2 in self.book_list:
            if "[분류]" in i2[1]:
                i2[2] = str(i2[2])
                i2[2] = "[가격]" + i2[2]
                print("           ".join(map(str, i2)))

    def Book_novel_serch(self):  # 3. 전체 소설 조회
        for i3 in self.book_list:
            if "[저자]" in i3[1]:
                i3[2] = str(i3[2])
                i3[2] = "[가격]" + i3[2]
                print("".join(map(str, i3)))

    def subscription_12year(self):  # 4. 잡지 연간 구독료 조회

        print("1.Cooking Light:{}".format(self.book_list[0][2]*12))
        print("2.Auto Bild:{}".format(self.book_list[1][2]*12))

    def novel_writer_serch(self):
        writer = input("검색할 저자명을 입력하세요:")
        for i5 in self.book_list:
            if writer in i5[1]:
                i5[2] = str(i5[2])
                i5[2] = "[가격]" + i5[2]
                print("".join(map(str, i5)))

    def min_max(self):
        minn_ = input("검색할 소설 가격의 최소값을 입력하세요:")
        maxx_ = input("검색할 소설 가격의 최대값을 입력하세요:")
        for i6 in self.book_list:
            if "[저자]" in i6[1]:
                if int(minn_) <= i6[2] <= int(maxx_):
                    i6[2] = str(i6[2])
                    i6[2] = "[가격]" + i6[2]
                    print("      ".join(i6))


while True:
    a = Book()
    a.getMenu()
    menu = a.getUserInput()
    if menu == 1:
        a.Book_info()
    elif menu == 2:
        a.Book_magazine_serch()
    elif menu == 3:
        a.Book_novel_serch()
    elif menu == 4:
        a.subscription_12year()
    elif menu == 5:
        a.novel_writer_serch()
    elif menu == 6:
        a.min_max()
    else:
        print("Bye~Bye~")
        break
