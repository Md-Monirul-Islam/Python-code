#Constructor with Super Method or Call Parent Class Constructor in Child Class in Python
class Father:
    def __init__(self,money):
        self.money = money
        print("Father class constructor.")
    def show(self):
        print("Father class instance method.")
class Son(Father):
    def __init__(self,money):
        super().__init__(money)               #calling parent class constructor
        print("Son class constructor.")
    def display(self):
        print("Son class instance method.",self.money)
object = Son(20300)
object.display()