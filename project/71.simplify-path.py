#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
71. Simplify Path
https://leetcode.com/problems/simplify-path/
解题思路：
最后一步可能跨了一级台阶，也可能跨了两级台阶，所以 当x > 1 时 f(x) = f(x-1) + f(x-2)，x表示当前台阶层数
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.strip().split("/")
        stack = []

        # 使用堆栈，如果目录不是“。”，“..”或“”，则将目录添加到堆栈。
        # 如果看到“..”，则弹出最后一个元素。
        # 遍历路径，因此我们正在从根目录检查目录。

        for i in path:
            # 每次看到".."，我们都必须转到父目录，因此必须删除堆栈中的最后一个目录。
            # 仅在堆栈不为空时执行此操作
            if i == ".." and stack:
                stack.pop()
            # 如果当前元素为"." 或 ""，我们将保留在当前目录中，无需执行任何操作
            # 否则将当前元素添加到堆栈中
            elif i != "." and i != "" and i != "..":
                stack.append(i)
        # 返回以 "/" 开头，且每个目录以 "/" 隔开的路径
        return "/" + "/".join(stack)


solution = Solution()
print(solution.simplifyPath("/a//b////c/d//././/.."))
print(solution.simplifyPath("/a/d//.././/.."))
