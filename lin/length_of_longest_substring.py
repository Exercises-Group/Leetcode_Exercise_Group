# -*- coding: utf-8 -*- 
"""
Create on : 2022/6/8
@Author   : Xiao QingLin 
@File    : length_of_longest_substring  
"""

"""
https://leetcode.cn/problems/longest-substring-without-repeating-characters/
"""


def length_of_longest_substring(s):
    start = -1
    # 最长字串的长度
    max_length = 0
    # 记录遍历过的字符
    d = dict()

    for i in range(len(s)):
        # 两种情况：
        # 1. s[i] in d
        if s[i] in d and d[s[i]] > start:  # d[s[i]] > start 重复字符的时候，更新index
            start = d[s[i]]
            d[s[i]] = i
        else:  # 2. s[i] not in d， 写入dict中， 更新max_length
            d[s[i]] = i
            if i - start > max_length:
                max_length = i - start
    return max
