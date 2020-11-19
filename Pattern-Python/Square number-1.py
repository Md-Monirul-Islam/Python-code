num = int(input("Please enter the number of rows : "))
n_list = [[0 for x in range(num)] for y in range(num)]
n = 1
low = 0
heigh = num-1
count = int((num+1)/2)
for i in  range(count):
    for j in range(low,heigh+1):
        n_list[i][j]=n
        n = n+1
    for j in range(low+1,heigh+1):
        n_list[j][heigh] = n
        n= n+1
    for j in range(heigh-1,low-1,-1):
        n_list[heigh][j]=n
        n = n+1
    for j in range(heigh-1,low,-1):
        n_list[j][low]=n
        n = n+1
    low = low+1
    heigh = heigh-1
for i in range(num):
    for j in range(num):
        print(n_list[i][j],end="\t")
    print()