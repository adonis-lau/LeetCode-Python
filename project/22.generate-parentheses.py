#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/

参考：
https://blog.csdn.net/timemagician/article/details/79096914
符合规则的一定是左括号开头，所以先从左括号开始暴力破解
左括号添加数量够了之后，再从右括号开始
效率较低
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 待研究
        # return [] if n == 0 else ['()'] if n == 1 else set([i[0:j] + '()' + i[j:] for i in self.generateParenthesis(n - 1) for j in range(len(i))])
        result = []
        self.dfs(0, 0, 0, result, [], n)
        return result

    def dfs(self, openCount, closeCount, cur, result, l, n):

        if len(l) == n * 2:
            result.append(''.join(l))
            return

        if openCount < n:
            l.append('(')
            self.dfs(openCount + 1, closeCount, cur + 1, result, l, n)
            # 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
            l.pop()

        if closeCount < n:
            if cur < 1:
                return
            l.append(')')
            self.dfs(openCount, closeCount + 1, cur - 1, result, l, n)
            # 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
            l.pop()


solution = Solution()
print(solution.generateParenthesis(2))
