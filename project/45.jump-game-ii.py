#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
45. Jump Game II
https://leetcode.com/problems/jump-game-ii/
解题思路：
贪心：从左到右查找，每次都选择能跳跃最远的位置就可以
https://leetcode-cn.com/problems/jump-game-ii/solution/tiao-yue-you-xi-ii-by-leetcode-solution/
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        maxPos, end, step = 0, 0, 0
        """
            关于为什么要 len(nums) - 1
            在遍历数组时，我们不访问最后一个元素，这是因为在访问最后一个元素之前，
            我们的边界一定大于等于最后一个位置，否则就无法跳到最后一个位置了。
            如果访问最后一个元素，在边界正好为最后一个位置的情况下，
            我们会增加一次「不必要的跳跃次数」，因此我们不必访问最后一个元素。
        """
        for i in range(len(nums) - 1):
            # 判断前面的步长是否能到当前循环位置（题目上说给定的数组都能，所以这个判断在当前题目是非必须的）
            if maxPos >= i:
                # 更新 下一步 能够到达的 最远下标
                maxPos = max(maxPos, i + nums[i])
                # 到达当前能够到达的最大下标位置
                if i == end:
                    # 更新边界
                    end = maxPos
                    # 步长+1
                    step += 1
        return step


solution = Solution()
print(solution.jump([2, 3, 1, 1, 4]))
