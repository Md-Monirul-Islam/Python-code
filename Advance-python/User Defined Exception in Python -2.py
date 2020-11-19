class BalanceException(Exception):
    pass
def checkbalance():
    money = 10000
    withdraw = 9000
    try:
        balance = money-withdraw
        if (balance<=2000):
            raise BalanceException("Insufficient balance")
        print(balance)
    except BalanceException as ba:
        print(ba)
checkbalance()