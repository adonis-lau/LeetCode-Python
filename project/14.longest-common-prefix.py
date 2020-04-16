#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/

解题思路：
使用zip函数取所有字符串前min(len(str))个字符，然后将zip压缩过的对象转enum
循环enum，当第i个字符不相同(将字符放入set，如果不相同，那么set长度大于1)
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        """zip函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，
           然后返回由这些元组组成的列表。
           如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，
           利用 * 号操作符，可以将元组解压为列表。"""
        for i, chars in enumerate(zip(*strs)):
            print(i, chars, set(chars), len(set(chars)))
            if len(set(chars)) > 1:
                return strs[0][:i]
        return min(strs)


solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
