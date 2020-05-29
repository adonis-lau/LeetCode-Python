#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
57. Insert Interval
https://leetcode.com/problems/insert-interval/
解题思路：
将 newInterval 添加到 intervals
对intervals的内部数组按照第一个数字进行排序
判断每个数组的最后一个数字是否在下一个数组的两个数字中间
"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        intervals.append(newInterval)

        intervals.sort(key=lambda x: x[0])

        for interval in intervals:
            # 如果result为空，或者当前区间与上一区间不重合，直接添加
            if not result or result[-1][-1] < interval[0]:
                result.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                result[-1][-1] = max(result[-1][-1], interval[-1])

        return result


solution = Solution()
print(solution.insert([[1, 3], [6, 9]], [2, 5]))
print(solution.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
