"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

link: https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = []
        res = 0
        for i in s:
            if i in a:
                a = a[a.index(i) + 1:]
            a.append(i)
            res = res if len(a) < res else len(a)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('asdasdff'))
