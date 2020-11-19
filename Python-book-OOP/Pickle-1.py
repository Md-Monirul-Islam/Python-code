import  pickle

class Animal:
    def __init__(self,number_of_legs,color):
        self.number_of_legs = number_of_legs
        self.color = color
class Cat(Animal):
    def __init__(self,color):
        Animal.__init__(self,4,'black')

pussy = Cat('black')

print(str.format('my pussy color is {0} and {1} legs',pussy.color,pussy.number_of_legs))

pickle_pussy = pickle.dumps(pussy)
print('would like to see her pickled? Here is!')
print(pickle_pussy)


binary_file = open('my_pickled_Pussy.bin', mode='wb')
my_pickled_Pussy = pickle.dump(pussy, binary_file)
binary_file.close()