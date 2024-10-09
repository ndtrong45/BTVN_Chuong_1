import math

class Diem:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class DuongTron(Diem):
    def __init__(self, x, y, ban_kinh):
        super().__init__(x, y)
        self.ban_kinh = ban_kinh

    def chu_vi(self):
        return 2 * math.pi * self.ban_kinh

    def dien_tich(self):
        return math.pi * self.ban_kinh**2

class Elip(DuongTron):
    def __init__(self, x, y, truc_lon, truc_be):
        super().__init__(x, y, truc_lon)
        self.truc_be = truc_be

    def tinh_dien_tich(self):
        return math.pi * self.truc_lon * self.truc_be

diem_A = Diem(2, 3)
duong_tron = DuongTron(0, 0, 5)
elip = Elip(1, 2, 4, 3)

print("Diện tích đường tròn:", duong_tron.dien_tich())
print("Diện tích elip:", elip.dien_tich())