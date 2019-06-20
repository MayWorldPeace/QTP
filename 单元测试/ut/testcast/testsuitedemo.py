import unittest
from testcast.sjxtest import sjxpd
from Commonlib.HTMLTestRunner import HTMLTestRunner


class SuiteTest(unittest.TestCase):
    def test_suite(self):
        # 创建列表
        case_list = ['test001']
        # 创建测试套件
        mysuit = unittest.TestSuite()
        # 使用循环将测试用例放入到测试套件中
        for case in case_list:
            mysuit.addTest(sjxpd(case))
        # # 运行测试套件中的每一个测试用例，并为每一个测试用例生成测试报告
        # unittest.TextTestRunner(verbosity=2).run(mysuit)
        # 生成html格式的测试报告
        with open('../report.html','wb') as f:
            HTMLTestRunner(
                stream=f,
                title='计算器单元测试',
                description="黑马测试一期",
                verbosity=2 # 为每个测试用例生成测试报告


            ).run(mysuit)
if __name__ == '__main__':
    unittest.main()
