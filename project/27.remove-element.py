#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
27. Remove Element
https://leetcode.com/problems/remove-element/
解题思路：
双指针
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = right = 0
        # 用双指针遍历一次
        while right < len(nums):
            # 如果是要删除的值，跳过
            if val == nums[right]:
                right += 1
            # 不相等时，把右值赋给左边
            elif right < len(nums):
                nums[left] = nums[right]
                right += 1
                left += 1
        return left


solution = Solution()
print(solution.removeElement([3, 3, 3, 3, 3, 0, 4, 2], 3))
