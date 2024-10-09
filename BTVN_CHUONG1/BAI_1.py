class hinh_chu_nhat:
    def __init__(self, chieu_dai, chieu_rong): 
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def chu_vi(self): 
        return (self.chieu_dai + self.chieu_rong) * 2
    
    def dien_tich(self): 
        return self.chieu_dai * self.chieu_rong
    
    def in_thong_tin(self):
        print(f"Chiều dài của hình chữ nhật là: {self.chieu_dai}")
        print(f"Chiều rộng của hình chữ nhật là: {self.chieu_rong}")
        print(f"Chu vi hình chữ nhật là: {self.chu_vi()}")
        print(f"Diện tích hình chữ nhật là: {self.dien_tich()}")

chieu_dai = float(input("Nhập chiều dài hình chữ nhật: "))
chieu_rong = float(input("Nhập chiều rộng hình chữ nhật: "))
hcn = hinh_chu_nhat(chieu_dai,chieu_rong)
hcn.in_thong_tin()