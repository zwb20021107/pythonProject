class Animal:

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")

class Dog(Animal):
    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):
    def fly(self):
        print("飞")

    def bark(self):
        #super().bark()
        #Dog.bark(self)
        print("哮天犬狂叫")

xiaotianquan = XiaoTianQuan()

xiaotianquan.fly()
xiaotianquan.bark()
