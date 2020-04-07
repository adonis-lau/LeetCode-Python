#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from typing import List, Tuple

"""
1. Two Sum
https://leetcode.com/problems/two-sum/
题目要求我们找出两个和为target的数，也就是 nums[i] + nums[j] = target。
转换一下，也就是 target - nums[i] = nums[j]。
把nums[i]和i以键值对的形式存到哈希表中，注意存的是{值:下标}这种格式 。
只用遍历一次nums就可以得到结果。在遍历的同时把数据写入哈希表中，并进行查询，这样最坏的情况下时间复杂度也就是O(N)
"""


class Solution:
    def two_sum(self, nums: List[int], target: int) -> Tuple[int, int]:
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d:
                return i, d[target - nums[i]]
            d[nums[i]] = i


solution = Solution()
print(solution.two_sum([2, 7, 11, 5], 9))
