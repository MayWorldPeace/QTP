
# #以只读文件模式打开文件
# f = open("hm.txt", "r", encoding="utf-8")
# # 读取文件中数据
# result = f.read()
# # 读取文件完成后 关闭文件
# f.close()


#通过此方式打开文件 不需要关闭
# as 是给文件起了名字
with open("hm.txt", "r", encoding="utf-8") as f:
    # 读取文件中数据
    result = f.read()
    print(result)