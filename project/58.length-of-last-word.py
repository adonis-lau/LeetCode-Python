#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
58. Length of Last Word
https://leetcode.com/problems/length-of-last-word/
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(" ")[-1])


solution = Solution()
print(solution.lengthOfLastWord("Hello World"))
