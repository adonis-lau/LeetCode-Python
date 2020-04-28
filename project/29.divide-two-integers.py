#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
29. Divide Two Integers
https://leetcode.com/problems/divide-two-integers/
解题思路：
因为不能使用乘除法，且暴力加减会超时，所以需要使用位运算
每次循环中，设置了一个temp，让dividend每次除以双倍的（prev）temp，又抵消掉了很多多余的遍历
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 这里设的也很巧妙， 同号为TRUE，异号False
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                # 这里的temp 左移*2， 对应i*2 也是为了做temp的记录，可以减少时间复杂度
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)


solution = Solution()
print(solution.divide(20, 3))
