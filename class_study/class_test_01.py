class Tool(object):
    @classmethod
    def work(cls):
        print("工具在工作")
        print("%d" %cls.count)
    # 使用复制语句定义类属性, 记录所有工具对象的数量
    count = 0

    def __init__(self, name):
        self.name = name;
        Tool.count += 1


#1.创建共v就对象
tool1= Tool("斧头")
print(Tool.count)
tool2= Tool("斧头")
print(Tool.count)
tool3= Tool("斧头")

print(Tool.count)

Tool.work()