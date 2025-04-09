# Link: https://leetcode.com/problems/missing-number/

class Solution(object):
    def missingNumber(self, nums):
        for i in range(len(nums)+1):
            if i not in nums:
                return i