class A:
    def __init__(self,x):
        self.x = x
    def __add__(self, other):
        return self.x + other.x
class B:
    def __init__(self,x):
        self.x = x
a = A(10)
b = B(20)
print(a+b)  # A.__add__(a,b) ,,,, int.__add__(a,b),,,str__add__("a","b")
print(dir(int))