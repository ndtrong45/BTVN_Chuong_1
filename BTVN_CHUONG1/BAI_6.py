class Stack:
    def __init__(self, ngan_xep):
        self.ngan_xep = ngan_xep  
        self.data = []  

    def __del__(self):
        self.data.clear()  

    def push(self, value):
        if self.isFull():
            print("Ngăn xếp đã đầy! Không thể thêm phần tử.")
        else:
            self.data.append(value)  

    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp rỗng! Không thể lấy phần tử.")
            return None  
        else:
            return self.data.pop()  

    def isEmpty(self):
        return len(self.data) == 0

    def isFull(self):
         return len(self.data) >= self.ngan_xep

    def count(self):
        return len(self.data)

    def print_stack(self):
        if self.isEmpty():
            print("Ngăn xếp rỗng!")
        else:
            print("Nội dung của ngăn xếp:")
            for i in reversed(self.data):
                print(i)


stack = int(input("Nhập dung lượng của ngăn xếp: "))
s= Stack(stack)

s.push(1.5)
s.push(2.5)
s.push(3.5)

print(s.print_stack())
print("Phần tử lấy ra:", s.pop())  
print("Ngăn xếp đã trống chưa ?", s.isEmpty()) 
print("Ngăn xếp đã đầy chưa ?", s.isFull())  