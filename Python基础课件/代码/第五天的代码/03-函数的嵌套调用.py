
# 定义一个函数
def my_func1():
    print("my_func1开始")
    print("my_func1结束")


# 定义一个函数
def my_func2():
    print("my_func2开始")
    my_func1()
    print("my_func2结束")

# 执行函数
my_func2()
print("测试")
"""
# 最终打印结果
my_func2开始
my_func1开始
my_func1结束
my_func2结束
测试

"""