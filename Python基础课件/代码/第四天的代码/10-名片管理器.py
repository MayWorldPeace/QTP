# 定义一个字典 保存所有人的数据
all_dict = {}
# {"小明": {"name": "小明", "age": "22"}, "小红": {"name": "小红", "age": "20"}}
# 引导用户选择
info_str = """1.添加名片
2.删除名片
3.修改名片
4.查询名片
5.退出系统
请选择:"""


# 定义一个死循环 重复执行功能
while True:
# 判断用户的输入
    index = input(info_str)
    # 添加名片
    if index == "1":
        # 引导用户输入他的名字和年龄
        my_name = input("请输入您的名字:")
        my_age = input("请输入您的年龄:")
        # 构造成 一个字典
        my_dict = {"name": my_name, "age": my_age}
        # 添加数据到all_dict中
        all_dict[my_name] = my_dict
        print("添加名片成功....")
    # 删除名片
    elif index == "2":
        # 引导用户输入需要删除的名字
        my_name = input("请输入要删除数据的名字:")
        # 判断这个名字是否存在在all_dict中
        if my_name in all_dict:
            # 删除
            del all_dict[my_name]
            print("删除数据成功...")
        else:
            print("您输入的名字有误!!!")
    # 修改名片
    elif index == "3":
        # 引导用户输入名字
        my_name = input("请输入要修改信息人的名字:")
        # 判断名字是否存在在all_dict中
        if my_name in all_dict:
            # 引导用户输入修改后的年龄
            my_age = input("请输入修改后的年龄:")
            all_dict[my_name]["age"] = my_age
            print("修改数据成功...")
        else:
            print("您输入的名字有误!!!")
    # 查询名片
    elif index == "4":
        # 引导用户输入查询的名字
        my_name = input("请输入您要查询的名字:")
        # 判断名字是否存在
        if my_name in all_dict:
            n = all_dict[my_name]["name"]
            a = all_dict[my_name]["age"]
            print("姓名:%s 年龄:%s" % (n, a))
        else:
            print("您输入的名字有误!!!")

    # 退出程序
    elif index == "5":
        print("欢迎下次使用程序!!!!")
        break






