class Add:
    def result(self,x,y):
        print("Addition :",x+y)
class MUlti(Add):
    def result(self,a,b):
        super(MUlti, self).result(a,b) #calling parent class method.
        print("Multiplication :",a*b)
output = MUlti()
output.result(10,20)

