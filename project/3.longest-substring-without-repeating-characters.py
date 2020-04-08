#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

参考：https://blog.csdn.net/fuxuemingzhu/article/details/82022530
"""

NO_OF_CHARS = 256


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        res = 0
        chars = dict()
        for right in range(len(s)):
            # 如果右边的字符在dict中
            if s[right] in chars:
                # 将左边字符下标右移一位
                left = max(left, chars[s[right]] + 1)
            # 将右边字符的下标放入dict
            chars[s[right]] = right
            # 最长字符串长度 = max(当前长度 : 右边字符下标 - 左边字符下标 + 1)
            res = max(res, right - left + 1)
            print(chars)
        return res

    # 方法2，只计算长度，字符串可能顺序不同
    def lengthOfLongestSubstringFun2(self, s: str):
        left, right = 0, 0
        chars = set()
        res = 0
        # 当左边字符下标和右边字符下标都还在字符串长度范围内时
        while left < len(s) and right < len(s):
            # 如果右边的字符在set中
            if s[right] in chars:
                # 如果左边字符也在set中
                if s[left] in chars:
                    # 删除左边的字符
                    chars.remove(s[left])
                # 那么左边字符下标右移一位
                left += 1
            # 如果右边的字符不在set中
            else:
                # 将右边的字符添加到set中
                chars.add(s[right])
                # 右边字符下标右移一位
                right += 1
                # 字符串最大长度 = max(当前最大长度 : 当前set中的字符数量)
                res = max(res, len(chars))
            print(chars)
        return res


solution = Solution()
string = "ABABEFGGG"
print("The input string is " + string)
length = solution.lengthOfLongestSubstring(string)
print("The length of the longest non-repeating character substring is " + str(length))
length2 = solution.lengthOfLongestSubstringFun2(string)
print("The length of the longest non-repeating character substring is " + str(length2))
