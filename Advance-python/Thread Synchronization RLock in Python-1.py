from threading import*
class Flight:
    def __init__(self,available_seat):
        self.available_seat = available_seat
        self.l = RLock()
        print(self.l)
    def reserve(self,need_seat):
        self.l.acquire(blocking=True)
        print(self.l)
        print("Available seat->>",self.available_seat)
        if self.available_seat >= need_seat:
            name = current_thread().name
            print(f"{need_seat} alloted for {name}.\n")
            self.available_seat -= need_seat
        else:
            print("SORRY! All seat is alloted.")
        self.l.release()
f = Flight(2)
t1 = Thread(target=f.reserve,args=(1,),name="Munna")
t2 = Thread(target=f.reserve,args=(1,),name="Monirul")
t3 = Thread(target=f.reserve,args=(1,),name="Swapan")
t1.start()
t2.start()
t3.start()