# 代码是从上往下执行 一行一行的读
# 第1种方式
# a = 4
# b = 5
# c = 0
#
# c = a # c = 4
# a = b # a = 5
# b = c # b = 4
#
# # 结果
# print(a)
# print(b)


# 第2种方式
# a = 4
# b = 5
#
# a = a + b  # a = 9 b = 5
# b = a - b  # a = 9 b = 4
# a = a - b  # a = 5 b = 4
#
# print(a)
# print(b)


# 第3种方式
a, b = 4, 5 # a = 4 b = 5
# 在执行35行的时候 看的是第30行的代码
# a = b
# b = a
#不是等价的
a, b = b, a # a = 5 b = 4
print(a)
print(b)