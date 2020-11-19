n = int(input("Please enter the number  of rows : "))
i = 2
for row in range(1,n+1):
    for col in range(1,2*n):
        if (row+col==n+1) or (col-row==n-1):
            print("*",end='')
        elif (row==n and (col!=i)):
            print("*",end='')
            i = i+2
        else:
            print(end=' ')
    print()
