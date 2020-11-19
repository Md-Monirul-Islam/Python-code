class A(object):
    def dothis(self):
        print('I am in class A.')
class B(A):
    pass
class C(A):
    def dothis(self):
        print(' I am in class C.')
class D(B,C):
    pass
d = D()
d.dothis()
print(D.mro())