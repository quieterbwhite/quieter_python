# -*- coding=utf-8 -*-
# Created Time: 2017年09月26日 星期二 09时52分43秒
# File Name: 05_design_sington.py

class MyClass(object):

    def __init__(self):
        pass

    @staticmethod
    def instance():
        if not hasattr(MyClass, "_instance"):
            MyClass._instance = MyClass()

        return MyClass._instance

    def func(self):
        pass


def main():

    c1 = MyClass().instance()

    c2 = MyClass().instance()

    print "id(c1): ", id(c1)
    print "id(c2): ", id(c2)

if __name__ == "__main__":
    main()
