# elif == else if

# 定义一个变量 记录分数
score = -100
# 通过判断分数 得到一个描述(优 良 中 差)
# s >= 90  优
# s >= 80 and s < 90 良
# s >= 60 and s < 80 中
# s >= 0 and s < 60  差
# if score >= 90:
#     print("优")
# elif score >= 80 and score < 90:
#     print("良")
# elif score >= 60 and score < 80:
#     print("中")
# elif score >= 0 and score < 60:
#     print("差")
#
# print("测试")


# if score >= 90:
#     print("优")
# elif score >= 80:
#     print("良")
# elif score >= 60:
#     print("中")
# elif score >= 0:
#     print("差")


# 可以包含判断负分
if score >= 90:
    print("优")
elif score >= 80:
    print("良")
elif score >= 60:
    print("中")
elif score >= 0:
    print("差")
else:
    print("卷面不整洁")

print("测试")


