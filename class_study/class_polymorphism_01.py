class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s在玩耍" %self.name)

class Person(object):
    def __init__(self, name):
        self.name =name
    def game_with_dog(self, dog):
        print("%s 和 %s 快乐的玩耍" %(self.name, dog.name))
        dog.game()

class XiaoTianQuan(Dog):
    def game(self):
        print("%s 飞到天上去玩耍" % self.name)

wangcai = XiaoTianQuan("飞天旺财")

xiaoming = Person("小明")

xiaoming.game_with_dog(wangcai)