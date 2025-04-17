# Link: https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/?envType=daily-question&envId=2025-04-17

class Solution(object):
    def countPairs(self, nums, k):
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    count = count + 1

        return count
        