class Date:
    def __init__(self, ngay=1, thang=1, nam=2000):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

    def display(self):
        print(f"{self.ngay:02}/{self.thang:02}/{self.nam}")

    def next(self):
        s = [31, 28 + (1 if self.is_leap_year() else 0), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.ngay += 1
        if self.ngay > s[self.thang - 1]:
            self.ngay = 1
            self.thang += 1
            if self.thang > 12:
                self.thang = 1
                self.nam += 1

    def is_leap_year(self):
        return (self.nam % 4 == 0 and self.nam % 100 != 0) or (self.nam % 400 == 0)


class Employee:
    def __init__(self, name, ngay_sinh, ngay_vao):
        self.name = name
        self.ngay_sinh = ngay_sinh  
        self.ngay_vao = ngay_vao   

    def display_info(self):
        print(f"Tên: {self.name}")
        print("Ngày sinh:", end=" ")
        self.ngay_sinh.display()
        print("Ngày vào công ty:", end=" ")
        self.ngay_vao.display()


class Company:
    def __init__(self):
        self.employees = []

    def them_nv(self, name, ngay_sinh, ngay_vao):
        nv_moi = Employee(name, ngay_sinh, ngay_vao)
        self.employees.append(nv_moi)

    def display_employees(self):
        for i in self.employees:
            i.display_info()
            print()



company = Company()

while True:
    print("1. Thêm nhân viên")
    print("2. Hiển thị danh sách nhân viên")
    print("3. Thoát")
    choice = input("Chọn một tùy chọn: ")

    if choice == '1':
        name = input("Nhập tên nhân viên: ")
        ngay = int(input("Nhập ngày sinh: "))
        thang = int(input("Nhập tháng sinh: "))
        nam = int(input("Nhập năm sinh: "))
        ngay_sinh = Date(ngay, thang, nam)

        ngay_vao = int(input("Nhập ngày vào công ty: "))
        thang_vao = int(input("Nhập tháng vào công ty: "))
        nam_vao = int(input("Nhập năm vào công ty: "))
        ngay_vao_ct = Date(ngay_vao, thang_vao, nam_vao)

        company.them_nv(name, ngay_sinh, ngay_vao_ct)

    elif choice == '2':
        print("Danh sách nhân viên:")
        company.display_employees()

    elif choice == '3':
        break

    else:
        print("Tùy chọn không hợp lệ. Vui lòng chọn lại.")
