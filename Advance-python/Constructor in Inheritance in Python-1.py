class Fathe:
    def __init__(self,money):
        self.money = money
        print("Father class constructor.")
    def show(self):
        print("Father class instance method.")
class Son(Fathe):
    def display(self):
        print("Son class instance method.")

object = Son(10000)
object.show()
print(object.money)