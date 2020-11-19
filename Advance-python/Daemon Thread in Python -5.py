from threading import Thread,current_thread
from time import sleep
def teacher():
    for i in range(1,11):
        print("Teaching season->>",i)
        sleep(2)
t1 = Thread(target=teacher)
t1.setDaemon(True)
print(t1.isDaemon())
t1.start()
t1.join()
sleep(5)
print("Exam finished.",current_thread().getName())