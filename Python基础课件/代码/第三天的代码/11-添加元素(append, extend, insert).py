# 添加元素(append, extend, insert)
# 列表是可变的(如果对当前列表的操作 是在原有的列表上进行更改)
# 定义一个列表
my_list = [1, 3, 5, 8]
# append 添加一个整体(一个对象)
# my_list.append([4, 5])
# print(my_list)
# [1, 3, [4, 5]]


# extend 添加一个可以遍历的对象(有序的字符序列)
# my_list.extend([4, 6, 9])
# print(my_list)

# insert 插入到指定位置
my_list.insert(0, "hello")
print(my_list)