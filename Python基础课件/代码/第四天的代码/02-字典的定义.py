

# 保存一个人的信息 (名字, 年龄 , 学号)
# my_list = ["小明", 22, "007"]
# 获取小明 0 代表是名字 1代表是年龄 2代表是学号
# 可读性不强
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])

# 使用字典保存
# 格式: 字典名 = {键值1: 实值1, 键值2: 实值2, .....}
# 键值1: 实值1 统称为 键值对  key value 也称之为元素
# 键值数据类型的选择: 必须是不可变的
# 键值 的名字不能重复(才能完成1对1 通过一个key 获取key 的value)
# 字典的key 一般都是使用字符串
# 字典的value 没有规定 (可以重复的)
my_dict = {"name": "小明", "age": 22, "no": "007"}
# 三个元素(键值对)
print(len(my_dict))

# 定义一个特殊 (空字典)
my_dict1 = {}
print(len(my_dict1))
# <class 'dict'>
print(type(my_dict1))
my_dict2 = dict()
print(type(my_dict2))