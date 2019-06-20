
# return 的总结

# 01-作为函数的返回值
# 02-执行的函数提前结束 (为了提高性能考虑)

# 包含多个return
def my_func(score):
    if score < 0:
        print("您传入的分数有误!!!")
        # 函数的执行提前结束
        return
    print("测试")
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




# 提出需求 如果调用函数的人 传入的分数小于0 那么就人为传入的分数错误 告知函数的调用者
my_func(-10)

