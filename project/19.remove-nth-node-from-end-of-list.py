#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 创建空链表当做链表头节点
        dummy = l = ListNode(0)
        # 将传入的链表添加到dummy
        dummy.next = r = head
        # 循环 n 次，为删除第 n 个节点做准备
        for _ in range(n):
            r = r.next

        # 将 l 移动 n - r 个长度，l 对应倒数第 n 个节点
        while r:
            l, r = l.next, r.next

        # 从末尾删除第n个元素
        l.next = l.next.next
        return dummy.next


# 创建链表
def create_list(*param):
    root = None
    for i in range(len(param)):
        tmp = ListNode(param[(len(param) - 1) - i])
        tmp.next = root
        root = tmp
    return root  # 返回根节点


l1 = create_list(1, 2, 3, 4, 5)
solution = Solution()
res = solution.removeNthFromEnd(l1, 5)
p = res
while p is not None:
    print(p.val)
    p = p.next
