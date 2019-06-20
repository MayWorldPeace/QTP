
# for循环
# for-else 配合使用 带for循环完成后 会走else中的代码
# for i in range(5):
#     print(i)
# else:
#     print("else")


# for循环中 如果执行了break else中的代码将不再执行
# for i in range(5):
#     print(i)
#     if i == 2:
#         break
# else:
#     print("else")


# while循环
i = 0
while i < 5:
    print(i)
    if i == 2:
        break
    i += 1
else:
    print("else")


"""
无论for-else  还是 while-else 如果在for循环中 或者 while循环中 没有执行break 待for循环
或者while结束后 会执行else中的代码
当for循环或者while循环中的break执行 else中的代码将不会执行
"""

