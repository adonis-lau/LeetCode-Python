#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
16. 3Sum Closest
https://leetcode.com/problems/3sum-closest/
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        以下代码运行超时
        result = sum(nums[:3])
        for lst in itertools.combinations(nums, 3):
            sum_lst = sum(lst)
            if abs(result - target) > abs(sum_lst - target):
                result = sum_lst
        return result
        """
        nums.sort()
        result = sum(nums[:3])
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum_three = nums[i] + nums[left] + nums[right]
                if sum_three == target:
                    return sum_three
                if abs(sum_three - target) < abs(result - target):
                    result = sum_three
                if sum_three < target:
                    left += 1
                else:
                    right -= 1
        return result


solution = Solution()
print(solution.threeSumClosest(
    [14, 55, 33, 92, 35, 7, -87, -11, -54, 13, -18, -92, -32, 94, 100, 32, 15, -83, -6, -25, 2, 29, 50, 5, 81, 41, -42,
     93, 58, -43, 62, -2, -28, 25, -91, -77, -15, -47, 12, -1, -37, 59, 41, -86, -69, -88, 36, 7, 7, 65, -14, -57, 80,
     -27, -56, 51, 71, -70, -26, 42, -16, 92, -51, -15, 63, 22, -54, 39, 48, 91, -60, -28, 17, -74, 20, 71, -10, 88, 93,
     86, -48, -65, -52, 34, 68, 70, -100, 91, 63, 59, -12, -51, 24, 50, 6, 71, 9, -56, 71, 28, 48, 32, 62, -96, 18, 39,
     -17, -19, -61, -91, -71, 89, 63, -75, 67, -38, 66, -60, -24, 85, -43, 5, 47, -67, -60, 7, -18, 77, 73, 47, 19, 53,
     54, 80, -34, -54, -20, -2, -50, 7, -26, 5, -43, -91, 100, -87, 56, 71, -52, 54, 46, -29, 33, 66, -67, -58, -54, -2,
     78, -78, -98, -29, 3, 62, 82, -73, 90, -26, 100], -235))
