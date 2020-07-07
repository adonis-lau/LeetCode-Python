#!/usr/bin/python3
# -*- coding: UTF-8 -*-


"""
77. Combinations
https://leetcode.com/problems/combinations/
解题思路：
字典序 (二进制排序) 组合
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 使用 Itertools 工具类
        # return itertools.combinations([i + 1 for i in range(n)], k)

        # 将 nums 初始化为从 1 到 k的整数序列。nums就是每次向output中添加的结果
        # 将 n + 1添加为末尾元素，起到“哨兵”的作用。
        nums = list(range(1, k + 1)) + [n + 1]

        # 将指针设为列表的开头 j = 0
        output, j = [], 0
        while j < k:
            # 将nums 中的前k个元素添加到输出中，换而言之，除了”哨兵“之外的全部元素。
            output.append(nums[:k])

            j = 0
            # 找到nums中的第一个满足 nums[j] + 1 != nums[j + 1] 的元素，并将其加一
            while j < k and nums[j + 1] == nums[j] + 1:
                nums[j] = j + 1
                j += 1
            # nums[j]++ 以转到下一个组合
            nums[j] += 1

        return output


solution = Solution()
print(solution.combine(4, 2))
