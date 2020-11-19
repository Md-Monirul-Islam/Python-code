#two task using two thread.
from threading import Thread
class Hotel:
    def __init__(self,table):
        self.table = table

    def food(self):
        for i in range(1,6):
            print(self.table,"Table number->>",i)

h1 = Hotel("Take order from table.")
h2 = Hotel("Serve order to table.")
t1 = Thread(target=h1.food())
print()
t2 = Thread(target=h2.food())
t1.start()
t2.start()