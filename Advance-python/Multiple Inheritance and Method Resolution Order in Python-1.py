class Father:
    def showF(self):
        print("Father class method.")
class Mother:
    def showM(self):
        print("Mother class method.")
class Son(Father,Mother):
    def showS(self):
        print("Son class method.")
boy = Son()
boy.showS()
boy.showF()
boy.showM()