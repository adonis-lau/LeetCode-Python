#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

解析：
https://blog.csdn.net/weixin_40418213/article/details/93292449?depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2&utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        # curr is the dummy linked list
        curr = head
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            sum = x + y + carry
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            # pointer move to the next node
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        # finally there need to carry
        if carry > 0:
            curr.next = ListNode(1)
        return head.next


# 创建链表
def create_list(*param):
    root = None
    for i in range(len(param)):
        tmp = ListNode(param[(len(param) - 1) - i])
        tmp.next = root
        root = tmp
    return root  # 返回根节点


l1 = create_list(2, 4, 3)
l2 = create_list(5, 6, 4)
solution = Solution()
res = solution.add_two_numbers(l1, l2)
p = res
while p is not None:
    print(p.val)
    p = p.next
