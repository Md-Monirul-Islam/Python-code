from threading import Thread
from queue import Queue
from time  import sleep
class producer:
    def __init__(self,prod):
        self.prod = prod
        self.q = Queue()
    def produce(self):
        for i in range(1,6):
            print("Item produce.....",i)
            self.q.put(i)
            sleep(2)
class consumer:
    def __init__(self,prod):
        self.prod = prod
    def consume(self):
        for i in range(1,6):
            print("Item received....",self.prod.q.get(i))
p = producer()
c = consumer()
t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)

t1.start()
t2.start()