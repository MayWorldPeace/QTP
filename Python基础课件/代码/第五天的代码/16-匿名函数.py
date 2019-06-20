# 匿名函数 藏匿名字的函数


# 对函数的简写

# 无参数无返回值的函数
# def my_print():
#     print("hello python")
#
# my_print()

# 表达式的定义
# f = lambda : print("hello python")
# # 执行
# f()
# 等价于
# (lambda : print("hello python"))()


# 无参数有返回值的函数
# def my_pi():
#     return 3.14
# print(my_pi())

# 表达式的定义
# f = lambda : 3.14
# print(f())

# 定义一个有参数无返回值的函数
# def my_print(name):
#     print("你好%s" % name)
#
# my_print("龟叔")
#
# f = lambda name: print("你好%s" % name)
# # 执行
# f("龟叔")


# 定义一个有参数有返回值的函数
# def add2num(a, b):
#     return a + b
#
# f = lambda a, b : a + b
# # ret = f(10, 20)
# print(f(10, 20))

##_______________________________________

# 函数作为参数传递
# 表达式
# f = lambda x,y:x+y

# 函数
# def fun(a, b, opt):
#     # print("a = %d" % a)
#     # print("b = %d" % b)
#     result = opt(a, b)
#     print("result = %d" % result)
#
#
# # 调用函数
# fun(1, 2, lambda x,y:x+y)


# def add2num(x, y):
#     return x + y

# f = lambda x, y : x +y
# def fun(a, b, opt):
#     result = opt(a, b)
#     print("结果:%d" % result)
#
#
# fun(10, 10, f)


##_______________________________________
# 自定义排序(最外层肯定是列表)

# my_list = [1, 4, -10, 20, 3]
# my_list.sort()
# print(my_list)

# stus = [{"name": "zhangsan", "age": 18}, {"name": "lisi", "age": 19}, {"name": "wangwu", "age": 17}]

# [{'name': 'zhangsan', 'age': 18}, {'name': 'lisi', 'age': 19}, {'name': 'wangwu', 'age': 17}]
# 按照年龄排序
# [{'name': 'wangwu', 'age': 17},{'name': 'zhangsan', 'age': 18}, {'name': 'lisi', 'age': 19}]
# print(stus)
# stus.sort(key=lambda my_dict:my_dict["age"])
# print(stus)

# 按照名字排序
# 使用的是每个名字的首字母排序 (规则是按照ascii码完成的)
# 格式: 列表名.sort(key=lambda 列表的元素(临时变量): 临时变量[key])
# stus.sort(key=lambda my_dict:my_dict["name"])
# print(stus)


# 列表中的列表嵌套
# my_list = [[10, 8, 9], [7, 10, 19], [9, 10, 29]]
# # 按照列表元素(小列表)最后一个元素排序
# 格式: 列表名.sort(key=lambda 列表的元素(临时变量): 临时变量[下标索引])
# my_list.sort(key=lambda new_list:new_list[2], reverse=True)
# print(my_list)
