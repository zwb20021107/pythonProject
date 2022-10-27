class Cat:

    """这是一个猫类"""

    def __init__(self, name):
        self.name = name
        self.age = 17
        self.grade = True

    def __str__(self):
        return "我是小猫[%s]" % self.name

    def __del__(self):
        print("%s销毁" % self.name)



Tom = Cat ("TO")
Tony = Cat("Tony")

print(Tom)
print(Tony)


