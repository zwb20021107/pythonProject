class Person:
    def __init__(self, name, weight):
        print("小明出生了")
        self.name = name
        self.weight = weight

    def __str__(self):
        return "%s 体重为%.2fkg" %(self.name, self.weight)

    def eat(self):

        self.weight += 1
        print("%s吃了饭，体重为%.2f" % (self.name, self.weight))
    def run(self):

        self.weight -= 0.5
        print("%s跑了步, 体重为%.2f" % (self.name, self.weight))

    def __del__(self):
        print("%s 死了" % self.name)

xiaoming = Person("小明", 75.0)

print(xiaoming)
xiaoming.run()
xiaoming.eat()
print(xiaoming)

