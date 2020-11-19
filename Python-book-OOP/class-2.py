class MyClass(object):
    def setAge(self, num):
        self.num = num

    def getAge(self):
        return self.num


zack = MyClass()
zack.setAge(45)
print(zack.getAge())

zack.setAge("\"Fourty Five\"")
print(zack.getAge())