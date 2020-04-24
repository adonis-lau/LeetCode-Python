#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/
"""

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        tmp = head = ListNode(0)

        # 取出每个链表中的值放入数组
        for li in lists:
            cur = li
            while cur:
                heap.append(cur.val)
                cur = cur.next
        # 对数组排序
        heap.sort()
        # 将数组放入链表
        for val in heap:
            tmp.next = ListNode(val)
            tmp = tmp.next

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
lists = [l1, l2]

solution = Solution()
res = solution.mergeKLists(lists)

while res is not None:
    print(res.val)
    res = res.next
