#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
31. Next Permutation
https://leetcode.com/problems/next-permutation/
解题思路：
[1,2,7,4,3,1] ====> [1,3,1,2,4,7]
规律就是说 从后向前遍历，找到第一个降序的数字，2。
然后继续从后向前遍历，找比这个数大的第一个数，3。
之后交换两个数字，变成 [1,3,7,4,2,1]
然后把后面的数字 反转，变成 [1,3,1,2,4,7] 即为最终答案。
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) <= 1:
            return nums
        n = len(nums)
        # 倒序循环
        for i in reversed(range(n - 1)):
            # 如果左边的值小于右边
            if nums[i] < nums[i + 1]:
                # 找到最大值的下标
                j = i
                for j in reversed(range(i, n)):
                    if nums[j] > nums[i]:
                        break
                # 交换当前值和第一个大于它的值
                nums[i], nums[j] = nums[j], nums[i]
                # 对后面的值排序（因为是从右往左循环，所以是对循环过的值排序）
                nums[i + 1:] = sorted(nums[i + 1:])
                break
        else:
            nums.sort()
        return nums


solution = Solution()
print(solution.nextPermutation([1, 3, 2]))
