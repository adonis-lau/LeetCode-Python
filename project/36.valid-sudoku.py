#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
36. Valid Sudoku
https://leetcode.com/problems/valid-sudoku/
解题思路：
遍历9 x 9 宫格，判断行、列和3x3宫格内没有重复数字。
"""
from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        lows, columns, boxes = defaultdict(set), defaultdict(set), defaultdict(set)
        for low in range(9):
            for col in range(9):
                if board[low][col].isdigit():  # 或者用 board[low][col] != '.'也可以
                    # 以下三个if判断是不是在行、列和 3*3宫格内存在有重复数字
                    if board[low][col] in lows[low]:
                        return False
                    if board[low][col] in columns[col]:
                        return False
                    # 这里3*3宫格缩小1/3
                    if board[low][col] in boxes[low // 3, col // 3]:
                        return False
                    # 没存在加入行、列和 3*3宫格
                    lows[low].add(board[low][col])
                    columns[col].add(board[low][col])
                    boxes[low // 3, col // 3].add(board[low][col])
        return True


solution = Solution()
print(solution.isValidSudoku([
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]))
