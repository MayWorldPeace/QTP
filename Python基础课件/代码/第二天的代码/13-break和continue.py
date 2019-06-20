
# while循环和break配合使用
# 如果执行了break  while循环将终止 break后面的也就不再执行 (直接跳出循环)
# 定义一个变量
# i = 0
# while i < 5:
#     print(i)
#     # 如果i == 2 执行下break
#     if i == 2:
#         break
#     i += 1
#
# print("测试")


# for循环和break配合使用
# 如果执行了break  for循环将终止 break后面的也就不再执行 (直接跳出循环)
# for i in range(5):
#     print(i)
#     if i == 2:
#         break
#
# print("测试")


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# while循环和continue配合使用
# 如果在while中 如果执行了continue 将提前结束本次循环 continue后面的代码将不再执行
# 定义一个变量
# i = 0
# while i < 5:
#     i += 1
#     if i == 2:
#         continue
#         print("测试")
#     print(i)


# for循环和continue 配合使用
# 如果在for中 如果执行了continue 将提前结束本次循环 continue后面的代码将不再执行
for i in range(5):
    if i == 2:
        continue
    print(i)
