# 自定义一个类 犬类
class Dog(object):

    # 构造方法
    def __init__(self, new_name, new_age, new_color="白色"):
        # 给对象的属性赋值
        self.name = new_name
        self.age = new_age
        self.color = new_color

    # 会吃骨头
    def eat(self):
        print("会吃骨头")

    # 定义一个方法
    def info(self):
        print("名字:%s" % self.name)
        print("年龄:%d" % self.age)
        print("毛色:%s" % self.color)
        print("="*30)

# 创建旺财
wangcai = Dog("旺财", 5)
wangcai.info()

# 创建斗牛犬
douniu = Dog("斗牛犬", 4)
douniu.info()



# 自定义学生类 有姓名 年龄 学号 80%学生都20岁 学生会学习 可以说出自己的的信息
# 创建两个学生 xx xxx
class Student(object):

    def __init__(self, name, no, age=20):
        # 设置属性
        self.name = name
        self.no = no
        self.age = age

    # 会学习
    def study(self):
        print("会学习")

    # 打印信息
    def info(self):
        print(self.name, self.age, self.no)


# 小明
xiaoming = Student("小明", "007")
xiaoming.info()

