try:
    dividend = int(input("Please enter dividend: "))
    divisor = int(input("Please enter divisor: "))
    print("%d / %d = %f " % (divisor,dividend,dividend/divisor))
except ValueError:
    print("The divisor and dividend have to be numbers!")
except ZeroDivisionError:
    print("The dividend may not be zero!")