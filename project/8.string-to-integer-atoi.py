#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
8. String to Integer (atoi)
https://leetcode.com/problems/string-to-integer-atoi/
"""


class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1
        str = str.strip()
        if not str:
            return 0
        number, flag = 0, 1
        if str[0] == '-':
            str = str[1:]
            flag = -1
        elif str[0] == '+':
            str = str[1:]
        for c in str:
            if '0' <= c <= '9':
                number = 10 * number + ord(c) - ord('0')
            else:
                break
        number = flag * number
        if number < INT_MIN:
            number = INT_MIN
        elif number > INT_MAX:
            number = INT_MAX
        return number


solution = Solution()
print(solution.myAtoi("0-1"))