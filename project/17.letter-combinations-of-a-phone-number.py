#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if not digits:
            return result
        chars = {'2': 'abc',
                 '3': 'def',
                 '4': 'ghi',
                 '5': 'jkl',
                 '6': 'mno',
                 '7': 'pqrs',
                 '8': 'tuv',
                 '9': 'wxyz'
                 }

        def perm(pre, digits):
            if not digits:
                result.append(''.join(pre))
                return
            for char in chars[digits[0]]:
                perm(pre + [char], digits[1:])

        perm([], digits)
        return result


solution = Solution()
print(solution.letterCombinations("234"))
