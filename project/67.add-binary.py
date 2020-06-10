#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
67. Add Binary
https://leetcode.com/problems/add-binary
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 方法1：使用内置函数
        # return '{0:b}'.format(int(a, 2) + int(b, 2))

        # 方法2：从右向左计算，当前位置上的结果值如果是2，那么当前位置设值为0，向前进1为
        # 获取最大长度
        str_len = max(len(a), len(b))
        # zfill方法返回指定长度的字符串，原字符串右对齐，前面填充0
        a = a.zfill(str_len)
        b = b.zfill(str_len)
        # carry用于存储是否进位
        carry = 0
        result = ''
        for i in range(str_len):
            # 将进位，a [〜i]和b [〜i]加到r作为一个整数
            r = carry
            # a[~i] 表示取倒数第 i 个值
            r += 1 if a[~i] == '1' else 0
            r += 1 if b[~i] == '1' else 0
            # 当a，b和 carry 中遇到多个'1'时可以进位
            carry = 1 if r > 1 else 0
            # 当前位置中，a，b和 carry 的值共有以下四种情况
            # case 1: 0 0 0  out 0
            # case 2: 0 0 1  out 1
            # case 3: 0 1 1  out 0
            # case 4: 1 1 1  out 0
            result = ('0' if (r == 2 or r == 0) else '1') + result
        # 如果还需要进位，那么把'1'添加到结果值的最前面
        if carry == 1:
            result = '1' + result
        return result


solution = Solution()
print(solution.addBinary("1010", "1011"))
