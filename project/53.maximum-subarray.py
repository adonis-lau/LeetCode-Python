#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # res 最大和
        # tmp 当前的和，如果当前的和 < 当前值，那么tmp就是当前值
        res = tmp = nums[0]
        # 从第二个开始循环
        for num in nums[1:]:
            tmp = max(num, num + tmp)
            res = max(res, tmp)
        return res


solution = Solution()
print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
