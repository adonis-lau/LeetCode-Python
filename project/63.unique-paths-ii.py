#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
63. Unique Paths II
https://leetcode.com/problems/unique-paths-ii/
解题方法：
每个位置的路径 = 该位置左边的路径 + 该位置上边的路径
首先遍历第一行，有障碍物的结点值设置为0；如果没有障碍物，那么设置当前节点的值为前一个节点的值
然后遍历第一列，有障碍物的结点值设置为0；如果没有障碍物，那么设置当前节点的值为上一个节点的值
然后开始遍历整个数组，如果某个结点初始不包含任何障碍物，那么设置当前节点的值为上方和左侧两个结点值之和
如果当前节点有障碍物，那么设值为 0 ，可以保证不会对后面的路径产生贡献

节点上的值 n 表示有 n 种路径到达当前节点
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 行数
        m = len(obstacleGrid)
        # 列数
        n = len(obstacleGrid[0])

        # 如果起始结点有障碍物，则只需返回即可，因为将没有到达目的地的路径
        if obstacleGrid[0][0] == 1:
            return 0

        # 已经排除了最左上角初始节点没有障碍物，初始化起始单元格的值为1，表示路径
        obstacleGrid[0][0] = 1

        # 填写第一列的值
        for i in range(1, m):
            # 有障碍物的结点值设置为0；如果没有障碍物，那么设置当前节点的值为上一个节点的值
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1)

        # 填写第一行的值
        for j in range(1, n):
            # 有障碍物的结点值设置为0；如果没有障碍物，那么设置当前节点的值为前一个节点的值
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j - 1] == 1)

        # 编译整个数组，从单元格(1,1)开始填充值
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    # 到达方式数量 = 上方 + 左侧  cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                else:
                    # 如果当前节点有障碍物，那么当前节点无法通过，故设值为0
                    obstacleGrid[i][j] = 0

        # 节点上的值 n 表示有 n 种路径到达当前节点
        return obstacleGrid[m - 1][n - 1]


solution = Solution()
print(solution.uniquePathsWithObstacles([
    [0, 1, 0],
    [0, 1, 0],
    [0, 0, 0]
]))
