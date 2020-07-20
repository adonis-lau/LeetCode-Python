#!/usr/bin/python3
# -*- coding: UTF-8 -*-


"""
84. Largest Rectangle in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram/
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        # left 表示直方图当前位置最大面积的起始位置
        # right 表示直方图当前位置最大面积的起始位置
        left, right = [0] * n, [n] * n

        mono_stack = list()
        # 遍历每个高度
        for i in range(n):
            # 如果当前高度比之前矮
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                # 记录当前高度
                right[mono_stack[-1]] = i
                # 移除以前更高的高度
                mono_stack.pop()
            # 如果存在较大的高度，我们可以将当前较矮高度的起始索引扩展到左侧
            left[i] = mono_stack[-1] if mono_stack else -1
            # 添加此高度并将其作为开始索引
            mono_stack.append(i)

        # 计算他们可以创建的最大面积，其中width =（直方图的长度-该高度的起始索引）
        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans


solution = Solution()
print(solution.largestRectangleArea([2, 1, 5, 6, 2, 3]))
