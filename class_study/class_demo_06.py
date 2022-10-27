class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def shoot(self):
        if self.bullet_count > 0:
            self.bullet_count -= 1
        else:
            print("子弹用完了")

    def add_bullet(self, count):
        self.bullet_count += count

    def __str__(self):
       return "%s 还有子弹 %d 发" %(self.model, self.bullet_count)

    def __del__(self):
        print("%s 已经销毁" %self.model)



class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def file(self):
        if self.gun is  None:
            print("%s 还没有枪" %self.name)
            return
        print("冲啊")
        self.gun.add_bullet(50)
        self.gun.shoot()


#1.创建枪对象
ak47 = Gun("Ak47")

# 2.创建许三多
xusanduo = Soldier("许三多")

xusanduo.gun = ak47

xusanduo.file()
print(xusanduo.gun)

