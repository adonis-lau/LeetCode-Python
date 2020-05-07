#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
38. Count and Say
https://leetcode.com/problems/count-and-say/
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        # 指定初始化的第一个整数序列
        prev_person = '1'
        # 因为指定了第一个序列，所以要少循环一次
        for i in range(1, n):
            # 初始化下一次的序列为空字符串
            next_person = ''
            # 取出当前序列的第一个数字
            num = prev_person[0]
            # 连续数字出现的次数
            count = 0
            # 循环当前序列的每个整数
            for person in prev_person:
                # 记录数字连续出现的次数
                if person == num:
                    count += 1
                # 当数字不连续时
                else:
                    # 为下一次的序列开始赋值
                    next_person += str(count) + num
                    # 将不连续的数字赋值给临时变量
                    num = person
                    # 不连续的数字至少出现了一次
                    count = 1
            next_person += str(count) + num
            prev_person = next_person
        return prev_person


solution = Solution()
print(solution.countAndSay(4))
