#想要读取csv文件的内容需要导包
import csv
#创建类
class readcsv():
    def read_csv(self,filename):
        my_list =[]
        csv_context = csv.reader(open(filename,"r"))
        # print(csv_context)
        for csv_con in csv_context:
            my_list.append(csv_con)
        # print(my_list)
        my_lists=my_list[1:]

        return my_lists
# # 创建对象
# cs = readcsv()
# aaa = cs.read_csv("../DataXml/data5.csv")
# print(aaa)