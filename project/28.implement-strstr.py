#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
28. Implement strStr()
https://leetcode.com/problems/implement-strstr/
解题思路：
双指针
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 直接使用库函数
        # return haystack.find(needle)
        if len(needle) == 0:
            return 0
        left = 0
        while left < len(haystack):
            if haystack[left:left + len(needle)] == needle:
                return left
            left += 1
        return -1


solution = Solution()
print(solution.strStr("hello", "ll"))
