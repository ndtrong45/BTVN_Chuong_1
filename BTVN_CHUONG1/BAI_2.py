class TS:
    def __init__(self, ho_ten='', diem_toan=0.0, diem_ly=0.0, diem_hoa=0.0):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

    def nhap_thong_tin(self):
        self.ho_ten = input("Nhập họ và tên thí sinh: ")
        self.diem_toan = float(input("Nhập điểm toán: "))
        self.diem_ly = float(input("Nhập điểm lý: "))
        self.diem_hoa = float(input("Nhập điểm hóa: "))

    def in_thong_tin(self):
        print(f"Họ và tên thí sinh: {self.ho_ten}")
        print(f"Tổng điểm: {self.tong_diem()}")

def sap_xep_theo_diem(danh_sach_thi_sinh):
    return sorted(danh_sach_thi_sinh, key=lambda ts: ts.tong_diem(), reverse=True)

so_luong_thi_sinh = int(input("Nhập số lượng thí sinh: "))

danh_sach = []
for i in range(so_luong_thi_sinh):
    thi_sinh = TS()  
    thi_sinh.nhap_thong_tin()  
    danh_sach.append(thi_sinh)  

danh_sach_sap_xep = sap_xep_theo_diem(danh_sach)

print("Danh sách thí sinh trúng tuyển:")
for thi_sinh in danh_sach_sap_xep:
    if thi_sinh.tong_diem() >= 20:
        thi_sinh.in_thong_tin()
