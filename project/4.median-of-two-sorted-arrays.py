#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
4. Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/

"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums: List[int] = nums1 + nums2
        nums.sort()
        print(nums)
        if len(nums) % 2 == 0:
            return (nums[int(len(nums) / 2 - 1)] + nums[int(len(nums) / 2)]) / 2
        else:
            return nums[int(len(nums) / 2 - 0.5)]


solution = Solution()
print(solution.findMedianSortedArrays([1, 3], [2]))
print(solution.findMedianSortedArrays([1, 2], [3, 4]))