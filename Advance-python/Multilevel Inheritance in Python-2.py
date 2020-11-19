class Father:
    def __init__(self):
        print("Father class constructor.")
    def showF(self):
        print("Father class method.")
class Son(Father):
    def __init__(self):
        super().__init__()    #calling parent(Father) class constructor.
        print("Son class constructor.")
    def showS(self):
        print("Son class method.")
class GrandSon(Son):
    def __init__(self):
        super().__init__()     #calling parent(Son) class constructor.
        print("GrandSon class constructor.")
    def showG(self):
        print("GrandSon class method.")
object = GrandSon()
#object.showF()
object.showS()