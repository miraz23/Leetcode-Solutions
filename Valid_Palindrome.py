# Link: https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        palindrome = ""

        for c in s:
            if c.isalnum():
                palindrome += lower(c)

        if palindrome == palindrome[::-1]:
            return True
        else:
            return False