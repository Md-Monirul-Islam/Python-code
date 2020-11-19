#with parameter
class Father:
    def __init__(self,money):
        self.money = money
        print("Father class constructor.")
    def show(self):
        print("Faather class instance method.")
class Son(Father):
    def __init__(self,salary):
        self.money = salary
        self.car = "BMW"
        print("Son class constructor.")
    def display(self):
        print("Son class instance mehtod.")
object = Son(320000)
object.show()
print(object.money)
object.display()
print(object.car)
object2 = Father(1000000)
print(object2.money)
