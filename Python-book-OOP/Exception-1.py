
import sys
print('exception error handling')
try:
    number = int(input('enter any number between 1 to 10: '))
except(ValueError):
    print('only for numbers')
    sys.exit()
print('you have enter a number :',number)

