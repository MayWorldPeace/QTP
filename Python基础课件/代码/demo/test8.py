import unittest


class Demo(unittest.TestCase):

    def setUp(self) -> None:
        print("nihao")

    def tearDown(self) -> None:
        print("bye")

    def test_01(self):
        print("001")

    def test_002(self):
        print("002")

    def hello(self):
        print("ello")

if __name__ == '__main__':
    unittest.main()