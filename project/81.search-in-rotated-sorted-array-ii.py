#!/usr/bin/python3
# -*- coding: UTF-8 -*-


"""
81. Search in Rotated Sorted Array II
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
解题思路：
二分法
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # 库函数
        # return target in nums
        l = 0
        r = len(nums) - 1
        # 左下标小于右下标
        while (l <= r):
            # 二分
            mid = (l + r) // 2
            # 当前值等于target
            if (nums[mid] == target):
                # 查找到正确结果
                return True
            # 如果中间值和两端值相同
            if (nums[mid] == nums[l] == nums[r]):
                # 将两端下标向中间移动一位
                l += 1
                r -= 1
            # 当中间值大于左边
            elif (nums[mid] >= nums[l]):
                # 当target在左边和中间值之间
                if (nums[l] <= target < nums[mid]):
                    # 中间值设置为右边界
                    r = mid - 1
                # 当target不在左边和中间值之间
                else:
                    # 中间值设置为左边界
                    l = mid + 1
            # 当中间值小于左边
            else:
                # 当target在右边
                if (nums[mid] < target <= nums[r]):
                    # 中间值设置为左边界
                    l = mid + 1
                else:
                    # 中间值设置为右边界
                    r = mid - 1
        return False


solution = Solution()
print(solution.search([2, 5, 6, 0, 0, 1, 2], 0))
print(solution.search([2, 5, 6, 0, 0, 1, 2], 3))
