
# 自定义一个英雄类
class Hero(object):

    # 构造方法
    def __init__(self, name, hp, atk):
        # 设置属性的值
        self.name = name
        self.hp = hp
        self.atk = atk

    # # 打印信息
    # def info(self):
    #     print(self.name, self.hp, self.atk)

    # 实现下父类已有的魔法方法
    # 不可以添加参数(形参)
    # 会返回一个字符串
    # 追踪对象属性信息变化
    def __str__(self):
        return "名字:%s 血量:%d 攻击力:%d" % (self.name,self.hp,self.atk)

# 悟空
wukong = Hero("悟空", 4000, 400)
# wukong.info()
# 默认情况下 打印的是对象的16进制地址
# 如果类中实现了__str__方法 如果打印对象名 会输出的是__str__方法中的返回值(字符串)
print(wukong)

# __str__一般用于程序员开发调试代码
