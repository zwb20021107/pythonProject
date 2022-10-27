class A:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.__num2 = num2
    def __test(self):
        print("A:__test")

    def test(self):
        print("A: test")

class B(A):
    def demo(self):
        print("B:demo")

b = B()
print(b)