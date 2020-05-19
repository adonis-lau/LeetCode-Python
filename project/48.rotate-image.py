#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
48. Rotate Image
https://leetcode.com/problems/rotate-image/
解题思路：
先列转行，然后反转每一行中字符的顺序
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 方法1
        # matrix[::-1] 反转一维数组顺序
        # *matrix[::-1] '*'表示将列表解开成两个独立的参数
        # zip 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
        # matrix[:] = zip(*matrix[::-1])

        # 方法2
        n = len(matrix[0])
        # 转置（列转行）
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        # 反转每一行
        for i in range(n):
            matrix[i].reverse()

solution = Solution()
solution.rotate([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
