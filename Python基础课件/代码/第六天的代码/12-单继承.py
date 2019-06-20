
# 自定义一个师傅类
class Master(object):

    # 构造方法
    def __init__(self):

        self.kongfu = "古法煎饼果子配方"

    # 擅长做煎饼果子
    def make_cake(self):
        print("按照<%s>制作煎饼果子" % self.kongfu)


# 创建出一个李师傅
# lishifu = Master()
# print(lishifu.kongfu)
# lishifu.make_cake()


# 自定义一个徒弟类
# 子类继承了父类 就拥有了父类的"方法"和"属性"
# 子类拥有了父类的属性 是因为子类使用了父类的__init__(对属性赋值的地方)
class Prentice(Master):
    pass

# 自定义一个大猫
damao = Prentice()
print(damao.kongfu)
damao.make_cake()
