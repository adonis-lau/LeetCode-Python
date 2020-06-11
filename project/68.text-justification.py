#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
68. Text Justification
https://leetcode.com/problems/text-justification/
"""
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # 最后的答案
        ans = []
        # 当前行的字母数
        cur_char = 0
        # 当前行的单词数
        cur_word = 0
        # 当前行的单词列表
        wl = []
        for i, wd in enumerate(words):
            l = len(wd)
            # 加上这个单词是否会超过最大长度
            if cur_char + l + cur_word > maxWidth:
                # 当前行仅有一个超长的单词，后面全部补空格
                if cur_word == 1:
                    ans.append(wl[0] + ' ' * (maxWidth - cur_char))
                else:  # 这一行有多个单词
                    # 这行一共有几个空格
                    left = maxWidth - cur_char
                    # 空格刚好平均分配
                    if left % (cur_word - 1) == 0:
                        ans.append((' ' * (left // (cur_word - 1))).join(wl))
                    else:  # 空格不能平均分配
                        # 多余的空格
                        x = left % (cur_word - 1)
                        # 平均每个间隔最少的空格数
                        b = left // (cur_word - 1)
                        cans = wl[0]
                        # 前 x 个间隔空 b + 1 个
                        for i in range(x):
                            cans += ' ' * (b + 1) + wl[i + 1]
                        # 后面的都空 b 个
                        for i in range(x + 1, len(wl)):
                            cans += ' ' * b + wl[i]
                        ans.append(cans)
                cur_char = l
                cur_word = 1
                wl = [wd]
            else:
                cur_char += l
                cur_word += 1
                wl.append(wd)

        # 所有单词过完了把余下的词放入最后一行
        if cur_word > 0:
            cans = ' '.join(wl)
            cans += ' ' * (maxWidth - len(cans))
            ans.append(cans)
        return ans


solution = Solution()
print(solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(''.join("asdfasdfasdfasdf"))
print(' '.join("asdfasdfasdfasdf"))
print('  '.join("asdfasdfasdfasdf"))