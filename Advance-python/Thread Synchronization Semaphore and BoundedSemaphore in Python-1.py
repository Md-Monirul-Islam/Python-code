from threading import *
class Flight:
    def __init__(self,available_seat):
        self.available_seat = available_seat
        self.l = Semaphore(2) #BoundeSemaphore(2)

        print(self.l)

    def reserve(self,need_seat):
        self.l.acquire()
        print(self.l._value)
        print("Available seat->>",self.available_seat)
        if self.available_seat >= need_seat:
            name = current_thread().name
            print(f"{need_seat} seat alloted for {name}\n")
            self.available_seat -= need_seat

        else:
            print("SORRY! All seat has alloted.")
        self.l.release()
        #self.l.release()
        #self.l.release()
        #self.l.release()


f = Flight(2)
t1 = Thread(target=f.reserve,args=(1,),name="Munna")
t2 = Thread(target=f.reserve,args=(1,),name="Swapan")
t3 = Thread(target=f.reserve,args=(1,),name="Habib")

t1.start()
t2.start()
t3.start()

