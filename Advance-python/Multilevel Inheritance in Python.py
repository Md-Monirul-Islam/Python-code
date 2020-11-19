class Father:
    def showF(self):
        print("Father class method.")
class Son(Father):
    def showS(self):
        print("Son class method.")
class GrandSon(Son):
    def showG(self):
        print("GrandSon class method.")
object = GrandSon()
object.showF()