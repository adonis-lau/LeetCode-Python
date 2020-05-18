#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
47. Permutations II
https://leetcode.com/problems/permutations-ii/
解题思路：
在一定会产生重复结果集的地方剪枝
搜索之前就对候选数组排序
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # return list(set((itertools.permutations(nums))))

        ans = []

        def dfs(nums, path):
            if not nums:
                ans.append(path)

            visited = set()
            for i, x in enumerate(nums):
                # 剪枝，减少循环次数，避免重复
                if x not in visited:
                    # nums[:i] + nums[i + 1:] 去掉当前元素，避免重复利用
                    dfs(nums[:i] + nums[i + 1:], path + [x])
                    visited.add(x)

        path = list()
        dfs(nums, path)
        return ans


solution = Solution()
print(solution.permuteUnique([1, 1, 2]))
