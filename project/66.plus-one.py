#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
66. Plus One
https://leetcode.com/problems/plus-one/
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lst = [str(i) for i in digits]
        res = int("".join(lst)) + 1
        return [int(i) for i in str(res)]


solution = Solution()
print(solution.plusOne([1, 2, 3]))
