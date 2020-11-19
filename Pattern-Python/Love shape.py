for row in range(6):
    for col in range(7):
        if (row==0 and (col!=0 and col!=3 and col!=6)) or (row-col==2) or (row+col==8) or (row==1 and (col!=1 and col!=2 and col!=4 and col!=5)):
            print("*",end='')
        else:
            print(end=' ')
    print()