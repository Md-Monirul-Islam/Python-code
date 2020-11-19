class BalanceException(Exception):
    pass
def checkbalance():
    money = 10000
    withdraw = 7000
    balance = money-withdraw
    print(balance)
checkbalance()