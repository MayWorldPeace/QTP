# 有序的"字符"序列

# 定义一个字符串
my_str = "hello"
# 得到e这个字符 并打印(程序中 是从0开始) -> 下标索引
# 传入一个正常的下标索引
# 如果从左到右开始索引是0, 1, 2, 3....
# ret = my_str[4]
# print(ret)

# 从右到左开始的索引是-1, -2, -3, ....
# ret = my_str[-4]
# print(ret)

# 一定要保证字符串的下标索引是存在的

# 利用while 打印出字符串中的每个字符
# 定义一个变量
index = 0
# 定义一个变量记录字符串的长度
l = len(my_str)
#
while index < l:
    ret = my_str[index]
    print(ret)
    index += 1

