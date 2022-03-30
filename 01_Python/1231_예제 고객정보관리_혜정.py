class Customer_Info:

    customers = [['Lee', '28', '010-5678-1234'],
                 ['Park', '31', '010-4567-9876'],
                 ['Choi', '25', '010-1111-2222']]

    def __init__(self, customer=customers):
        self.customer = customer

    @staticmethod
    def printMenu():
        print("=== << 고객 관리 프로그램 >> ===")
        print("1. 전체 고객 정보 조회")
        print("2. 고객 정보 추가")
        print("3. 고객 정보 삭제")
        print("9. 종료")
        print("================================")

    @staticmethod
    def add_info():
        print("================================")
        print("새로운 고객정보를 추가합니다")
        print("새로운 고객의 정보를 입력하세요")
        print("================================")

    @staticmethod
    def del_info():
        print("================================")
        print("고객의 정보를 삭제합니다.")
        print("삭제할 고객의 번호를 입력하세요.")
        print("================================")

    def new(self):
        n = input("이름 :")
        ag = input("나이 :")
        num = input("전화번호 :")
        print("@고객 정보를 추가하였습니다.")

        lst = [n, ag, num]
        self.customer.append(lst)

#     def delete(self):
#         del_num = int(input("번호 :"))
#         self.customer.remove(self.customer[del_num-1])

    def delete(self):
        del_num = int(input("번호 :"))
        del self.customer[del_num-1]
        print('@', del_num, '번 고객 정보를 삭제하였습니다.')

    def tue(self):
        for i in range(len(self.customer)):
            customer_form = '{0}. [이름] {1}   [나이] {2}   [전화번호] {3}'.format(
                i+1, self.customer[i][0], self.customer[i][1], self.customer[i][2])
            print(customer_form)


c_info = Customer_Info()

while 1:
    c_info.printMenu()
    Menu_input = int(input("## 메뉴 입력 :"))
    if Menu_input == 1:
        c_info.tue()
    elif Menu_input == 2:
        c_info.add_info()
        c_info.new()
    elif Menu_input == 3:
        c_info.del_info()
        c_info.delete()
    elif Menu_input == 9:
        print("프로그램을 종료합니다.")
        break
