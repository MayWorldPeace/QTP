# 可以遍历的 字符串 列表 元组 字典 -> for循环

# 自定义一个字符串
# my_name = "hello"
# for c in my_name:
#     print(c)


# 自定义一个列表 快速创建一个有规律的列表
# my_list = list("abcd")
# for value in my_list:
#     print(value)


# 自定义一个元组
# my_tuple = tuple("123456")
# for value in my_tuple:
#     print(value)


# 定义一个字典
# my_dict = {"name": "小红", "age": 22, "no": "009"}
#
# 遍历-key
# for key in my_dict.keys():
#     print(key)

# 遍历value
# for value in my_dict.values():
#     print(value)

# 遍历items
# for item in my_dict.items():
#     print(item[0])
#     print(item[1])


# 通过设置两个临时变量
# for key, value in my_dict.items():
#     print("key:", key)
#     print("value:", value)



# 如果想使用元素和下标索引 请使用enumerate(列表名)
# 定义一个列表
# my_list = list("abcd")
# 不仅要获取列表中的元素 而且需要知道这个元素下标索引
# for i, value in enumerate(my_list):
#     print(i,value)