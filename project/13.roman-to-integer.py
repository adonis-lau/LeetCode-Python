#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/

解题思路：
因为限定了值范围，所以直接使用穷举法
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        dictValues = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        # 将罗马数字转换为枚举
        for i, val in enumerate(s):
            # 因为罗马数字中有组合数字，所以应该先判断该位数字是否为组合数字
            if i + 1 < len(s):
                if dictValues[val] < dictValues[s[i + 1]]:
                    num -= dictValues[val]
                    continue
            num += dictValues[val]
        return num


solution = Solution()
print(solution.romanToInt("CXXIII"))