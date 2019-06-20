# 自定义一个悟空对象  他会走(方法 行为) 他有名字 悟空 有年龄 500 有血量 3000 攻击力 400(属性 特征)


# 自定义一个英雄类
class Hero(object):
    # 方法(实例 或者 对象)
    def move(self):
        # self 是谁? 哪个对象调用了这个方法 self就是哪个对象
        print(id(self))
        print("英雄会走")


# 无论是使用对象调用其类的方法 或者是属性 都是使用的"点"语法
# 使用类创建对象
wukong = Hero()
# 执行下对象方法
wukong.move()
# 给对象添加属性
# 名字
wukong.name = "悟空"
# 年龄
wukong.age = 20
# 血量
wukong.hp = 3000
# 攻击力
wukong.atk = 400

# 获取对象身上的属性
print(wukong.name, wukong.age, wukong.hp, wukong.atk)


# 什么时候才可以给对象添加属性?
# 先要有对象 才可以给这个对象添加属性

# 如何查看同一个类创建的多个对象 是否是一个对象呢?
# <__main__.Hero object at 0x00000000023EF860>  -> 16进制
# 保存到内存中 需要开辟内存空间(底层是二进制(0 , 1))
# 如果想查看10进制
# 37812320
print(id(wukong))

# huangzhong
# huangzhong = Hero()
# print(id(huangzhong))

# 了解 逢x进1
# 二进制 0 1
# 十进制 0 1 2...9 20
# 16进制 0 1 2...ABCDEF 10

# 在类的外面使用的是对象名
# 在类的方法里面 使用的是self
# 对象名 和 self 本身就是一个人


