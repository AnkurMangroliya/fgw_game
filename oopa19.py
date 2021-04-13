class A:
    def met(self):
        print("from a")
class B(A):
    def met(self):
        print("from b")
class C(A):
    def met(self):
        print("from c")
class D(C,B):
    def met(self):
        print("from d")


a = A()
b =B()
c=C()
d=D()
d.met()