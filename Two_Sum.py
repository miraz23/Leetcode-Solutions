#Brute Force Solution
'''
class Solution(object):
    def twoSum(self, nums, target):
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
'''

#Optimized solution using Hash Map
class Solution(object):
    def twoSum(self, nums, target):
        prev = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev:
                return [prev[diff], i]
            prev[n] = i