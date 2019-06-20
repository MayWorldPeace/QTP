# 删除元素 del, pop, remove
# 定义一个列表
my_list = ["小明", 20, "小红", 50]

# del 删除指定的元素 (通过下标索引)
# 格式: del 列表名[下标索引]
# del 这个函数 是python内置函数(len  del)
# del my_list[1]
# print(my_list)


# pop是属于列表的方法
# pop 默认情况下 会从列表的后面开始删除
# .pop() 会有一个返回值 告知删除元素的值
# print(my_list.pop())
# print(my_list)

# pop(下标索引)
# ret = my_list.pop(0)
# print(ret)
# print(my_list)

# remove 通过对象(数值)来删除列表中的元素
# my_list.remove("小红")
# print(my_list)


# del 第二种用法 了解
# 提前杀死对象 提前释放内存
# del my_list


# clear 清空列表(列表中所有的元素全部删除)
my_list.clear() # 等价于 my_list = [] 或者 my_list = list()
print(my_list)