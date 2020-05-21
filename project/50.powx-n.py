#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
50. Pow(x, n)
https://leetcode.com/problems/powx-n/
解题思路：
对N进行二进制拆分，
参考：
https://leetcode-cn.com/problems/powx-n/solution/powx-n-by-leetcode-solution/
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # ??????
        # return x ** n

        def quickMul(N):
            ans = 1.0
            # 贡献的初始值为 x
            x_contribute = x
            # 在对 N 进行二进制拆分的同时计算答案
            while N > 0:
                print(N, ans, x_contribute)
                if N % 2 == 1:
                    # 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                    ans *= x_contribute
                # 将贡献不断地平方
                x_contribute *= x_contribute
                # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
                N //= 2
            return ans

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


solution = Solution()
print(solution.myPow(2, 4))