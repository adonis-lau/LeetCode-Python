#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
解题思路：
双指针
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 1
        # 遍历nums
        while right < len(nums):
            # 当左边的数值等于右边的数值，那么右指针右移（因为是有序数组）
            # 增加一个长度判断，因为可能溢出
            while right < len(nums) and nums[left] == nums[right]:
                right += 1
            # 增加一个长度判断，因为可能溢出
            if right < len(nums):
                # 将此时的右值放到当前左值的右边
                nums[left + 1] = nums[right]
                left += 1
                right += 1
        return left + 1


solution = Solution()
print(solution.removeDuplicates([1, 1]))
