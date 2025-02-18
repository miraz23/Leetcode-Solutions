# Link: https://leetcode.com/problems/search-insert-position/

'''
# O(n)

class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        
        return len(nums)
        
'''

# O(logn)

class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = left + (right - left) / 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return left