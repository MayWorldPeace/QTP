# 导入模块
import random
# 定义一个列表列表中有6个元素
# 六个元素每个数值范围 [-10, 50]

# 定义一个空的列表 用来保存数据
my_list = []
# 定义一个for循环
for i in range(6):
    # 获取随机数
    value = random.randint(-10, 50)
    # 把随机数添加到列表中
    my_list.append(value)
print(my_list)

# [6, -3, -8, 7, 9, -2] 进行排序 -> 升序 (从小到大)
# 列表名.sort() 等价于 列表名.sort(reverse=False)
# my_list.sort()
# print(my_list)

# 降序 (从大到小)
# my_list.sort(reverse=True)
# print(my_list)

# python3.x中列表的排序只能是数字类型
