# 导入模块 -> 随机模块
import random
# # 定义一个变量 记录用户(玩家)的输入(拳法)
# player = int(input("请输入: 剪刀(0) 石头(1) 布(2):"))
# # 定义一个变量 记录电脑的输入
# # randint(0, 2) -> [0, 2]   0<=x<=2
# computer = random.randint(0, 2)
#
# # 以玩家为第一视角
# # 假如说玩家胜利(剪刀 = 布 或者 石头 = 剪刀 或者 布 = 石头)
# # 假如说玩家和电脑平局 (玩家输入的==电脑输入的)
# # 假如说玩家失败(除了胜利和平局 其他的都是失败)
#
# print("玩家:%d" % player)
# print("电脑:%d" % computer)
# print("==========================")
# # 玩家胜利
# if (player == 0 and computer  == 2 ) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
#     print("玩家胜利!!!!")
# # 判断玩家和电脑平局
# elif (player == computer):
#     print("玩家和电脑打成平局!!!")
# # 其他就是为玩家失败
# else:
#     print("玩家失败!!!")



# 使用循环
print("马上开始游戏~~~~~~~~~~~")
# 死循环
while True:
    # 定义一个变量 记录用户(玩家)的输入(拳法)
    player = int(input("请输入: 剪刀(0) 石头(1) 布(2):"))
    # 定义一个变量 记录电脑的输入
    # randint(0, 2) -> [0, 2]   0<=x<=2
    computer = random.randint(0, 2)
    print("玩家:%d" % player)
    print("电脑:%d" % computer)
    print("==========================")
    # 玩家胜利
    if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
        print("玩家胜利!!!!")
    # 判断玩家和电脑平局
    elif (player == computer):
        print("玩家和电脑打成平局!!!")
    # 其他就是为玩家失败
    else:
        print("玩家失败!!!")
