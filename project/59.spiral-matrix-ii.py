#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
59. Spiral Matrix II
https://leetcode.com/problems/spiral-matrix-ii/
解题思路：
生成 n * n 的空矩阵，然后模拟整个向内环绕的填入过程
参考：
https://leetcode-cn.com/problems/spiral-matrix-ii/solution/spiral-matrix-ii-mo-ni-fa-she-ding-bian-jie-qing-x/
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 创建空矩阵
        result = [[0 for _ in range(n)] for _ in range(n)]
        # 初始化 左 右 上 下 边界
        l, r, t, b = 0, n - 1, 0, n - 1
        num, tar = 1, n * n
        while num <= tar:
            # 从左到右
            for i in range(l, r + 1):
                result[t][i] = num
                num += 1
            t += 1
            # 从上到下
            for i in range(t, b + 1):
                result[i][r] = num
                num += 1
            r -= 1
            # 从右到左
            for i in range(r, l - 1, -1):
                result[b][i] = num
                num += 1
            b -= 1
            # 从下到上
            for i in range(b, t - 1, -1):
                result[i][l] = num
                num += 1
            l += 1

        return result


solution = Solution()
for row in solution.generateMatrix(3):
    for col in row:
        print(col, end="\t")
    print("\n")
