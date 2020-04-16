#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/
"""
from typing import List
import itertools


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        运行超时的代码：
        result = []
        # 完全排列组合
        for lst in itertools.combinations(nums, 3):
            # 如果三个数和为0
            if sum(lst) == 0:
                # 将Tuple类型转为List
                lst = list(lst)
                # 对list中的数值从小到大排序，为后面的去重做准备
                lst.sort()
                result.append(lst)
        # 去重
        unique_lst = []
        [unique_lst.append(sublst) for sublst in result if not unique_lst.count(sublst)]
        return unique_lst
        """

        # HashTable
        ht = {}
        nums.sort()
        ans = set()
        for i, n in enumerate(nums):
            ht[n] = i
        print(ht)
        # 双重循序，左值 + 右值
        for left in range(len(nums)):
            for right in range(left + 1, len(nums)):
                target = -(nums[left] + nums[right])
                # 如果 左值 + 右值 的负值target在ht中（那么左值 + 右值 + target = 0）
                if target in ht and ht[target] > right:
                    ans.add((nums[left], nums[right], -(nums[left] + nums[right])))

        return list(ans)


solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
