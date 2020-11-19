class BalanceException(Exception):
    pass
def checkbalance():
    money = 10000
    withdraw = 9000
    balance = money-withdraw
    if (balance<=2000):
        raise BalanceException("Insufficient balance")
    print(balance)
try:
    checkbalance()
except BalanceException as ba:
    print(ba)