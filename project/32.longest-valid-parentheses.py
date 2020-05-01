#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
32. Longest Valid Parentheses
https://leetcode.com/problems/longest-valid-parentheses/
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack, curr_longest, max_longest = [], 0, 0
        for c in s:
            # 因为所有成对的括号，一定是从'('开始的
            if c == '(':
                stack.append(curr_longest)
                curr_longest = 0
            # 拿右括号跟跟栈中的左括号匹配
            elif c == ')':
                # 如果栈中有左括号，那么当前长度加2（左右括号各一个）
                if stack:
                    curr_longest += stack.pop() + 2
                    max_longest = max(max_longest, curr_longest)
                else:
                    # 如果栈中已经没有括号了，那么当前的右括号就是无匹配的，那么当前最长长度重置为0
                    curr_longest = 0
        return max_longest


solution = Solution()
print(solution.longestValidParentheses("(())())()()()"))
