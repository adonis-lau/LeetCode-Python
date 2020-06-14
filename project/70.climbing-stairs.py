#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/
解题思路：
最后一步可能跨了一级台阶，也可能跨了两级台阶，所以 当x > 1 时 f(x) = f(x-1) + f(x-2)，x表示当前台阶层数
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # second_in_front 前二级台阶的到达路径有几种
        # first_in_front 前一级台阶的到达路径有几种
        # curr 当前台阶的到达路径有几种，当前台阶的到达路径，等于 first_in_front + second_in_front
        second_in_front, first_in_front, curr = 0, 0, 1
        for i in range(1, n + 1):
            second_in_front = first_in_front
            first_in_front = curr
            curr = second_in_front + first_in_front
        return curr


solution = Solution()
print(solution.climbStairs(0))
print(solution.climbStairs(1))
print(solution.climbStairs(2))
print(solution.climbStairs(3))
print(solution.climbStairs(4))
print(solution.climbStairs(5))
print(solution.climbStairs(10))
print(solution.climbStairs(100))
print(solution.climbStairs(1000))
