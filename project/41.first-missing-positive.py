#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
41. First Missing Positive
https://leetcode.com/problems/first-missing-positive/
这道题难度为什么是Hard
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        x = 1
        while True:
            if x not in nums:
                return x
            x += 1


solution = Solution()
print(solution.firstMissingPositive([1, 2, 0]))
