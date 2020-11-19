while True:
    try:
        a = int(input("Input a integer value :"))
        break
    except ValueError:
        print("This is not a integer number.Please try again.....")