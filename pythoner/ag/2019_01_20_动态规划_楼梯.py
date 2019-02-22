# -*- coding=utf-8 -*-

"""
下楼梯每次有两种走法

动态规划
"""

def stair(n):
    """  """

    if n < 1:
        return 0

    if n == 1:
        return 1

    if n == 2:
        return 2

    return stair(n-1) + stair(n-2)

def stair_rem(n, result_dict):
    """ 增加备忘录算法 - 暂存计算结果 """

    if n < 1:
        return 0

    if n == 1:
        return 1

    if n == 2:
        return 2

    if str(n) in result_dict:
        return result_dict[str(n)]
    else:
        result = stair_rem(n-1, result_dict) + stair_rem(n-2, result_dict)
        result_dict[str(n)] = result
        return result

def stair_from_bottom(n):
    """ 动态规划 - 自底向上

    上面一个方法从时间上进行了优化
    这个方法继续从空间上优化
    只存储两个临时变量

    这就是动态规划
    利用简洁的自底向上的递推方式
    实现了时间和空间上的最优化
    """

    if n < 1:
        return 0

    if n == 1:
        return 1

    if n == 2:
        return 2

    a = 1
    b = 2
    temp = 0

    for i in range(3, n+1):
        temp = a + b
        a = b
        b = temp

    return temp

def main():

    m = stair(10)
    print m

    result_dict = {}
    n = stair_rem(10, result_dict)
    print n

    x = stair_from_bottom(10)
    print x

if __name__ == "__main__":
    main()
