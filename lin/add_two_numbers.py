# -*- coding: utf-8 -*- 
"""
Create on : 2022/6/7
@Author   : Xiao QingLin 
@File    : add_two_numbers  
"""

"""
https://leetcode.cn/problems/add-two-numbers/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    关键点：
    1. 两数相加，还需存进位、加进位；
    2. 检查每个节点的数据是否为null;
    3. 如何返回数据；
    :param l1:
    :param l2:
    :return:
    """
    dummy = tail = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        carry += (l1.val if l1 else 0) + (l2.val if l2 else 0)
        tail.next = ListNode(carry % 10)
        tail = tail.next
        carry //= 10
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next
