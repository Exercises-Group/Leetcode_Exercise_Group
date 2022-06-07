# -*- coding: utf-8 -*- 
"""
Create on : 2022/6/6
@Author   : Xiao QingLin 
@File    : 3sum  
"""


def three_sum(nums):
    """
    关键点： 排序 + 双指针
    三数之和 < 0  移动 左指针 + 1
    三数之和 > 0  移动 右指针 - 1
    左边遇到重复值：左指针 + 1
    右边遇到重复值：右执政 - 1
    当 左指针 大于等于又指针 返回结果
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    length = len(nums)
    res = []
    if not nums or length < 3:
        return res
    nums.sort()
    for i in range(length - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, length - 1
        while left < right:
            temp = nums[i] + nums[left] + nums[right]
            if temp > 0:
                right -= 1
            elif temp < 0:
                left += 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                right -= 1
                left += 1
    return res


def test_3sum():
    test_cases = [([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]), ([], []), ([0], [])]
    for test_case, result in test_cases:
        assert three_sum(test_case) == result


if __name__ == '__main__':
    test_3sum()
