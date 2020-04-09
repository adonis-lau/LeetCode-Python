#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

从左到右，双重循环，一个一个的分割字符串判断是否为回文字符串，并将最长的回文字符串储存到结果中
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 用于储存返回结果
        result = ""
        for left in range(len(s)):
            right = left + 1
            while right <= len(s) and len(result) <= len(s[left:]):
                # 当字符串片段为回文子串，且长度大于当前结果值中的回文子串
                if s[left:right] == s[left:right][::-1] and len(s[left:right]) > len(result):
                    result = s[left:right]
                right += 1
        return result


solution = Solution()
print(solution.longestPalindrome("ddbabab"))
