# 定义一个字符串
a = "      "

# <22>splitlines
# 按照行分隔，返回一个包含各行作为元素的列表
# ret1 = a.splitlines()
# print(ret1)


# <23>isalpha
# 如果 mystr 所有字符都是字母 则返回 True,否则返回 False
# ret2 = a.isalpha()
# print(ret2)


# <24>isdigit
# 如果 mystr 只包含数字则返回 True 否则返回 False.
# ret3 = a.isdigit()
# print(ret3)

# <25>isalnum
# 如果 mystr 所有字符都是字母或数字则返回 True,否则返回 False
# ret4 = a.isalnum()
# print(ret4)


# <26>isspace
# 如果 mystr 中只包含空格，则返回 True，否则返回 False.
# ret5 = a.isspace()
# print(ret5)


# <27>join
# mystr 中每个元素后面插入str,构造出一个新的字符串
# 定义一个变量 记录列表
# my_list = ["1", "x", "hello"]

# 最终打印出来一个字符串为 100x00hello
# ret6 = "00".join(my_list)
# print(ret6)


# __________________________________________
my_str = "    ab cd    "
# # 最终结果为abcd
# ret = my_str.replace(" ", "")
# print(ret)
ret2 = my_str.split()
print(ret2)
ret3 = "".join(ret2)
print(ret3)
