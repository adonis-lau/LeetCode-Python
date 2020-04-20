#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
18. 4Sum
https://leetcode.com/problems/4sum/
"""
import collections
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 对每个出现的数字进行计数
        counter = collections.Counter(nums)
        nums = sorted(list(set(nums)))
        length = len(nums)
        res = []

        # 从最左侧第一个数字开始循环
        for i in range(length):
            a = nums[i]
            """
            如果 target 减去最小数的 差 小于三个最小数的和，
            那么 整个数组中，四个数一定不可能等于target，结束循环
            """
            diffA = target - a
            if diffA < 3 * a:
                break
            """
            如果 target 减去最小数的 差 大于三个最大数的和，
            那么本次循环不符合要求，结束当前循环
            """
            if diffA > 3 * nums[-1]:
                continue
            # 从当前位置第二个数字开始循环
            for j in range(i, length):
                b = nums[j]
                # a和b是同一个数字且这个数字在数组中只出现一次
                if counter[b] < 1 + (a == b):
                    continue
                diffB = diffA - b
                if diffB < 2 * b:
                    break
                # key judgement diff Soltion 2
                if diffB > 2 * nums[-1]:
                    continue
                # 从当前位置第三个数字开始循环
                for k in range(j, length):
                    c = nums[k]
                    if counter[c] < 1 + (a == c) + (b == c):
                        continue
                    d = diffB - c
                    if d < c:
                        break
                    # key judgement diff Soltion 2
                    if d > nums[-1]:
                        continue
                    if counter[d] < 1 + (a == d) + (b == d) + (c == d):
                        continue
                    res.append([a, b, c, d])
        return res


solution = Solution()
print(solution.fourSum([1, 0, -1, 0, -2, 2], 0))
