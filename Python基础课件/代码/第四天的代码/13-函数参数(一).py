
# 利用函数完成
# 函数的定义
# def my_func1():
#     # 定义两个变量
#     num1 = 15
#     num2 = 6
#     ret = num1 + num2
#     # 打印
#     print(ret)
#
# # 函数的调用
# my_func1()
#
# #定义一个函数
# def my_func2():
#     num1 = 80
#     num2 = 9
#     ret = num1 + num2
#     # 打印
#     print(ret)
#
# my_func2()


# 定义一个有参数的函数
# 形参: 形式参数
# 格式: def 函数名(形参1, 形参2, ...):
# def my_func(a, b):
#
#     # 求和
#     ret = a + b
#     # 打印
#     print(ret)
#
# # 执行一个有参数的函数
# # 实参: 实际参数
# # 格式: 函数名(实参1, 实参2,...)
# num1 = 80
# num2 = 9
# # 在执行函数的时候 就好比是a = num1 b = num2
# my_func(num1, num2)

# 通过一个函数 打印一句话 无论输入什么字符串
# 最终格式: 你好XX
# def my_func(name):
#     print("你好%s" % name)
#     print("你好%s" % name)
#     print("你好%s" % name)
#     print("你好%s" % name)
#
#
# my_func("小红")


# 定义一个函数 有三个参数 名字 年龄 手机号 调用函数 打印 名字:xx 年龄:xx 手机号:xxxx
def my_print_info(name, age, tel):
    print("姓名:%s 年龄:%d 电话:%s" % (name, age, tel))

# 调用
my_print_info("小明", 22, "13790909090")