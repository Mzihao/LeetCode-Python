"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

link: https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = defaultdict(int)
        start = 0
        end = 0
        max_len = 0
        counter = 0
        while end < len(s):
            if lookup[s[end]] > 0:
                counter += 1
            lookup[s[end]] += 1
            end += 1
            while counter > 0:
                if lookup[s[start]] > 1:
                    counter -= 1
                lookup[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start)
        return max_len


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('jgfjaghjahghewuhghegjkbqt3iowjekgnvhg'))
