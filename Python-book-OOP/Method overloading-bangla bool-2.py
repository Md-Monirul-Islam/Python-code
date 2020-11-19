class My_num:
    def __init__(self,value):
        self.__value = value
    def __int__(self):
        return self.__value
    def __add__(self, other):
        return self.__value+int(other)*int(other)

a=2
b=3
c=a+b
print(c)