# 查找元素("查"in, not in, index, count)

# 定义一个字符串
my_list = ["老李", "老张", "小明", 400, 400]
# 判断老李是否存在列表中

# 使用in 判断一个元素是否存在列表中
# if "老李1" in my_list:
#     print("存在在列表中")
#
# print("测试")

# 使用not in 判断一个元素不存在列表中
# if "小红" not in my_list:
#     print("小红不存在")

# index 通过index 获取某个元素在列表中的下标索引
# ret1 = my_list.index(400)
# print(ret1)

# count 查找某个元素的值在列表中出现的次数
# ret2 = my_list.count(400)
# print(ret2)

# 查询4000 如果有给我下标索引 如果没有 什么也不做

# 使用count 配合完成
# count = my_list.count(400)
# if count > 0:
#     index = my_list.index(400)
#     print(index)
#
# print("测试")

# 使用in 配合完成
# if 400 in my_list:
#     index = my_list.index(400)
#     print(index)
#
# print("测试")