#以只写文件模式打开文件
f = open("hm.txt", "w", encoding="utf-8")
# 写入数据到文件中
f.write("hello python!!!")
# 写入数据完成后 关闭文件
f.close()