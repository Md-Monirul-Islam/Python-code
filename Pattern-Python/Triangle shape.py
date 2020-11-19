for row in range(5):
    for col in range(5):
        if (col==4) or (row==0) or (row==col):
            print("*",end='')
        else:
            print(end=' ')
    print()