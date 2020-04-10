#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
6. ZigZag Conversion
https://leetcode.com/problems/zigzag-conversion/
题目要求：把一个字符串按照锯齿型的方式去写，然后按照行进行拼接到一起。输出这样得到的结果。

解题思路：
s中的第i个字符（下标从第0个开始），如果按照zigzag书写方式会出现在的行数为（行数为0到numRows-1行）：
i % (2 * numRows - 2), if i % (2 * numRows - 2) < numRows
2 * numRows - 2 - (i % (2 * numRows - 2)), if i % (2 * numRows - 2) >= numRows
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1 or numRows >= len(s):
            return s
        # 创建二维数组
        arr = [''] * numRows
        for i in range(len(s)):
            tmp = i % (numRows + numRows - 2)
            if tmp < numRows:
                arr[tmp] += s[i]
            else:
                arr[numRows + numRows - 2 - tmp] += s[i]
        return ''.join(arr)


solution = Solution()
print(solution.convert("PAHNAPLSIIGYIR", 4))