

# 自定义一个类 犬类
class Dog(object):

    # 构造方法
    # 在python中使用__开头 并以__结尾的方法 称之为魔法方法
    # 魔法方法是python提供给我们的
    # object的提供的魔法方法
    # 在特殊的情况下(python可以监听到你使用自己的类创建一个对象) 被python执行
    # 在自定义类(程序员自己写的类)中实现(重写)魔法方法 做自己特有的事情
    # 注意 当走进__init__方法的时候 对象已经创建成功
    def __init__(self):
        print("__init__")
        # 给对象的属性赋值
        self.name = "旺财"
        self.age = 5
        self.color = "灰色"

    # 会吃骨头
    def eat(self):
        print("会吃骨头")

    # 定义一个方法
    def info(self):
        print("名字:%s" % self.name)
        print("年龄:%d" % self.age)
        print("毛色:%s" % self.color)
        print("="*30)



# 通过自定义的类创建狗 -> 对象
# 特征 叫的名字都是旺财 年龄都是5岁 毛色都是灰色
wangcai1 = Dog()

# # 添加属性
# # 名字
# wangcai1.name = "旺财"
# # 年龄
# wangcai1.age = 5
# # 毛色
# wangcai1.color = "灰色"
# 调用对象方法
wangcai1.info()


wangcai2 = Dog()
# 添加属性
# 名字
# wangcai2.name = "旺财"
# # 年龄
# wangcai2.age = 5
# # 毛色
# wangcai2.color = "灰色"
# 调用对象方法
wangcai2.info()


wangcai3 = Dog()
# 添加属性
# 名字
# wangcai3.name = "旺财"
# # 年龄
# wangcai3.age = 5
# # 毛色
# wangcai3.color = "灰色"
# 调用对象方法
wangcai3.info()

