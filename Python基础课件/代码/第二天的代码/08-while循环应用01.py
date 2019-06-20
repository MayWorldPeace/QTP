# 计算1~100的累积和（包含1和100）
# 定义一个变量
num = 1
# 定义一个变量 记录累积和
my_sum = 0
while num < 101:
    # 求和
    my_sum += num

    num += 1

# 打印结果
print("1~100累计和:%d" % my_sum)

