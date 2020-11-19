from threading import*
import time
class Flight:
    def __init__(self,available_seat):
        self.available_seat = available_seat
        self.l = Lock()
    def reserve(self,need_seat):
        self.l.acquire(blocking=True,timeout=-1)#(blocking=True,timeout=-1)-optional.by defalut-True and timeout=-1
        print("Available seat->>",self.available_seat)
        if self.available_seat >= need_seat:
            name = current_thread().name
            print(f"{need_seat} seat has alloted for {name}")
            self.available_seat -= need_seat
            #time.sleep(4)
        else:
            print("SORRY! all seats has alloted.")
        self.l.release()
f = Flight(2)
t1 = Thread(target=f.reserve,args=(1,),name="Munna")
t2 = Thread(target=f.reserve,args=(1,),name ="Monirul")
t3 = Thread(target=f.reserve,args=(1,),name="Swapon")
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("Main thread.")

