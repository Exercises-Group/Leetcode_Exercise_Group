# -*- coding: utf-8 -*- 
"""
Create on : 2022/6/6
@Author   : Xiao QingLin 
@File    : is_palindrome  
"""
"""
2022-06-05 100-2 判断是否为回文数
https://leetcode.cn/problems/palindrome-number/ 
"""


def is_palindrome_1(x):
    """
    关键点在于： while 循环的判断条件和什么时候跳出循环
    :type x: int
    :rtype: bool
    """
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    s = str(x)
    start, end = 0, len(s) - 1
    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            return False
    return True


def is_palindrome_2(x):
    """
    除基取余构数法
    2个关键点：
    1.边界条件(x 不等于0, 能被10整除的数)；
    2.循环的结束条件；当通过余数不等构建的数大于等于x时，退出。
    :param x:
    :return:
    """
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    rev_num = 0
    while x > rev_num:
        rev_num = rev_num * 10 + x % 10
        x //= 10
    return x == rev_num or x == rev_num // 10
