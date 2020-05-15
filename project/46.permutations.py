#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
46. Permutations
https://leetcode.com/problems/permutations/
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 直接使用库函数
        # return list(itertools.permutations(nums))

        ans = []

        def dfs(nums, path):
            # 当前路径满足条件
            if path and len(path) == len(nums):
                ans.append(list(path))

            # 在剩余的数字中选择下一个数字
            for num in (set(nums) - set(path)):
                path.append(num)
                dfs(nums, path)
                # 回溯
                path.pop()
            return ans

        path = list()
        dfs(nums, path)
        return ans


solution = Solution()
print(solution.permute([1, 2, 3]))
