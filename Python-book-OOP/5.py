class A:
    def A(self):
        print('I am in A.')
class B:
    def B(self):
        print('I am in B.')
class C(A,B):
    def C(self):
        print('I am in C.')

C = C()
C.A()
C.B()