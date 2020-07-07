#!/usr/bin/python3
# -*- coding: UTF-8 -*-


"""
78. Subsets
https://leetcode.com/problems/subsets/
解题思路：
递归
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]

        for num in nums:
            output += [curr + [num] for curr in output]

        return output


solution = Solution()
print(solution.subsets([1, 2, 3]))
