# 定义一个字符串
a = "acbdf"

# <18>rfind
# 类似于 find()函数，不过是从右边开始查找.
# 从左侧到右侧查找
# ret1 = a.find("b")
# print(ret1)
# ret1 = a.rfind("b")
# print(ret1)


# <19>rindex
# 类似于 index()，不过是从右边开始. 异常


# <20>partition 开发中使用
# 把mystr以str分割成三部分,str前，str和str后
# ret2 = a.partition("c")
# print(type(ret2))
# print(ret2)

# <21>rpartition
# 类似于 partition()函数,不过是从右边开始.
ret3 = a.rpartition("c")
print(ret3)

