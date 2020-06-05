#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
10. Regular Expression Matching
https://leetcode.com/problems/regular-expression-matching/

1、"."表示任意字符
2、"*"表示任意个*前面的字符（aaaaaa = a*, aaaab != a*）
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        lens = len(s)
        lenp = len(p)
        dp = [[False for col in range(lenp + 1)] for row in range(lens + 1)]
        dp[0][0] = True

        # 对p以*进行分组
        for j in range(1, lenp + 1):
            print(j - 1, p[j - 1], p[j - 1] == '*', j - 2, dp[0][j - 2], dp[0][j - 2] == 1)
            dp[0][j] = p[j - 1] == '*' and dp[0][j - 2] == 1

        for i in range(1, lens + 1):
            for j in range(1, lenp + 1):
                """
                    s[i - 1] == p[j - 2] or '.' == p[j - 2] 表示判断 p 当前位的字符是否为 '.' 
                    如果不是，判断 p 当前位字符是否为 s 当前位字符
                """
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or dp[i][j - 1] or (
                                dp[i - 1][j] and (s[i - 1] == p[j - 2] or '.' == p[j - 2]))
                else:
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or '.' == p[j - 1])

        return dp[lens][lenp]


solution = Solution()
print(solution.isMatch("", ""))