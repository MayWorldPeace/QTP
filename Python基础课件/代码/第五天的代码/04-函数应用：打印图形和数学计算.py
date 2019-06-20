
# # 写一个函数打印一条横线
# def print_one_line():
#     print("-"*10)
#
# # 调用函数
# # print_one_line()
#
#
# # 打印自定义行数的横线
# def print_lines(num):
#     # for循环
#     for i in range(num):
#         # 执行函数print_one_line
#         print_one_line()
#
# # 最终执行print_lines
# print_lines(10)



# 写一个函数求三个数的和
def add3num(a, b, c):
    return a + b + c

# ret = add3num(10, 12, 14)
# print(ret)

# 写一个函数求三个数的平均值
def average3num(num1, num2, num3):
    # 求num1 + num2 + num3 和
    # ret = num1 + num2 + num3
    # 通过求和函数完成的
    ret = add3num(num1, num2, num3)
    # 把和除以3
    return ret / 3

result = average3num(10, 12, 17)
print(result)
