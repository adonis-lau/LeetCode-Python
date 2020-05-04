#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/
解题思路：
二分法
将数组从中间分开成左右两部分的时候，一定有一部分的数组是有序的。
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            # 找到数组的中间下标，以此分为左右两部分
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # 先去左边查找
            if nums[0] <= nums[mid]:
                # 因为二分的数组是有序的，所以可以用值大小判断target是否在左边数组中
                if nums[0] <= target < nums[mid]:
                    # 如果target在左数组中，那么将右下标设置为从左数组开始
                    right = mid - 1
                else:
                    # 反之将左下标设置为从右数组开始
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


solution = Solution()
print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))
