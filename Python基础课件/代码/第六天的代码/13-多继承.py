# 自定义一个师傅类-(古法)
class Master(object):

    # 构造方法
    def __init__(self):

        self.kongfu = "古法煎饼果子配方"

    # 擅长做煎饼果子
    def make_cake(self):
        print("按照<%s>制作煎饼果子" % self.kongfu)

    # 大烟袋
    def dayandai(self):
        print("大烟袋")


# 自定义一个新东方-(现代)
class School(object):

    # 构造方法
    def __init__(self):
        self.kongfu = "现代煎饼果子配方"

    # 擅长做煎饼果子
    def make_cake(self):
        print("按照<%s>制作煎饼果子" % self.kongfu)

    # 小烟袋
    def xiaoyandai(self):
        print("小烟袋")


# 自定义一个徒弟类
class Prentice(Master, School):
    pass

# 自定义一个大猫
damao = Prentice()
# 为什么会打印的是第一个父类的属性-> 古法煎饼果子配方?
#如果两个父类的方法名(__init__ )相同
print(damao.kongfu)
# 如果两个父类的方法名相同 子类会执行第一个父类的
damao.make_cake()
# 如果两个父类的方法名不同 子类会分别执行
damao.dayandai()
damao.xiaoyandai()
