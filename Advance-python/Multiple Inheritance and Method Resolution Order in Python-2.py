class Father:
    def __init__(self):
        super(Father, self).__init__()  #callin parent call constructor
        print("Father class constructor.")
    def showF(self):
        print("Father class method.")
class Mother:
    def __init__(self):
        super(Mother, self).__init__()   #calling parent class constructor
        print("Mother class constructor.")
    def showM(self):
        print("Mother class method.")
class Son(Father,Mother):
    def __init__(self):
        super(Son, self).__init__()  #calling parent class constructor
        print("Son class constructor.")
    def showS(self):
        print("Son class method.")
boy = Son()