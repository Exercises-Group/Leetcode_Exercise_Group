# -*- coding: utf-8 -*- 
"""
Create on : 2022/6/5
@Author   : Xiao QingLin 
@File    : two_sum  
"""

"""
题目链接： https://leetcode.cn/problems/two-sum/
"""


def two_sum_1(nums: list[int], target: int) -> tuple[int, int]:
    """
    暴力破解
    关键点：同一个元素不能重复出现，第二层遍历时，起始位置index + 1
    :param nums:
    :param target:
    :return:
    """
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            if target - nums[j] == nums[i]:
                return i, j


def two_sum_2(nums: list[int], target: int) -> tuple[int, int]:
    """
    哈希表
    关键点：字典的键值设置{num: index}  -> key: num  value: index
           遍历时num时，判断target-num是否存在字典中，否，放入num，避免同一元素出现
    :param nums:
    :param target:
    :return:
    """
    result = {}
    for i, num in enumerate(nums):
        if target - num in result:
            return result[target - num], i
        result[num] = i
