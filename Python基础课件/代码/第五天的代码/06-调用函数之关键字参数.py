
#定义一个函数
# python是一个弱类型
def my_print(name, age, no):
    print("我的名字:%s" % name)
    print("我的年龄:%d" % age)
    print("学号:%s" % no)

# 调用-> 位置参数
# my_print("小明", 20)


# 关键字参数
# 调用函数的时候使用的是函数的形参名
# my_print(age=22, name="老王")
# my_print(name="老王", age=22)

# 调用函数的时候 使用了位置和关键字参数混合
# 如果混合使用 需要叫位置参数在前 关键字参数再后
# 如果某个参数使用了关键字参数 后面的都需要使用关键字参数
my_print("小明", age=20, no="007")
