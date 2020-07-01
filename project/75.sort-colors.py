#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
75. Sort Colors
https://leetcode.com/problems/sort-colors/
解题思路：
荷兰三色旗问题
三个指针（p0, p2 和curr）来分别追踪0的最右边界、2的最左边界和当前考虑的元素
沿着数组移动 curr 指针，若nums[curr] = 0，则将其与 nums[p0]互换，p0向右移；若 nums[curr] = 2 ，则与 nums[p2]互换，p2向左移
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 对于所有 idx < p0 : nums[idx < p0] = 0
        # curr是当前考虑元素的下标
        p0 = curr = 0
        # 对于所有 idx > p2 : nums[idx > p2] = 2
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1


solution = Solution()
list = [2, 0, 2, 1, 1, 0]
solution.sortColors(list)
print(list)
