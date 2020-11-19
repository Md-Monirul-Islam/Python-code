class Father:
    def showF(self):
        print("Father class instance method.")

class Son(Father):
    def showS(self):
        print("Son class instance method.")
class Dauther(Father):
    def showD(self):
        print("Dauther class instance method.")
object = Dauther()
object.showD()

object2 = Son()
object2.showS()
object2.showF()