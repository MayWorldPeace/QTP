
# # 创建一个原文件
# # 打开文件
# old_f = open("hm.txt", "w")
# # 写入数据
# old_f.write("helloworld")
# # 关闭文件
# old_f.close()


# 做备份文件 -> 伪代码
# 01 打开hm.txt文件
# 02 读取hm.txt文件的数据
# 03 创建一个hm[复件].txt文件
# 04 把从hm.txt读取的数据写入到hm[复件].txt文件中
# 05关闭文件

# 01 打开hm.txt文件
old_f = open("hm.txt", "r")
# 02 读取hm.txt文件的数据
result = old_f.read()

# 03 创建一个hm[复件].txt文件
new_f = open("hm[复件].txt", "w")
# 04 把从hm.txt读取的数据写入到hm[复件].txt文件中
new_f.write(result)

# 05关闭文件
old_f.close()
new_f.close()









