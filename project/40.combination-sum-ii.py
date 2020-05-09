#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
40. Combination Sum II
https://leetcode.com/problems/combination-sum-ii/
参考：
https://leetcode-cn.com/problems/combination-sum-ii/solution/xiong-mao-shua-ti-python3-hui-su-by-lotuspanda/
"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        if size == 0:
            return []

        def dfs(begin, path, residue):
            if residue == 0:
                res.append(path[:])
                return

            for index in range(begin, size):
                # 当前值大于要寻找的和时
                if candidates[index] > residue:
                    break
                # 当遍历的下标 index 严格大于当前搜索起点 begin 的时候，并且当前的数字和上一轮数字数值上相等的时候，跳过这个分支。
                # 用于递归回溯时去重
                if index > begin and candidates[index - 1] == candidates[index]:
                    continue

                path.append(candidates[index])
                # 下面调用dfs时，第二个参数的位置是index + 1，一定是从当前一位的下一位开始找
                dfs(index + 1, path, residue - candidates[index])
                # 回溯时恢复状态
                path.pop()

        candidates.sort()
        res = []
        dfs(0, [], target)
        return res


solution = Solution()
print(solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
