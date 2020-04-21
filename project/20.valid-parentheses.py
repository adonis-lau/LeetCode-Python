#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        dict = {'(': ')', '[': ']', '{': '}'}
        for c in s:
            if c in dict.keys():
                stack.append(dict[c])
            elif c in dict.values():
                # pop 用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
                if len(stack) == 0 or c != stack.pop():
                    return False
            else:
                return False
        return len(stack) == 0


solution = Solution()
print(solution.isValid("{()[]{}}"))
