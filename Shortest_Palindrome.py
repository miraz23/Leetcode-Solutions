# Link: https://leetcode.com/problems/shortest-palindrome/

class Solution(object):
    def shortestPalindrome(self, s):
        if not s:
            return s

        rev_s = s[::-1]

        for i in range(len(s) + 1):
            if s.startswith(rev_s[i:]):
                return rev_s[:i] + s