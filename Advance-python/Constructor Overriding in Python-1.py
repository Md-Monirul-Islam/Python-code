#without parameter
class Father:
    def __init__(self):
        self.money = 10000
        print("Father class constructor.")
    def show(self):
        print("Faather class instance method.")
class Son(Father):
    def __init__(self):
        self.money = 50000
        self.car = "BMW"
        print("Son class constructor.")
    def display(self):
        print("Son class instance mehtod.")
object = Son()
object.show()
print(object.money)
object.display()
print(object.car)
object2 = Father()
print(object2.money)
