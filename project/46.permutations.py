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
        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组，变换待填数字的位置
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res


solution = Solution()
print(solution.permute([1, 2, 3]))
