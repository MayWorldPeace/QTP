import unittest
from funcdemo.CalcDemo3 import calcdemo
from Commonlib.Readcsv1 import readcsv

# 创建对象
rea = readcsv()

# #调用方法
# m_list = rea.read_csv()
# print(m_list)
# for m_li in m_list:
#     print(m_li)
#     print(m_li[0])
#     print(m_li[1])
# 测试类
class calctest1(unittest.TestCase):
    def setUp(self):
        print("开始")

    def tearDown(self):
        print("结束")

    def test001(self):
        m_list = rea.read_csv()
        for m_li in m_list:
            # 创建对象
            ca = calcdemo()
            act = ca.add(int(m_li[0]),int(m_li[1]))
            self.assertEqual(act,int(m_li[2]))
if __name__ == '__main__':
    unittest.main()
