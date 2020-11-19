class Rectangle(object):
    def __init__(self,length,weight):
        self.length = length
        self.weight = weight

    def calculate_area(self):
        return self.length*self.weight
    @classmethod
    def new_square(cls,side_length):
        return cls(side_length,side_length)

obj = Rectangle(4,5)
print(obj.calculate_area())

square = Rectangle.new_square(6)
print(square.calculate_area())
