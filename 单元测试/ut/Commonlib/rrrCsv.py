import csv
class red():
    def read_cs(self):
        lists =[]
        csv_cc = csv.reader(open("../DataXml/data2.csv","r"))
        for csv_con in csv_cc:
            # print(csv_con)
            lists.append(csv_con)

        return lists

if __name__ =='__main__':
    cccc = red()
    cccc.read_cs()