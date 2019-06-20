
# 以w方式打开文件 编码
# f = open("hmhm.txt", "w", encoding="utf-8")
# # 写入数据
# # 默认情况下如果在windows电脑中(中国) 保存中文编码格式为gbk (mac电脑或者是linux 没有问题)
# # 如果其他字符 例如abcd 编码格式为utf-8
# f.write("你好世界")
# # 关闭文件
# f.close()


# 以r方式打开文件 解码
# f = open("hmhm.txt", "r", encoding="utf-8")
# ret = f.read()
# print(ret)
# f.close()