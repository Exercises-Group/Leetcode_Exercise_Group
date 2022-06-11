# -*- coding: utf-8 -*- 
"""
Create on : 2022/6/11
@Author   : Xiao QingLin 
@File    : longest_palindrome  
"""
"""
https://leetcode.cn/problems/longest-palindromic-substring/
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 两种判断条件 (中心扩展法)
        # DP - CABAC
        # B
        # ABA
        # CABAC
        n = len(s)

        def get_len(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        start = 0
        length = 0
        for i in range(n):
            cur = max(get_len(i, i), get_len(i, i + 1))
            if cur <= length:
                continue
            length = cur
            start = i - (cur - 1) // 2
        return s[start: start + length]
