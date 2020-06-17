#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
72. Edit Distance
https://leetcode.com/problems/edit-distance/
参考：
https://leetcode-cn.com/problems/edit-distance/solution/bian-ji-ju-chi-by-leetcode-solution/
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        # 有一个字符串为空串
        if n * m == 0:
            return n + m

        # DP 数组，保存变化步长
        D = [[0] * (m + 1) for _ in range(n + 1)]

        # 边界状态初始化
        for i in range(n + 1):
            D[i][0] = i
        for j in range(m + 1):
            D[0][j] = j

        # 计算所有 DP 值（编辑距离）
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # 当前值左边做一个操作变成当前值的编辑距离
                left = D[i - 1][j] + 1
                # 当前值下方做一个操作变成当前值的编辑距离
                down = D[i][j - 1] + 1
                # 如果两个字符串在此位置的值相同，当前值左下方变成当前值的编辑距离
                left_down = D[i - 1][j - 1]
                # 如果两个字符串在此位置的值不相同，那么就需要变换一次
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                # 取这三种变换的最小值
                D[i][j] = min(left, down, left_down)

        return D[n][m]


solution = Solution()
print(solution.minDistance("horse", "ros"))
print(solution.minDistance("intention", "execution"))
print(solution.minDistance("intention", "ros"))