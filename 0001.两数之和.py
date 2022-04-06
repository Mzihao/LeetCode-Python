'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出
和为目标值 target  的那 两个 整数，并返回它们的数组下标。

link: https://leetcode-cn.com/problems/two-sum/
'''

from typing import List
import time


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i, num in enumerate(nums):
            if target - num in hashtable:
                print(hashtable)
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []


if __name__ == '__main__':
    t1 = time.time()
    s = Solution()
    index = s.twoSum([124, 34, 235, 64, 24, 36, 27, 23, 534, 234, 645], 87)
    print(index)
    t2 = time.time()
    print('用时：', t2-t1)

