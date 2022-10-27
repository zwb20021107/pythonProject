def demo(*args, **kwargs):
    print(args)
    print(kwargs)


#元组变量和字典变量
gl_nums = (1, 2, 3)
gl_xiaoming = {"姓名": "小明", "年龄": 10}

demo(*gl_nums, ** gl_xiaoming)