#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/
"""
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 字典 need 表示当前滑动窗口中需要的各元素的数量
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1

        # needCnt 记录所需元素的总数量
        needCnt = len(t)
        i = 0
        # float('inf') 表示正负无穷
        res = (0, float('inf'))
        for j, c in enumerate(s):
            # 如果当前元素 c 在need中
            if need[c] > 0:
                # 那么所需元素的总数量减去1
                needCnt -= 1
            need[c] -= 1

            # 步骤一：滑动窗口包含了所有T元素
            if needCnt == 0:
                # 步骤二：增加i，排除多余元素（左下标右移，直到左边界值为t中所需要的的字符）
                while True:
                    c = s[i]
                    if need[c] == 0:
                        break
                    need[c] += 1
                    i += 1

                # 如果当前窗口长度小于之前找到的窗口长度，那么设置结果值为当前窗口
                if j - i < res[1] - res[0]:
                    res = (i, j)
                need[s[i]] += 1  # 步骤三：左下标右移，寻找新的满足条件滑动窗口
                needCnt += 1
                i += 1
        return '' if res[1] > len(s) else s[res[0]:res[1] + 1]  # 如果res始终没被更新过，代表无满足条件的结果


solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))
print(solution.minWindow("ABCODEBAC", "ABC"))
