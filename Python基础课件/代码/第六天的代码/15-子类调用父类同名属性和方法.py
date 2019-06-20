
# 自定义师傅类-古法
class Master(object):

    # 方法
    def make_cake(self):
        print("古法煎饼果子")


# 自定义师傅类-现代
class School(object):

    # 方法
    def make_cake(self):
        print("现代煎饼果子")


# 自定义一个徒弟类
class Prentice(Master, School):

    # 方法
    def make_cake(self):
        print("猫氏煎饼果子")

    # 古法
    def make_old_cake(self):

        Master.make_cake(self)

    # 现代
    def make_new_cake(self):

        School.make_cake(self)


# 自定义一个对象 大猫
damao = Prentice()
# 猫氏
damao.make_cake()
# 古法
damao.make_old_cake()
# 现代
damao.make_new_cake()