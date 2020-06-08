#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
65. Valid Number
https://leetcode.com/problems/valid-number/
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()  # 去掉两端的空白符
        if not s:
            return False
        else:
            # 去掉开头的正负号
            if s[0] in ['+', '-']:
                s = s[1:]
            # 如果字符中有e
            if 'e' in s:
                temp_list = s.split('e')
                # 字符串s中含有多于一个的’e‘,返回False
                if len(temp_list) > 2:
                    return False
                # 去掉e前面的字符串中的'.'
                temp_list[0] = temp_list[0].replace('.', '', 1)
                # 去掉e后面字符串中的'+'或者'-'
                if len(temp_list[1]) > 0 and temp_list[1][0] in ['+', '-']:
                    temp_list[1] = temp_list[1].replace(temp_list[1][0], '', 1)
                # 如果e前后都是数字，那么输入的字符串是数字
                if temp_list[0].isnumeric() and temp_list[1].isnumeric():
                    return True
                return False
            else:  # s中不含'e'
                s = s.replace('.', '', 1)
                if s.isnumeric():
                    return True
                return False


solution = Solution()
print(solution.isNumber("  -90e3   "))
print(solution.isNumber(" 99e2.5 "))