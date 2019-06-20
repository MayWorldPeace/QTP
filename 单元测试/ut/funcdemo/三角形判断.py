class Sjx():
    # 输入三条边，进行判断，是否等边、等腰、普通三角形，否则提示不能组成三角形，用函数来实现
    def sjxpd(self,a,b,c):
        if a + b > c and a + c > b and b + c > a:
            if a == b and b == c:
                return 1
            elif a == b or b == c or a == c:

                return 2
            else:
                return 3
        else:
            # print("不能组成三角形")
            return -1

if __name__ == '__main__':
   s = Sjx()
   s.sjxpd(1,2,3)