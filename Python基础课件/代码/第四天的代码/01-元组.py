# 列表是可变的
# 元组是不可变的

# 定义一个字符串 "" 或者 ''
# 定义一个列表 []
# 定义一个元组 ()

# 定义一个元组
# my_tuple = (1, 3.14, True, "HELLO")
#查看数据类型<class 'tuple'>
# print(type(my_tuple))

# 定义一个空元组
# my_tuple = ()
# print(type(my_tuple))
# my_tuple = tuple()
# print(type(my_tuple))


# 特列
# 如果元组中只有一个元素
# 人为是把一个整数用小括号包裹起来 还是认识int类型
# (1,) -> 元组  (1) -> int
# my_tuple = (1,)
# print(type(my_tuple))


# 通过下标获取元组中的元素
# my_tuple = (1, 3.14, True, "HELLO")
# 获取3.14
# value = my_tuple[1]
# print(value)

# 通过下标修改元组的元素
# 因为元组是不可变的 不可以修改元素 或者删除元素
# 只能查看元素 或者遍历元组中的元素
# my_tuple = (1, 3.14, True, "HELLO")
# my_tuple[3] = 666


# index count
# my_tuple = (1, 3.14, True, "HELLO", 3.14)

# 元组中元素的位置
# index = my_tuple.index(3.14)
# print(index)

# 获取某个元素在 元组中出现的次数
# count = my_tuple.count(3.14)
# print(count)


# for循环遍历

# my_tuple = (1, 3.14, True, "HELLO", 3.14)

# for value in my_tuple:
#     print(value)


# while循环遍历
# index = 0
# while index < len(my_tuple):
#     # 通过下标获取指定的元素
#     value = my_tuple[index]
#     print(value)
#     index += 1

# 元组是不可变的  列表是可变的?
# 有时候我们需要保存一些数据 而这些数据不会改变 那么久应该使用元组进行保存
# 元组的不可变 是为了数据安全考虑
# my_tuple = ("hello", 3.14)
# my_tuple[0]
# my_tuple[1] = 3.1415926

# 定义一个空的元组 只要定义完成 就已经决定了数值 是不能改变的 -> 不可变的
my_tuple = ()


# 问题讲解
# True 为 1  False 为 0
# my_tuple = (3.14, True, "HELLO", 3.14)
#
# ret = my_tuple.index(True)
# print(ret)