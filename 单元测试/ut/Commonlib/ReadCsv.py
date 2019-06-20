import csv
class readCsv():
    def read_csv(self):
        list =[]
        # 读取
        csv_file = csv.reader(open("../DataXml/data2.csv","r"))
        for csv_con in csv_file:
            print(csv_con)
            list.append(csv_con)
        print(list[0])
        return list
# re = readCsv()
# ll = re.read_csv()
# def aaa():
#     leng =len(ll)
#
#     for cs in range(leng):
#
#
#
# aaa()
