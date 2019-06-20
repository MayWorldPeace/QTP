
# 定义一个函数
def my_func1(a, b):
    print(a + b)


# 函数的调用 -> 位置参数调用函数
# 使用位置参数调用函数 需要注意实参的位置
# 实参的位置和形参的位置要一一对应
# TypeError: my_func1() missing 1 required positional argument: 'b'
# 如果实参传入的少一个实参 会报错
# my_func1(11)
