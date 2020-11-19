#Constructor with Super Method or Call Parent Class Constructor in Child Class in Python
class Father:
    def __init__(self):
        print("Father class constructor.")
    def show(self):
        print("Father class instance method.")
class Son(Father):
    def __init__(self):
        super().__init__()               #calling parent class constructor
        print("Son class constructor.")
    def display(self):
        print("Son class instance method.")
object = Son()
object.display()