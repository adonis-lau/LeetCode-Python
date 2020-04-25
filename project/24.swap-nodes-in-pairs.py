#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
24. Swap Nodes in Pairs
https://leetcode.com/problems/swap-nodes-in-pairs/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head
        prev = None
        while cur and cur.next:
            # 第二个结点会变成头结点
            if head == cur:
                head = cur.next

            next = cur.next.next

            # 交换 cur 和 next
            if prev:
                prev.next = cur.next

            cur.next.next = cur
            cur.next = next
            prev = cur

            cur = next

        return head


# 创建链表
def create_list(*param):
    root = None
    for i in range(len(param)):
        tmp = ListNode(param[(len(param) - 1) - i])
        tmp.next = root
        root = tmp
    return root  # 返回根节点

l1 = create_list(1, 2, 3, 4)

solution = Solution()
res = solution.swapPairs(l1)

while res is not None:
    print(res.val)
    res = res.next
