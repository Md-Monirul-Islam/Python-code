class Add:
    def result(self,a,b):
        print("Addition :",a+b)
class Multi(Add):
    def result(self,a,b):
        print("Multiplication :",a*b)
output = Multi()
output.result(3,5)
output1 = Add()
output1.result(3,5)