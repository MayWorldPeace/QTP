
# 计算1~100之间偶数的累积和（包含1和100）
# 一个数可以被2整除 也就是余数为0 就代表是偶数
# x % 2 == 0

# # 定义一个变量
# num = 1
# # 定义一个变量 记录偶数和
# my_sum = 0
# # 判断while
# while num <= 100:
#     # 判断num是否是偶数
#     if num % 2 == 0:
#         my_sum += num
#
#     num += 1

# print("1~100的偶数和为%d" % my_sum)

# 计算1~100之间偶数的乘积（包含1和100）
num = 1
# 定义一个变量记录
result = 1
while num <= 100:

    # 判断是否是偶数
    if num % 2 == 0:
        result *= num

    num += 1

print("1~100的偶数的乘积:%d" % result)