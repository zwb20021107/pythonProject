class Women:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def secret(self):
        print("我的年龄为 %d" %self.__age)



zhangsan = Women("张三", 18)
zhangsan.secret()

print(zhangsan._Women__age)



