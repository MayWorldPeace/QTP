# 编程实现对一个元素全为数字的列表，求最大值、最小值

# 准备一个列表
# my_list = [-1, -5, -10, -200, -300, -40]

# 定义一个变量 记录最终的最大值
# 不是所有的默认值都要设置为0 考虑到语境
# my_max = my_list[0]
# # for循环
# for value in my_list:
#     #判断如果列表中的元素值大于最大值
#     if value > my_max:
#         # 赋值
#         my_max = value
#
# print(my_max)


my_list = [-1, -5, -10, -200, -300, -40]

# 定义一个变量 记录最小值
my_min = my_list[0]
# 遍历
for value in my_list:
    if value < my_min:
        my_min = value

print("最小值:%d" % my_min)