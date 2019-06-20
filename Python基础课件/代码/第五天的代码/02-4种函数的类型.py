
# 四种函数的类型
# 01- 无参数无返回值
# 02- 无参数有返回值
# 03- 有参数无返回值
# 04- 有参数有返回值


# 01- 无参数无返回值
def my_print():
    print("你好")
    print("python")

# 执行函数
# my_print()

# 02- 无参数有返回值
def my_pi():
    return 3.1415926

# print(my_pi())


# 03- 有参数无返回值
def print_info(name):
    print("你好%s" % name)

# print_info("龟叔")

# 定义一个列表
# name_list = ["龟叔", "小明", "小红", "张三"]
#
# for new_name in name_list:
#     # print(new_name)
#     print_info(new_name)



# 04- 有参数有返回值
# def my_func(a, b):
#     ret = a - b
#     return ret

def my_func(a, b):
    return a - b

result = my_func(10, 5)
print(result)





