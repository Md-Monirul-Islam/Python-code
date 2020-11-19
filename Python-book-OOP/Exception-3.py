class NegativeNumberException(RuntimeError):
    def __init__(self,age):
        super().__init__()
        self.age = age

#from NegativeNumberException import NegativeNumberException
import sys
def enterAge(age):
    if age < 0:
        raise NegativeNumberException('Only positive integer number are allowed.')
    if age % 2 ==0:
        print('The number is even.')
    else:
        print('The number is odd.')

try:
    num = int(input('enter your age :'))
    enterAge(num)
    sys.exit()
except NegativeNumberException:
    print('Only positive integer number are allowed.')
#except:
   # print('Something was woring.')