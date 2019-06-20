import random
# 一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机的分配

# 定义一个学校
school = [[], [], []]

# index = random.randint(0, 2)
# # 随机安排到哪个办公室
# school[index].append("A")
#
# index = random.randint(0, 2)
# school[index].append("B")
#
# index = random.randint(0, 2)
# school[index].append("F")
# print(school)


# 定义一个变量保存8名老师
# 让八名老师站好等待随机分配办公室
my_str = "ABCDEFGH"
for c in my_str:
    # 产生随机数
    index = random.randint(0, 2)
    #
    school[index].append(c)


print(school)

