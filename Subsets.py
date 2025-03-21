# Link: https://leetcode.com/problems/subsets/

class Solution(object):
    def subsets(self, nums):
        result = []
        subs = []
        def backtrack(i):
            if i >= len(nums):
                result.append(subs[:])
                return
            
            subs.append(nums[i])
            backtrack(i + 1)
            subs.pop()
            backtrack(i + 1)

            
        backtrack(0)
        return result