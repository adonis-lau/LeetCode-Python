#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
34. Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
解题思路：
二分法
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 分两次查找
        # 查找左边界
        low = 0
        high = len(nums) - 1
        res = []
        # 寻找左边界
        while low <= high:
            mid = (low + high) // 2
            # 当前值等于target
            if nums[mid] == target:
                # 当前值是数组的第一个值或者是第一次出现的时候
                if mid == 0 or nums[mid - 1] != target:
                    res.append(mid)
                    break
                else:
                    high = mid
            # 当前值大于target，右边界左移
            elif nums[mid] > target:
                high = mid - 1
            # 当前值小于target，左边界右移
            else:
                low = mid + 1
        # 如果未找到第一个符合的值，那么该数组中没有符合值
        if not res:
            return [-1, -1]
        # 寻找右边界
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                if (mid == len(nums) - 1) or nums[mid + 1] != target:
                    res.append(mid)
                    break
                else:
                    low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return res


solution = Solution()
print(solution.searchRange([5, 7, 7, 8, 8, 10], 8))
