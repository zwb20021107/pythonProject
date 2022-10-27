def input_password():
    num = input("请输入密码")

    if len(num) >= 8:
        return num
    print("主动抛出异常")
    ex = Exception("密码长度不够")
    raise ex


print(input_password())