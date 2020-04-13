#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/

解题思路：
Two Pointer Approach
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0
        while left < right:
            x = right - left
            y = min(height[left], height[right])
            area = x * y if x * y > area else area
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
            print(area)
        return area


solution = Solution()
print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
