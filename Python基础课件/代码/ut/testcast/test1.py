# 导入unittest
import unittest
from funcdemo.CalcDemo import Calc
from Commonlib.ReadXml import readXml

# # 创建对象
# r = readXml()
# a = int(r.read_xml("../DataXml/data.xml","jia","num1"))
# b = int(r.read_xml("../DataXml/data.xml","jia","num2"))
# ex = int(r.read_xml("../DataXml/data.xml","jia","expect"))

# 优化
r = readXml()


# 继承
class Test1(unittest.TestCase):
    # 初始化函数
    def setUp(self):
        print("开始")
    # 结结束函数

    def tearDown(self):
        print("结束")

    def test001(self):
        #创建对象
        ca = Calc()
        res1 = ca.jia(int(r.read_xml("../DataXml/data.xml","jia","num1")),int(r.read_xml("../DataXml/data.xml","jia","num2")))
        # 判断
        self.assertEqual(res1,int(r.read_xml("../DataXml/data.xml","jia","expect")))

    def test002(self):
        # 创建对象
        ca = Calc()
        res2 = ca.jian(int(r.read_xml("../DataXml/data.xml","jian","num1")),int(r.read_xml("../DataXml/data.xml","jian","num2")))
        #进行比对
        self.assertEqual(res2,int(r.read_xml("../DataXml/data.xml","jian","expect")))

if __name__ == '__main__':
    unittest.main()
