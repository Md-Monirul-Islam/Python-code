try:
    dividend = int(input("Please the dividend: "))
    divisor = int(input("Please enter divisor: "))
    print("%d/%d = %f" % (dividend,divisor,dividend/divisor))
except(ValueError,ZeroDivisionError):
    print("Invalid value.")