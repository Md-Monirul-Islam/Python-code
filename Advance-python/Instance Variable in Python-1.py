class Color:
    def __init__(self):
        self.color = "Green"  # instance variable
    def show(self):    # instance method
        print("This is",self.color)    # accessing instance variable
object = Color()
object.show()
object1 = Color()
object1.show()
print(object.color)