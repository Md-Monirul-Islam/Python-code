class My_num:
    def __init__(self,value):
        self.value = value

    def __add__(self, other):
        return (self.value*2)+(other.value*2)
a=My_num(2)
b=My_num(3)
c=a+b
print(c)