class Father:
    money = 10000 
    def show(self):
        print("Parents class instance method.")
    @classmethod
    def show_money(cls):
        print("Parents class method",cls.money)
    @staticmethod
    def star():
        age = 50
        print("Father's ages",age)

class Son(Father):
    def display(self):
        print("Child class instance method.")

object2 = Son()
object2.display()
object = Father()
object2.show()
object2.star()
print(object.money)