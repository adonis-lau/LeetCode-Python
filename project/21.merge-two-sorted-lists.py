#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

注意事项：
初始化的链表已经有序
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        temp = head = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        if l2 is None:
            temp.next = l1
        else:
            temp.next = l2
        return head.next


# 创建链表
def create_list(*param):
    root = None
    for i in range(len(param)):
        tmp = ListNode(param[(len(param) - 1) - i])
        tmp.next = root
        root = tmp
    return root  # 返回根节点


l1 = create_list(2, 5, 6)
l2 = create_list(1, 1)

solution = Solution()
res = solution.mergeTwoLists(l1, l2)

while res is not None:
    print(res.val)
    res = res.next
