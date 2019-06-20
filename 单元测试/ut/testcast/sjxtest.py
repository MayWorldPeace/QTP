import unittest
from Commonlib.Readcsv1 import readcsv
from funcdemo.三角形判断 import Sjx
r2 =readcsv()
class sjxpd(unittest.TestCase):
    def setUp(self):
        print("开始")
    def tearDown(self):
        print("结束")

    def test001(self):
        my_list = r2.read_csv("../DataXml/data5.csv")
        for m_li in my_list:
            sj =Sjx()
            act = sj.sjxpd(int(m_li[0]),int(m_li[1]),int(m_li[2]))
            self.assertEqual(act,int(m_li[3]))

if __name__ == '__main__':
    unittest.main()
