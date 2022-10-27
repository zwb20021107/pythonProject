class A:
    def test(self):
        print("A的test调用")

    def demo(self):
        print("A的demo调用")

class B:
    def test(self):
        print("B的test调用")
    def demo(self):
        print("B的demo调用")

class C(B, A):
    pass


c = C()
c.test()
c.demo()

print(C.__mro__)