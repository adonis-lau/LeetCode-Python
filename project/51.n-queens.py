#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
51. N-Queens
https://leetcode.com/problems/n-queens/
解题思路：
八皇后问题，一行只可能有一个皇后、一列也只可能有一个皇后，两条对角线上也只能有这一个皇后
从第一行开始，尝试在每个位置放置皇后
放置之后，排除对应 行 列 对角线，然后判断是否符合要求。符合要求那么继续，不符合就回溯
然后到下一位置重复上面操作

难点：
'/'对角线上，所有的row+col=常数
'\'对角线上，所有的row-col=常数
"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack():
            # 下标为行的索引
            row = len(queens)
            # 若已有n个元素则满足要求
            if row == n:
                output.append(queens[:])
            # 从第一行第一列开始遍历
            for col in range(n):
                # 判断是否能放置棋子
                if col not in queens and xy_dif[row - col] and xy_sum[row + col]:
                    # 放置棋子
                    queens.append(col)
                    # 设置攻击状态
                    if row == 1 and col == 3: print(row - col, row + col)
                    xy_dif[row - col], xy_sum[row + col] = False, False
                    # 向下一行探索
                    backtrack()
                    # 回溯，挪开棋子
                    queens.pop()
                    # 恢复攻击状态
                    xy_dif[row - col], xy_sum[row + col] = True, True

        # 用于存储皇后放置的位置
        queens = []
        # 用于标记是否被次对角线方向的皇后攻击
        xy_dif = [True] * (2 * n - 1)
        # 用于标记是否被主对角线方向的皇后攻击
        xy_sum = [True] * (2 * n - 1)
        output = []  # 所有的结果集
        backtrack()  # 开始回溯

        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in output]


solution = Solution()
result = solution.solveNQueens(4)
for list in result:
    for row in list:
        for colum in row:
            print(colum, end="\t")
        print()
    print()
    print()
