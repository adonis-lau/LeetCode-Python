#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
29. Divide Two Integers
https://leetcode.com/problems/divide-two-integers/
"""


class Solution:
    def divide(self, a: int, b: int) -> int:
        # 确定运算结果的正负号
        is_negative = -1 if (a < 0 and b >= 0) or (a >= 0 and b < 0) else 1
        res = is_negative * self.helper(abs(a), abs(b))
        return min(res, 2 ** 31 - 1)

    def helper(self, a, b):
        if b == 1: return a
        res = 0
        while a >= b:
            t, i = b, 1
            while a >= t:
                a -= t
                res += i
                i <<= 1
                t <<= 1
        return res


solution = Solution()
print(solution.divide(10, 3))
