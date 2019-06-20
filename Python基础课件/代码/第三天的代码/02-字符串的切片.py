# 切片的语法：[起始:结束(开区间):步长]
# 字符串是不可变的(复制版的)
a = "abcdef"
# 'abc' -> a[0:3]   或者  a[:3]
# 如果是从头部开始 0可以省略
# ret1 = a[:3]
# print(ret1)
# 验证字符串是不可变的
# print(a)
 # 'ace'  a[:5:2]  或者  a[0:5:2] 或者 a[::2]
 #默认步长是1
# ret2 = a[::2]
# print(ret2)

# 'bd'
# ret3 = a[1:4:2]
# print(ret3)

# 'fdb'
# ret4 = a[::-2]
# print(ret4)

# 'fd'
# ret5 = a[-1:-4:-2]
# print(ret5)
