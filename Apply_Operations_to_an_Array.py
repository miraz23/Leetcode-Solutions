# Link: https://leetcode.com/problems/apply-operations-to-an-array/

class Solution(object):
    def applyOperations(self, nums):
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        non_zero = [num for num in nums if num != 0]
        zeros = [0] * (len(nums) - len(non_zero))
        return non_zero + zeros