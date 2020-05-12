#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
43. Multiply Strings
https://leetcode.com/problems/multiply-strings/
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, "0": 0}

        def strToInt(a: str):
            res = 0
            for index, l_key in enumerate(a):
                res += l[l_key] * (10 ** (len(a) - index - 1))
            return res

        return str(strToInt(num1) * strToInt(num2))


solution = Solution()
print(solution.multiply("12", "1"))
