#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
62. Unique Paths
https://leetcode.com/problems/unique-paths/
解题方法：
每个位置的路径 = 该位置左边的路径 + 该位置上边的路径
参考：
https://leetcode-cn.com/problems/unique-paths/solution/dong-tai-gui-hua-by-powcai-2/
"""
import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 排列组合
        # return int(math.factorial(m + n - 2) / math.factorial(m - 1) / math.factorial(n - 1))

        # 用于保存每行到达最右需要的步数
        cur = [1] * n
        # 因为行循环和列循环第一格都不用走，所以都要少循环一次
        # 行循环
        for i in range(1, m):
            # 列循环
            for j in range(1, n):
                # cur[j - 1] 保存的是上一行到达最右的步数
                cur[j] += cur[j - 1]
        return cur[-1]


solution = Solution()
print(solution.uniquePaths(3, 2))

print(math.factorial(3 + 2 - 2) )
print(math.factorial(3 - 1))
print(math.factorial(2 - 1))
print(math.factorial(3 + 2 - 2) / math.factorial(3 - 1) / math.factorial(2 - 1))