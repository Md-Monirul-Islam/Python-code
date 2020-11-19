num = int(input("enter the number of rows : "))
for i in range(1,num+1):
    print("  "*(num-i)+ "* "*i)
for i in range(num-1,0,-1): # check without -1
    print("  "*(num-i)+"* "*i)