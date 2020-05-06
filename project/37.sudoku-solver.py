#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
37. Sudoku Solver
https://leetcode.com/problems/sudoku-solver/
解题思路：
假设在数独上已经成功放置了几个数字。
但是该组合不是最优的并且不能继续放置数字了。该怎么办？ 回溯。
意思是回退，来改变之前放置的数字并且继续尝试。如果还是不行，再次 回溯。
使用set可以增加效率
参考资料：
https://leetcode-cn.com/problems/sudoku-solver/solution/pythonsethui-su-chao-guo-95-by-mai-mai-mai-mai-zi/
"""
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set(range(1, 10)) for _ in range(9)]  # 行剩余可用数字
        col = [set(range(1, 10)) for _ in range(9)]  # 列剩余可用数字
        block = [set(range(1, 10)) for _ in range(9)]  # 块剩余可用数字

        empty = []  # 收集需填数位置
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':  # 更新可用数字
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    block[(i // 3) * 3 + j // 3].remove(val)
                else:
                    empty.append((i, j))

        def backtrack(iter=0):
            if iter == len(empty):  # 处理完empty代表找到了答案
                return True
            i, j = empty[iter]
            """
            b表示子数独的位置
            0 1 2
            3 4 5
            6 7 8
            """
            b = (i // 3) * 3 + j // 3
            # 遍历这几个里面共有的元素
            for val in row[i] & col[j] & block[b]:
                # 从 行 列 子块 中删除想要填充的当前值
                row[i].remove(val)
                col[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)
                if backtrack(iter + 1):
                    # 如果进行到了最后一步，即所有位置全部填充完成
                    return True
                # 如果不能进行下一步填充，那么就回溯
                row[i].add(val)
                col[j].add(val)
                block[b].add(val)
            # 如果数独没有全部填充完（因为empty不为空），且 行 列 子块 中没有共有元素，表示数独填充失败，回溯
            return False

        backtrack()

        for child in board:
            print(child)


solution = Solution()
solution.solveSudoku(
    [["5", "3", ".", ".", "7", ".", ".", ".", "."],
     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", "6", "."],
     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", "6", ".", ".", ".", ".", "2", "8", "."],
     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
