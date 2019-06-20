# 自定义一个师傅类-(古法)
class Master(object):

    # 构造方法
    def __init__(self):
        self.kongfu = "古法煎饼果子配方"

    # 擅长做煎饼果子
    def make_cake(self):
        print("按照<%s>制作煎饼果子" % self.kongfu)


# 自定义一个新东方-(现代)
class School(object):

    # 构造方法
    def __init__(self):
        self.kongfu = "现代煎饼果子配方"

    # 擅长做煎饼果子
    def make_cake(self):
        print("按照<%s>制作煎饼果子" % self.kongfu)


# 自定义一个徒弟类
class Prentice(Master, School):

    # 构造方法
    def __init__(self):
        self.kongfu = "猫氏煎饼果子配方"

    # 擅长做煎饼果子
    # 子类继承了父类 子类重写父类已有的方法
    # 重写: 子类继承父类 做自己特有的事情
    def make_cake(self):
        print("按照<%s>制作煎饼果子" % self.kongfu)


# 自定义对象 大猫
# 如果子类的方法名(子类已经重写父类的方法)和父类的相同的时候 默认会使用子类的方法
# 为什么会使用子类的属性(kongfu) 子类重写了父类已有的__init__方法
damao = Prentice()
damao.make_cake()



