try:
    num = int(input("请输入一个整数："))
    result = 8 / num
    print(result)
except ValueError:
    print("值错误")
except Exception as result:
    print("错误: %s" %result)

else:
    print('程序运行成功')
finally:
    print("程序运行结束")




