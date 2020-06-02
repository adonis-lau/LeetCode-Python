#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
61. Rotate List
https://leetcode.com/problems/rotate-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 判断链表是否为空
        if not head or not head.next:
            return head

        # 将链表连接成环，并记录链表长度
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head

        # 找到新的尾结点，新尾结点位置为 n - k % n - 1
        # 第 n - k % n 个节点为新的头结点
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        # 将新的尾结点的下一节点设置为空
        new_tail.next = None

        return new_head


# 创建链表
def create_list(*param):
    root = None
    for i in range(len(param)):
        tmp = ListNode(param[(len(param) - 1) - i])
        tmp.next = root
        root = tmp
    return root  # 返回根节点

solution = Solution()
res = solution.rotateRight(create_list(1, 2, 3, 4, 5), 0)
while res is not None:
    print(res.val)
    res = res.next