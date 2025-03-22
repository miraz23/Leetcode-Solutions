# Link: https://leetcode.com/problems/contains-duplicate-ii/

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        index = {}
        for i, j in enumerate(nums):
            if j in index and i - index[j] <= k:
                return True
            index[j] = i
        return False