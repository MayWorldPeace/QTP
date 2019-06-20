import unittest
from Commonlib.rrrCsv import red
from funcdemo.CalcDemo2 import Clac

class TestDemo(unittest.TestCase):

    def test001(self):
        rrr1 = red()
        for xxx in rrr1.read_cs():
            xy =Clac();
            # print(xy)
            res1 = xy.jia(int(xxx[0]),int(xxx[1]))
            self.assertEqual(res1,int(xxx[2]))



if __name__ == '__main__':
    unittest.main()

