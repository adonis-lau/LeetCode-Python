#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
55. Jump Game
https://leetcode.com/problems/jump-game/
解题思路：
从左到右，每次都选择能跳跃最远的位置就可以
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 能跳到的最远下标
        maxPos = 0
        # nums的最右边的下标
        maxIndex = len(nums) - 1
        for i in (range(maxIndex)):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
            # 如果增加下面的判断，那么可能不需要遍历完就可以返回结果，但是会增加判断次数
            # if maxPos >= maxIndex:
            #     return True
        return maxPos >= maxIndex


solution = Solution()
print(solution.canJump([0]))
print(solution.canJump([2, 3, 1, 1, 4]))
print(solution.canJump([3, 2, 1, 0, 4]))
