def enterAge(age):
    if age<0:
        raise ValueError('only positive number is allowed.')
    if age % 2 == 0:
        print('the number is even.')
    else:
        print('the number is odd.')

try:
    num = int(input('enter your age :'))
    print('enterAge(num)')
except ValueError:
    print('only positive number is allowed.')



