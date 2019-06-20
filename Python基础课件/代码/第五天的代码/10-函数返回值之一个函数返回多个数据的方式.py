# 需求 传入一个人名字 和年龄
# 例如 小明 22
# 通过调用函数后 得到两个字符串 姓名:小明  年龄:22

# 列表
# def deal_name_age(name, age):
#     # 处理后 姓名:小明  年龄:22
#     new_name = "姓名:%s" % name
#     new_age = "年龄:%d" % age
#     return [new_name, new_age]
#
# # 变量为列表
# ret = deal_name_age("小明", 22)
# print(ret[0])
# print(ret[1])

# 字典
# def deal_name_age(name, age):
#     # 处理后 姓名:小明  年龄:22
#     new_name = "姓名:%s" % name
#     new_age = "年龄:%d" % age
#     return {"name":new_name, "age":new_age}
#
# my_dict = deal_name_age("小明", 22)
# print(my_dict["name"])
# print(my_dict["age"])


# 元组
def deal_name_age(name, age):
    # 处理后 姓名:小明  年龄:22
    new_name = "姓名:%s" % name
    new_age = "年龄:%d" % age
    # 如果在函数内部 使用return 返回值1 返回值2,... 默认就是元组类型 不需要写小括号
    return new_name, new_age
#
my_tuple = deal_name_age("小明", 22)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[1])