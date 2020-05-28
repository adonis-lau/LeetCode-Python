#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/
解题思路：
对内部数组按照第一个数字进行排序
判断每个数组的最后一个数字是否在下一个数组的两个数字中间
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        # 从第二个数组开始循环
        index = 1
        while index < len(intervals):
            # 如果前一个数组与当前数组有交集
            if intervals[index][0] <= intervals[index - 1][1]:
                # 那么将当前数组与前一个数组‘合并’
                intervals[index - 1][1] = max(intervals[index][1], intervals[index - 1][1])
                # 移除当前数组
                intervals.pop(index)
            else:
                index += 1
        return intervals


solution = Solution()
print(solution.merge([[1, 3], [8, 10], [2, 6], [15, 18]]))
print(solution.merge([[1, 4], [4, 5]]))
