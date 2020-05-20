#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/
解题思路：
对每个单词进行排序，排序后的值当做key放入hashmap
key不存在，就把word放入数组然后添加到value
key存在，就在key对应的数组中追加word
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in dict:
                dict[sorted_word].append(word)
            else:
                dict[sorted_word] = [word]
        return [arr for arr in dict.values()]


solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
