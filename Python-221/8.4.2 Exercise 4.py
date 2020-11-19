''''
1. Write a recursive function which calculates the factorial
of a given number. Use exception handling to raise an appropriate
exception if the input parameter is not a positive integer, but allow the user
to enter ﬂoats as long as they are whole numbers
'''
def facterial(n):
    ni = int(n)
    if ni != n or ni <= 0:
        raise ValueError("%s in not a positive integer "%n)
    if ni ==1:
        return 1
    return ni * facterial(ni - 1)
print(facterial(6))