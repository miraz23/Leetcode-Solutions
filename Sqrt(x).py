# Link: https://leetcode.com/problems/sqrtx/

'''
8
left = 0, right = 5

0 <= 5
    mid = 0+5 /2 = 2
    2 * 2 = 4 < 8
    left = 2 + 1 = 3

3 <= 5
    mid = 3+5 / 2 = 4
    4 * 4 = 16 > 8
    right = 4 - 1 = 3

3 <= 3
    mid = 3+3 / 2 = 3
    3 * 3 = 9 > 8
    right = 3 - 1 = 2

return 2
'''

class Solution(object):
    def mySqrt(self, x):
        left = 0
        right = x / 2 + 1

        while left <= right:
            mid = (left + right) / 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right