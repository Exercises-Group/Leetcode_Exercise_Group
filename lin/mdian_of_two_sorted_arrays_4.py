# -*- coding: utf-8 -*- 
"""
Create on : 2022/6/9
@Author   : Xiao QingLin 
@File    : mdian_of_two_sorted_arrays_4  
"""
"""
https://leetcode.cn/problems/median-of-two-sorted-arrays/
https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/908004/Python-Binary-Search-(Diagram) 
"""


def find_median_sorted_arrays(nums1, nums2) -> float:
    """
    中位数位置：
    1. 偶： (length + 1) / 2  or length / 2
    2. 奇： (length + 1) / 2
    合： sizeleft = m + n + 1 / 2


    1.红线左右的元素个数相等，或者左边元素的个数比右边个数多1个；
    2.红线左右的所有元素的数值 <= 红线右边的所有元素的数值[交叉小于等于]；（ 奇分左多一个， 偶分右多一个）


    A 1 3 6 9 20 25
    B 2 4 7 16 17 28
    start: 0
    end:  6 = (length + 1) / 2
    Apart: 3 = (0 + 6) / 2   apart left < bpart right
    Bpart: 3 = 6 - 3         bpart left < apart right
                      奇数：  max (aprt left, bpart left) -> max_value
                      偶数：  avg(max_value, min(aprt right, bpart right))
    """
    n1, n2 = len(nums1), len(nums2)
    while n1 > n2:
        return find_median_sorted_arrays(nums2, nums1)
    left, right = 0, n1
    k = (n1 + n2 + 1) // 2
    while left < right:
        x = left + (right - left) // 2
        y = k - x
        if nums1[x] < nums2[y - 1]:
            left = x + 1
        else:
            right = x
    x, y = left, k - left
    if x == 0:
        m1 = nums2[y - 1]
    elif y == 0:
        m1 = nums1[x - 1]
    else:
        m1 = max(nums1[x-1], nums2[y-1])
    if (n1 + n2) & 1:
        return m1

    if x == n1:
        m2 = nums2[y]
    elif y == n2:
        m2 = nums1[x]
    else:
        m2 = min(nums1[x], nums2[y])
    return (m1 + m2) / 2