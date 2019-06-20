# 轨道交通价格调整为：
# 6公里(含)内3元;
# 6公里至12公里(含)4元;
# 12公里至22公里(含)5元;
# 22公里至32公里(含)6元;
# 32公里以上部分，每增加1元可乘坐20公里。

# 定义一个变量 模拟出行的公里数
km = 5

# 定义一个变量保存单程票价
every_money = 0

# 判断
# 6公里(含)内3元;
if km > 0 and km <= 6:
    every_money = 3

# 6公里至12公里(含)4元;
elif km > 6 and km <= 12:
    every_money = 4

# 12公里至22公里(含)5元;
elif km > 12 and km <= 22:
    every_money = 5

# 22公里至32公里(含)6元;
elif km > 22 and km <= 32:
    every_money = 6

# 32公里以上部分，每增加1元可乘坐20公里。
elif km > 32:
    # 分析: 假设 50 (32 + 18) -> 6 + 1
    # 分析: 假设 52 (32 +20) -> 6 + 1
    # 分析: 假设 53 (32 + 20 + 1) -> 6 + 1 + 1
    # 定义一个变量 求公里数的差值
    temp_km = km - 32

    # 分两种情况 temp_km是否可以被20整除
    # 整除了
    if temp_km % 20 == 0:
        # 32公里以内的 加上超出的
        every_money = 6 + temp_km / 20
    else:
        # int去掉小数部分
        every_money = 6 + int(temp_km/20) + 1

print("当成票价:%d" % every_money)

# 使用市政交通一卡通刷卡乘坐轨道交通，
# 每自然月内每张卡支出累计满100元以后的乘次，价格给予8折优惠;
# 满150元以后的乘次，价格给予5折优惠;
# 支出累计达到400元以后的乘次，不再享受打折优惠。

# 假设每个月，小明都需要上20天班，每次上班需要来回1次，即每天需要乘坐2次同样路线的地铁
# 最终得出这"20"天小明做地铁消费多少钱?(20天 40个来回)
# 定义一个变量 保存总的消费金额
total_money = 0
# 循环模拟40次
for i in range(40):
    # 判断小明消费的金额
    if total_money < 100:
        total_money += every_money

    # # 每自然月内每张卡支出累计满100元以后的乘次，价格给予8折优惠;
    elif total_money >= 100 and total_money < 150:
        total_money += every_money * 0.8

    # 满150元以后的乘次，价格给予5折优惠;
    elif total_money >= 150 and total_money < 400:
        total_money += every_money * 0.5

    # 支出累计达到400元以后的乘次，不再享受打折优惠。
    elif total_money >= 400:
        total_money += every_money


print("小明这个月消费%.2f" % total_money)







