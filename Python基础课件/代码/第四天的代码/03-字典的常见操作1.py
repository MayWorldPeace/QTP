# 字典是无序的 可变的

# 定义一个字典 名字 年龄 学号
# my_dict = {"name": "小红", "age": 22, "no": "009"}

# <1>修改元素
# 字典的每个元素中的数据是可以修改的，只要通过key找到，即可修改
# 通过key 获取对应key的value的值
# print(my_dict["age"])
# # 通过key 修该对应key的value的值
# my_dict["age"] = 220
# print(my_dict)

# <2>添加元素
# title - "哈哈"
# 格式: 字典名[key] = value
# 如果使用上面的格式 如果这个key不存在 添加一组键值对
#如果使用上面的格式 如果这个key存在 会吧key原来的value的值进行覆盖
# my_dict["title"] = "哈哈"
# print(my_dict)


# <3>删除元素
# 对字典进行删除操作，有一下几种：
#
# del (python内置函数)
# clear()
my_dict = {"name": "小红", "age": 22, "no": "009"}
# 删除no 009
# 删除键值对 格式: del 字典名[key]
# del my_dict["no"]
# print(my_dict)


#  clear 删除字典中的所有的元素
my_dict.clear()
# 等价于 my_dict = {} 或者 my_dict = dict()
print(my_dict)