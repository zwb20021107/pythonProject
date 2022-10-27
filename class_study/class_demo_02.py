class Cat:
    def drink(self):
        print("小猫要喝水")

    def eat(self):
        print("小猫爱吃鱼")


c1 = Cat()
c1.eat()
c1.drink()

print("%x" % (id(c1)))