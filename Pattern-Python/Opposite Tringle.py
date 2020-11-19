num = int(input('Please enter the num of row:'))
for i in range(num,0,-1):
    for j in range(0,i):
        print('*',end=' ')
    print()