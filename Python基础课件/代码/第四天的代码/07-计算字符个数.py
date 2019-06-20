# 统计字符串中，各个字符的个数
# 比如："hello world" 字符串统计的结果为： h:1 e:1 l:3 o:2 d:1 r:1 w:1

# # 01 准备一个字符串
# my_str = "hello world"
#
# # 字符串的有一个count
# # 循环 -> for循环
# # 定义一个列表
# my_list = []
#
# # 循环
# for c in my_str:
#
#     # 去除空格 且 这个字符列表没有保存过
#     if c != " " and c not in my_list:
#         # 计算每个字符出现的次数
#         count = my_str.count(c)
#         print("%s:%d" % (c, count))
#         # 保存下这个字符
#         my_list.append(c)



# 01 准备一个字符串
my_str = "hello world"
new_list = my_str.split()
# 把列表的元素组成一个字符串
new_str = "".join(new_list)
print(new_str)
# 字符串的有一个count
# 循环 -> for循环
# 定义一个列表
my_list = []

# 循环
for c in new_str:

    # 这个字符列表没有保存过
    if c not in my_list:
        # 计算每个字符出现的次数
        count = my_str.count(c)
        print("%s:%d" % (c, count))
        # 保存下这个字符
        my_list.append(c)


