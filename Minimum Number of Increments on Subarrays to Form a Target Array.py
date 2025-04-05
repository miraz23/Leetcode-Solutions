# Link: https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/

class Solution(object):
    def minNumberOperations(self, target):
        ans = 0
        prev = 0
        for num in target:
            if num > prev:
                ans += num - prev
            prev = num
            
        return ans