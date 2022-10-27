class Person(object):
    def __init__(self, name):
        self.name = name


    def __str__(self):
        return "名字为%s" %self.name
