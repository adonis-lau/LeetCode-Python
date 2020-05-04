#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
35. Search Insert Position
https://leetcode.com/problems/search-insert-position/
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 将list做成枚举（map）
        for idx, value in enumerate(nums):
            # 如果当前值大于等于target，那么target应该插入到当前位置，所以返回当前位置
            # 如果当前值等于target，那么返回当前值
            if value >= target:
                return idx
        return len(nums)


solution = Solution()
print(solution.searchInsert([1, 3, 5, 6], 7))
