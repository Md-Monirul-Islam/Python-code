n = int(input("Please enter your row : "))
for row in range(n,0,-1):
    for col in range(1,row+1):
        print(row,end=" ")
    print()

n = int(input("enter"))
for row in range(1,n,1):
    for col in range(1,row+1):
        print("*",end='')
    print()