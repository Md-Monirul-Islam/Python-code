class Father:
    def __init__(self):
        print("Father class constructor.")
    def showF(self):
        print("Father class instance method.")

class Son(Father):
    def __init__(self):
        super().__init__() #calling parent(Father) class constructor.
        print("Son class constructor.")
    def showS(self):
        print("Son class instance method.")
class Daugther(Father):
    def __init__(self):
        super(Daugther, self).__init__()
        print("Daugther class constructor.")
    def showD(self):
        print("Dauther class instance method.")
object = Son()
object2 = Daugther()