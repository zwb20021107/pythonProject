class HouseItem:
    def __init__(self, name , area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.1f" %(self.name, self.area)

    def __del__(self):
        print("%s烧了" %self.name)




class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        #剩余面积
        self.free_area  = area
        #家具名称列表
        self.item_list = []

    def __str__(self):
        return "户型为%s, 总面积为%.1f, 剩余面积为%.1f \n家具：%s"\
               %(self.house_type, self.area,
                 self.free_area, self.item_list)

    def add_item(self, item):
        # 1.判断家具面积
        if item.area > self.free_area:
            print("%s 的面积过大，无法添加" % item.name)
            return

        # 2.将家具的名称添加到列表中
        self.item_list.append(item.name)
        # 3. 计算剩余面积
        self.free_area -= item.area

    def __del__(self):
        print("房子塌了")



bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)



my_home = House("两室一厅", 60.0)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)
