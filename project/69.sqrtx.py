#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
69. Sqrt(x)
https://leetcode.com/problems/sqrtx/
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        # 方法1：直接求平方根，然后取整
        # return int(x ** 0.5)

        # 方法2：二分法查找，用中位数，速度快
        left = 0
        right = x
        # 使用二分找到第一个数的平方大于等于x
        while left < right:
            # 这种取中位数的方法又快又好，是我刚学会的，原因在下面这篇文章的评论区
            # https://www.liwei.party/2019/06/17/leetcode-solution-new/search-insert-position/
            # 加1是为了防止出现 mid 恒等于 (left + right)/2 的情况
            mid = (left + right + 1) >> 1
            print(mid)
            square = mid * mid
            if square > x:
                right = mid - 1
            else:
                left = mid

        return left


solution = Solution()
# print(solution.mySqrt(2147395600))
# print(solution.mySqrt(0))
print(solution.mySqrt(2))
