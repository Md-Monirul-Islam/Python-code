n = int(input("Please enter the number of rows : "))
for row in range(0,n,1):
    for col in range(0,row):
        print("*",end='')
    print()
