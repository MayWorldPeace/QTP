# 列表和字符串一样 是有序的
# "abcd"
# ["a", "b", "c", "d"]

# for循环
# 字符串
# name = "hello"
# for c in name:
#     print(c)

# for循环
# 定义一个列表
# my_list = [1, 3, "hello", "哈哈"]
# 遍历列表的元素
# for value in my_list:
#     print(value)

# while循环
# 定义一个列表
my_list = [1, 3, "hello", "哈哈"]
# 定义一个变量 -> 下标索引
index = 0
# 定义一个变量 保存列表中的元素个数
l = len(my_list)
while index < l:
    # 通过下标索引获取列表中的元素
    value = my_list[index]
    print(value)
    index += 1


