#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
64. Minimum Path Sum
https://leetcode.com/problems/minimum-path-sum/
解题方法：
走到当前单元格 (i,j) 的最小路径和 = 从左方单元格 (i−1,j) 与 从上方单元格 (i,j-1) 走来的 两个最小路径和中较小的 + 当前单元格值 grid[i][j]
共有4中情况：
设 dp 为大小 m×n 的矩阵，其中 dp[i][j] 的值代表直到走到 (i,j) 的最小路径和
当左边和上边都不是矩阵边界时：即当i != 0,j != 0 时，dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
当只有上边是矩阵边界时：只能从上面来，即当i = 0, j != 0 时，dp[i][j] = dp[i][j - 1] + grid[i][j]
当只有左边是矩阵边界时：只能从左面来，即当i != 0, j = 0 时，dp[i][j] = dp[i - 1][j] + grid[i][j]
当左边和上边都是矩阵边界时：即当i = 0, j = 0 时，其实就是起点，dp[i][j] = grid[i][j]

参考：
https://leetcode-cn.com/problems/minimum-path-sum/solution/zui-xiao-lu-jing-he-dong-tai-gui-hua-gui-fan-liu-c/
题解中的 上 和 左 对应的 i 和 j搞错了
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 当左边和上边都是矩阵边界时（起点）
                if i == j == 0:
                    continue
                # 当只有上边是矩阵边界时
                elif i == 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                # 当只有左边是矩阵边界时
                elif j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                # 当左边和上边都不是矩阵边界时
                else:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]


solution = Solution()
print(solution.minPathSum([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]))
