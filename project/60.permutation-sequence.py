#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
60. Permutation Sequence
https://leetcode.com/problems/permutation-sequence/
解题思路：
求第 k%(n-1)! 个排列
"""
import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 从1到n的列表
        tokens = [str(i) for i in range(1, n + 1)]
        res = ''
        # 下标是从0开始
        index = k - 1
        while n > 0:
            n -= 1
            # divmod 把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)
            # factorial 阶乘
            a, index = divmod(index, math.factorial(n))
            res += tokens.pop(a)
        return res


solution = Solution()
print(solution.getPermutation(3, 3))
