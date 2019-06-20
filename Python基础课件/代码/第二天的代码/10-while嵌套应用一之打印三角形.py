"""
*
**
***
****
*****
"""

# 考虑第一件事情 分析如何打印出5行
# 定义一个变量
# row = 1
# # 循环
# while row <= 5:
#     print("*")
#     row += 1

# 考虑第二件事情 打印出每一行的每一列的*
# 在默认的情况下 使用print 默认打印完成后 会有一个换行
# print("哈哈") 完整的格式 print("哈哈", end="\n")
# 定义一个变量
# col = 1
# while col <= 5:
#     print("*", end="")
#     col += 1

# 定义一个变量 记录行数
row = 1
while row <= 5:
    # 定义一个变量 记录列数
    col = 1
    while col <= row:
        print("*", end="")
        col += 1
    # 换行
    print()
    row += 1







