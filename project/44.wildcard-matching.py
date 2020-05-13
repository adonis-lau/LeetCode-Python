#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
44. Wildcard Matching
https://leetcode.com/problems/wildcard-matching/
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        s_idx = p_idx = 0
        star_idx = s_tmp_idx = -1

        while s_idx < s_len:
            # 当p未循环完 且 p等于s或者p等于? 时，表名s符合p规则，两个指针向前移动
            if p_idx < p_len and p[p_idx] in ['?', s[s_idx]]:
                s_idx += 1
                p_idx += 1
            # 当p未循环完 且 p等于'*'
            elif p_idx < p_len and p[p_idx] == '*':
                # 记录可能回溯的位置 star_idx
                star_idx = p_idx
                # 记录当前字符串的位置 s_tmp_idx
                s_tmp_idx = s_idx
                # p右移，第一次右移的时候，*不匹配任何字符
                p_idx += 1
            # 如果 p != s 或 p 已经循环完，并且p中没有*号，那么表示不匹配
            elif star_idx == -1:
                return False
            # 如果 p != s 或 p 已经循环完，但是p中有*号
            else:
                # 回溯，让*匹配再多匹配一个字符
                p_idx = star_idx + 1
                s_idx = s_tmp_idx + 1
                s_tmp_idx = s_idx

        # p中剩余的字符应该全部都是*，否则就不匹配
        return all(x == '*' for x in p[p_idx:])


solution = Solution()
print(solution.isMatch("adceb", "*a*b"))
