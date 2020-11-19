class A:
    def where(self):
        print('I am in class A.')

class B:
    def where(self):
        print('I am in class B.')

class C(A,B):
    pass
obj_1 = C()
obj_1.where()
print(C.mro())
