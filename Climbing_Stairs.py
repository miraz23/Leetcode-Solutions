# Link: https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2: 
            return 2

        a = 2
        b = 1

        for i in range(3, n + 1):
            sum = a + b
            b = a
            a = sum

        return a