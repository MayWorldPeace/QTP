from xml.dom import minidom

# class readXml():
#     def read_xml(self):
#         # 打开文件
#         root = minidom.parse("../DataXml/data.xml")
#         firstnode = root.getElementsByTagName("jia")[0]
#         secondnode = firstnode.getElementsByTagName("num1")[0].firstChild.data
#         return secondnode
#
# # 创建对象
# r = readXml()
# print(r.read_xml())


class readXml():
    def read_xml(self,filename,onenode,twonode):
        # 打开文件
        root = minidom.parse(filename)
        firstnode = root.getElementsByTagName(onenode)[0]
        secondnode = firstnode.getElementsByTagName(twonode)[0].firstChild.data
        return secondnode

# # 创建对象
# r = readXml()
# print(r.read_xml("../DataXml/data.xml","jia","num1"))
# print(r.read_xml("../DataXml/data.xml","jia","num2"))
