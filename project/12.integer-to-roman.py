#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
12. Integer to Roman
https://leetcode.com/problems/integer-to-roman/

解题思路：
因为限定了值范围，所以直接使用穷举法
"""
from collections import OrderedDict


class Solution:
    def intToRoman(self, num: int) -> str:
        roman = OrderedDict()
        roman[1000] = "M"
        roman[900] = "CM"
        roman[500] = "D"
        roman[400] = "CD"
        roman[100] = "C"
        roman[90] = "XC"
        roman[50] = "L"
        roman[40] = "XL"
        roman[10] = "X"
        roman[9] = "IX"
        roman[5] = "V"
        roman[4] = "IV"
        roman[1] = "I"

        def roman_num(num):
            for r in roman.keys():
                # divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)
                # x 为商，y为余数
                x, y = divmod(num, r)
                # 字符串 * 数字n，就是把这个字符串重复n次
                yield roman[r] * x
                num -= (r * x)
                if num <= 0:
                    break
        return "".join([a for a in roman_num(num)])


solution = Solution()
print(solution.intToRoman(123))