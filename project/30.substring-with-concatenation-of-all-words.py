#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
30. Substring with Concatenation of All Words
https://leetcode.com/problems/substring-with-concatenation-of-all-words/
"""
import collections
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        # 记录每个单词出现的次数并放入数组，下标为单词
        count = collections.Counter(words)
        # 每个单词的长度
        wordLen = len(words[0])
        # 单词的数量
        numWords = len(words)
        # 总长度
        windowLen = wordLen * numWords
        # 用于储存结果
        res = []
        # 遍历s中所有长度为 windowLen 的子串，当剩余子串的长度小于 windowLen 时，就不用再判断了
        for i in range(len(s) - windowLen + 1):
            check = count.copy()
            # 对于每个遍历到的长度为 windowLen 的子串，需要验证其是否刚好由 words 中所有的单词构成
            for j in range(numWords):
                startIdx = i + j * wordLen
                word = s[startIdx: startIdx + wordLen]
                # 如果当前遍历到的单词刚好在字典中
                if word in check:
                    # 从字典中去除该单词（值从0设置为1）
                    check[word] -= 1
                    # 如果是多次出现的重复单词，那么不符合要求，跳过
                    if check[word] < 0:
                        break
                # 当前单词不在词典中，跳过
                else:
                    break
            # 如果词典中的所有单词值都为0，证明该 windowLen 长度的子串恰好是由 words 中的单词组成
            if all([x == 0 for x in check.values()]):
                # 将子串的开头下标添加到结果中
                res.append(i)
        return res


solution = Solution()
print(solution.findSubstring("barfoothefoobarman", ["foo", "bar"]))
