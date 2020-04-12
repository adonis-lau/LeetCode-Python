#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
9. Palindrome Number
https://leetcode.com/problems/palindrome-number/
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 如果输入的数字为负数
        if x < 0:
            return False
        tmp = x
        result = 0
        while tmp > 0:
            result = result * 10 + tmp % 10
            tmp = tmp // 10
        if x == result:
            return True
        else:
            return False


solution = Solution()
print(solution.isPalindrome(55))
