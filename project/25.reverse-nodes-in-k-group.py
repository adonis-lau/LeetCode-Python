#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
25. Reverse Nodes in k-Group
https://leetcode.com/problems/reverse-nodes-in-k-group/submissions/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count = 0
        cur = head
        # 计算出链表的总长度
        while cur:
            count += 1
            cur = cur.next
        if k <= 1 or count < k:
            return head

        pre = None
        cur = head
        # 每次只交换 k 个值
        for _ in range(k):
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        # 剩下的值下次递归是再交换
        head.next = self.reverseKGroup(cur, k)
        return pre


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
res = solution.reverseKGroup(l1, 2)

while res is not None:
    print(res.val)
    res = res.next
