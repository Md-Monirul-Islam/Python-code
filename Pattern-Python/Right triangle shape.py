num = int(input("Please enter the num of rows : "))
n = 1
for i in range(num):
    for j in range(i+1):
        print(format(n,"<5"),end="")
        n = n+1
    print()