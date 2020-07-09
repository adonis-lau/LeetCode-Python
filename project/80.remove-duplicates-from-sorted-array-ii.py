#!/usr/bin/python3
# -*- coding: UTF-8 -*-


"""
80. Remove Duplicates from Sorted Array II
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
解题思路：
1、使用两个指针，i 是遍历指针，指向当前遍历的元素；j 指向下一个要覆盖元素的位置。
2、用 count 记录当前数字出现的次数。count 的最小计数始终为 1。
3、从索引 1 开始一次处理一个数组元素。
4、若当前元素与前一个元素相同，即 nums[i]==nums[i-1]，则 count++。若 count > 2，则说明遇到了多余的重复项。在这种情况下，我们只向前移动 i，而 j 不动。
5、若 count <=2，则我们将 i 所指向的元素移动到 j 位置，并同时增加 i 和 j。
6、若当前元素与前一个元素不相同，即 nums[i] != nums[i - 1]，说明遇到了新元素，则我们更新 count = 1，并且将该元素移动到 j 位置，并同时增加 i 和 j。
7、当数组遍历完成，则返回 j。
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # j 指向下一个要覆盖元素的位置
        # count 记录当前数字出现的次数。count 的最小计数始终为 1。
        j, count = 1, 1

        # 从第二个数开始依次遍历
        for i in range(1, len(nums)):

            # 当前元素与前一个元素相同，即 nums[i]==nums[i-1]，则 count++
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                # 若当前元素与前一个元素不相同，即 nums[i] != nums[i - 1]，说明遇到了新元素，则我们更新 count = 1，并且将该元素移动到 j 位置，并同时增加 i 和 j。
                # count 的最小计数始终为 1
                count = 1

            # 若 count > 2，则说明遇到了多余的重复项。在这种情况下，我们只向前移动 i，而 j 不动。
            # 若 count <=2，则我们将 i 所指向的元素移动到 j 位置，并同时增加 i 和 j。
            if count <= 2:
                nums[j] = nums[i]
                j += 1

        # 当数组遍历完成，则返回 j。
        return j


solution = Solution()
print(solution.removeDuplicates([1, 1, 1, 2, 2, 3]))
print(solution.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
