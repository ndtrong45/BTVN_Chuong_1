import math

class TamGiac:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def kiem_tra_ton_tai(self):
        return (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a)

    def tinh_chu_vi(self):
        if self.kiem_tra_ton_tai():
            return self.a + self.b + self.c
        else:
            return 0

    def tinh_dien_tich(self):
        if self.kiem_tra_ton_tai():
            p = (self.a + self.b + self.c) / 2
            return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        else:
            return 0

class TamGiacCan(TamGiac):
    pass

class TamGiacDeu(TamGiacCan):
    pass

class TamGiacVuong(TamGiac):
    def la_tam_giac_vuong(self):
        return self.a**2 + self.b**2 == self.c**2 or self.a**2 + self.c**2 == self.b**2 or self.b**2 + self.c**2 == self.a**2

tam_giac_deu = TamGiacDeu(5, 5, 5)
print("Diện tích tam giác đều:", tam_giac_deu.tinh_dien_tich())

tam_giac_vuong = TamGiacVuong(3, 4, 5)
print("Tam giác có phải là tam giác vuông không ?", tam_giac_vuong.la_tam_giac_vuong())