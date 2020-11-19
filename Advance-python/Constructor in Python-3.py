class Color:
    def __init__(self,color1,color2="green"):
        self.color1 = color1
        self.color2 = color2
    def show(self,car):
        vechile = car
        print("this is",self.color1,vechile)
        print("this is ",self.color2,vechile)
object = Color("Red")
object.show("Car")
object2 =Color('yellow',color2='blue')
object2.show("car")