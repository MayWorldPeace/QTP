# 自定义一个英雄类
class Hero(object):

    # 构造方法
    def __init__(self, name):
        # 设置属性的值
        self.name = name

    # 输出一个字符串(追踪对象属性信息变化)
    def __str__(self):
        return "名字:%s" % self.name

    # 监听对象销毁后会走的方法
    def __del__(self):
        print("再见")

# # 创建一个对象
# gailun = Hero("盖伦")
# # 程序员杀死对象
# del gailun
#
# input("停在这里")
#
# # python中是自动内存管理


# 创建一个对象
gailun = Hero("盖伦")

gailun1 = gailun
gailun2 = gailun

# 引用计数问题
del gailun
del gailun1
del gailun2
input("停在这里")

# python中是自动内存管理
