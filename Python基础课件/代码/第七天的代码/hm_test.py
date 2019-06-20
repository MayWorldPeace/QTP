# 测试人员自己创建的模块
#如果一个模块被另一个模块导入后 就把这个模块里面可以执行的代码都执行一遍
import hm_sum




def main():
    print(hm_sum.name)
    ret = hm_sum.add2num(10, 30)
    print(ret)
    p = hm_sum.Person()
    p.eat()



if __name__ == '__main__':
    main()