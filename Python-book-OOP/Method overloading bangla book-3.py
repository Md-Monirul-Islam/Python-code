class MyInt():
    def __init__(self, value):
        self.__value = value

    def __int__(self):
        return self.__value


    def __iadd__(self, other):
        return self.__value + int(other) * int(other)


a = MyInt(2)

a += MyInt(3)

print(a)