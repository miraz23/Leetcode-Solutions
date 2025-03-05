# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ch = set()
        left = 0
        length = 0

        for i in range(len(s)):
            while s[i] in ch:
                ch.remove(s[left])
                left += 1

            ch.add(s[i])
            length = max(length, i - left + 1)

        return length