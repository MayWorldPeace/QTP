import unittest
from funcdemo.三角形判断 import Sjx
from Commonlib.ReadXml import readXml
# 创建对象
r = readXml()

class Test(unittest.TestCase):
    # 初始化函数
    def setUp(self):
        print("开始")
    # 结结束函数

    def tearDown(self):
        print("结束")
    def test001(self):
        s = Sjx()
        res1 = s.sjxpd(int(r.read_xml("../DataXml/data1.xml","db","b1")),int(r.read_xml("../DataXml/data1.xml","db","b2")),int(r.read_xml("../DataXml/data1.xml","db","b3")))
        self.assertEqual(res1,r.read_xml("../DataXml/data1.xml","db","expect"))

    def test002(self):
        s = Sjx()
        res1 = s.sjxpd(int(r.read_xml("../DataXml/data1.xml", "dy", "b1")),
                       int(r.read_xml("../DataXml/data1.xml", "dy", "b2")),
                       int(r.read_xml("../DataXml/data1.xml", "dy", "b3")))
        self.assertEqual(res1, r.read_xml("../DataXml/data1.xml", "dy", "expect"))


if __name__ == '__main__':
    unittest.main()

