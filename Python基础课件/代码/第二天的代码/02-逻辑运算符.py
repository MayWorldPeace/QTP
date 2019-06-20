# and	x and y	布尔"与"：如果 x 为 False，x and y 返回 False，否则它返回 y 的值。	True and False， 返回 False。
# or	x or y	布尔"或"：如果 x 是 True，它返回 True，否则它返回 y 的值。	False or True， 返回 True。
# not	not x	布尔"非"：如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not True 返回 False, not False 返回 True


# # 定义一个变量 记录名字
# my_name = "mngr"
# # 定义一个变量 记录密码
# my_passwd = "12345"
#
# # 使用and 且 或者 与
# # 同真为真(True) 一假为假(False)
# # 进行判断
# if my_name == "mngr" and my_passwd == "12345":
#     print("用户名和密码正确登录成功")

# or 或
# 定义一个变量 记录名字
# my_name = "mngr1"
# # 定义一个变量 记录密码
# my_passwd = "12345"
#
# # 全假为假 一真则真
# if my_name != "mngr" or my_passwd != "12345":
#     print("您输入的用户名或者密码错误!!!")
#
# print("测试")

# not 非 (取反)
# 非真则假 非假则真
is_man = False
print(is_man)
if not is_man:
    print("是女性")