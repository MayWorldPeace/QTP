import unittest
from Testcase.testcase import Test
# 导入HtmlTextRunner，用于生成html的测试报告
from Commonlib.HTMLTestRunner import HTMLTestRunner

class SuitTest(unittest.TestCase):
    def test_suit(self):
        case_list = ['test_001','test_002','test_003','test_004']
        # 创建测试套件
        mysuit = unittest.TestSuite()

        # 循环将测试用例放到测试套件中
        for case in case_list:
            mysuit.addTest(Test(case))

        # 创建测试运行器,设置为每一个测试用例生成测试报告，运行测试套件中的测试用例
        # unittest.TextTestRunner(verbosity=2).run(mysuit)

        # 生成html测试报告
        with open('report.html','wb')as f:
            HTMLTestRunner(
                stream=f,           # 相当于f.write(报告)
                title='第一个测试报告',
                description='it黑马第一个测试报告',
                verbosity=2         # 为每个测试用例生成测试报告
            ).run(mysuit)


if __name__ == '__main__':
    unittest.main()
