#!/usr/bin/python3
# -*- coding: UTF-8 -*-


"""
82. Remove Duplicates from Sorted List II
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
解题思路：
创建新的链表，尾插
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 创建空链表当做链表头节点
        dummy = ListNode(0)
        # 创建一个尾巴，用于尾插法
        tail = dummy
        left = right = head
        while left is not None:
            # 只要r不为空并且与l的值相等则一直向后移动
            while right is not None and right.val == left.val:
                right = right.next

            # 若长度为1，则通过尾插法加入。
            if left.next == right:
                # 基本的尾插法
                tail.next = left
                tail = left
                # 这里记得将尾部的后面置为null，不然可能后面会带着一些其他的节点。
                tail.next = None
            left = right

        return dummy.next


# 创建链表
def create_list(*param):
    root = None
    for i in range(len(param)):
        tmp = ListNode(param[(len(param) - 1) - i])
        tmp.next = root
        root = tmp
    return root  # 返回根节点


l1 = create_list(1, 1, 2, 2, 3, 4, 5)
solution = Solution()
res = solution.deleteDuplicates(l1)
p = res
while p is not None:
    print(p.val)
    p = p.next
