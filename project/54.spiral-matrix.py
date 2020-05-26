#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
54. Spiral Matrix
https://leetcode.com/problems/spiral-matrix/
解题思路：
拿一行，剩下的逆时针旋转
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            # 取剩余元素的第一行
            res += matrix.pop(0)
            # *matrix '*'表示将列表解开成两个独立的参数
            # zip 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
            # map 会根据提供的函数对指定序列做映射，第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表
            # [::-1] 从后向前取元素
            matrix = list(map(list, zip(*matrix)))[::-1]
        return res


solution = Solution()
print(solution.spiralOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
