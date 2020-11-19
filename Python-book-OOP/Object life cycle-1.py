class sum_num:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a+self.b
obj_1 = sum_num(3,5)
print(obj_1.add())