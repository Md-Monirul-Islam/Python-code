#Constructor with Super Method or Call Parent Class Constructor in Child Class in Python
class Father:
    def __init__(self,money):
        self.money = money
        print("Father class constructor.")
    def show(self):
        print("Father class instance method.")
class Son(Father):
    def __init__(self,money,job):
        super().__init__(money)           #calling parent class constructor
        self.job = job
        print("Son class constructor.")
    def display(self):
        print("Son class instance method.",self.money,"\nJob->>",self.job)
object = Son(20300,"Python")
object.display()