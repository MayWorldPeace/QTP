# 定义一个变量 记录行数
# x = 1
# while x <= 9:
#     print(x)
#     x += 1

# 定义一个变量 记录列数
# y = 1
# while y <= 5:
#     print(y, end="")
#     y += 1


# 定义一个变量 记录行数
# %2d 显示两位 如果只有一位 使用空格占位 默认为右对齐
# 如果左对齐 就是 %-2d
x = 1
while x <= 9:
    # 定义一个变量 记录列数
    y = 1
    while y <= x:
        print("%d * %d = %-2d" % (y, x, x * y), end="  ")
        y += 1
    # 换行
    print()
    x += 1