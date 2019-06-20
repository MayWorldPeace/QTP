import os
# 1. 文件重命名
#
# os模块中的rename()可以完成对文件的重命名操作
#
# rename(需要修改的文件名, 新的文件名)
# os.rename("hm.txt", "hmhm.txt")


# 2. 删除文件
#
# os模块中的remove()可以完成对文件的删除操作
#
# remove(待删除的文件名)
# os.remove("hm[复件].txt")


# 3. 创建文件夹
# os.mkdir("黑马")


# 4. 获取当前目录
# ret = os.getcwd()
# 获取的是绝对路径(可以看到盘符)
# print(ret)

# 5. 改变默认目录
# ../ 上一级目录 ./ 或者../ 都是相对路径
# os.chdir("../")
# ret= os.getcwd()
# print(ret)

# 6. 获取目录列表
# .idea python项目中个一个隐藏文件
# 文件名以.开头的就是一个隐藏文件
# my_list = os.listdir()
# print(my_list)

# 7. 删除文件夹
# os.rmdir("黑马")