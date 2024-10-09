import math

class HinhChuNhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)

    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong

class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)

class HinhBinhHanh(HinhChuNhat):
    def __init__(self, canh_day, canh_ben, goc):
        super().__init__(canh_day, canh_ben)
        self.goc = goc  # Góc giữa hai cạnh bên (độ)

    def tinh_chieu_cao(self):
        return self.chieu_rong * math.sin(math.radians(self.goc))

    def tinh_dien_tich(self):
        return self.chieu_dai * self.tinh_chieu_cao()

class DaGiacHinhBinhHanh(HinhBinhHanh):
    pass

hinh_vuong = HinhVuong(5)
print("Chu vi hình vuông:", hinh_vuong.chu_vi())
print("Diện tích hình vuông:", hinh_vuong.dien_tich())

hinh_binh_hanh = HinhBinhHanh(10, 6, 60)
print("Chu vi hình bình hành:", hinh_binh_hanh.chu_vi())
print("Diện tích hình bình hành:", hinh_binh_hanh.dien_tich())