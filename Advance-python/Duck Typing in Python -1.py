class Duck:
    def walkD(self):
        print("Thapak Thapak Thapak Thapak")
class Horse:
    def walkH(self):
         print("Tabdak tabdak tabdak tabdak")
def myfunction(obj):
    #obj.walkD()
    obj.walkH()

h = Horse()
myfunction(h)