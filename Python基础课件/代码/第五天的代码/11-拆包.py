# 拆包

# 定义一个列表
# my_list = [1, 3.14, "hello", True]
# 可以获取列表中元素的值 但是可读性不强
# print(my_list[1])
# print(my_list[2])

# 拆包
# num, pi, my_str, my_bool = my_list
# print(pi)
# print(my_bool)
# num, pi, my_str, my_bool = [1, 3.14, "hello", True]


# 定义一个元组
# my_tuple = (1, 3.14, "hello", True)
# num, pi, my_str, my_bool = my_tuple
# print(pi)


# 定义一个字典
# my_dict = {"name":"老王", "age": 19}
# ret1, ret2 = my_dict
# 得到的是key  字典是无序的
# print(ret1, ret2)

# 一次定义多个变量
# num1 = 10
# num2 = 20
# num3 = 30
# num4 = 3.14
# # 龟叔 称之为比较pythonic 自夸
# # 变量名和值是一一对应
# num1, num2, num3, num4 = 10, 20, 30, 3.14
# print(num4)


# 元组
def deal_name_age(name, age):
    # 处理后 姓名:小明  年龄:22
    new_name = "姓名:%s" % name
    new_age = "年龄:%d" % age
    # 如果在函数内部 使用return 返回值1 返回值2,... 默认就是元组类型 不需要写小括号
    return new_name, new_age

# 可以拆包me?
my_name, my_age = deal_name_age("小明", 20)
print(my_name, my_age)