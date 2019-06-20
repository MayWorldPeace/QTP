# 定义一个字符串
a = "abcdef"

# <1>find
#获取对应字符串的下标索引
#如果查询到对应的字符串 会返回一个下标索引
#如果没有查询到 会返回一个-1
# ret1 = a.find("cdd")
# print(ret1)


# <2>index
# 跟find()方法一样，只不过如果str不在 mystr中会报一个异常.
# ret2 = a.index("cdd")
# print(ret2)


# <3>count
# 返回 str在start和end之间 在 mystr里面出现的次数
# ret3 = a.count("q")
# print(ret3)


# <4>replace
# 把 mystr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次.
# ret4 = a.replace("a", "w")
# print(ret4)
# print(a)

# 5>split
# 以 str 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串
# ret5 = a.split("ad")
# print(ret5)

#可以使用count来判断下字符的个数 如果字符的个数大于0 存在index
count = a.count("a")
#如果大于0
if count > 0:
    index = a.index("a")
    print(index)