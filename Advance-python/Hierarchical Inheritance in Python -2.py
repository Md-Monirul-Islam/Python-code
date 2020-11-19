class Father:
    def __init__(self):
        print("Father class constructor.")
    def showF(self):
        print("Father class instance method.")

class Son(Father):
    def __init__(self):
        print("Son class constructor.")
    def showS(self):
        print("Son class instance method.")
class Daugther(Father):
    def __init__(self):
        print("Daugther class constructor.")
    def showD(self):
        print("Dauther class instance method.")
object = Daugther()
object.showD()

object2 = Son()
object2.showS()
object2.showF()