# Link: https://leetcode.com/problems/power-of-two/

class Solution(object):
    def isPowerOfTwo(self, n):
        return (n & (n - 1))==0 and n > 0