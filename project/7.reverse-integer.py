#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
7. Reverse Integer
https://leetcode.com/problems/reverse-integer/

解题思路：
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x < -2**31 or x > 2 ** 31 - 1:
            return 0
        if x > 0:
            return int(str(x)[::-1])
        else:
            return - int(str(-x)[::-1])


solution = Solution()
print(solution.reverse(-2**32))
