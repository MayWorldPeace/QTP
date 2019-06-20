# 定义类 -> 自定义类(由程序员创建的类)

# python创建的list类
# class list(object):

# 开发 王者荣耀 我想创建一个悟空(对象)  -> 类(英雄类) -> 类型 (Hero)

# 自定义类
# class 标识这一个类


# 快速查看某个类的源文件实现 点住类名 ctrl + 鼠标左键

# 三种类的创建方式都是在python2.x产生的
# object 是所有类的父类
# 03是后期产生的
# 01 02 叫做经典类 他们都是没有父类(基类)的
# 03 叫做新式类

# 在phthon3.x中 无论 写 01  02  03哪种方式 都是继承与object 类
# 但是如果在python2.x中他是区分 01 02 相同 而03是有父类的

# 01
# class Hero:
#     pass
#
# # 02
# class Hero():
#     pass

# 03 建议这么写
class Hero(object):
    pass

