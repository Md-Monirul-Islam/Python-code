n = int(input("enter the number of row : "))
for i in range(n):
    count = 0
    for j in range(n-i-1):
        print(" ",end='')
    for j in range(i+1):
        print("*",end='')
        if count<i:
            print("A",end='')
            count+=1
    print()