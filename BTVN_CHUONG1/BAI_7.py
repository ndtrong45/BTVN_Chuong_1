class Date:
    def __init__(self, ngay=1, thang=10, nam=2024):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

    def display(self):
        print(f"Ngày: {self.ngay}/{self.thang}/{self.nam}")

    def next(self):

        s = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.nam % 4 == 0 and (self.nam % 100 != 0 or self.nam % 400 == 0):
            s[1] = 29  
        
        self.ngay += 1
        if self.ngay > s[self.thang - 1]:
            self.ngay = 1
            self.thang += 1
            if self.thang > 12:
                self.thang = 1
                self.nam += 1


ngay = Date(8, 10, 2024)
ngay.display()

ngay.next()
ngay.display()