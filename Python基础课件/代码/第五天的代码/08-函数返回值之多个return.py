

# 定义一个函数 当执行函数的时候 传入一个分数 可以返回一个字符串 (优 良 中 差)

# 包含多个return
def my_func(score):
    # 对分数进行判断
    if score >= 90:
        return "优"
    elif score >= 80:
        return "良"
    elif score >= 60:
        return "中"
    elif score >= 0:
        return "差"
    # 他不会执行 因为在第11行已经执行了return
    print("测试")


ret = my_func(89)
print(ret)

def my_func1():
    print("开始")
    # 只要函数中执行了return 提前结束函数的执行 而且return后面的代码将不再执行
    return "3.14"
    print("开始1")
    return 20
    print("结束")

ret = my_func1()
print(ret)
print("测试")
"""
开始
3.14
测试
"""