#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/
解题思路：
下雨后水能达到的最高位置，等于两边最大高度的较小值减去当前高度的值
"""


class Solution:
    def trap(self, height):
        if len(height) < 3:
            return 0

        ret = 0
        left = [-1] * len(height)
        right = [-1] * len(height)
        left_max = 0
        right_max = 0

        # 从左扫描，遇到当前最大值就向右抹平
        for i in range(0, len(height)):
            left[i] = left_max = max(left_max, height[i])
        # 从右扫描，遇到当前最大值就向左抹平
        for i in range(len(height) - 1, -1, -1):
            right[i] = right_max = max(right_max, height[i])
        # 左右最大值中的最小值 减去当前值就是雨水的高度，因为步长是1，所以不需要再做乘法运算
        for i in range(1, len(height) - 1):
            ret += min(left[i], right[i]) - height[i]

        return ret


solution = Solution()
print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
