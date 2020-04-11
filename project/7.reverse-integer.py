#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
7. Reverse Integer
https://leetcode.com/problems/reverse-integer/

解题思路：
"""


class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        if x > 0:
            result = int(str(x)[::-1])
        else:
            result = - int(str(-x)[::-1])
        if result < -2 ** 31 or result > 2 ** 31 - 1:
            result = 0
        return result


solution = Solution()
print(solution.reverse(1534236469))
