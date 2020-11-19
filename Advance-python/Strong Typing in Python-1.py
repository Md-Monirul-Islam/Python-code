class Duck:
    def walk(self):
        print("Thapak Thapak Thapak Thapak")
class Horse:
    def walk(self):
         print("Tabdak tabdak tabdak tabdak")
class Cat:
    def talk(self):
        print("Meow Meow")
def myfunction(obj):
    if hasattr(obj,"walk"):
       obj.walk()
    #if hasattr(obj,"talk"):
        #obj.talk()

h = Horse()
myfunction(h)
d = Duck()
myfunction(d)
c = Cat()
myfunction(c)