num = int(input("entr the num of row"))
for i in range(0,num):
    for j in range(0,num-1-i):
        print(end=" ")
    for j in range(0,i+1):
        print('*',end=' ')
    print()